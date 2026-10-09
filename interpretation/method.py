"""Analytical Method domain model and validation.

An :class:`AnalyticalMethod` represents a complete, reusable calibration
package that can be loaded independently from a physical PalmSens device.
It contains everything needed to interpret a new measurement:

- Signal extraction configuration.
- Blank statistics.
- Calibration parameters.
- Detection limits (LOB / LOD / LOQ).
- Quality acceptance criteria.
- Provenance records linking back to the original calibration data.

The method is the **output** of the calibration-building workflow and the
**input** to the routine-sample interpretation path.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from config.settings import (
    MAX_CV_PERCENT,
    MAX_DRIFT_FRACTION,
    MAX_STEADY_STATE_SLOPE_UA_PER_S,
    MIN_BLANK_REPLICATES,
    MIN_CALIBRATION_POINTS,
    MIN_R_SQUARED,
    MIN_SNR,
)
from data.importer_models import (
    CalibrationMeasurement,
    SignalMetric,
    SourceFileInfo,
)
from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult
from interpretation.detection_limits import DetectionLimit
from interpretation.signal_extraction import PreprocessingConfig

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Quality configuration
# ---------------------------------------------------------------------------

@dataclass
class QualityConfig:
    """Configurable acceptance criteria for an analytical method.

    These override the global defaults from ``config.settings`` when a
    method is active.
    """

    max_steady_state_slope: float = MAX_STEADY_STATE_SLOPE_UA_PER_S
    max_drift_fraction: float = MAX_DRIFT_FRACTION
    min_snr: float = MIN_SNR
    max_cv_percent: float = MAX_CV_PERCENT
    min_r_squared: float = MIN_R_SQUARED
    min_blank_replicates: int = MIN_BLANK_REPLICATES
    min_calibration_points: int = MIN_CALIBRATION_POINTS

    def to_dict(self) -> dict:
        return {
            "max_steady_state_slope": self.max_steady_state_slope,
            "max_drift_fraction": self.max_drift_fraction,
            "min_snr": self.min_snr,
            "max_cv_percent": self.max_cv_percent,
            "min_r_squared": self.min_r_squared,
            "min_blank_replicates": self.min_blank_replicates,
            "min_calibration_points": self.min_calibration_points,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "QualityConfig":
        return cls(**{k: v for k, v in d.items() if hasattr(cls, k)})


# ---------------------------------------------------------------------------
# Validation result
# ---------------------------------------------------------------------------

@dataclass
class ValidationCheck:
    """Outcome of a single method-validation check."""

    name: str
    passed: bool
    message: str
    value: Any = None


@dataclass
class MethodValidationResult:
    """Aggregated validation of an analytical method."""

    checks: list[ValidationCheck] = field(default_factory=list)

    @property
    def is_valid(self) -> bool:
        return all(c.passed for c in self.checks)

    @property
    def status(self) -> str:
        return "VALID" if self.is_valid else "INVALID"

    @property
    def failures(self) -> list[ValidationCheck]:
        return [c for c in self.checks if not c.passed]


# ---------------------------------------------------------------------------
# Analytical Method
# ---------------------------------------------------------------------------

@dataclass
class AnalyticalMethod:
    """A complete, reusable analytical method for interpreting measurements.

    Attributes
    ----------
    name : str
        Human-readable method name (e.g. "IL-6 PEC").
    version : str
        Version string (e.g. "1.0").
    analyte : str
        Target analyte name (e.g. "IL-6").
    technique : str
        Electrochemical technique (e.g. "Chronoamperometry").
    concentration_unit : str
        Unit for concentration values (e.g. "pg/mL").
    signal_metric : SignalMetric
        How the analytical signal is extracted from a trace.
    preprocessing_config : PreprocessingConfig
        Signal preprocessing parameters.
    quality_config : QualityConfig
        QC acceptance criteria.
    blank_stats : BlankStats | None
        Blank characterisation statistics.
    calibration_result : CalibrationResult | None
        Calibration curve fit result.
    lob : float | None
        Limit of Blank (µA).
    lod : DetectionLimit | None
        Limit of Detection.
    loq : DetectionLimit | None
        Limit of Quantitation.
    calibration_range : tuple[float, float] | None
        (min_conc, max_conc) of the calibration curve.
    source_measurements : list[CalibrationMeasurement]
        Individual measurements used to build the calibration (provenance).
    source_files : list[SourceFileInfo]
        Files from which calibration data was imported.
    created_at : str
        ISO-8601 creation timestamp.
    status : str
        "VALID", "INVALID", or "DRAFT".
    validation : MethodValidationResult | None
        Last validation result.
    metadata : dict[str, Any]
        Arbitrary extra metadata.
    """

    name: str = ""
    version: str = "1.0"
    analyte: str = ""
    technique: str = "Chronoamperometry"
    concentration_unit: str = ""

    signal_metric: SignalMetric = SignalMetric.MEAN_FINAL_WINDOW
    preprocessing_config: PreprocessingConfig = field(default_factory=PreprocessingConfig)
    quality_config: QualityConfig = field(default_factory=QualityConfig)

    blank_stats: BlankStats | None = None
    calibration_result: CalibrationResult | None = None

    lob: float | None = None
    lod: DetectionLimit | None = None
    loq: DetectionLimit | None = None
    calibration_range: tuple[float, float] | None = None

    source_measurements: list[CalibrationMeasurement] = field(default_factory=list)
    source_files: list[SourceFileInfo] = field(default_factory=list)

    created_at: str = ""
    status: str = "DRAFT"
    validation: MethodValidationResult | None = None
    metadata: dict[str, Any] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate_method(method: AnalyticalMethod) -> MethodValidationResult:
    """Validate an analytical method against its quality criteria.

    Checks:
        1. Sufficient blank replicates.
        2. Sufficient calibration levels (distinct concentrations).
        3. At least 1 replicate per level.
        4. Calibration R² meets acceptance criterion.
        5. Calibration range is non-degenerate.

    Returns
    -------
    MethodValidationResult
        Individual pass/fail checks and an overall status.
    """
    qc = method.quality_config
    checks: list[ValidationCheck] = []

    # -- 1. Blank replicates ------------------------------------------------
    blank_count = 0
    if method.blank_stats is not None:
        blank_count = method.blank_stats.count

    checks.append(ValidationCheck(
        name="blank_replicates",
        passed=blank_count >= qc.min_blank_replicates,
        message=(
            f"Blank replicates: {blank_count} "
            f"({'≥' if blank_count >= qc.min_blank_replicates else '<'} "
            f"{qc.min_blank_replicates} required)."
        ),
        value=blank_count,
    ))

    # -- 2. Calibration levels ----------------------------------------------
    standards = [
        m for m in method.source_measurements
        if m.role.value == "standard" and m.concentration is not None
    ]
    distinct_concs = set(m.concentration for m in standards)
    n_levels = len(distinct_concs)

    checks.append(ValidationCheck(
        name="calibration_levels",
        passed=n_levels >= 2,
        message=f"Calibration levels: {n_levels} distinct concentrations.",
        value=n_levels,
    ))

    # -- 3. Replicates per level --------------------------------------------
    min_reps = min(
        (sum(1 for m in standards if m.concentration == c) for c in distinct_concs),
        default=0,
    )
    checks.append(ValidationCheck(
        name="replicates",
        passed=min_reps >= 1,
        message=f"Minimum replicates per level: {min_reps}.",
        value=min_reps,
    ))

    # -- 4. Calibration fit -------------------------------------------------
    cal = method.calibration_result
    if cal is not None:
        r2_ok = cal.r_squared >= qc.min_r_squared
        checks.append(ValidationCheck(
            name="calibration_fit",
            passed=r2_ok,
            message=(
                f"R² = {cal.r_squared:.4f} "
                f"({'≥' if r2_ok else '<'} {qc.min_r_squared})."
            ),
            value=cal.r_squared,
        ))

        # -- 5. Calibration points ------------------------------------------
        n_pts_ok = cal.n_points >= qc.min_calibration_points
        checks.append(ValidationCheck(
            name="calibration_points",
            passed=n_pts_ok,
            message=(
                f"Calibration points: {cal.n_points} "
                f"({'≥' if n_pts_ok else '<'} {qc.min_calibration_points})."
            ),
            value=cal.n_points,
        ))
    else:
        checks.append(ValidationCheck(
            name="calibration_fit",
            passed=False,
            message="No calibration fit available.",
            value=None,
        ))

    # -- 6. Calibration range -----------------------------------------------
    if method.calibration_range is not None:
        lo, hi = method.calibration_range
        range_ok = hi > lo
        from utils.formatting import format_concentration
        c_min_str = format_concentration(lo)
        c_max_str = format_concentration(hi, unit=method.concentration_unit)
        checks.append(ValidationCheck(
            name="calibration_range",
            passed=range_ok,
            message=(
                f"Calibration range: {c_min_str} – {c_max_str}."
                if range_ok
                else "Degenerate calibration range (min == max)."
            ),
            value=(lo, hi),
        ))

    result = MethodValidationResult(checks=checks)

    # Update method status.
    method.status = result.status
    method.validation = result

    logger.info(
        "Method '%s' v%s validation: %s (%d/%d checks passed).",
        method.name, method.version, result.status,
        sum(1 for c in checks if c.passed), len(checks),
    )
    return result
