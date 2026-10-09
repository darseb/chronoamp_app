"""Orchestrate the construction of an Analytical Method.

The :class:`MethodBuilder` takes normalized measurements (blanks and
standards), extracts their analytical signals, computes statistics and
calibration curves, and produces a validated :class:`AnalyticalMethod`.
"""

from __future__ import annotations

import logging
from datetime import datetime
from typing import Any

from data.importer_models import (
    CalibrationMeasurement,
    MeasurementRole,
    SignalMetric,
    SourceFileInfo,
)
from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationCurve, CalibrationResult, FitType
from interpretation.detection_limits import compute_lod, compute_loq
from interpretation.method import AnalyticalMethod, QualityConfig, validate_method
from interpretation.signal_extraction import (
    PreprocessingConfig,
    extract_signal_from_imported,
)

logger = logging.getLogger(__name__)


class MethodBuildError(Exception):
    """Raised when method construction fails."""


class MethodBuilder:
    """Builder for assembling an Analytical Method step-by-step."""

    def __init__(self) -> None:
        self._name: str = "New Method"
        self._version: str = "1.0"
        self._analyte: str = "Unknown"
        self._technique: str = "Chronoamperometry"
        self._concentration_unit: str = ""
        self._fit_type: FitType = FitType.LINEAR

        self._signal_metric: SignalMetric = SignalMetric.MEAN_FINAL_WINDOW
        self._prep_config: PreprocessingConfig = PreprocessingConfig()
        self._quality_config: QualityConfig = QualityConfig()

        self._measurements: list[CalibrationMeasurement] = []
        self._source_files: dict[str, SourceFileInfo] = {}

    def set_identity(
        self,
        name: str,
        version: str,
        analyte: str,
        technique: str,
        concentration_unit: str,
    ) -> "MethodBuilder":
        """Set the method's identity and metadata."""
        self._name = name
        self._version = version
        self._analyte = analyte
        self._technique = technique
        self._concentration_unit = concentration_unit
        return self

    def set_fit_type(self, fit_type: FitType | str) -> "MethodBuilder":
        """Set the calibration fit strategy (linear or logarithmic)."""
        self._fit_type = FitType(fit_type)
        return self

    def set_extraction_params(
        self,
        metric: SignalMetric,
        prep_config: PreprocessingConfig | None = None,
        quality_config: QualityConfig | None = None,
    ) -> "MethodBuilder":
        """Set signal extraction and quality criteria."""
        self._signal_metric = metric
        if prep_config is not None:
            self._prep_config = prep_config
        if quality_config is not None:
            self._quality_config = quality_config
        return self

    def add_measurement(self, measurement: CalibrationMeasurement) -> "MethodBuilder":
        """Add a measurement (blank or standard) to the method."""
        if measurement.role in (MeasurementRole.BLANK, MeasurementRole.STANDARD):
            self._measurements.append(measurement)
            self._track_source_file(measurement)
        return self

    def _track_source_file(self, measurement: CalibrationMeasurement) -> None:
        """Track the provenance of the imported file."""
        src = measurement.source
        file_id = f"{src.source_file}:{src.source_format}"

        if file_id not in self._source_files:
            self._source_files[file_id] = SourceFileInfo(
                filename=src.source_file,
                format=src.source_format,
                import_date=datetime.now().isoformat(),
                measurement_ids=[],
            )

        sf = self._source_files[file_id]
        if measurement.measurement_id not in sf.measurement_ids:
            sf.measurement_ids.append(measurement.measurement_id)

    def build(self) -> AnalyticalMethod:
        """Construct the method, extracting signals and fitting the curve.

        Returns
        -------
        AnalyticalMethod
            The completed (and validated) method.

        Raises
        ------
        MethodBuildError
            If there is insufficient data to build the method.
        """
        logger.info("Building method: %s v%s", self._name, self._version)

        # 1. Extract signals for all measurements.
        for m in self._measurements:
            try:
                m.signal_value = extract_signal_from_imported(
                    m.source,
                    metric=self._signal_metric,
                    config=self._prep_config,
                )
            except Exception as exc:
                raise MethodBuildError(
                    f"Failed to extract signal for {m.measurement_id}: {exc}"
                ) from exc

        # 2. Compute blank statistics.
        blanks = [m for m in self._measurements if m.role == MeasurementRole.BLANK]
        blank_stats: BlankStats | None = None

        if blanks:
            # Re-use BlankStats computation (mean, stdev).
            # We don't use the blank_store's append logic, just the dataclass.
            # However, BlankStats doesn't compute itself. We compute it here.
            import statistics
            signals = [b.signal_value for b in blanks]
            mean = statistics.mean(signals)
            stdev = statistics.stdev(signals) if len(signals) > 1 else 0.0
            # standard normal 95% is 1.645
            lob = mean + 1.645 * stdev
            blank_stats = BlankStats(
                mean=mean,
                stdev=stdev,
                count=len(signals),
                lob=lob,
            )

        # 3. Fit calibration curve.
        standards = [m for m in self._measurements if m.role == MeasurementRole.STANDARD]
        cal_result: CalibrationResult | None = None
        cal_range: tuple[float, float] | None = None

        if standards:
            # We reuse the CalibrationCurve engine from interpretation.calibration
            # We create a temporary curve just to get the fit result.
            curve = CalibrationCurve(
                path=None,  # No persistence needed here.
                concentration_unit=self._concentration_unit,
                fit_type=self._fit_type,
            )
            for m in standards:
                if m.concentration is not None:
                    curve.add_point(m.concentration, m.signal_value)

            cal_result = curve.fit()

            if cal_result:
                # Compute range.
                concs = [m.concentration for m in standards if m.concentration is not None]
                if concs:
                    cal_range = (min(concs), max(concs))

        # 4. Compute LOD / LOQ.
        lob, lod, loq = None, None, None
        if blank_stats:
            slope_is_neg = bool(cal_result and cal_result.slope < 0)
            direction = -1.0 if slope_is_neg else 1.0
            lob = blank_stats.mean + direction * 1.645 * blank_stats.stdev
            if cal_result and abs(cal_result.slope) > 1e-30:
                lod = compute_lod(blank_stats, cal_result)
                loq = compute_loq(blank_stats, cal_result)
                if slope_is_neg:
                    lod.current_ua = blank_stats.mean - 3.0 * blank_stats.stdev
                    loq.current_ua = blank_stats.mean - 10.0 * blank_stats.stdev

        # 5. Assemble Method.
        method = AnalyticalMethod(
            name=self._name,
            version=self._version,
            analyte=self._analyte,
            technique=self._technique,
            concentration_unit=self._concentration_unit,
            signal_metric=self._signal_metric,
            preprocessing_config=self._prep_config,
            quality_config=self._quality_config,
            blank_stats=blank_stats,
            calibration_result=cal_result,
            lob=lob,
            lod=lod,
            loq=loq,
            calibration_range=cal_range,
            source_measurements=self._measurements,
            source_files=list(self._source_files.values()),
            created_at=datetime.now().isoformat(),
        )

        # 6. Validate.
        validate_method(method)

        return method
