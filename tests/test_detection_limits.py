"""Unit tests for interpretation.detection_limits."""

from __future__ import annotations

import math

import pytest

from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult
from interpretation.detection_limits import (
    DetectionLimit,
    compute_analytical_sensitivity,
    compute_lob,
    compute_lod,
    compute_loq,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _blank(mean: float = 0.050, stdev: float = 0.010, count: int = 20) -> BlankStats:
    lob = mean + 1.645 * stdev
    return BlankStats(mean=mean, stdev=stdev, count=count, lob=lob)


def _calibration(
    slope: float = 2.0,
    intercept: float = 0.5,
    r_squared: float = 0.999,
    unit: str = "ng/mL",
    fit_type: str = "linear",
) -> CalibrationResult:
    return CalibrationResult(
        slope=slope, intercept=intercept, r_squared=r_squared,
        concentration_min=0.0, concentration_max=10.0,
        n_points=5, concentration_unit=unit,
        fit_type=fit_type,
    )


# ---------------------------------------------------------------------------
# LoB
# ---------------------------------------------------------------------------

class TestComputeLoB:
    def test_basic(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        lob = compute_lob(bs)
        expected = 0.050 + 1.645 * 0.010
        assert abs(lob - expected) < 1e-10

    def test_zero_stdev(self) -> None:
        bs = _blank(mean=0.050, stdev=0.0)
        lob = compute_lob(bs)
        assert abs(lob - 0.050) < 1e-10


# ---------------------------------------------------------------------------
# LOD
# ---------------------------------------------------------------------------

class TestComputeLOD:
    def test_current_only(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        lod = compute_lod(bs)
        assert abs(lod.current_ua - (0.050 + 3.0 * 0.010)) < 1e-10
        assert lod.concentration is None

    def test_with_linear_calibration(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        cal = _calibration(slope=2.0, unit="ng/mL", fit_type="linear")
        lod = compute_lod(bs, cal)
        # LOD_current = 0.05 + 0.03 = 0.08
        assert abs(lod.current_ua - 0.080) < 1e-10
        # LOD_conc = 3 x 0.01 / 2.0 = 0.015
        assert lod.concentration is not None
        assert abs(lod.concentration - 0.015) < 1e-10
        assert lod.concentration_unit == "ng/mL"

    def test_with_logarithmic_calibration(self) -> None:
        # Model: I = -0.806 * log10(C_nM) - 1.25  (negative currents from amperometry)
        # Blank mean = 0.1753 uA, stdev = 0.0103 uA
        bs = _blank(mean=0.1753, stdev=0.0103)
        cal = _calibration(slope=-0.806, intercept=-1.25, fit_type="logarithmic", unit="nM")
        lod = compute_lod(bs, cal)
        # LOD_current = 0.1753 + 3*0.0103 = 0.2062
        assert pytest.approx(lod.current_ua, rel=1e-4) == 0.2062
        # IUPAC Eq. 2: LOD = 10^(3σ / |m|) = 10^(3*0.0103 / 0.806)
        expected_exponent = (3.0 * 0.0103) / abs(-0.806)
        expected_lod_conc = 10.0 ** expected_exponent
        assert lod.concentration is not None
        assert pytest.approx(lod.concentration, rel=1e-4) == expected_lod_conc


# ---------------------------------------------------------------------------
# LOQ
# ---------------------------------------------------------------------------

class TestComputeLOQ:
    def test_current_only(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        loq = compute_loq(bs)
        assert abs(loq.current_ua - (0.050 + 10.0 * 0.010)) < 1e-10
        assert loq.concentration is None

    def test_with_linear_calibration(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        cal = _calibration(slope=2.0, unit="µM", fit_type="linear")
        loq = compute_loq(bs, cal)
        # LOQ_conc = 10 x 0.01 / 2.0 = 0.05
        assert loq.concentration is not None
        assert abs(loq.concentration - 0.05) < 1e-10
        assert loq.concentration_unit == "µM"

    def test_with_logarithmic_calibration(self) -> None:
        bs = _blank(mean=0.1753, stdev=0.0103)
        cal = _calibration(slope=-0.806, intercept=-1.25, fit_type="logarithmic", unit="nM")
        loq = compute_loq(bs, cal)
        # IUPAC Eq. 3: LOQ = 10^(10σ / |m|) = 10^(10*0.0103 / 0.806)
        expected_exponent = (10.0 * 0.0103) / abs(-0.806)
        expected_loq_conc = 10.0 ** expected_exponent
        assert loq.concentration is not None
        assert pytest.approx(loq.concentration, rel=1e-4) == expected_loq_conc


# ---------------------------------------------------------------------------
# Analytical Sensitivity
# ---------------------------------------------------------------------------

class TestAnalyticalSensitivity:
    def test_basic(self) -> None:
        cal = _calibration(slope=2.0)
        bs = _blank(stdev=0.010)
        sens = compute_analytical_sensitivity(cal, bs)
        assert sens is not None
        assert abs(sens - 200.0) < 1e-10

    def test_returns_none_with_zero_stdev(self) -> None:
        cal = _calibration(slope=2.0)
        bs = _blank(stdev=0.0)
        assert compute_analytical_sensitivity(cal, bs) is None


# ---------------------------------------------------------------------------
# LOD / LOQ relationship
# ---------------------------------------------------------------------------

class TestRelationships:
    def test_loq_greater_than_lod(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        lod = compute_lod(bs)
        loq = compute_loq(bs)
        assert loq.current_ua > lod.current_ua

    def test_lod_greater_than_lob(self) -> None:
        bs = _blank(mean=0.050, stdev=0.010)
        lob = compute_lob(bs)
        lod = compute_lod(bs)
        assert lod.current_ua > lob

    def test_hierarchy_lob_lod_loq_linear(self) -> None:
        """LoB < LOD < LOQ must always hold for linear fits."""
        bs = _blank(mean=0.050, stdev=0.010)
        cal = _calibration(slope=2.0, fit_type="linear")
        lob = compute_lob(bs)
        lod = compute_lod(bs, cal)
        loq = compute_loq(bs, cal)
        assert lob < lod.current_ua < loq.current_ua
        assert lod.concentration is not None
        assert loq.concentration is not None
        assert lod.concentration < loq.concentration
        assert lod.concentration_value == lod.concentration
        assert loq.concentration_value == loq.concentration
