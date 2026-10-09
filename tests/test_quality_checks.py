"""Unit tests for interpretation.quality_checks."""

from __future__ import annotations

import math

import pytest

from core.models import DataPoint
from interpretation.blank_store import BlankStats
from interpretation.quality_checks import (
    QCResult,
    check_cv,
    check_drift,
    check_snr,
    check_steady_state,
    run_all_checks,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _uniform_points(current: float, n: int = 100, dt: float = 0.1) -> list[DataPoint]:
    return [DataPoint(time=i * dt, current=current) for i in range(n)]


def _make_blank_stats(mean: float = 0.05, stdev: float = 0.01, count: int = 20) -> BlankStats:
    lob = mean + 1.645 * stdev
    return BlankStats(mean=mean, stdev=stdev, count=count, lob=lob)


# ---------------------------------------------------------------------------
# check_steady_state
# ---------------------------------------------------------------------------

class TestCheckSteadyState:
    def test_flat_signal_passes(self) -> None:
        points = _uniform_points(5.0, n=100)
        result = check_steady_state(points, max_slope=0.01)
        assert result.passed
        assert result.name == "steady_state"
        assert result.value < 1e-10  # slope should be ~0

    def test_rising_signal_fails(self) -> None:
        # Linear ramp: 0, 0.1, 0.2, ... → slope = 1.0 µA/s
        points = [DataPoint(time=i * 0.1, current=i * 0.1) for i in range(100)]
        result = check_steady_state(points, max_slope=0.01)
        assert not result.passed
        assert result.value > 0.01

    def test_too_few_points(self) -> None:
        points = _uniform_points(1.0, n=2)
        result = check_steady_state(points)
        assert not result.passed


# ---------------------------------------------------------------------------
# check_drift
# ---------------------------------------------------------------------------

class TestCheckDrift:
    def test_no_drift_passes(self) -> None:
        points = _uniform_points(5.0, n=100)
        result = check_drift(points, max_drift_fraction=0.15)
        assert result.passed
        assert result.value < 1e-10

    def test_large_drift_fails(self) -> None:
        # Build 100 points where the final window (last 30 = indices 70–99)
        # transitions from 5.0 to 10.0 mid-window → detectable drift.
        points = []
        for i in range(100):
            if i < 70:
                current = 5.0  # pre-window: stable
            elif i < 85:
                current = 5.0  # first half of final window
            else:
                current = 10.0  # second half of final window — big jump
            points.append(DataPoint(time=i * 0.1, current=current))
        result = check_drift(points, max_drift_fraction=0.15)
        assert not result.passed
        assert result.value > 0.15

    def test_too_few_points(self) -> None:
        points = _uniform_points(1.0, n=2)
        result = check_drift(points)
        assert not result.passed


# ---------------------------------------------------------------------------
# check_snr
# ---------------------------------------------------------------------------

class TestCheckSNR:
    def test_high_snr_passes(self) -> None:
        # Signal at 5.0, blank mean at 0.05, blank stdev 0.01 → SNR ≈ 495
        points = _uniform_points(5.0, n=100)
        blank = _make_blank_stats(mean=0.05, stdev=0.01)
        result = check_snr(points, blank, min_snr=3.0)
        assert result.passed
        assert result.value > 3.0

    def test_low_snr_fails(self) -> None:
        # Signal at 0.052, blank mean at 0.05, stdev 0.01 → SNR ≈ 0.2
        points = _uniform_points(0.052, n=100)
        blank = _make_blank_stats(mean=0.05, stdev=0.01)
        result = check_snr(points, blank, min_snr=3.0)
        assert not result.passed
        assert result.value < 3.0

    def test_skipped_without_blanks(self) -> None:
        points = _uniform_points(5.0, n=100)
        result = check_snr(points, None, min_snr=3.0)
        assert result.passed  # skipped = auto-pass
        assert math.isnan(result.value)


# ---------------------------------------------------------------------------
# check_cv
# ---------------------------------------------------------------------------

class TestCheckCV:
    def test_low_cv_passes(self) -> None:
        points = _uniform_points(5.0, n=100)
        result = check_cv(points, max_cv_percent=10.0)
        assert result.passed
        assert result.value < 1e-10  # zero stdev

    def test_high_cv_fails(self) -> None:
        # Alternating values → high CV.
        points = []
        for i in range(100):
            current = 10.0 if i % 2 == 0 else 0.0
            points.append(DataPoint(time=i * 0.1, current=current))
        result = check_cv(points, max_cv_percent=10.0)
        assert not result.passed
        assert result.value > 10.0


# ---------------------------------------------------------------------------
# run_all_checks
# ---------------------------------------------------------------------------

class TestRunAllChecks:
    def test_all_pass_on_clean_data(self) -> None:
        points = _uniform_points(5.0, n=100)
        blank = _make_blank_stats(mean=0.05, stdev=0.01)
        results = run_all_checks(points, blank)

        assert len(results) == 4
        assert all(r.passed for r in results)

    def test_returns_four_results_without_blanks(self) -> None:
        points = _uniform_points(5.0, n=100)
        results = run_all_checks(points, None)
        assert len(results) == 4
        # SNR should be skipped (auto-pass).
        snr_result = [r for r in results if r.name == "snr"][0]
        assert snr_result.passed
