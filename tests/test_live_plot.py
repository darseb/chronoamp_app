"""Unit tests for CurrentAxisItem and dynamic current unit scaling."""

from __future__ import annotations

import pytest
from PySide6.QtWidgets import QApplication

from ui.live_plot_widget import CurrentAxisItem
from ui.telemetry_panel import _format_current


@pytest.fixture(scope="module")
def qapp() -> QApplication:
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app


class TestCurrentAxisItem:
    def test_default_unit(self, qapp: QApplication) -> None:
        axis = CurrentAxisItem("left")
        assert axis.current_unit == "µA"
        assert axis.scale_factor == 1.0
        assert "Current (µA)" in axis.labelText

    def test_user_scenario_microampere_scale(self, qapp: QApplication) -> None:
        """In the user's use case, max current goes up to 2.8 µA."""
        axis = CurrentAxisItem("left")
        axis.setRange(-2.8, 0.0)

        assert axis.current_unit == "µA"
        assert axis.scale_factor == 1.0
        assert "Current (µA)" in axis.labelText

        ticks = axis.tickStrings([0.0, -0.5, -1.0, -1.5, -2.0, -2.5, -2.8], 1.0, 0.5)
        # Verify no scientific notation
        for t in ticks:
            assert "e" not in t.lower(), f"Tick {t} contains scientific notation!"
        assert ticks[0] == "0.0"
        assert ticks[1] == "-0.5"
        assert ticks[2] == "-1.0"

    def test_nanoampere_scale_transition(self, qapp: QApplication) -> None:
        """When current decreases to nanoampere range (e.g. 50 nA = 0.05 µA)."""
        axis = CurrentAxisItem("left")
        axis.setRange(-0.05, 0.0)

        assert axis.current_unit == "nA"
        assert axis.scale_factor == 1000.0
        assert "Current (nA)" in axis.labelText

        ticks = axis.tickStrings([0.0, -0.01, -0.02, -0.03, -0.04, -0.05], 1.0, 0.01)
        for t in ticks:
            assert "e" not in t.lower(), f"Tick {t} contains scientific notation!"
        assert ticks == ["0", "-10", "-20", "-30", "-40", "-50"]

    def test_milliampere_scale_transition(self, qapp: QApplication) -> None:
        """When current increases to milliampere range (e.g. 5000 µA = 5 mA)."""
        axis = CurrentAxisItem("left")
        axis.setRange(0.0, 5000.0)

        assert axis.current_unit == "mA"
        assert axis.scale_factor == 0.001
        assert "Current (mA)" in axis.labelText

        ticks = axis.tickStrings([0.0, 1000.0, 2000.0, 3000.0, 4000.0, 5000.0], 1.0, 1000.0)
        for t in ticks:
            assert "e" not in t.lower(), f"Tick {t} contains scientific notation!"
        assert ticks == ["0", "1", "2", "3", "4", "5"]

    def test_ampere_scale_transition(self, qapp: QApplication) -> None:
        """When current increases to ampere range (e.g. 2,000,000 µA = 2 A)."""
        axis = CurrentAxisItem("left")
        axis.setRange(0.0, 2000000.0)

        assert axis.current_unit == "A"
        assert axis.scale_factor == 1e-6
        assert "Current (A)" in axis.labelText

        ticks = axis.tickStrings([0.0, 500000.0, 1000000.0, 1500000.0, 2000000.0], 1.0, 500000.0)
        for t in ticks:
            assert "e" not in t.lower(), f"Tick {t} contains scientific notation!"
        assert ticks == ["0.0", "0.5", "1.0", "1.5", "2.0"]

    def test_reset(self, qapp: QApplication) -> None:
        axis = CurrentAxisItem("left")
        axis.setRange(-0.05, 0.0)
        assert axis.current_unit == "nA"

        axis.reset()
        assert axis.current_unit == "µA"
        assert axis.scale_factor == 1.0
        assert "Current (µA)" in axis.labelText


class TestTelemetryFormatting:
    def test_format_current_none(self) -> None:
        assert _format_current(None) == "-- µA"

    def test_format_current_microamperes(self) -> None:
        assert _format_current(2.8) == "+2.8000 µA"
        assert _format_current(-1.405) == "-1.4050 µA"
        assert _format_current(0.0) == "+0.0000 µA"

    def test_format_current_nanoamperes(self) -> None:
        assert _format_current(0.05) == "+50.0000 nA"
        assert _format_current(-0.0125) == "-12.5000 nA"

    def test_format_current_milliamperes(self) -> None:
        assert _format_current(2500.0) == "+2.5000 mA"
        assert _format_current(-12000.0) == "-12.0000 mA"

    def test_format_current_amperes(self) -> None:
        assert _format_current(2000000.0) == "+2.0000 A"


class TestLivePlotWidgetMarkers:
    def test_set_and_clear_sampling_marker(self, qapp: QApplication) -> None:
        from ui.live_plot_widget import LivePlotWidget
        plot = LivePlotWidget()
        assert plot._sampling_line is None
        assert plot._sampling_scatter is None

        # Set sampling marker at 185s, 2.5 µA
        plot.set_sampling_marker(185.0, 2.5)
        assert plot._sampling_line is not None
        assert plot._sampling_scatter is not None
        assert plot._sampling_line.value() == 185.0

        # Clear should remove both
        plot.clear()
        assert plot._sampling_line is None
        assert plot._sampling_scatter is None

