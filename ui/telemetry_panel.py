"""Live telemetry and acquisition status panel.

Displays real-time instrument metrics during chronoamperometry runs:
elapsed time, progress bar, live current reading, collected points count,
and applied potential setpoint.
"""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QProgressBar,
    QVBoxLayout,
    QWidget,
    QFrame,
)

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


def _format_current(val: float | None) -> str:
    if val is None:
        return "-- µA"
    abs_v = abs(val)
    if abs_v >= 1e6:
        return f"{val * 1e-6:+.4f} A"
    elif abs_v >= 1e3:
        return f"{val * 1e-3:+.4f} mA"
    elif abs_v >= 1.0 or abs_v == 0.0:
        return f"{val:+.4f} µA"
    elif abs_v >= 1e-3:
        return f"{val * 1e3:+.4f} nA"
    else:
        return f"{val * 1e6:+.4f} pA"


class TelemetryPanel(QGroupBox):
    """Panel displaying real-time acquisition status, progress, and telemetry metrics."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("LIVE TELEMETRY", parent)
        self._target_time = 10.0
        self._target_potential = 0.0
        self._points_count = 0
        self.setFixedHeight(155)
        self._build_ui()
        self.set_ready()

    def _build_ui(self) -> None:
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 6, 10, 8)
        main_layout.setSpacing(6)

        # 1. Status row
        status_row = QHBoxLayout()
        status_row.setContentsMargins(0, 0, 0, 0)

        self._lbl_status_badge = QLabel("● Ready")
        self._lbl_status_badge.setStyleSheet(
            f"background-color: {PANEL_SECONDARY_BG}; color: {SUCCESS}; "
            f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
        )

        self._lbl_rate = QLabel("10 Hz (100 ms)")
        self._lbl_rate.setObjectName("secondary")
        self._lbl_rate.setStyleSheet(
            f"color: {TEXT_SECONDARY}; font-size: 8pt; padding: 2px 4px;"
        )

        status_row.addWidget(self._lbl_status_badge)
        status_row.addStretch()
        status_row.addWidget(self._lbl_rate)

        # 2. Progress bar
        self._progress_bar = QProgressBar()
        self._progress_bar.setRange(0, 100)
        self._progress_bar.setValue(0)
        self._progress_bar.setTextVisible(True)
        self._progress_bar.setFormat("%p%")
        self._progress_bar.setFixedHeight(13)

        # 3. Telemetry metrics container
        grid_container = QFrame()
        grid_container.setObjectName("telemetry_grid")
        grid_container.setFixedHeight(54)
        grid_container.setStyleSheet(
            f"#telemetry_grid {{ background-color: #F8FAFD; border: 1px solid #D5DFE8; border-left: 3px solid {ACCENT_CYAN}; border-radius: 4px; }}"
        )
        grid_layout = QGridLayout(grid_container)
        grid_layout.setContentsMargins(8, 4, 8, 4)
        grid_layout.setHorizontalSpacing(16)
        grid_layout.setVerticalSpacing(4)
        grid_layout.setColumnStretch(0, 1)
        grid_layout.setColumnStretch(1, 1)

        self._lbl_elapsed_val = QLabel("Elapsed: <b>0.0 / 10.0 s</b>")
        self._lbl_elapsed_val.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt;")

        self._lbl_curr_val = QLabel("Current: <b>-- µA</b>")
        self._lbl_curr_val.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt;")

        self._lbl_points_val = QLabel("Points: <b>0 pts</b>")
        self._lbl_points_val.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt;")

        self._lbl_pot_val = QLabel("Potential: <b>0.000 V</b>")
        self._lbl_pot_val.setStyleSheet(f"color: {TEXT}; font-size: 8.5pt;")

        grid_layout.addWidget(self._lbl_elapsed_val, 0, 0)
        grid_layout.addWidget(self._lbl_curr_val, 0, 1)
        grid_layout.addWidget(self._lbl_points_val, 1, 0)
        grid_layout.addWidget(self._lbl_pot_val, 1, 1)

        main_layout.addLayout(status_row)
        main_layout.addWidget(self._progress_bar)
        main_layout.addWidget(grid_container)

    def set_ready(self, potential: float = 0.0, run_time: float = 10.0) -> None:
        """Reset telemetry to ready state."""
        self._target_time = max(0.1, run_time)
        self._target_potential = potential
        self._points_count = 0

        self._lbl_status_badge.setText("● Ready")
        self._lbl_status_badge.setStyleSheet(
            f"background-color: {PANEL_SECONDARY_BG}; color: {SUCCESS}; "
            f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
        )
        self._progress_bar.setValue(0)
        self._lbl_elapsed_val.setText(f"Elapsed:  <b>0.0 / {self._target_time:.1f} s</b>")
        self._lbl_curr_val.setText("Current:  <b>-- µA</b>")
        self._lbl_points_val.setText("Points:  <b>0 pts</b>")
        self._lbl_pot_val.setText(f"Potential:  <b>{self._target_potential:+.3f} V</b>")

    def start_measuring(self, potential: float, run_time: float) -> None:
        """Configure and show measuring state."""
        self._target_time = max(0.1, run_time)
        self._target_potential = potential
        self._points_count = 0

        self._lbl_status_badge.setText("● Measuring...")
        self._lbl_status_badge.setStyleSheet(
            f"background-color: {ACCENT_CYAN_LIGHT}; color: {ACCENT_CYAN_DARK}; "
            f"border: 1px solid {ACCENT_CYAN_BORDER}; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
        )
        self._progress_bar.setValue(0)
        self._lbl_pot_val.setText(f"Potential:  <b>{self._target_potential:+.3f} V</b>")
        self._lbl_elapsed_val.setText(f"Elapsed:  <b>0.0 / {self._target_time:.1f} s</b>")
        self._lbl_curr_val.setText("Current:  <b>-- µA</b>")
        self._lbl_points_val.setText("Points:  <b>0 pts</b>")

    def update_reading(self, elapsed: float, current: float | None = None, points: int | None = None) -> None:
        """Update live values during measurement."""
        if points is not None:
            self._points_count = points
            self._lbl_points_val.setText(f"Points:  <b>{points} pts</b>")

        if current is not None:
            self._lbl_curr_val.setText(
                f"Current:  <b><font color='{ACCENT_CYAN_DARK}'>{_format_current(current)}</font></b>"
            )

        pct = min(100, int((elapsed / self._target_time) * 100)) if self._target_time > 0 else 0
        self._progress_bar.setValue(pct)
        self._lbl_elapsed_val.setText(f"Elapsed:  <b>{elapsed:.1f} / {self._target_time:.1f} s</b>")

    def finish(self, points: int, final_current: float | None = None, is_error: bool = False, stopped: bool = False) -> None:
        """Mark acquisition as finished."""
        self._points_count = points
        self._lbl_points_val.setText(f"Points:  <b>{points} pts</b>")
        if final_current is not None:
            self._lbl_curr_val.setText(f"Current:  <b>{_format_current(final_current)}</b>")

        if is_error:
            self._lbl_status_badge.setText("✕ Error")
            self._lbl_status_badge.setStyleSheet(
                f"background-color: #FDE8E8; color: {ERROR}; "
                f"border: 1px solid #F8B4B4; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
            )
        elif stopped:
            self._lbl_status_badge.setText("■ Stopped")
            self._lbl_status_badge.setStyleSheet(
                f"background-color: {PANEL_SECONDARY_BG}; color: {TEXT_SECONDARY}; "
                f"border: 1px solid {BORDER}; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
            )
        else:
            self._progress_bar.setValue(100)
            self._lbl_status_badge.setText("✓ Complete")
            self._lbl_status_badge.setStyleSheet(
                f"background-color: #EBF7F0; color: {SUCCESS}; "
                f"border: 1px solid #A3D8B9; border-radius: 3px; padding: 2px 8px; font-weight: bold; font-size: 8.5pt;"
            )
