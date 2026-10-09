"""Sidebar controls for measurement parameters and run actions.

Exposes user-editable parameters (applied potential and run time) plus
Start / Stop buttons and live elapsed-time tracking.
"""

from __future__ import annotations

import logging
import time

from PySide6.QtCore import QTimer, Signal, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QDoubleSpinBox,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from config.settings import DEFAULT_POTENTIAL, DEFAULT_RUN_TIME, DEFAULT_INTERVAL_TIME
from ui.theme import (
    ACCENT_CYAN,
    ACCENT_CYAN_LIGHT,
    ACCENT_CYAN_BORDER,
    ACCENT_PRIMARY,
    BORDER,
    TEXT,
    TEXT_SECONDARY,
)

logger = logging.getLogger(__name__)


class ControlPanel(QWidget):
    """Sidebar widget for measurement configuration and run control.

    Signals
    -------
    start_requested(potential: float, run_time: float)
        Emitted when the user clicks **Start**.
    stop_requested()
        Emitted when the user clicks **Stop**.
    elapsed_updated(elapsed: float)
        Emitted periodically while a measurement is active.
    """

    start_requested = Signal(float, float)
    stop_requested = Signal()
    elapsed_updated = Signal(float)

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._start_time: float | None = None
        self._build_ui()
        self._connect_signals()

        # Elapsed-time refresh timer (~10 Hz).
        self._elapsed_timer = QTimer(self)
        self._elapsed_timer.setInterval(100)
        self._elapsed_timer.timeout.connect(self._update_elapsed)

    # -- UI construction ----------------------------------------------------

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # --- Measurement Group Box -----------------------------------------
        params_group = QGroupBox("MEASUREMENT")
        group_layout = QVBoxLayout(params_group)
        group_layout.setContentsMargins(10, 14, 10, 10)
        group_layout.setSpacing(8)

        # Inputs Form
        params_layout = QFormLayout()
        params_layout.setContentsMargins(0, 0, 0, 0)
        params_layout.setHorizontalSpacing(10)
        params_layout.setVerticalSpacing(8)
        params_layout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        self._potential_spin = QDoubleSpinBox()
        self._potential_spin.setRange(-5.0, 5.0)
        self._potential_spin.setDecimals(3)
        self._potential_spin.setSingleStep(0.01)
        self._potential_spin.setSuffix(" V")
        self._potential_spin.setValue(DEFAULT_POTENTIAL)
        self._potential_spin.setFixedHeight(26)
        
        lbl_potential = QLabel("Applied potential (V):")
        lbl_potential.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt; font-weight: 500;")
        params_layout.addRow(lbl_potential, self._potential_spin)

        self._run_time_spin = QDoubleSpinBox()
        self._run_time_spin.setRange(0.1, 3600.0)
        self._run_time_spin.setDecimals(1)
        self._run_time_spin.setSingleStep(1.0)
        self._run_time_spin.setSuffix(" s")
        self._run_time_spin.setValue(DEFAULT_RUN_TIME)
        self._run_time_spin.setFixedHeight(26)

        lbl_run_time = QLabel("Run time (s):")
        lbl_run_time.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt; font-weight: 500;")
        params_layout.addRow(lbl_run_time, self._run_time_spin)

        # Action buttons
        self._start_btn = QPushButton("Start Measurement")
        self._start_btn.setObjectName("btn_primary")
        self._start_btn.setFixedHeight(30)
        font_start = QFont()
        font_start.setBold(True)
        self._start_btn.setFont(font_start)

        self._stop_btn = QPushButton("Stop")
        self._stop_btn.setObjectName("btn_stop")
        self._stop_btn.setFixedHeight(30)
        self._stop_btn.setEnabled(False)

        btn_layout = QHBoxLayout()
        btn_layout.setContentsMargins(0, 4, 0, 0)
        btn_layout.setSpacing(8)
        btn_layout.addWidget(self._start_btn, stretch=3)
        btn_layout.addWidget(self._stop_btn, stretch=2)

        group_layout.addLayout(params_layout)
        group_layout.addLayout(btn_layout)

        root.addWidget(params_group)

    def _connect_signals(self) -> None:
        self._start_btn.clicked.connect(self._on_start_clicked)
        self._stop_btn.clicked.connect(self._on_stop_clicked)

    # -- Slot handlers -------------------------------------------------------

    def _on_start_clicked(self) -> None:
        potential = self._potential_spin.value()
        run_time = self._run_time_spin.value()
        logger.info("Start requested: potential=%.3f V, run_time=%.1f s",
                     potential, run_time)
        self.set_running(True)
        self.start_requested.emit(potential, run_time)

    def _on_stop_clicked(self) -> None:
        logger.info("Stop requested.")
        self.stop_requested.emit()

    # -- Elapsed time --------------------------------------------------------

    def _update_elapsed(self) -> None:
        """Refresh the elapsed-time (called by timer at ~10 Hz)."""
        if self._start_time is not None:
            elapsed = time.monotonic() - self._start_time
            self.elapsed_updated.emit(elapsed)

    def reset_elapsed(self) -> None:
        """Reset the elapsed counter to 0.0 s and start ticking."""
        self._start_time = time.monotonic()
        self.elapsed_updated.emit(0.0)
        self._elapsed_timer.start()

    def freeze_elapsed(self) -> None:
        """Stop the elapsed counter at its current value."""
        self._elapsed_timer.stop()
        self._update_elapsed()

    # -- Public helpers ------------------------------------------------------

    def set_running(self, running: bool) -> None:
        """Toggle the widget between *running* and *idle* states."""
        self._start_btn.setEnabled(not running)
        self._potential_spin.setEnabled(not running)
        self._run_time_spin.setEnabled(not running)
        self._stop_btn.setEnabled(running)

    @property
    def potential(self) -> float:
        return self._potential_spin.value()

    @property
    def run_time(self) -> float:
        return self._run_time_spin.value()
