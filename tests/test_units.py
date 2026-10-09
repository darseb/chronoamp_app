"""Unit tests for utils.units (convert_concentration, convert_method_unit)."""

import pytest
import math
from utils.units import convert_concentration, convert_method_unit
from interpretation.method import AnalyticalMethod, QualityConfig
from interpretation.calibration import CalibrationResult, FitType
from interpretation.blank_store import BlankStats
from interpretation.detection_limits import compute_lod, compute_loq
from data.importer_models import CalibrationMeasurement, ImportedMeasurement, MeasurementRole, SignalMetric


def test_convert_concentration_molar():
    assert convert_concentration(1.0, "nM", "nM") == 1.0
    assert pytest.approx(convert_concentration(1.0, "nM", "pM")) == 1000.0
    assert pytest.approx(convert_concentration(1000.0, "pM", "nM")) == 1.0
    assert pytest.approx(convert_concentration(0.1, "nM", "pM")) == 100.0


def test_convert_method_unit_linear():
    m = AnalyticalMethod(
        name="Linear Method",
        version="1.0",
        analyte="Test",
        concentration_unit="nM",
        calibration_range=(0.1, 100.0),
        calibration_result=CalibrationResult(
            slope=2.0,
            intercept=0.5,
            r_squared=0.999,
            concentration_min=0.1,
            concentration_max=100.0,
            n_points=5,
            concentration_unit="nM",
            fit_type="linear",
        ),
    )

    converted = convert_method_unit(m, "pM")
    assert converted.concentration_unit == "pM"
    assert pytest.approx(converted.calibration_range[0]) == 100.0
    assert pytest.approx(converted.calibration_range[1]) == 100000.0
    assert pytest.approx(converted.calibration_result.concentration_min) == 100.0
    assert pytest.approx(converted.calibration_result.concentration_max) == 100000.0
    assert pytest.approx(converted.calibration_result.slope) == 0.002
    assert pytest.approx(converted.calibration_result.intercept) == 0.5


def test_convert_method_unit_logarithmic():
    # Model: I = -1.25 + 0.806 * log10(C_nM)
    # When converting to pM (ratio = 1000), intercept becomes -1.25 - 0.806 * log10(1000) = -3.668
    m = AnalyticalMethod(
        name="Log Method",
        version="1.0",
        analyte="Test",
        concentration_unit="nM",
        calibration_range=(0.1, 100.0),
        calibration_result=CalibrationResult(
            slope=0.806,
            intercept=-1.25,
            r_squared=0.997,
            concentration_min=0.1,
            concentration_max=100.0,
            n_points=5,
            concentration_unit="nM",
            fit_type="logarithmic",
        ),
    )

    converted = convert_method_unit(m, "pM")
    assert converted.concentration_unit == "pM"
    assert pytest.approx(converted.calibration_range[0]) == 100.0
    assert pytest.approx(converted.calibration_range[1]) == 100000.0
    assert pytest.approx(converted.calibration_result.slope) == 0.806
    assert pytest.approx(converted.calibration_result.intercept) == -1.25 - 0.806 * 3.0

    # Check validation check message update
    check_range = [c for c in converted.validation.checks if c.name == "calibration_range"][0]
    assert "100" in check_range.message
    assert "100000" in check_range.message
    assert "pM" in check_range.message
