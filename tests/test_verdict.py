"""Unit tests for interpretation.verdict — the full analytical pipeline."""

from __future__ import annotations

import pytest

from core.models import DataPoint, MeasurementConfig
from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult
from interpretation.verdict import Verdict, VerdictReport, interpret, interpret_full


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_config() -> MeasurementConfig:
    return MeasurementConfig(potential=0.0, run_time=10.0, interval_time=0.1)


def _uniform_points(current: float, n: int = 100, t0: float = 3.0) -> list[DataPoint]:
    """Generate *n* points with constant current, starting at t0.

    t0=3.0 ensures they survive the default 2.0 s transient trim.
    """
    return [
        DataPoint(time=t0 + i * 0.1, current=current)
        for i in range(n)
    ]


def _blank(mean: float = 0.050, stdev: float = 0.010) -> BlankStats:
    return BlankStats(mean=mean, stdev=stdev, count=20, lob=mean + 1.645 * stdev)


def _calibration(slope: float = 2.0, intercept: float = 0.5) -> CalibrationResult:
    return CalibrationResult(
        slope=slope, intercept=intercept, r_squared=0.999,
        concentration_min=0.0, concentration_max=10.0,
        n_points=5, concentration_unit="ng/mL",
    )


# ---------------------------------------------------------------------------
# Legacy mode (no blanks)
# ---------------------------------------------------------------------------

class TestLegacyMode:
    """Tests that exercise the legacy cutoff path (no blank stats)."""

    def test_positive(self) -> None:
        # POSITIVE_CUTOFF_UA is -0.0001; current=1.0 is well above.
        points = _uniform_points(current=1.0, n=100)
        verdict, reason = interpret(points, _make_config(), run_preprocessing=False)
        assert verdict is Verdict.POSITIVE
        assert "above threshold" in reason.lower()

    def test_negative(self) -> None:
        points = _uniform_points(current=-5.0, n=100)
        verdict, reason = interpret(points, _make_config(), run_preprocessing=False)
        assert verdict is Verdict.NEGATIVE
        assert "below threshold" in reason.lower()

    def test_mode_is_legacy(self) -> None:
        points = _uniform_points(current=1.0, n=100)
        report = interpret_full(points, _make_config(), run_preprocessing=False)
        assert report.mode == "legacy"


# ---------------------------------------------------------------------------
# Too few points
# ---------------------------------------------------------------------------

class TestTooFewPoints:
    def test_returns_inconclusive_with_zero(self) -> None:
        verdict, reason = interpret([], _make_config())
        assert verdict is Verdict.INCONCLUSIVE
        assert "too few" in reason.lower()

    def test_returns_inconclusive_with_nine(self) -> None:
        points = _uniform_points(current=1.0, n=9)
        verdict, reason = interpret(points, _make_config())
        assert verdict is Verdict.INCONCLUSIVE
        assert "too few" in reason.lower()


# ---------------------------------------------------------------------------
# Out of plausible range
# ---------------------------------------------------------------------------

class TestOutOfPlausibleRange:
    def test_above_max(self) -> None:
        points = _uniform_points(current=2000.0, n=100)
        verdict, reason = interpret(points, _make_config(), run_preprocessing=False)
        assert verdict is Verdict.INCONCLUSIVE
        assert "plausible" in reason.lower()

    def test_below_min(self) -> None:
        points = _uniform_points(current=-2000.0, n=100)
        verdict, reason = interpret(points, _make_config(), run_preprocessing=False)
        assert verdict is Verdict.INCONCLUSIVE
        assert "plausible" in reason.lower()


# ---------------------------------------------------------------------------
# Blank-aware mode
# ---------------------------------------------------------------------------

class TestBlankAwareMode:
    def test_positive_above_lod(self) -> None:
        # blank mean=0.05, stdev=0.01 → LOD = 0.05 + 0.03 = 0.08
        # Signal at 1.0 is well above LOD.
        bs = _blank(mean=0.05, stdev=0.01)
        points = _uniform_points(current=1.0, n=100)
        report = interpret_full(
            points, _make_config(), blank_stats=bs, run_preprocessing=False,
        )
        assert report.verdict is Verdict.POSITIVE
        assert report.mode == "blank_aware"
        assert "LOD" in report.explanation

    def test_negative_below_lob(self) -> None:
        # LoB = 0.05 + 1.645 × 0.01 = 0.06645
        # Signal at 0.04 is below LoB.
        bs = _blank(mean=0.05, stdev=0.01)
        points = _uniform_points(current=0.04, n=100)
        report = interpret_full(
            points, _make_config(), blank_stats=bs, run_preprocessing=False,
        )
        assert report.verdict is Verdict.NEGATIVE
        assert report.mode == "blank_aware"
        assert "blank" in report.explanation.lower()

    def test_inconclusive_grey_zone(self) -> None:
        # LoB = 0.06645, LOD = 0.08. Signal at 0.07 is in the grey zone.
        bs = _blank(mean=0.05, stdev=0.01)
        points = _uniform_points(current=0.07, n=100)
        report = interpret_full(
            points, _make_config(), blank_stats=bs, run_preprocessing=False,
        )
        assert report.verdict is Verdict.INCONCLUSIVE
        assert report.mode == "blank_aware"
        assert "grey zone" in report.explanation.lower()


# ---------------------------------------------------------------------------
# Concentration prediction
# ---------------------------------------------------------------------------

class TestConcentrationPrediction:
    def test_includes_concentration_when_calibrated(self) -> None:
        bs = _blank(mean=0.05, stdev=0.01)
        cal = _calibration(slope=2.0, intercept=0.5)
        points = _uniform_points(current=5.0, n=100)
        report = interpret_full(
            points, _make_config(),
            blank_stats=bs, calibration=cal,
            run_preprocessing=False,
        )
        assert report.predicted_concentration is not None
        # C = (5.0 - 0.5) / 2.0 = 2.25
        assert abs(report.predicted_concentration - 2.25) < 1e-10
        assert report.concentration_unit == "ng/mL"

    def test_no_concentration_without_calibration(self) -> None:
        points = _uniform_points(current=5.0, n=100)
        report = interpret_full(points, _make_config(), run_preprocessing=False)
        assert report.predicted_concentration is None


# ---------------------------------------------------------------------------
# QC gating
# ---------------------------------------------------------------------------

class TestQCGating:
    def test_drifting_signal_is_inconclusive(self) -> None:
        """A linearly rising signal should fail the steady-state check."""
        # Build 100 points with a strong ramp: current = 0.1 * i
        points = [
            DataPoint(time=3.0 + i * 0.1, current=0.1 * i)
            for i in range(100)
        ]
        report = interpret_full(points, _make_config(), run_preprocessing=False)
        assert report.verdict is Verdict.INCONCLUSIVE
        assert report.mode == "qc_gated"
        # Should have QC results attached.
        assert len(report.qc_results) > 0


# ---------------------------------------------------------------------------
# VerdictReport.as_tuple
# ---------------------------------------------------------------------------

class TestVerdictReportAsTuple:
    def test_returns_tuple(self) -> None:
        report = VerdictReport(
            verdict=Verdict.POSITIVE,
            explanation="test reason",
        )
        v, r = report.as_tuple()
        assert v is Verdict.POSITIVE
        assert r == "test reason"


# ---------------------------------------------------------------------------
# Preprocessing integration
# ---------------------------------------------------------------------------

class TestPreprocessingIntegration:
    def test_with_preprocessing(self) -> None:
        """Data starting at t=0 should have transient trimmed."""
        # 200 points at dt=0.1 → 0–20s. First 2s trimmed → 180 points left.
        points = [
            DataPoint(time=i * 0.1, current=5.0)
            for i in range(200)
        ]
        report = interpret_full(points, _make_config(), run_preprocessing=True)
        # Should succeed despite trimming.
        assert report.verdict in (Verdict.POSITIVE, Verdict.NEGATIVE)


# ---------------------------------------------------------------------------
# Target Time Sampling (185 s stabilized point)
# ---------------------------------------------------------------------------

class TestTargetTimeSampling:
    def test_samples_at_185s_for_200s_measurement(self) -> None:
        """In a 200s run, the current at 185s must be used for calibration interpolation."""
        # Simulate a 200s measurement with dt=1.0s where current stabilizes to 2.5 µA at 185s
        points = []
        for t in range(0, 201):
            if t < 185:
                # decaying curve towards 2.5
                curr = 2.5 + 5.0 * (185 - t) / 185.0
            else:
                # flat stabilized plateau around 2.5 µA
                curr = 2.5
        points = [
            DataPoint(time=float(t), current=2.5 if t >= 180 else 2.5 + 0.001 * (180 - t))
            for t in range(0, 201)
        ]
        
        cal = _calibration(slope=2.0, intercept=0.5)
        config = MeasurementConfig(potential=-0.015, run_time=200.0, interval_time=1.0)
        
        report = interpret_full(points, config, calibration=cal, run_preprocessing=False)
        
        assert report.sampling_time == 185.0
        assert pytest.approx(report.mean_current, rel=1e-4) == 2.5
        # C = (2.5 - 0.5) / 2.0 = 1.0
        assert report.predicted_concentration is not None
        assert pytest.approx(report.predicted_concentration, rel=1e-4) == 1.0
        assert "t=185 s" in report.explanation

    def test_fallback_when_measurement_is_under_185s(self) -> None:
        """When measurement is shorter than 185s, fall back to final-window mean."""
        points = _uniform_points(current=1.8, n=100, t0=3.0)  # max t = 12.9s
        cal = _calibration(slope=2.0, intercept=0.5)
        config = MeasurementConfig(potential=-0.015, run_time=10.0, interval_time=0.1)
        
        report = interpret_full(points, config, calibration=cal, run_preprocessing=False)
        
        assert report.sampling_time is None
        assert pytest.approx(report.mean_current, rel=1e-4) == 1.8
        # C = (1.8 - 0.5) / 2.0 = 0.65
        assert report.predicted_concentration is not None
        assert pytest.approx(report.predicted_concentration, rel=1e-4) == 0.65
        assert "final-window mean" in report.explanation


class TestNegativeSlopeAssay:
    def test_negative_slope_decision(self) -> None:
        """When slope is negative, more negative current indicates higher analyte."""
        # Blank mean = -0.175, stdev = 0.010
        bs = BlankStats(mean=-0.175, stdev=0.010, count=10, lob=-0.1585)
        # cal slope = -0.815 (negative reduction slope)
        cal = CalibrationResult(
            slope=-0.815, intercept=1.318, r_squared=0.99,
            concentration_min=100.0, concentration_max=100000.0,
            n_points=15, concentration_unit="pM", fit_type="logarithmic"
        )
        config = MeasurementConfig(potential=-0.15, run_time=10.0, interval_time=0.1)

        # Blank sample at -0.096 µA: higher than LoB (-0.191 µA) -> NEGATIVE
        pts_blank = _uniform_points(current=-0.096, n=100)
        report_blank = interpret_full(pts_blank, config, blank_stats=bs, calibration=cal, run_preprocessing=False)
        assert report_blank.verdict is Verdict.NEGATIVE

        # Positive sample at -0.956 µA: more negative than LOD (-0.205 µA) -> POSITIVE
        pts_pos = _uniform_points(current=-0.956, n=100)
        report_pos = interpret_full(pts_pos, config, blank_stats=bs, calibration=cal, run_preprocessing=False)
        assert report_pos.verdict is Verdict.POSITIVE
        assert report_pos.predicted_concentration is not None
        assert 500 < report_pos.predicted_concentration < 700


