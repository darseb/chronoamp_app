"""Dockable widget displaying the active analytical method status."""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFrame,
)

from interpretation.method import AnalyticalMethod
from ui.theme import (
    ACCENT_CYAN,
    ACCENT_CYAN_LIGHT,
    ACCENT_CYAN_BORDER,
    ACCENT_CYAN_DARK,
    PANEL_BG,
    PANEL_SECONDARY_BG,
    BORDER,
    SUCCESS,
    ERROR,
    TEXT,
    TEXT_SECONDARY,
)
from utils.formatting import format_concentration


class MethodPanel(QGroupBox):
    """A group box showing the currently active Analytical Method.

    Emits signals when the user wants to load a new method, create one,
    or deactivate the current one.
    """

    load_requested = Signal()
    new_requested = Signal()
    deactivate_requested = Signal()

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("ANALYTICAL METHOD", parent)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 14, 10, 10)
        layout.setSpacing(8)

        # 1. Title & Badge Row
        title_row = QHBoxLayout()
        title_row.setContentsMargins(0, 0, 0, 0)
        title_row.setSpacing(8)

        self._lbl_badge = QLabel("○ LEGACY MODE")
        self._lbl_badge.setStyleSheet(
            f"background-color: {PANEL_SECONDARY_BG}; color: {TEXT_SECONDARY}; "
            f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 7px; "
            f"font-size: 8pt; font-weight: bold;"
        )

        self._lbl_name = QLabel("No analytical method loaded")
        name_font = QFont()
        name_font.setBold(True)
        name_font.setPointSize(9)
        self._lbl_name.setFont(name_font)

        title_row.addWidget(self._lbl_badge)
        title_row.addWidget(self._lbl_name, stretch=1)

        # 2. Details Box
        self._details_frame = QFrame()
        self._details_frame.setStyleSheet(
            f"background-color: #F8FAFD; border: 1px solid #E2EBF2; border-left: 3px solid {ACCENT_CYAN}; border-radius: 4px;"
        )
        details_layout = QVBoxLayout(self._details_frame)
        details_layout.setContentsMargins(10, 7, 10, 7)
        details_layout.setSpacing(2)

        self._lbl_details = QLabel("Acquisition uses configured legacy thresholds.")
        self._lbl_details.setStyleSheet(f"color: {TEXT_SECONDARY}; font-size: 8.5pt;")
        self._lbl_details.setWordWrap(True)
        details_layout.addWidget(self._lbl_details)

        # 3. Actions Row
        action_layout = QHBoxLayout()
        action_layout.setContentsMargins(0, 0, 0, 0)
        action_layout.setSpacing(6)

        self._btn_load = QPushButton("Load Method")
        self._btn_load.setFixedHeight(26)
        self._btn_new = QPushButton("New Calibration")
        self._btn_new.setFixedHeight(26)
        self._btn_deactivate = QPushButton("Deactivate")
        self._btn_deactivate.setFixedHeight(26)
        self._btn_deactivate.setObjectName("btn_stop")
        self._btn_deactivate.setVisible(False)

        self._btn_load.clicked.connect(self.load_requested.emit)
        self._btn_new.clicked.connect(self.new_requested.emit)
        self._btn_deactivate.clicked.connect(self.deactivate_requested.emit)

        action_layout.addWidget(self._btn_load)
        action_layout.addWidget(self._btn_new)
        action_layout.addWidget(self._btn_deactivate)

        layout.addLayout(title_row)
        layout.addWidget(self._details_frame)
        layout.addLayout(action_layout)

    def set_method(self, method: AnalyticalMethod | None) -> None:
        """Update the panel to display the given method, or fallback to legacy."""
        if method is None:
            self._lbl_badge.setText("○ LEGACY MODE")
            self._lbl_badge.setStyleSheet(
                f"background-color: {PANEL_SECONDARY_BG}; color: {TEXT_SECONDARY}; "
                f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 7px; "
                f"font-size: 8pt; font-weight: bold;"
            )
            self._lbl_name.setText("No analytical method loaded")
            self._lbl_details.setText("Acquisition uses configured legacy thresholds.")
            self._btn_deactivate.setVisible(False)
            return

        self._lbl_name.setText(f"{method.name} v{method.version}")

        if method.status == "VALID":
            self._lbl_badge.setText("● ACTIVE")
            self._lbl_badge.setStyleSheet(
                f"background-color: {ACCENT_CYAN_LIGHT}; color: {ACCENT_CYAN_DARK}; "
                f"border: 1px solid {ACCENT_CYAN_BORDER}; border-radius: 3px; padding: 2px 7px; "
                f"font-size: 8pt; font-weight: bold;"
            )
        else:
            self._lbl_badge.setText("● INVALID")
            self._lbl_badge.setStyleSheet(
                f"background-color: #FDE8E8; color: {ERROR}; "
                f"border: 1px solid #F8B4B4; border-radius: 3px; padding: 2px 7px; "
                f"font-size: 8pt; font-weight: bold;"
            )

        details = f"Analyte: <b>{method.analyte}</b>"
        if method.lod:
            lod_str = (
                format_concentration(method.lod.concentration, unit=method.concentration_unit)
                if method.lod.concentration is not None
                else f"{method.lod.current_ua:.4g} µA"
            )
            details += f"  |  LOD: <b>{lod_str}</b>"
        if method.calibration_range:
            c_min_str = format_concentration(method.calibration_range[0])
            c_max_str = format_concentration(method.calibration_range[1], unit=method.concentration_unit)
            details += f"  |  Range: <b>{c_min_str} – {c_max_str}</b>"

        self._lbl_details.setText(details)
        self._btn_deactivate.setVisible(True)
