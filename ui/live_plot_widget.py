"""Real-time XY plot widget for streaming chronoamperometry data.

Uses pyqtgraph for high-performance rendering and pglive's
:class:`DataConnector` for thread-safe data ingestion — the acquisition
callback fires on a background thread and ``add_point()`` can be called
safely from *any* thread.
"""

from __future__ import annotations

import logging

from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QFont
import pyqtgraph as pg

# pglive 0.5.x references np.VisibleDeprecationWarning which was removed in
# numpy 2.x. Patch it back to avoid an AttributeError on import.
import numpy as np
if not hasattr(np, "VisibleDeprecationWarning"):
    np.VisibleDeprecationWarning = DeprecationWarning  # type: ignore[attr-defined]

import math

from pglive.sources.data_connector import DataConnector
from pglive.sources.live_plot import LiveLinePlot
from pglive.sources.live_plot_widget import LivePlotWidget as _PgLivePlotWidget

from ui.theme import (
    PLOT_BG,
    PLOT_TRACE,
    PLOT_GRID,
    TEXT,
    TEXT_SECONDARY,
    BORDER,
    ACCENT_CYAN,
    ACCENT_CYAN_LIGHT,
    ACCENT_CYAN_BORDER,
    ACCENT_PRIMARY,
)

logger = logging.getLogger(__name__)


class CurrentAxisItem(pg.AxisItem):
    """Adaptive Y-axis for chronoamperometry current measurements.

    Features:
    - Automatically adjusts units (A, mA, µA, nA, pA) based on the current
      visible Y-range.
    - Prevents scientific notation (e.g. 1e-06, -4e+07) by formatting tick values
      directly in fixed decimal notation tailored to the active unit.
    - Automatically updates the axis title to reflect the active unit
      (e.g., 'Current (nA)', 'Current (µA)', 'Current (mA)', 'Current (A)').
    """

    def __init__(
        self,
        orientation: str = "left",
        label_color: str = TEXT,
        *args,
        **kwargs,
    ) -> None:
        self.current_unit = "µA"
        self.scale_factor = 1.0
        self.label_color = label_color
        super().__init__(orientation, *args, **kwargs)
        self.enableAutoSIPrefix(False)
        self.setLabel(f"Current ({self.current_unit})", color=self.label_color)

    def setRange(self, mn: float, mx: float) -> None:
        super().setRange(mn, mx)
        self._update_unit(mn, mx)

    def on_view_range_changed(self, view: Any, y_range: tuple[float, float]) -> None:
        self._update_unit(y_range[0], y_range[1])

    def _update_unit(self, mn: float, mx: float) -> None:
        peak = max(abs(mn), abs(mx))
        if peak <= 0:
            target = "µA"
        elif peak >= 1e6:
            target = "A"
        elif peak >= 1e3:
            target = "mA"
        elif peak >= 1.0:
            target = "µA"
        elif peak >= 1e-3:
            target = "nA"
        else:
            target = "pA"

        # Hysteresis to prevent jitter near unit boundaries
        if self.current_unit == "A" and peak >= 8e5:
            target = "A"
        elif self.current_unit == "mA" and 800.0 <= peak < 1e6:
            target = "mA"
        elif self.current_unit == "µA" and 0.8 <= peak < 1000.0:
            target = "µA"
        elif self.current_unit == "nA" and 0.0008 <= peak < 1.0:
            target = "nA"

        scales = {
            "A": 1e-6,
            "mA": 1e-3,
            "µA": 1.0,
            "nA": 1e3,
            "pA": 1e6,
        }
        factor = scales[target]

        if target != self.current_unit or factor != self.scale_factor:
            self.current_unit = target
            self.scale_factor = factor
            self.setLabel(f"Current ({target})", color=self.label_color)
            self.picture = None
            self.update()

    def tickStrings(self, values: list[float], scale: float, spacing: float) -> list[str]:
        scaled_spacing = spacing * self.scale_factor
        if scaled_spacing > 0:
            places = max(0, math.ceil(-math.log10(scaled_spacing) - 1e-6))
        else:
            places = 0
        places = min(places, 6)

        strings: list[str] = []
        for v in values:
            vs = v * self.scale_factor
            if abs(vs) < 1e-12:
                vs = 0.0
            strings.append(f"{vs:.{places}f}")
        return strings

    def reset(self) -> None:
        self.current_unit = "µA"
        self.scale_factor = 1.0
        self.setLabel(f"Current ({self.current_unit})", color=self.label_color)
        self.picture = None
        self.update()


class LivePlotWidget(QWidget):
    """A real-time XY plot that displays time vs. current.

    Parameters
    ----------
    max_points : int
        Maximum number of points kept in the visible buffer.
    update_rate : int
        How many times per second the plot redraws (Hz).
    parent : QWidget | None
        Optional parent widget.
    """

    def __init__(
        self,
        max_points: int = 2000,
        update_rate: int = 30,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        # Container frame for unified scientific appearance
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)

        # --- Plot Header Toolbar -----------------------------------------
        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(4, 8, 0, 4)
        toolbar_layout.setSpacing(6)

        title_lbl = QLabel("Chronoamperometry Plot")
        title_font = QFont()
        title_font.setBold(True)
        title_font.setPointSize(9)
        title_lbl.setFont(title_font)
        title_lbl.setStyleSheet(f"color: {TEXT_SECONDARY};")

        btn_auto = QPushButton("Auto Range")
        btn_auto.setFixedHeight(24)
        btn_auto.clicked.connect(self._on_auto_range)

        btn_reset = QPushButton("Reset View")
        btn_reset.setFixedHeight(24)
        btn_reset.clicked.connect(self._on_reset_view)

        btn_grid = QPushButton("Toggle Grid")
        btn_grid.setFixedHeight(24)
        btn_grid.clicked.connect(self._on_toggle_grid)

        btn_clear = QPushButton("Clear")
        btn_clear.setFixedHeight(24)
        btn_clear.clicked.connect(self.clear)

        toolbar_layout.addWidget(title_lbl)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(btn_auto)
        toolbar_layout.addWidget(btn_reset)
        toolbar_layout.addWidget(btn_grid)
        toolbar_layout.addWidget(btn_clear)

        # --- pyqtgraph / pglive setup ------------------------------------
        self._left_axis = CurrentAxisItem("left", label_color=TEXT)
        self._plot_widget = _PgLivePlotWidget(axisItems={"left": self._left_axis})
        self._plot_widget.setBackground(PLOT_BG)

        # Axis labels and styling
        bottom_axis = self._plot_widget.getAxis("bottom")
        left_axis = self._left_axis

        axis_font = QFont("Segoe UI", 9)
        bottom_axis.setStyle(tickFont=axis_font)
        left_axis.setStyle(tickFont=axis_font)

        bottom_axis.setLabel("Time (s)", color=TEXT)

        bottom_axis.setPen(BORDER)
        bottom_axis.setTextPen(TEXT)
        left_axis.setPen(BORDER)
        left_axis.setTextPen(TEXT)

        # Disable automatic SI-prefix notation
        left_axis.enableAutoSIPrefix(False)
        bottom_axis.enableAutoSIPrefix(False)

        # Connect view range changes to update units dynamically
        self._plot_widget.getViewBox().sigYRangeChanged.connect(self._left_axis.on_view_range_changed)

        # Light gridlines
        self._plot_widget.showGrid(x=True, y=True, alpha=0.3)
        self._grid_visible = True

        # Vibrant scientific cyan/blue trace line
        trace_color = PLOT_TRACE if PLOT_TRACE else "#157A9E"
        self._curve = LiveLinePlot(pen=pg.mkPen(color=trace_color, width=2.2))
        self._plot_widget.addItem(self._curve)

        self._plot_widget.getViewBox().enableAutoRange(x=True, y=True)

        # Border frame around plot widget
        plot_frame = QFrame()
        plot_frame.setObjectName("panel")
        plot_frame.setStyleSheet(
            f"QFrame#panel {{ background-color: #FFFFFF; border: 1px solid {BORDER}; border-radius: 6px; }}"
        )
        pf_layout = QVBoxLayout(plot_frame)
        pf_layout.setContentsMargins(2, 2, 2, 2)
        pf_layout.addWidget(self._plot_widget)

        layout.addWidget(toolbar)
        layout.addWidget(plot_frame, stretch=1)

        # Sampling marker (vertical line + highlight point at stabilized time e.g. 185s)
        self._sampling_line: pg.InfiniteLine | None = None
        self._sampling_scatter: pg.ScatterPlotItem | None = None

        # DataConnector
        self._connector = DataConnector(
            self._curve,
            max_points=max_points,
            update_rate=update_rate,
        )

    # -- public API --------------------------------------------------------

    @property
    def current_unit(self) -> str:
        """The currently active current display unit (A, mA, µA, nA, pA)."""
        return self._left_axis.current_unit

    def add_point(self, time: float, current: float) -> None:
        """Append a single data point."""
        self._connector.cb_append_data_point(current, time)

    def set_sampling_marker(self, time_s: float, current_val: float | None = None) -> None:
        """Draw a visual marker at the stabilized sampling point (e.g. 185 s)."""
        if self._sampling_line is not None:
            self._plot_widget.removeItem(self._sampling_line)
            self._sampling_line = None
        if self._sampling_scatter is not None:
            self._plot_widget.removeItem(self._sampling_scatter)
            self._sampling_scatter = None

        pen = pg.mkPen(color="#D32F2F", width=1.5, style=Qt.PenStyle.DashLine)
        self._sampling_line = pg.InfiniteLine(
            pos=time_s,
            angle=90,
            pen=pen,
            label=f"Stabilized ({time_s:.0f}s)",
            labelOpts={"color": "#D32F2F", "position": 0.92, "movable": False},
        )
        self._plot_widget.addItem(self._sampling_line)

        if current_val is not None:
            self._sampling_scatter = pg.ScatterPlotItem(
                [{"pos": (time_s, current_val), "brush": "#D32F2F", "pen": pg.mkPen("#FFFFFF", width=1.5), "size": 9, "symbol": "o"}]
            )
            self._plot_widget.addItem(self._sampling_scatter)

    def clear(self) -> None:
        """Clear all data and reset the plot for a new measurement."""
        self._connector.cb_set_data([], [])
        self._curve.setData([], [])
        self._left_axis.reset()
        if self._sampling_line is not None:
            self._plot_widget.removeItem(self._sampling_line)
            self._sampling_line = None
        if self._sampling_scatter is not None:
            self._plot_widget.removeItem(self._sampling_scatter)
            self._sampling_scatter = None

    @Slot()
    def _on_auto_range(self) -> None:
        self._plot_widget.getViewBox().enableAutoRange(x=True, y=True)

    @Slot()
    def _on_reset_view(self) -> None:
        self._plot_widget.getViewBox().autoRange()

    @Slot()
    def _on_toggle_grid(self) -> None:
        self._grid_visible = not self._grid_visible
        self._plot_widget.showGrid(x=self._grid_visible, y=self._grid_visible, alpha=0.3)

    # -- cleanup -----------------------------------------------------------

    def closeEvent(self, event) -> None:  # noqa: N802
        self._connector.pause()
        super().closeEvent(event)
