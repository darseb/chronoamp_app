"""Unit conversion utilities for electrochemical concentration measurements."""

from __future__ import annotations

import math
from typing import Any

MOLAR_FACTORS: dict[str, float] = {
    "m": 1.0,
    "mm": 1e-3,
    "um": 1e-6,
    "µm": 1e-6,
    "nm": 1e-9,
    "pm": 1e-12,
    "fm": 1e-15,
}

MASS_FACTORS: dict[str, float] = {
    "g/l": 1.0,
    "mg/ml": 1.0,
    "mg/l": 1e-3,
    "ug/ml": 1e-3,
    "µg/ml": 1e-3,
    "ug/l": 1e-6,
    "µg/l": 1e-6,
    "ng/ml": 1e-6,
    "ng/l": 1e-9,
    "pg/ml": 1e-9,
    "pg/l": 1e-12,
    "fg/ml": 1e-12,
}


def convert_concentration(val: float, from_unit: str, to_unit: str) -> float:
    """Convert a concentration value between compatible units."""
    fu = from_unit.strip().lower()
    tu = to_unit.strip().lower()
    if fu == tu or not fu or not tu:
        return val

    if fu in MOLAR_FACTORS and tu in MOLAR_FACTORS:
        return val * MOLAR_FACTORS[fu] / MOLAR_FACTORS[tu]

    if fu in MASS_FACTORS and tu in MASS_FACTORS:
        return val * MASS_FACTORS[fu] / MASS_FACTORS[tu]

    return val


def get_conversion_factor(from_unit: str, to_unit: str) -> float:
    """Get the multiplicative conversion factor from_unit -> to_unit."""
    fu = from_unit.strip().lower()
    tu = to_unit.strip().lower()
    if fu == tu or not fu or not tu:
        return 1.0

    if fu in MOLAR_FACTORS and tu in MOLAR_FACTORS:
        return MOLAR_FACTORS[fu] / MOLAR_FACTORS[tu]

    if fu in MASS_FACTORS and tu in MASS_FACTORS:
        return MASS_FACTORS[fu] / MASS_FACTORS[tu]

    return 1.0


def convert_method_unit(method: Any, target_unit: str) -> Any:
    """Convert an AnalyticalMethod's concentration unit and all dependent values."""
    from_unit = getattr(method, "concentration_unit", "")
    if not from_unit or from_unit.strip().lower() == target_unit.strip().lower():
        method.concentration_unit = target_unit
        return method

    ratio = get_conversion_factor(from_unit, target_unit)

    # 1. Update primary unit string
    method.concentration_unit = target_unit

    # 2. Update source measurements
    for m in getattr(method, "source_measurements", []):
        if getattr(m, "concentration", None) is not None:
            m.concentration = convert_concentration(m.concentration, from_unit, target_unit)
            m.concentration_unit = target_unit

    # 3. Update calibration range
    if getattr(method, "calibration_range", None) is not None:
        lo = convert_concentration(method.calibration_range[0], from_unit, target_unit)
        hi = convert_concentration(method.calibration_range[1], from_unit, target_unit)
        method.calibration_range = (lo, hi)

    # 4. Update calibration result
    cal = getattr(method, "calibration_result", None)
    if cal is not None:
        c_min = convert_concentration(cal.concentration_min, from_unit, target_unit)
        c_max = convert_concentration(cal.concentration_max, from_unit, target_unit)

        fit_type_str = str(cal.fit_type.value if hasattr(cal.fit_type, "value") else cal.fit_type).lower()
        if fit_type_str == "logarithmic":
            new_slope = cal.slope
            new_intercept = cal.intercept - cal.slope * math.log10(ratio) if ratio > 0 else cal.intercept
        else:
            new_slope = cal.slope / ratio if ratio != 0 else cal.slope
            new_intercept = cal.intercept

        from interpretation.calibration import CalibrationResult
        method.calibration_result = CalibrationResult(
            slope=new_slope,
            intercept=new_intercept,
            r_squared=cal.r_squared,
            concentration_min=c_min,
            concentration_max=c_max,
            n_points=cal.n_points,
            concentration_unit=target_unit,
            fit_type=cal.fit_type,
        )

    # 5. Update LOD and LOQ
    blank_stats = getattr(method, "blank_stats", None)
    if blank_stats and method.calibration_result:
        from interpretation.detection_limits import compute_lod, compute_loq
        if getattr(method, "lod", None):
            method.lod = compute_lod(blank_stats, method.calibration_result)
        if getattr(method, "loq", None):
            method.loq = compute_loq(blank_stats, method.calibration_result)

    # 6. Re-run validation checks to ensure clean, consistent messages
    from interpretation.method import validate_method
    validate_method(method)

    return method
