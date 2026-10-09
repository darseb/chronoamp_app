"""Unit tests for interpretation.filtering — signal preprocessing pipeline."""

from __future__ import annotations

import math

import pytest

from core.models import DataPoint
from interpretation.filtering import (
    hampel_filter,
    preprocess,
    savgol_smooth,
    trim_transient,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_points(
    currents: list[float],
    dt: float = 0.1,
    t0: float = 0.0,
) -> list[DataPoint]:
    """Generate data points from a list of current values."""
    return [
        DataPoint(time=t0 + i * dt, current=c)
        for i, c in enumerate(currents)
    ]


# ---------------------------------------------------------------------------
# trim_transient
# ---------------------------------------------------------------------------

class TestTrimTransient:
    def test_trims_initial_window(self) -> None:
        points = _make_points([1.0] * 50, dt=0.1)  # 0.0 .. 4.9 s
        result = trim_transient(points, trim_seconds=2.0)
        # First retained point should be at t >= 2.0
        assert len(result) > 0
        assert result[0].time >= 2.0
        # All points before 2.0 should be gone.
        assert all(dp.time >= 2.0 for dp in result)

    def test_zero_trim_returns_all(self) -> None:
        points = _make_points([1.0] * 10)
        result = trim_transient(points, trim_seconds=0.0)
        assert len(result) == 10

    def test_empty_input(self) -> None:
        assert trim_transient([], trim_seconds=2.0) == []

    def test_trim_exceeds_data_returns_empty(self) -> None:
        points = _make_points([1.0] * 5, dt=0.1)  # 0.0 .. 0.4 s
        result = trim_transient(points, trim_seconds=10.0)
        assert result == []


# ---------------------------------------------------------------------------
# hampel_filter
# ---------------------------------------------------------------------------

class TestHampelFilter:
    def test_removes_spike(self) -> None:
        # Flat signal at 1.0 with a big spike at index 10.
        currents = [1.0] * 20
        currents[10] = 100.0  # obvious outlier
        points = _make_points(currents)

        result = hampel_filter(points, window_size=3, n_sigma=3.0)

        # The spike should be replaced with something close to 1.0.
        assert abs(result[10].current - 1.0) < 1.0
        # Non-spike points should be unchanged.
        assert result[0].current == 1.0
        assert result[5].current == 1.0

    def test_preserves_clean_signal(self) -> None:
        currents = [float(i) for i in range(20)]
        points = _make_points(currents)
        result = hampel_filter(points, window_size=3, n_sigma=3.0)
        # No huge outliers, so values should be unchanged.
        for orig, filt in zip(points, result):
            assert orig.current == filt.current

    def test_short_input_returns_copy(self) -> None:
        points = _make_points([1.0, 2.0])
        result = hampel_filter(points, window_size=3, n_sigma=3.0)
        assert len(result) == 2

    def test_time_is_preserved(self) -> None:
        currents = [1.0] * 10
        currents[5] = 999.0
        points = _make_points(currents)
        result = hampel_filter(points, window_size=3, n_sigma=3.0)
        for orig, filt in zip(points, result):
            assert orig.time == filt.time


# ---------------------------------------------------------------------------
# savgol_smooth
# ---------------------------------------------------------------------------

class TestSavgolSmooth:
    def test_smooths_noisy_signal(self) -> None:
        # Create noisy data around 5.0.
        import random
        random.seed(42)
        currents = [5.0 + random.gauss(0, 0.5) for _ in range(50)]
        points = _make_points(currents)

        result = savgol_smooth(points, window_length=11, polyorder=2)

        # After smoothing, the std-dev of the interior should be lower.
        half = 11 // 2
        orig_interior = [p.current for p in points[half:-half]]
        smooth_interior = [p.current for p in result[half:-half]]

        orig_std = _std(orig_interior)
        smooth_std = _std(smooth_interior)
        assert smooth_std < orig_std

    def test_leaves_linear_signal_unchanged(self) -> None:
        # A perfectly linear signal should pass through unchanged.
        currents = [2.0 + 0.5 * i for i in range(21)]
        points = _make_points(currents)

        result = savgol_smooth(points, window_length=5, polyorder=2)
        half = 5 // 2
        for i in range(half, len(result) - half):
            assert abs(result[i].current - points[i].current) < 1e-10

    def test_short_input_returns_copy(self) -> None:
        points = _make_points([1.0, 2.0, 3.0])
        result = savgol_smooth(points, window_length=11, polyorder=2)
        assert len(result) == 3

    def test_preserves_length(self) -> None:
        points = _make_points([1.0] * 30)
        result = savgol_smooth(points, window_length=7, polyorder=2)
        assert len(result) == 30


# ---------------------------------------------------------------------------
# preprocess (full pipeline)
# ---------------------------------------------------------------------------

class TestPreprocess:
    def test_full_pipeline_reduces_length(self) -> None:
        """Trimming should reduce the number of points."""
        points = _make_points([1.0] * 100, dt=0.1)  # 0.0 .. 9.9 s
        result = preprocess(points, trim_seconds=2.0)
        assert len(result) < len(points)
        assert len(result) > 0

    def test_full_pipeline_removes_spike(self) -> None:
        # After trim, inject a spike and verify it gets cleaned.
        currents = [5.0] * 100
        currents[50] = 500.0  # spike in the post-trim region
        points = _make_points(currents, dt=0.1)

        result = preprocess(
            points,
            trim_seconds=1.0,
            hampel_window=3,
            hampel_sigma=3.0,
            sg_window=7,
            sg_order=2,
        )
        # The spike at index ~50 (t=5.0s) should be reduced.
        # Find the point closest to t=5.0 in the result.
        spike_pts = [dp for dp in result if abs(dp.time - 5.0) < 0.05]
        if spike_pts:
            assert spike_pts[0].current < 100.0  # should be well below 500

    def test_empty_input(self) -> None:
        assert preprocess([]) == []


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def _std(values: list[float]) -> float:
    """Standard deviation (population)."""
    if len(values) < 2:
        return 0.0
    mean = sum(values) / len(values)
    return math.sqrt(sum((v - mean) ** 2 for v in values) / len(values))
