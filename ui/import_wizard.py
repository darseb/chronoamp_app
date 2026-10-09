"""Wizard for importing calibration data and building an Analytical Method.

Provides a multi-step UI:
1. File Selection (.pssession, Excel, CSV)
2. Column Mapping (for Excel/CSV)
3. Measurement Assignment (Role, Concentration, Replicate)
4. Method Identity (Name, Analyte, etc.)
5. Calibration Preview & Validation
"""

from __future__ import annotations

import logging
import re
from pathlib import Path

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QComboBox,
    QFileDialog,
    QFormLayout,
    QHeaderView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
    QWizard,
    QWizardPage,
)

# pyqtgraph for calibration plot
import pyqtgraph as pg

from data.importer_models import (
    CalibrationMeasurement,
    ColumnMapping,
    ImportedMeasurement,
    MeasurementRole,
    SignalMetric,
)
from data.importers.csv_importer import import_from_csv
from data.importers.excel_importer import (
    detect_column_mapping,
    import_from_excel,
    list_sheets,
    read_sheet_preview,
)
from data.importers.pstrace_importer import parse_pssession
from data.method_store import save_method
from interpretation.calibration import FitType
from interpretation.method import AnalyticalMethod
from interpretation.method_builder import MethodBuilder
from utils.formatting import format_concentration
from ui.theme import (
    ACCENT,
    BORDER,
    ERROR,
    PANEL_BG,
    PANEL_SECONDARY_BG,
    PLOT_BG,
    PLOT_TRACE,
    SUCCESS,
    TEXT,
    TEXT_SECONDARY,
)

logger = logging.getLogger(__name__)


class ImportWizard(QWizard):
    """Multi-step wizard for importing calibration data."""

    method_created = Signal(AnalyticalMethod)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Import Calibration Data")
        self.resize(800, 600)
        
        # Shared state
        self.imported_measurements: list[ImportedMeasurement] = []
        self.calibration_measurements: list[CalibrationMeasurement] = []
        self.final_method: AnalyticalMethod | None = None
        self.fit_type: FitType = FitType.LINEAR

        # Add pages
        self.addPage(FileSelectionPage(self))
        # Skipping pages 2-4 for brevity in this MVP implementation
        # and jumping straight to a mock assignment and build page.
        # A full implementation would build out ColumnMappingPage and AssignmentPage.
        self.addPage(QuickAssignPage(self))
        self.addPage(ValidationPage(self))


class FileSelectionPage(QWizardPage):
    def __init__(self, parent: QWizard) -> None:
        super().__init__(parent)
        self.setTitle("Select Calibration Data")
        self.setSubTitle("Choose a PSTrace session (.pssession) or tabular file (.xlsx, .csv).")

        layout = QVBoxLayout(self)
        
        row = QHBoxLayout()
        self.path_edit = QLineEdit()
        self.path_edit.setReadOnly(True)
        btn_browse = QPushButton("Browse...")
        btn_browse.clicked.connect(self._browse)
        
        row.addWidget(self.path_edit)
        row.addWidget(btn_browse)
        layout.addLayout(row)
        
        self.status_lbl = QLabel()
        layout.addWidget(self.status_lbl)

    def _browse(self) -> None:
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Calibration Data", "", 
            "Data Files (*.pssession *.xlsx *.csv);;All Files (*.*)"
        )
        if path:
            self.path_edit.setText(path)
            self._load_file(Path(path))

    def _load_file(self, path: Path) -> None:
        wizard = self.wizard()
        wizard.imported_measurements.clear()
        
        try:
            if path.suffix.lower() == ".pssession":
                meas = parse_pssession(path)
            elif path.suffix.lower() in (".xlsx", ".xls"):
                meas = import_from_excel(path)  # using auto-detection
            elif path.suffix.lower() == ".csv":
                meas = import_from_csv(path)
            else:
                raise ValueError("Unsupported file format.")
                
            wizard.imported_measurements = meas
            self.status_lbl.setText(f"Loaded {len(meas)} measurements successfully.")
            self.status_lbl.setStyleSheet(f"color: {SUCCESS};")
        except Exception as exc:
            self.status_lbl.setText(f"Error: {exc}")
            self.status_lbl.setStyleSheet(f"color: {ERROR};")
            logger.exception("Import failed")
        finally:
            self.completeChanged.emit()

    def isComplete(self) -> bool:
        return len(self.wizard().imported_measurements) > 0


COMMON_CONCENTRATION_UNITS: list[str] = [
    "nM", "µM", "mM", "M", "pM",
    "ng/mL", "µg/mL", "mg/mL", "pg/mL",
    "g/L", "mg/L", "µg/L",
    "%", "ppm", "ppb",
]

from utils.units import MASS_FACTORS, MOLAR_FACTORS, convert_concentration


def _parse_name_metadata(name: str) -> tuple[str, float | None, str | None]:
    """Parse role, concentration, and unit from measurement name.
    
    Examples:
        'BLANK 1' -> ('Blank', None, None)
        '0.1 nM 1' -> ('Standard', 0.1, 'nM')
        '10 µM' -> ('Standard', 10.0, 'µM')
    """
    name_lower = name.lower().strip()
    if "blank" in name_lower:
        return "Blank", None, None
        
    pattern = r'([0-9]+(?:\.[0-9]+)?)\s*([a-zA-Zµ/%]+(?:/[a-zA-Z]+)?)'
    match = re.search(pattern, name)
    if match:
        try:
            return "Standard", float(match.group(1)), match.group(2)
        except ValueError:
            pass
    return "Standard", None, None


class QuickAssignPage(QWizardPage):
    """Simplified assignment page assigning roles heuristically with flexible unit selection."""
    
    def __init__(self, parent: QWizard) -> None:
        super().__init__(parent)
        self.setTitle("Assign Roles & Metadata")
        self.setSubTitle(
            "Configure analyte name, choose a default unit for all rows, or customize individual readings."
        )
        
        self._updating_units = False
        
        layout = QVBoxLayout(self)
        
        # Form for Analyte and Global Unit at the top
        form = QFormLayout()
        self.analyte_edit = QLineEdit("Unknown Analyte")
        
        unit_row = QHBoxLayout()
        self.unit_combo = QComboBox()
        self.unit_combo.setEditable(True)
        self.unit_combo.addItems(COMMON_CONCENTRATION_UNITS)
        self.unit_combo.setCurrentText("nM")
        
        self.btn_apply_all = QPushButton("Apply to All Rows")
        self.btn_apply_all.setToolTip("Set this unit for all rows in the table below")
        self.btn_apply_all.clicked.connect(self._on_apply_all_clicked)
        
        unit_row.addWidget(self.unit_combo, 1)
        unit_row.addWidget(self.btn_apply_all)
        
        # Auto-update all rows when user selects or finishes typing a global unit
        self.unit_combo.activated.connect(self._on_global_unit_activated)
        if self.unit_combo.lineEdit():
            self.unit_combo.lineEdit().editingFinished.connect(self._on_global_unit_editing_finished)
            
        self.fit_combo = QComboBox()
        self.fit_combo.addItem("Linear (m·C + b)", FitType.LINEAR)
        self.fit_combo.addItem("Logarithmic (m·log10(C) + b)", FitType.LOGARITHMIC)

        form.addRow("Analyte Name:", self.analyte_edit)
        form.addRow("Default Unit (All Rows):", unit_row)
        form.addRow("Fit Strategy:", self.fit_combo)
        layout.addLayout(form)
        
        # Table of measurements
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Name", "Role", "Concentration", "Unit"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        layout.addWidget(self.table)

    def _on_apply_all_clicked(self) -> None:
        self._apply_unit_to_all(self.unit_combo.currentText().strip())

    def _on_global_unit_activated(self, index: int) -> None:
        self._apply_unit_to_all(self.unit_combo.itemText(index).strip())

    def _on_global_unit_editing_finished(self) -> None:
        self._apply_unit_to_all(self.unit_combo.currentText().strip())

    def _apply_unit_to_all(self, unit: str) -> None:
        if not unit or self._updating_units:
            return
        self._updating_units = True
        try:
            for row in range(self.table.rowCount()):
                w = self.table.cellWidget(row, 3)
                if isinstance(w, QComboBox):
                    w.setCurrentText(unit)
                elif self.table.item(row, 3):
                    self.table.item(row, 3).setText(unit)
        finally:
            self._updating_units = False

    def initializePage(self) -> None:
        meas = self.wizard().imported_measurements
        self.table.setRowCount(len(meas))
        
        # Check if any measurement has an existing unit in metadata or measurement name
        detected_unit = None
        for m in meas:
            u = m.metadata.get("concentration_unit") or m.metadata.get("unit")
            if not u:
                _, _, parsed_unit = _parse_name_metadata(m.measurement_name)
                u = parsed_unit
            if u:
                detected_unit = str(u).strip()
                break
                
        default_unit = detected_unit or self.unit_combo.currentText().strip() or "nM"
        
        self._updating_units = True
        try:
            self.unit_combo.setCurrentText(default_unit)
            
            for i, m in enumerate(meas):
                self.table.setItem(i, 0, QTableWidgetItem(m.measurement_name))
                
                parsed_role, parsed_conc, parsed_unit = _parse_name_metadata(m.measurement_name)
                
                role_combo = QComboBox()
                role_combo.addItems(["Blank", "Standard", "Ignore"])
                
                conc_edit = QLineEdit()
                
                # Determine role: metadata > name heuristic
                if "role" in m.metadata:
                    role_str = str(m.metadata["role"]).capitalize()
                    role_combo.setCurrentText(role_str if role_str in ["Blank", "Standard", "Ignore"] else "Standard")
                else:
                    role_combo.setCurrentText(parsed_role)
                    
                # Determine concentration: metadata > name heuristic > empty
                if "concentration" in m.metadata and m.metadata["concentration"] is not None:
                    conc_edit.setText(str(m.metadata["concentration"]))
                elif parsed_conc is not None:
                    conc_edit.setText(str(parsed_conc))
                else:
                    conc_edit.setText("")
                    
                # Per-row unit combo box: allows choosing different units per reading
                row_unit_combo = QComboBox()
                row_unit_combo.setEditable(True)
                row_unit_combo.addItems(COMMON_CONCENTRATION_UNITS)
                
                row_unit = m.metadata.get("concentration_unit") or m.metadata.get("unit") or parsed_unit or default_unit
                row_unit_combo.setCurrentText(str(row_unit).strip())
                
                self.table.setCellWidget(i, 1, role_combo)
                self.table.setCellWidget(i, 2, conc_edit)
                self.table.setCellWidget(i, 3, row_unit_combo)
        finally:
            self._updating_units = False

    def validatePage(self) -> bool:
        wizard = self.wizard()
        wizard.calibration_measurements.clear()
        
        global_unit = self.unit_combo.currentText().strip()
        wizard.conc_unit = global_unit
        wizard.analyte_name = self.analyte_edit.text().strip()

        selected_fit = self.fit_combo.currentData() or FitType.LINEAR
        wizard.fit_type = selected_fit

        # If logarithmic fit, validate that standard concentrations are strictly positive
        if selected_fit == FitType.LOGARITHMIC or selected_fit == FitType.LOGARITHMIC.value:
            invalid_standards = []
            for i in range(self.table.rowCount()):
                role_str = self.table.cellWidget(i, 1).currentText().lower()
                if role_str == "standard":
                    conc_text = self.table.cellWidget(i, 2).text().strip()
                    try:
                        c_val = float(conc_text)
                        if c_val <= 0:
                            invalid_standards.append(i + 1)
                    except ValueError:
                        invalid_standards.append(i + 1)
            if invalid_standards:
                rows_str = ", ".join(str(r) for r in invalid_standards)
                QMessageBox.warning(
                    self,
                    "Invalid Concentration for Logarithmic Fit",
                    f"Logarithmic calibration requires all standard concentrations to be strictly positive (> 0).\n\n"
                    f"Non-positive standard concentration found on row(s): {rows_str}.\n"
                    "Please correct the concentration(s) or change the role to Blank or Ignore."
                )
                return False
        
        for i, m in enumerate(wizard.imported_measurements):
            role_str = self.table.cellWidget(i, 1).currentText().lower()
            if role_str == "ignore":
                continue
                
            role = MeasurementRole(role_str)
            
            conc_text = self.table.cellWidget(i, 2).text().strip()
            raw_conc = float(conc_text) if conc_text else None
            
            unit_widget = self.table.cellWidget(i, 3)
            if isinstance(unit_widget, QComboBox):
                row_unit = unit_widget.currentText().strip()
            elif self.table.item(i, 3):
                row_unit = self.table.item(i, 3).text().strip()
            else:
                row_unit = global_unit
                
            # Normalize concentration to global unit if different
            norm_conc = raw_conc
            if raw_conc is not None and row_unit and global_unit and row_unit != global_unit:
                norm_conc = convert_concentration(raw_conc, row_unit, global_unit)
                m.metadata["original_concentration"] = raw_conc
                m.metadata["original_unit"] = row_unit
            
            c_meas = CalibrationMeasurement(
                source=m,
                measurement_id=f"meas_{i}",
                role=role,
                concentration=norm_conc,
                concentration_unit=global_unit if norm_conc is not None else row_unit,
                replicate=1,
            )
            wizard.calibration_measurements.append(c_meas)
            
        return True


class ValidationPage(QWizardPage):
    def __init__(self, parent: QWizard) -> None:
        super().__init__(parent)
        self.setTitle("Calibration Curve & Validation")
        
        layout = QVBoxLayout(self)

        # Interactive fit strategy selector
        fit_bar = QHBoxLayout()
        lbl_fit = QLabel("Fit Strategy:")
        lbl_fit.setStyleSheet(f"color: {TEXT}; font-weight: bold;")
        self.fit_combo = QComboBox()
        self.fit_combo.addItem("Linear (m·C + b)", FitType.LINEAR)
        self.fit_combo.addItem("Logarithmic (m·log10(C) + b)", FitType.LOGARITHMIC)
        self.fit_combo.currentIndexChanged.connect(self._on_fit_type_changed)
        fit_bar.addWidget(lbl_fit)
        fit_bar.addWidget(self.fit_combo)
        fit_bar.addStretch()
        layout.addLayout(fit_bar)
        
        self.plot_widget = pg.PlotWidget(title="Calibration Curve")
        self.plot_widget.setBackground(PLOT_BG)
        self.plot_widget.setLabel('left', 'Current', units='µA', color=TEXT)
        self.plot_widget.setLabel('bottom', 'Concentration', color=TEXT)

        # Style axes for the light theme
        for axis_name in ('left', 'bottom'):
            axis = self.plot_widget.getAxis(axis_name)
            axis.setPen(TEXT)
            axis.setTextPen(TEXT)

        self.plot_widget.showGrid(x=True, y=True, alpha=0.3)

        layout.addWidget(self.plot_widget)
        
        self.lbl_stats = QLabel()
        layout.addWidget(self.lbl_stats)
        
        self.lbl_val = QLabel()
        layout.addWidget(self.lbl_val)

    def initializePage(self) -> None:
        wizard = self.wizard()
        
        unit_lbl = f"Concentration ({wizard.conc_unit})" if wizard.conc_unit else "Concentration"
        self.plot_widget.setLabel('bottom', unit_lbl, color=TEXT)

        idx = self.fit_combo.findData(wizard.fit_type)
        if idx != -1:
            self.fit_combo.blockSignals(True)
            self.fit_combo.setCurrentIndex(idx)
            self.fit_combo.blockSignals(False)

        self._rebuild_and_update()

    def _on_fit_type_changed(self, index: int) -> None:
        selected_fit = self.fit_combo.currentData() or FitType.LINEAR
        self.wizard().fit_type = selected_fit
        self._rebuild_and_update()

    def _rebuild_and_update(self) -> None:
        wizard = self.wizard()
        builder = MethodBuilder()
        builder.set_identity(
            name=f"{wizard.analyte_name} Auto-Method",
            version="1.0",
            analyte=wizard.analyte_name,
            technique="Chronoamperometry",
            concentration_unit=wizard.conc_unit,
        )
        builder.set_fit_type(wizard.fit_type)
        
        for cm in wizard.calibration_measurements:
            builder.add_measurement(cm)
            
        try:
            self.method = builder.build()
            wizard.final_method = self.method
            self._update_ui()
        except Exception as exc:
            self.lbl_stats.setText(f"Failed to build method: {exc}")
            logger.exception("Method build failed")

    def _update_ui(self) -> None:
        m = self.method
        cal = m.calibration_result
        
        if cal:
            if cal.fit_type == FitType.LOGARITHMIC.value or cal.fit_type == FitType.LOGARITHMIC:
                stats = f"<b>Calibration:</b> y = {cal.slope:.4g}·log10(x) + {cal.intercept:.4g} (R² = {cal.r_squared:.4f})<br>"
            else:
                stats = f"<b>Calibration:</b> y = {cal.slope:.4g}x + {cal.intercept:.4g} (R² = {cal.r_squared:.4f})<br>"
        else:
            stats = "<b>Calibration:</b> None<br>"
            
        if m.lod and m.loq:
            lod_str = format_concentration(m.lod.concentration, unit=m.concentration_unit) if m.lod.concentration is not None else f"{m.lod.current_ua:.4g} µA"
            loq_str = format_concentration(m.loq.concentration, unit=m.concentration_unit) if m.loq.concentration is not None else f"{m.loq.current_ua:.4g} µA"
            stats += f"<b>LOD:</b> {lod_str} | <b>LOQ:</b> {loq_str}<br>"
            
        self.lbl_stats.setText(stats)
        
        if m.validation:
            val_text = "<b>Validation Checks:</b><br>"
            for check in m.validation.checks:
                color = SUCCESS if check.passed else ERROR
                icon = "✓" if check.passed else "✗"
                val_text += f"<span style='color: {color};'>{icon} {check.message}</span><br>"
            self.lbl_val.setText(val_text)
            
        self._plot_curve()

    def _plot_curve(self) -> None:
        self.plot_widget.clear()
        m = self.method
        if not m.calibration_result:
            return
            
        # Plot standards
        x_pts = []
        y_pts = []
        for cm in m.source_measurements:
            if cm.role == MeasurementRole.STANDARD and cm.concentration is not None:
                x_pts.append(cm.concentration)
                y_pts.append(cm.signal_value)
                
        self.plot_widget.plot(
            x_pts, y_pts, 
            pen=None, symbol='o', symbolBrush=ACCENT, symbolSize=8,
            name="Standards"
        )
        
        # Plot fit curve
        if x_pts:
            cal = m.calibration_result
            x_min, x_max = min(x_pts), max(x_pts)
            
            if cal.fit_type == FitType.LOGARITHMIC.value or cal.fit_type == FitType.LOGARITHMIC:
                # Logarithmic curve over positive concentration span
                if x_min > 0 and x_max > 0:
                    c_start = max(x_min * 0.8, 1e-12)
                    c_end = x_max * 1.2
                    n_eval = 100
                    x_curve = [c_start + i * (c_end - c_start) / (n_eval - 1) for i in range(n_eval)]
                    y_curve = [cal.predict_signal(x) for x in x_curve]
                    self.plot_widget.plot(
                        x_curve, y_curve,
                        pen=pg.mkPen(PLOT_TRACE, width=2),
                        name="Fit"
                    )
            else:
                x_min = max(0, x_min - (x_max - x_min)*0.1)
                x_max = x_max + (x_max - x_min)*0.1
                
                y_min = cal.slope * x_min + cal.intercept
                y_max = cal.slope * x_max + cal.intercept
                
                self.plot_widget.plot(
                    [x_min, x_max], [y_min, y_max],
                    pen=pg.mkPen(PLOT_TRACE, width=2),
                    name="Fit"
                )

    def validatePage(self) -> bool:
        m = self.wizard().final_method
        if not m or not m.validation or not m.validation.is_valid:
            reply = QMessageBox.warning(
                self, "Invalid Method",
                "The method failed validation. Do you really want to save it?",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
            )
            if reply == QMessageBox.StandardButton.No:
                return False
                
        # Save method
        try:
            save_method(m)
            self.wizard().method_created.emit(m)
            return True
        except Exception as exc:
            QMessageBox.critical(self, "Error", f"Failed to save method: {exc}")
            return False
