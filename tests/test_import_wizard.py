import sys
from pathlib import Path
from unittest.mock import MagicMock, patch
import pytest
from PySide6.QtWidgets import QApplication, QComboBox
from ui.import_wizard import (
    ImportWizard,
    FileSelectionPage,
    QuickAssignPage,
    ValidationPage,
    convert_concentration,
)
from data.importer_models import ImportedMeasurement, CalibrationMeasurement, MeasurementRole
from interpretation.calibration import FitType

# Ensure QApplication exists for test run
app = QApplication.instance() or QApplication(sys.argv)


def test_file_selection_page_completeness_signal():
    wizard = ImportWizard()
    page = wizard.page(0)
    assert isinstance(page, FileSelectionPage)
    
    # Initially, wizard has no measurements, so isComplete is False
    assert not page.isComplete()
    
    # Track completeChanged emissions
    signal_emitted = []
    page.completeChanged.connect(lambda: signal_emitted.append(True))
    
    # Mock parse_pssession to return simulated measurements
    mock_meas = [MagicMock(measurement_name=f"Curve_{i}", metadata={}) for i in range(18)]
    with patch("ui.import_wizard.parse_pssession", return_value=mock_meas):
        page._load_file(Path("dummy.pssession"))
        
    assert len(signal_emitted) > 0
    assert page.isComplete()
    assert len(wizard.imported_measurements) == 18


def test_convert_concentration():
    # Same unit
    assert convert_concentration(10.0, "nM", "nM") == 10.0
    
    # Molar conversions
    assert pytest.approx(convert_concentration(1.0, "µM", "nM")) == 1000.0
    assert pytest.approx(convert_concentration(1000.0, "nM", "µM")) == 1.0
    assert pytest.approx(convert_concentration(2.5, "mM", "µM")) == 2500.0
    
    # Mass conversions
    assert pytest.approx(convert_concentration(1.0, "mg/mL", "µg/mL")) == 1000.0
    assert pytest.approx(convert_concentration(50.0, "ng/mL", "µg/mL")) == 0.05
    
    # Unknown / mismatched
    assert convert_concentration(5.0, "nM", "mg/mL") == 5.0


def test_quick_assign_page_unit_selection():
    wizard = ImportWizard()
    
    # Populate with 4 mock measurements
    meas_list = [
        ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name=f"Reading_{i}",
            measurement_index=i,
            time_s=[0.0, 1.0],
            current_ua=[0.0, 1.0],
            metadata={},
        )
        for i in range(4)
    ]
    wizard.imported_measurements = meas_list
    
    page = wizard.page(1)
    assert isinstance(page, QuickAssignPage)
    
    # Initialize page
    page.initializePage()
    assert page.table.rowCount() == 4
    
    # All 4 rows should start with default unit ("nM")
    for r in range(4):
        unit_w = page.table.cellWidget(r, 3)
        assert isinstance(unit_w, QComboBox)
        assert unit_w.currentText() == "nM"
        
    # User selects/sets a defined unit for all: e.g. "µg/mL"
    page.unit_combo.setCurrentText("µg/mL")
    page.btn_apply_all.click()
    
    for r in range(4):
        unit_w = page.table.cellWidget(r, 3)
        assert unit_w.currentText() == "µg/mL"
        
    # Now user overrides row 2 individually to "mg/mL"
    row2_combo = page.table.cellWidget(2, 3)
    row2_combo.setCurrentText("mg/mL")
    
    # Confirm row 2 is mg/mL while other rows remain µg/mL
    assert page.table.cellWidget(0, 3).currentText() == "µg/mL"
    assert page.table.cellWidget(1, 3).currentText() == "µg/mL"
    assert page.table.cellWidget(2, 3).currentText() == "mg/mL"
    assert page.table.cellWidget(3, 3).currentText() == "µg/mL"
    
    # Test validatePage with mixed units (mg/mL converted to µg/mL in row 2)
    # Set conc in row 2 to 1.0 mg/mL -> should become 1000 µg/mL in calibration measurement
    page.table.cellWidget(2, 2).setText("1.0")
    page.table.cellWidget(2, 1).setCurrentText("Standard")
    
    page.validatePage()
    assert wizard.conc_unit == "µg/mL"
    
    # Find measurement corresponding to row 2
    cm_row2 = wizard.calibration_measurements[2]
    assert pytest.approx(cm_row2.concentration) == 1000.0
    assert cm_row2.concentration_unit == "µg/mL"


def test_quick_assign_page_fit_type_selection():
    wizard = ImportWizard()
    meas_list = [
        ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name=f"Standard_{i}",
            measurement_index=i,
            time_s=[0.0, 1.0],
            current_ua=[0.0, 1.0],
            metadata={"role": "Standard", "concentration": 1.0 + i},
        )
        for i in range(3)
    ]
    wizard.imported_measurements = meas_list
    page = wizard.page(1)
    page.initializePage()

    # Default is linear
    assert page.fit_combo.currentData() == FitType.LINEAR

    # Switch to logarithmic
    idx = page.fit_combo.findData(FitType.LOGARITHMIC)
    page.fit_combo.setCurrentIndex(idx)
    assert page.validatePage() is True
    assert wizard.fit_type == FitType.LOGARITHMIC


def test_quick_assign_page_log_fit_rejection():
    wizard = ImportWizard()
    meas_list = [
        ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name="Std_0",
            measurement_index=0,
            time_s=[0.0, 1.0],
            current_ua=[0.0, 1.0],
            metadata={"role": "Standard", "concentration": 0.0},
        )
    ]
    wizard.imported_measurements = meas_list
    page = wizard.page(1)
    page.initializePage()

    idx = page.fit_combo.findData(FitType.LOGARITHMIC)
    page.fit_combo.setCurrentIndex(idx)

    with patch("PySide6.QtWidgets.QMessageBox.warning") as mock_warn:
        assert page.validatePage() is False
        assert mock_warn.called


def test_validation_page_interactive_fit_toggle():
    import math
    wizard = ImportWizard()
    wizard.conc_unit = "nM"
    wizard.analyte_name = "AnalyteX"
    wizard.fit_type = FitType.LINEAR

    # Create synthetic calibration measurements with log response
    # y = -0.819 * log10(C) - 1.145
    concs = [0.1, 1.0, 10.0, 100.0]
    for i, c in enumerate(concs):
        sig = -0.819 * math.log10(c) - 1.145
        m = ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name=f"Std_{c}",
            measurement_index=i,
            time_s=[t * 0.1 for t in range(50)],
            current_ua=[sig] * 50,
            metadata={},
        )
        cm = CalibrationMeasurement(
            source=m,
            measurement_id=f"cm_{i}",
            role=MeasurementRole.STANDARD,
            concentration=c,
            concentration_unit="nM",
            signal_value=sig,
        )
        wizard.calibration_measurements.append(cm)

    val_page = wizard.page(2)
    assert isinstance(val_page, ValidationPage)
    val_page.initializePage()

    # Initially linear fit: R² should be relatively low (~0.69)
    assert wizard.final_method.calibration_result.fit_type == "linear"
    linear_r2 = wizard.final_method.calibration_result.r_squared
    assert linear_r2 < 0.85
    assert "x" in val_page.lbl_stats.text()

    # Switch interactive combo to Logarithmic
    idx = val_page.fit_combo.findData(FitType.LOGARITHMIC)
    val_page.fit_combo.setCurrentIndex(idx)

    # Rebuilt method should now be logarithmic with R² ≈ 1.0
    assert wizard.fit_type == FitType.LOGARITHMIC
    assert wizard.final_method.calibration_result.fit_type == "logarithmic"
    assert wizard.final_method.calibration_result.r_squared > 0.99
    assert "log10" in val_page.lbl_stats.text()


def test_validation_page_with_blanks_displays_lod_loq():
    wizard = ImportWizard()
    wizard.conc_unit = "nM"
    wizard.analyte_name = "AnalyteWithBlanks"
    wizard.fit_type = FitType.LINEAR

    # Add blanks
    for i in range(3):
        sig = 0.01 + 0.001 * i
        m = ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name=f"Blank_{i}",
            measurement_index=i,
            time_s=[t * 0.1 for t in range(50)],
            current_ua=[sig] * 50,
            metadata={},
        )
        cm = CalibrationMeasurement(
            source=m,
            measurement_id=f"blank_{i}",
            role=MeasurementRole.BLANK,
            concentration=0.0,
            concentration_unit="nM",
            signal_value=sig,
        )
        wizard.calibration_measurements.append(cm)

    # Add standards
    concs = [1.0, 5.0, 10.0]
    for i, c in enumerate(concs, start=3):
        sig = 0.5 * c + 0.01
        m = ImportedMeasurement(
            source_file="test.pssession",
            source_format="pssession",
            measurement_name=f"Std_{c}",
            measurement_index=i,
            time_s=[t * 0.1 for t in range(50)],
            current_ua=[sig] * 50,
            metadata={},
        )
        cm = CalibrationMeasurement(
            source=m,
            measurement_id=f"cm_{i}",
            role=MeasurementRole.STANDARD,
            concentration=c,
            concentration_unit="nM",
            signal_value=sig,
        )
        wizard.calibration_measurements.append(cm)

    val_page = wizard.page(2)
    assert isinstance(val_page, ValidationPage)
    # This must not throw 'DetectionLimit' object has no attribute 'concentration_value'
    val_page.initializePage()

    assert wizard.final_method.lod is not None
    assert wizard.final_method.loq is not None
    stats_text = val_page.lbl_stats.text()
    assert "Failed to build method" not in stats_text
    assert "LOD:" in stats_text
    assert "LOQ:" in stats_text
