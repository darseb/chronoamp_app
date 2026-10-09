"""Main application window — assembles all widgets and orchestrates the
measurement lifecycle.
"""

from __future__ import annotations

import logging
import os
import queue
import subprocess
from datetime import datetime
from pathlib import Path

from PySide6.QtCore import QTimer, Slot, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QInputDialog,
    QSplitter,
    QStatusBar,
    QComboBox,
    QCheckBox,
    QFrame,
)

from config.settings import DEFAULT_INTERVAL_TIME, SESSIONS_FOLDER
from core.acquisition import AcquisitionEngine
from core.device_manager import DeviceManager, DeviceNotFoundError
from core.models import DataPoint, MeasurementConfig
from data.exporter import export_to_excel
from data.session_store import save_session
from interpretation.blank_store import BlankStore
from interpretation.calibration import CalibrationCurve
from interpretation.method import AnalyticalMethod
from interpretation.verdict import Verdict, VerdictReport, interpret_full, interpret_with_method
from ui.control_panel import ControlPanel
from ui.live_plot_widget import LivePlotWidget
from ui.result_banner import ResultBanner
from ui.method_panel import MethodPanel
from ui.telemetry_panel import TelemetryPanel
from ui.activity_log import ActivityLogPanel, QtLogHandler
from ui.import_wizard import ImportWizard
from data.method_store import load_method
from ui.theme import (
    ACCENT_CYAN,
    ACCENT_CYAN_LIGHT,
    ACCENT_CYAN_BORDER,
    ACCENT_PRIMARY,
    BORDER,
    SUCCESS,
    ERROR,
    TEXT,
    TEXT_SECONDARY,
)
from utils.formatting import (
    get_scientific_notation_preference,
    set_scientific_notation_preference,
)

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    """Top-level application window for ChronoAmp."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("ChronoAmp — Electrochemical Biosensor Workstation")
        self.resize(1120, 740)
        self.setMinimumSize(960, 640)

        # -- Core services --------------------------------------------------
        self._dm = DeviceManager()
        self._engine: AcquisitionEngine | None = None
        self._collected_points: list[DataPoint] = []
        self._current_config: MeasurementConfig | None = None
        self._last_saved_path: Path | None = None
        self._last_report: VerdictReport | None = None

        # -- Analytical stores ----------------------------------------------
        self._blank_store = BlankStore()
        self._calibration = CalibrationCurve(concentration_unit="ng/mL")
        self._active_method: AnalyticalMethod | None = None

        # -- Build widgets --------------------------------------------------
        self._method_panel = MethodPanel()
        self._method_panel.load_requested.connect(self._on_load_method)
        self._method_panel.new_requested.connect(self._on_new_method)
        self._method_panel.deactivate_requested.connect(self._on_deactivate_method)
        self._method_panel.set_method(None)

        self._control_panel = ControlPanel()
        self._telemetry_panel = TelemetryPanel()
        self._activity_log = ActivityLogPanel()

        # Connect UI logging handler
        self._log_handler = QtLogHandler(self._activity_log)
        self._log_handler.setFormatter(logging.Formatter("%(message)s"))
        logging.getLogger().addHandler(self._log_handler)

        self._banner = ResultBanner()
        self._session_bar = self._build_session_bar()
        self._plot = LivePlotWidget(max_points=5000, update_rate=30)

        # -- No-device overlay (hidden when connected) ----------------------
        self._no_device_widget = self._build_no_device_widget()

        # -- Layout ---------------------------------------------------------
        central = QWidget()
        self.setCentralWidget(central)

        # Main horizontal splitter
        main_splitter = QSplitter(Qt.Orientation.Horizontal)
        main_splitter.setChildrenCollapsible(False)
        
        # Left Sidebar
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(8)
        left_layout.addWidget(self._method_panel)
        left_layout.addWidget(self._control_panel)
        left_layout.addWidget(self._telemetry_panel)
        left_layout.addWidget(self._activity_log, stretch=1)
        
        # Right Column
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(8)
        right_layout.addWidget(self._plot, stretch=1)
        right_layout.addWidget(self._no_device_widget)
        right_layout.addWidget(self._banner)
        right_layout.addWidget(self._session_bar)
        
        main_splitter.addWidget(left_widget)
        main_splitter.addWidget(right_widget)
        main_splitter.setStretchFactor(0, 0)
        main_splitter.setStretchFactor(1, 1)
        main_splitter.setSizes([380, 720])

        # Top Toolbar and Status Bar
        top_toolbar = self._build_top_toolbar()
        
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._update_status_bar("Initializing...")

        layout = QVBoxLayout(central)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(10)
        layout.addWidget(top_toolbar)
        layout.addWidget(main_splitter, stretch=1)

        # -- Queue-drain timer (runs continuously while measurement active) -
        self._poll_timer = QTimer(self)
        self._poll_timer.setInterval(33)  # ~30 Hz
        self._poll_timer.timeout.connect(self._poll_data_queue)

        # -- Connect control-panel signals ----------------------------------
        self._control_panel.start_requested.connect(self._on_start_requested)
        self._control_panel.stop_requested.connect(self._on_stop_requested)
        self._control_panel.elapsed_updated.connect(self._on_elapsed_updated)

        self._activity_log.log("ChronoAmp workstation initialized.")

        # -- Attempt initial device discovery -------------------------------
        self._try_connect_device()

    # -----------------------------------------------------------------------
    # Session-actions toolbar
    # -----------------------------------------------------------------------

    def _build_session_bar(self) -> QWidget:
        """Build the post-measurement session toolbar (hidden until first save)."""
        widget = QFrame()
        widget.setObjectName("panel_secondary")
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(10, 6, 10, 6)
        layout.setSpacing(8)

        self._saved_label = QLabel("")
        self._saved_label.setStyleSheet(
            f"color: {TEXT_SECONDARY}; background: transparent; font-size: 8.5pt; font-weight: 500;"
        )

        self._record_blank_btn = QPushButton("Record as Blank")
        self._record_blank_btn.setFixedHeight(26)
        self._record_blank_btn.clicked.connect(self._on_record_blank)

        self._add_cal_btn = QPushButton("Add to Calibration...")
        self._add_cal_btn.setFixedHeight(26)
        self._add_cal_btn.clicked.connect(self._on_add_calibration)

        self._open_file_btn = QPushButton("Open File")
        self._open_file_btn.setFixedHeight(26)
        self._open_file_btn.clicked.connect(self._on_open_file)

        self._open_folder_btn = QPushButton("Open Folder")
        self._open_folder_btn.setFixedHeight(26)
        self._open_folder_btn.clicked.connect(self._on_open_folder)

        self._export_excel_btn = QPushButton("Export to Excel")
        self._export_excel_btn.setFixedHeight(26)
        self._export_excel_btn.setObjectName("btn_primary")
        self._export_excel_btn.clicked.connect(self._on_export_excel)

        layout.addWidget(self._saved_label, stretch=1)
        layout.addWidget(self._record_blank_btn)
        layout.addWidget(self._add_cal_btn)
        layout.addWidget(self._open_file_btn)
        layout.addWidget(self._open_folder_btn)
        layout.addWidget(self._export_excel_btn)

        widget.hide()
        return widget

    # -----------------------------------------------------------------------
    # No-device overlay
    # -----------------------------------------------------------------------

    def _build_no_device_widget(self) -> QWidget:
        """Build a friendly overlay shown when no device is found."""
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(0, 20, 0, 20)

        msg = QLabel(
            "Potentiostat not connected.\n\n"
            "Connect a PalmSens device to begin acquisition."
        )
        msg.setWordWrap(True)
        msg_font = QFont()
        msg_font.setPointSize(11)
        msg.setFont(msg_font)
        msg.setAlignment(Qt.AlignmentFlag.AlignCenter)

        retry_btn = QPushButton("Refresh Devices")
        retry_btn.setObjectName("btn_primary")
        retry_btn.setFixedSize(140, 30)
        retry_btn.clicked.connect(self._try_connect_device)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        btn_row.addWidget(retry_btn)
        btn_row.addStretch()

        layout.addStretch()
        layout.addWidget(msg)
        layout.addSpacing(12)
        layout.addLayout(btn_row)
        layout.addStretch()

        widget.hide()
        return widget

    # -----------------------------------------------------------------------
    # Top Toolbar and Status Bar
    # -----------------------------------------------------------------------
    
    def _build_top_toolbar(self) -> QWidget:
        """Build the top toolbar with connection controls and notation settings."""
        toolbar = QFrame()
        toolbar.setObjectName("panel")
        layout = QHBoxLayout(toolbar)
        layout.setContentsMargins(12, 6, 14, 6)
        layout.setSpacing(10)
        
        lbl_conn = QLabel("Connection:")
        lbl_conn.setStyleSheet(f"color: {TEXT}; font-weight: 600; font-size: 9pt;")
        
        # Connection status pill
        self._conn_pill = QFrame()
        self._conn_pill.setObjectName("conn_pill")
        self._conn_pill.setStyleSheet(
            f"#conn_pill {{ background-color: #FDF2F2; border: 1px solid #F8B4B4; border-radius: 4px; }}"
        )
        pill_layout = QHBoxLayout(self._conn_pill)
        pill_layout.setContentsMargins(8, 2, 8, 2)
        pill_layout.setSpacing(5)

        self._conn_status_icon = QLabel("○")
        self._conn_status_icon.setStyleSheet(f"color: {ERROR}; font-weight: bold;")
        self._conn_status_label = QLabel("Disconnected")
        self._conn_status_label.setStyleSheet(f"color: {TEXT_SECONDARY}; font-size: 8.5pt;")

        pill_layout.addWidget(self._conn_status_icon)
        pill_layout.addWidget(self._conn_status_label)

        self._device_combo = QComboBox()
        self._device_combo.setMinimumWidth(160)
        self._device_combo.setFixedHeight(28)
        self._device_combo.addItem("Auto-detect Device")
        self._device_combo.setEnabled(False)
        
        self._btn_connect = QPushButton("Connect")
        self._btn_connect.setObjectName("btn_primary")
        self._btn_connect.setFixedHeight(28)
        self._btn_connect.clicked.connect(self._try_connect_device)
        
        self._btn_disconnect = QPushButton("Disconnect")
        self._btn_disconnect.setFixedHeight(28)
        self._btn_disconnect.clicked.connect(self._disconnect_device)
        self._btn_disconnect.setEnabled(False)

        # Subtle vertical divider
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.VLine)
        divider.setFrameShadow(QFrame.Shadow.Plain)
        divider.setStyleSheet(f"color: {BORDER};")

        self._sci_notation_cb = QCheckBox("Scientific notation (1.23e-04)")
        self._sci_notation_cb.setChecked(get_scientific_notation_preference())
        self._sci_notation_cb.toggled.connect(self._on_scientific_notation_toggled)
        self._sci_notation_cb.setStyleSheet(f"color: {TEXT_SECONDARY}; font-size: 8.5pt;")
        
        layout.addWidget(lbl_conn)
        layout.addWidget(self._conn_pill)
        layout.addSpacing(6)
        layout.addWidget(self._device_combo)
        layout.addWidget(self._btn_connect)
        layout.addWidget(self._btn_disconnect)
        layout.addSpacing(10)
        layout.addWidget(divider)
        layout.addStretch()
        layout.addWidget(self._sci_notation_cb)
        
        return toolbar

    @Slot(bool)
    def _on_scientific_notation_toggled(self, checked: bool) -> None:
        """Handle toggle between scientific notation and plain decimal display."""
        set_scientific_notation_preference(checked)
        self._activity_log.log(f"Display notation set to {'scientific (1.23e-04)' if checked else 'standard decimal'}.")
        if self._active_method:
            self._method_panel.set_method(self._active_method)
        if hasattr(self, "_last_report") and self._last_report:
            if hasattr(self, "_collected_points") and self._collected_points and self._current_config:
                if self._active_method is not None and self._active_method.status == "VALID":
                    report = interpret_with_method(
                        self._collected_points, self._current_config, self._active_method
                    )
                else:
                    report = interpret_full(
                        self._collected_points, self._current_config,
                        blank_stats=self._blank_store.get_stats(),
                        calibration=self._calibration.result,
                    )
                self._last_report = report
                self._banner.set_verdict(report.verdict, report.explanation)
                if report.sampling_time is not None:
                    self._plot_widget.set_sampling_marker(report.sampling_time, report.mean_current)

    def _update_status_bar(self, state: str, elapsed: float | None = None) -> None:
        """Update the bottom status bar."""
        dev = "PalmSens (Connected)" if self._dm.is_connected else "Disconnected"
        meth = self._active_method.name if self._active_method else "Legacy Mode"
        
        msg = f"Device: {dev}    |    Method: {meth}    |    Status: {state}"
        if elapsed is not None:
            msg += f"    |    Elapsed: {elapsed:.1f} s"
            
        self._status_bar.showMessage(msg)

    # -----------------------------------------------------------------------
    # Device discovery
    # -----------------------------------------------------------------------

    @Slot()
    def _try_connect_device(self) -> None:
        """Attempt device discovery and connection."""
        if self._dm.is_connected:
            self._dm.disconnect()

        try:
            devices = self._dm.list_devices()
        except DeviceNotFoundError:
            logger.warning("No device found during discovery.")
            self._activity_log.log("No potentiostat detected on USB.")
            self._show_no_device(True)
            return

        target = devices[0]
        try:
            self._dm.connect(target)
        except Exception as exc:
            logger.exception("Failed to connect to %s", target)
            self._activity_log.log(f"Connection failed to {target}: {exc}", level="ERROR")
            self._show_no_device(True)
            return

        logger.info("Connected to %s", target)
        self._activity_log.log(f"Successfully connected to potentiostat: {target}")
        self._show_no_device(False)

    def _show_no_device(self, show: bool) -> None:
        """Toggle between the no-device overlay and the normal UI."""
        has_completed_data = bool(self._collected_points and self._last_report is not None)

        # Do not hide the plot or show the blank overlay if we have completed measurement data
        if show and not has_completed_data:
            self._no_device_widget.setVisible(True)
            self._plot.setVisible(False)
        else:
            self._no_device_widget.setVisible(False)
            self._plot.setVisible(True)
        
        # Update connection UI states
        if show:
            if not has_completed_data:
                self._banner.set_verdict(None, "")
            self._conn_status_icon.setText("○")
            self._conn_status_icon.setStyleSheet(f"color: {ERROR}; font-weight: bold;")
            self._conn_status_label.setText("Disconnected")
            self._conn_status_label.setStyleSheet(f"color: {TEXT_SECONDARY};")
            self._conn_pill.setStyleSheet(
                f"#conn_pill {{ background-color: #FDF2F2; border: 1px solid #F8B4B4; border-radius: 4px; }}"
            )
            self._btn_connect.setEnabled(True)
            self._btn_disconnect.setEnabled(False)
            self._update_status_bar("Disconnected")
            if not has_completed_data:
                self._telemetry_panel.set_ready(0.0, 10.0)
        else:
            self._conn_status_icon.setText("●")
            self._conn_status_icon.setStyleSheet(f"color: {SUCCESS}; font-weight: bold;")
            self._conn_status_label.setText("Connected")
            self._conn_status_label.setStyleSheet(f"color: {SUCCESS}; font-weight: 600;")
            self._conn_pill.setStyleSheet(
                f"#conn_pill {{ background-color: #EBF7F0; border: 1px solid #A3D8B9; border-radius: 4px; }}"
            )
            self._btn_connect.setEnabled(False)
            self._btn_disconnect.setEnabled(True)
            self._update_status_bar("Ready")
            self._telemetry_panel.set_ready(self._control_panel.potential, self._control_panel.run_time)

    @Slot()
    def _disconnect_device(self) -> None:
        """Disconnect the currently connected device."""
        if self._dm.is_connected:
            self._dm.disconnect()
            self._activity_log.log("Potentiostat disconnected by user.")
        self._show_no_device(True)

    # -----------------------------------------------------------------------
    # Start / Stop
    # -----------------------------------------------------------------------

    @Slot(float, float)
    def _on_start_requested(self, potential: float, run_time: float) -> None:
        """Handle the Start button press."""
        # Force a device reconnect to clear stale internal SDK state
        self._try_connect_device()

        if not self._dm.is_connected:
            QMessageBox.warning(
                self, "Not Connected",
                "No potentiostat is connected. Please connect a device first.",
            )
            self._control_panel.set_running(False)
            return

        # Build config (interval_time is a hidden default).
        config = MeasurementConfig(
            potential=potential,
            run_time=run_time,
            interval_time=DEFAULT_INTERVAL_TIME,
        )
        self._current_config = config
        self._collected_points.clear()

        # Reset UI state for a fresh run.
        self._plot.clear()
        self._banner.set_verdict(None, "Measurement in progress…")
        self._session_bar.hide()
        self._control_panel.reset_elapsed()
        self._telemetry_panel.start_measuring(potential, run_time)
        self._activity_log.log(f"Acquisition started (E = {potential:+.3f} V, t = {run_time:.1f} s).")

        # Create a *fresh* engine every run
        self._engine = AcquisitionEngine(self._dm, config)
        self._engine.on_finished = self._on_engine_finished
        self._engine.start()

        self._poll_timer.start()
        logger.info("Measurement started via MainWindow.")

    @Slot()
    def _on_stop_requested(self) -> None:
        """Handle the Stop button press."""
        if self._engine is not None and self._engine.is_running:
            self._engine.stop()
            self._telemetry_panel.finish(len(self._collected_points), stopped=True)
            self._activity_log.log("Acquisition stop requested by user.", level="WARNING")
            logger.info("Stop requested via MainWindow.")

    @Slot(float)
    def _on_elapsed_updated(self, elapsed: float) -> None:
        self._update_status_bar("Measuring...", elapsed)

    # -----------------------------------------------------------------------
    # Data polling (GUI-thread timer)
    # -----------------------------------------------------------------------

    @Slot()
    def _poll_data_queue(self) -> None:
        """Drain the engine's data queue and feed points to the plot."""
        if self._engine is None:
            return

        batch = 0
        latest_dp: DataPoint | None = None
        while batch < 300:
            try:
                dp = self._engine.data_queue.get_nowait()
            except queue.Empty:
                break
            self._collected_points.append(dp)
            self._plot.add_point(dp.time, dp.current)
            latest_dp = dp
            batch += 1

        if latest_dp is not None:
            self._telemetry_panel.update_reading(
                elapsed=latest_dp.time,
                current=latest_dp.current,
                points=len(self._collected_points),
            )

        # Check if measurement is done and queue is empty.
        if not self._engine.is_running and self._engine.data_queue.empty():
            self._poll_timer.stop()
            self._finalize_measurement()

    # -----------------------------------------------------------------------
    # Measurement completion
    # -----------------------------------------------------------------------

    def _on_engine_finished(self, error: BaseException | None) -> None:
        """Called from the background thread when measurement ends."""
        if error is not None:
            logger.error("Engine reported error: %s", error)

    def _finalize_measurement(self) -> None:
        """Interpret results, update the banner, save session, re-enable controls."""
        config = self._current_config
        engine = self._engine

        if engine is None or config is None:
            return

        # Freeze elapsed timer at final value.
        self._control_panel.freeze_elapsed()

        # Check for engine-level error.
        if engine.error is not None:
            self._banner.set_verdict(
                Verdict.INCONCLUSIVE,
                f"Measurement error: {engine.error}",
            )
            self._telemetry_panel.finish(len(self._collected_points), is_error=True)
            self._activity_log.log(f"Acquisition error: {engine.error}", level="ERROR")
            self._control_panel.set_running(False)
            return

        # Interpret the collected data.
        if self._active_method is not None and self._active_method.status == "VALID":
            report = interpret_with_method(
                self._collected_points, config, self._active_method
            )
        else:
            report = interpret_full(
                self._collected_points, config,
                blank_stats=self._blank_store.get_stats(),
                calibration=self._calibration.result
            )
        self._last_report = report
        self._banner.set_verdict(report.verdict, report.explanation)

        if report.sampling_time is not None:
            self._plot.set_sampling_marker(report.sampling_time, report.mean_current)
            self._activity_log.log(
                f"Stabilized current sampled at t={report.sampling_time:.1f} s: {report.mean_current:.4f} µA."
            )
        
        last_val = self._collected_points[-1].current if self._collected_points else None
        self._telemetry_panel.finish(len(self._collected_points), final_current=last_val)
        self._activity_log.log(
            f"Measurement complete ({len(self._collected_points)} points). Verdict: {report.verdict.value}."
        )
        logger.info("Verdict: %s — %s", report.verdict.value, report.explanation)

        # Auto-save session.
        try:
            ts = datetime.now()
            path = save_session(
                config=config,
                data_points=self._collected_points,
                verdict=report.verdict,
                explanation=report.explanation,
                timestamp=ts,
            )
            self._last_saved_path = path
            self._activity_log.log(f"Session auto-saved to {path.name}.")
            logger.info("Session saved: %s", path)

            # Show session toolbar.
            self._saved_label.setText(f"Saved: {path.name}")
            self._session_bar.show()
        except Exception as exc:
            logger.exception("Failed to save session.")
            self._activity_log.log(f"Failed to auto-save session: {exc}", level="ERROR")

        # Re-enable controls for the next measurement.
        self._control_panel.set_running(False)

    # -----------------------------------------------------------------------
    # Session-action handlers
    # -----------------------------------------------------------------------

    @Slot()
    def _on_record_blank(self) -> None:
        """Save the current measurement as a blank standard."""
        if self._last_report is None or self._last_report.mean_current == 0.0:
            return

        current = self._last_report.mean_current
        self._blank_store.add_blank(current)
        self._activity_log.log(f"Blank standard recorded: {current:.4f} µA (Total blanks: {self._blank_store.count}).")
        
        QMessageBox.information(
            self, "Blank Recorded",
            f"Recorded blank current: {current:.4f} µA\n\n"
            f"Total blanks in store: {self._blank_store.count}"
        )

    @Slot()
    def _on_add_calibration(self) -> None:
        """Prompt for concentration and add to the calibration curve."""
        if self._last_report is None or self._last_report.mean_current == 0.0:
            return

        unit = self._calibration.concentration_unit
        conc, ok = QInputDialog.getDouble(
            self, "Add Calibration Standard",
            f"Enter known concentration ({unit}):",
            0.0, 0.0, 1e6, 4
        )

        if ok:
            current = self._last_report.mean_current
            self._calibration.add_point(conc, current)
            result = self._calibration.fit()
            self._activity_log.log(f"Calibration standard added: {conc} {unit} → {current:.4f} µA.")
            
            msg = f"Added calibration point:\n{conc} {unit} → {current:.4f} µA\n\n"
            msg += f"Total points: {self._calibration.count}\n"
            if result:
                msg += f"Current fit: R² = {result.r_squared:.4f}"
            else:
                msg += "Need more points for a valid fit."

            QMessageBox.information(self, "Calibration Point Added", msg)

    @Slot()
    def _on_open_file(self) -> None:
        """Open the saved CSV in its default application."""
        if self._last_saved_path and self._last_saved_path.exists():
            os.startfile(self._last_saved_path)  # type: ignore[attr-defined]

    @Slot()
    def _on_open_folder(self) -> None:
        """Open Windows Explorer with the saved file selected."""
        if self._last_saved_path and self._last_saved_path.exists():
            subprocess.Popen(
                ["explorer", "/select,", str(self._last_saved_path)],
            )

    @Slot()
    def _on_export_excel(self) -> None:
        """Export the saved session to Excel and open the result."""
        if self._last_saved_path is None or not self._last_saved_path.exists():
            return

        xlsx_path = self._last_saved_path.with_suffix(".xlsx")
        try:
            result = export_to_excel(self._last_saved_path, xlsx_path)
            self._activity_log.log(f"Exported session to Excel: {xlsx_path.name}")
            logger.info("Excel export: %s", result)
            os.startfile(result)  # type: ignore[attr-defined]
        except Exception as e:
            logger.exception("Excel export failed.")
            self._activity_log.log(f"Excel export failed: {e}", level="ERROR")
            QMessageBox.warning(
                self, "Export Failed",
                f"Could not export to Excel.\n\n"
                f"Error: {e}\n\n"
                f"If you already have the file open in Excel, please close it "
                f"first, as Excel locks the file.",
            )

    # -----------------------------------------------------------------------
    # Method Management Handlers
    # -----------------------------------------------------------------------

    @Slot()
    def _on_load_method(self) -> None:
        """Prompt to load an analytical method from JSON."""
        from PySide6.QtWidgets import QFileDialog
        from config.settings import METHODS_FOLDER
        
        path, _ = QFileDialog.getOpenFileName(
            self, "Load Analytical Method", METHODS_FOLDER, "Method Files (*.json);;All Files (*.*)"
        )
        if path:
            try:
                method = load_method(path)
                self._active_method = method
                self._method_panel.set_method(method)
                self._activity_log.log(f"Loaded method: {method.name} v{method.version} ({method.analyte}).")
                logger.info("Loaded method: %s v%s", method.name, method.version)
            except Exception as exc:
                QMessageBox.critical(self, "Load Error", f"Failed to load method:\n\n{exc}")
                self._activity_log.log(f"Failed to load method from {path}: {exc}", level="ERROR")
                logger.exception("Failed to load method from %s", path)

    @Slot()
    def _on_new_method(self) -> None:
        """Launch the method builder wizard."""
        self._wizard = ImportWizard(self)
        self._wizard.method_created.connect(self._on_method_created)
        self._wizard.show()

    @Slot(AnalyticalMethod)
    def _on_method_created(self, method: AnalyticalMethod) -> None:
        """Handle a newly created method from the wizard."""
        self._active_method = method
        self._method_panel.set_method(method)
        self._activity_log.log(f"Created and activated method: {method.name} v{method.version}.")
        QMessageBox.information(
            self, "Method Activated",
            f"Method '{method.name}' activated successfully."
        )

    @Slot()
    def _on_deactivate_method(self) -> None:
        """Deactivate the current method and revert to legacy cutoffs."""
        self._active_method = None
        self._method_panel.set_method(None)
        self._activity_log.log("Method deactivated. Reverted to legacy mode.")
        logger.info("Active method deactivated. Reverted to legacy mode.")

    def closeEvent(self, event) -> None:  # noqa: N802
        """Ensure we stop measurements and disconnect on window close."""
        self._poll_timer.stop()

        if self._engine is not None and self._engine.is_running:
            self._engine.stop()
            self._engine.finished_event.wait(timeout=3.0)

        if self._dm.is_connected:
            self._dm.disconnect()

        super().closeEvent(event)
