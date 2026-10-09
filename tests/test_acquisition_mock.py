"""Tests for the acquisition module using a mock potentiostat device."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock

from core.acquisition import AcquisitionEngine
from core.models import MeasurementConfig


def test_on_new_data_current_units_not_multiplied_by_1e6() -> None:
    """Verify that current from callback_data.y_array is treated as µA directly."""
    dm = MagicMock()
    config = MeasurementConfig(potential=0.0, run_time=10.0, interval_time=0.1)
    engine = AcquisitionEngine(dm, config)

    # In user's use case, readings go up to ~2.8 µA
    cb_data = SimpleNamespace(
        x_array=[0.0, 0.1, 0.2],
        y_array=[-2.8, -1.5, -0.4],
    )
    engine._on_new_data(cb_data)

    points = []
    while not engine.data_queue.empty():
        points.append(engine.data_queue.get_nowait())

    assert len(points) == 3
    assert points[0].time == 0.0
    assert points[0].current == -2.8
    assert points[1].current == -1.5
    assert points[2].current == -0.4


def test_on_new_data_incremental_tail() -> None:
    """Verify cumulative array slicing only enqueues new points."""
    dm = MagicMock()
    config = MeasurementConfig(potential=0.0, run_time=10.0, interval_time=0.1)
    engine = AcquisitionEngine(dm, config)

    # First callback batch
    cb_data1 = SimpleNamespace(
        x_array=[0.0, 0.1],
        y_array=[1.0, 1.2],
    )
    engine._on_new_data(cb_data1)

    points1 = []
    while not engine.data_queue.empty():
        points1.append(engine.data_queue.get_nowait())
    assert len(points1) == 2

    # Second cumulative callback batch
    cb_data2 = SimpleNamespace(
        x_array=[0.0, 0.1, 0.2, 0.3],
        y_array=[1.0, 1.2, 1.4, 1.6],
    )
    engine._on_new_data(cb_data2)

    points2 = []
    while not engine.data_queue.empty():
        points2.append(engine.data_queue.get_nowait())
    assert len(points2) == 2
    assert points2[0].current == 1.4
    assert points2[1].current == 1.6
