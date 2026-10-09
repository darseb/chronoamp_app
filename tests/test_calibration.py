"""Unit tests for interpretation.calibration — calibration curve engine."""

from __future__ import annotations

import json
import math

import pytest

from interpretation.calibration import (
    CalibrationCurve,
    CalibrationPoint,
    CalibrationResult,
    FitType,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

@pytest.fixture
def tmp_cal_path(tmp_path):
    return tmp_path / "calibration.json"


def _add_linear_standards(
    curve: CalibrationCurve,
    slope: float = 2.0,
    intercept: float = 0.5,
    concentrations: list[float] | None = None,
) -> None:
    """Add points that lie perfectly on y = slope * x + intercept."""
    if concentrations is None:
        concentrations = [0.0, 1.0, 2.0, 5.0, 10.0]
    for c in concentrations:
        current = slope * c + intercept
        curve.add_point(c, current)


# ---------------------------------------------------------------------------
# Basic fit
# ---------------------------------------------------------------------------

class TestCalibrationFit:
    def test_too_few_points_returns_none(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        curve.add_point(1.0, 2.0)
        curve.add_point(2.0, 4.0)
        assert curve.fit() is None

    def test_perfect_linear_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve, slope=3.0, intercept=1.0)

        result = curve.fit()
        assert result is not None
        assert abs(result.slope - 3.0) < 1e-10
        assert abs(result.intercept - 1.0) < 1e-10
        assert abs(result.r_squared - 1.0) < 1e-10
        assert result.n_points == 5

    def test_r_squared_below_one_with_noise(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        # Add points with slight noise.
        curve.add_point(0.0, 0.51)
        curve.add_point(1.0, 2.49)
        curve.add_point(2.0, 4.52)
        curve.add_point(5.0, 10.48)
        curve.add_point(10.0, 20.53)

        result = curve.fit()
        assert result is not None
        assert result.r_squared < 1.0
        assert result.r_squared > 0.999  # very close to linear still

    def test_concentration_range(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve, concentrations=[0.1, 0.5, 1.0, 5.0])
        result = curve.fit()
        assert result is not None
        assert result.concentration_min == 0.1
        assert result.concentration_max == 5.0


# ---------------------------------------------------------------------------
# Concentration prediction
# ---------------------------------------------------------------------------

class TestPredictConcentration:
    def test_predicts_correctly(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve, slope=2.0, intercept=0.5)
        curve.fit()

        # For current = 2.0 * 3.0 + 0.5 = 6.5, concentration should be 3.0.
        predicted = curve.predict_concentration(6.5)
        assert predicted is not None
        assert abs(predicted - 3.0) < 1e-10

    def test_returns_none_without_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        assert curve.predict_concentration(5.0) is None

    def test_inverse_roundtrip(self, tmp_cal_path) -> None:
        """Feeding the calibration current back should return the original concentration."""
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve, slope=111.4, intercept=29.6)
        curve.fit()

        for conc in [0.025, 0.1, 0.4, 0.8]:
            current = 111.4 * conc + 29.6
            predicted = curve.predict_concentration(current)
            assert predicted is not None
            assert abs(predicted - conc) < 1e-8


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------

class TestCalibrationPersistence:
    def test_saves_and_loads(self, tmp_cal_path) -> None:
        curve1 = CalibrationCurve(path=tmp_cal_path, concentration_unit="ng/mL")
        _add_linear_standards(curve1, slope=2.0, intercept=0.5)
        curve1.fit()

        # Load from same file.
        curve2 = CalibrationCurve(path=tmp_cal_path)
        assert curve2.count == 5
        assert curve2.result is not None
        assert abs(curve2.result.slope - 2.0) < 1e-10
        assert curve2.concentration_unit == "ng/mL"

    def test_handles_corrupt_file(self, tmp_cal_path) -> None:
        tmp_cal_path.write_text("not valid json")
        curve = CalibrationCurve(path=tmp_cal_path)
        assert curve.count == 0
        assert curve.result is None

    def test_reset_clears_all(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve)
        curve.fit()
        curve.reset()
        assert curve.count == 0
        assert curve.result is None
        assert not tmp_cal_path.exists()


# ---------------------------------------------------------------------------
# Validity
# ---------------------------------------------------------------------------

class TestCalibrationValidity:
    def test_is_valid_with_perfect_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        _add_linear_standards(curve, slope=2.0, intercept=0.5)
        curve.fit()
        assert curve.is_valid  # R² = 1.0 ≥ 0.99

    def test_is_not_valid_without_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path)
        assert not curve.is_valid


# ---------------------------------------------------------------------------
# Concentration unit
# ---------------------------------------------------------------------------

class TestConcentrationUnit:
    def test_unit_in_result(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, concentration_unit="µM")
        _add_linear_standards(curve)
        result = curve.fit()
        assert result is not None
        assert result.concentration_unit == "µM"

    def test_unit_setter(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, concentration_unit="µM")
        _add_linear_standards(curve)
        curve.fit()
        curve.concentration_unit = "ng/mL"
        assert curve.result is not None
        assert curve.result.concentration_unit == "ng/mL"


# ---------------------------------------------------------------------------
# Logarithmic fit
# ---------------------------------------------------------------------------

class TestLogarithmicFit:
    def test_perfect_log_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, fit_type=FitType.LOGARITHMIC)
        slope = -0.819
        intercept = -1.145
        # Add standards at 0.1, 1.0, 10.0, 100.0
        concs = [0.1, 1.0, 10.0, 100.0]
        for c in concs:
            y = slope * math.log10(c) + intercept
            curve.add_point(c, y)

        result = curve.fit()
        assert result is not None
        assert result.fit_type == "logarithmic"
        assert abs(result.slope - slope) < 1e-10
        assert abs(result.intercept - intercept) < 1e-10
        assert abs(result.r_squared - 1.0) < 1e-10
        assert result.n_points == 4

    def test_blank_points_excluded_from_log_fit(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, fit_type=FitType.LOGARITHMIC)
        slope = 1.5
        intercept = 2.0
        for c in [0.1, 1.0, 10.0]:
            curve.add_point(c, slope * math.log10(c) + intercept)
        # Add a blank point with concentration 0.0
        curve.add_point(0.0, 0.5)

        result = curve.fit()
        assert result is not None
        # 3 points used, 0.0 excluded
        assert result.n_points == 3
        assert abs(result.slope - slope) < 1e-10

    def test_negative_concentration_raises_value_error(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, fit_type=FitType.LOGARITHMIC)
        curve.add_point(1.0, 2.0)
        curve.add_point(10.0, 3.5)
        curve.add_point(-1.0, 0.5)

        with pytest.raises(ValueError, match="Logarithmic calibration requires all concentrations to be strictly positive"):
            curve.fit()

    def test_log_predict_concentration_and_signal(self, tmp_cal_path) -> None:
        curve = CalibrationCurve(path=tmp_cal_path, fit_type=FitType.LOGARITHMIC)
        slope = -0.819
        intercept = -1.145
        for c in [0.1, 1.0, 10.0, 100.0]:
            curve.add_point(c, slope * math.log10(c) + intercept)
        curve.fit()

        # For c = 10.0, signal should be -0.819 * 1 - 1.145 = -1.964
        expected_signal = slope * math.log10(10.0) + intercept
        assert abs(curve.result.predict_signal(10.0) - expected_signal) < 1e-10

        # Predict concentration from signal
        pred_c = curve.predict_concentration(expected_signal)
        assert pred_c is not None
        assert abs(pred_c - 10.0) < 1e-6

        # Zero or negative concentration signal prediction returns None
        assert curve.result.predict_signal(0.0) is None
        assert curve.result.predict_signal(-5.0) is None

    def test_log_fit_persistence(self, tmp_cal_path) -> None:
        curve1 = CalibrationCurve(path=tmp_cal_path, fit_type=FitType.LOGARITHMIC, concentration_unit="nM")
        for c in [0.1, 1.0, 10.0]:
            curve1.add_point(c, 2.0 * math.log10(c) + 1.0)
        curve1.fit()

        # Reload
        curve2 = CalibrationCurve(path=tmp_cal_path)
        assert curve2.fit_type == FitType.LOGARITHMIC
        assert curve2.result is not None
        assert curve2.result.fit_type == "logarithmic"
        assert abs(curve2.result.slope - 2.0) < 1e-10
