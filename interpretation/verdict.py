"""Evaluate measured current against analytical thresholds and return a verdict.

This module is the **final consumer** of the analytical pipeline:

    Raw data → Preprocessing (Module 1)
             → QC checks (Module 4)
             → Blank-aware or legacy decision
             → Optional concentration prediction (Module 3)

The primary entry point is :func:`interpret`, which returns a
:class:`VerdictReport` containing the verdict, explanation, QC details,
detection limits, and optional predicted concentration.

For backward compatibility, the function also supports returning a simple
``(Verdict, str)`` tuple via the report's ``.as_tuple()`` method.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass, field
from enum import Enum

from config.settings import (
    FINAL_WINDOW_PERCENTAGE,
    NOISE_THRESHOLD_UA,
    PLAUSIBLE_CURRENT_MAX_UA,
    PLAUSIBLE_CURRENT_MIN_UA,
    POSITIVE_CUTOFF_UA,
    TARGET_SAMPLING_TIME_S,
)
from core.models import DataPoint, MeasurementConfig
from data.importer_models import SignalMetric
from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult
from interpretation.detection_limits import (
    DetectionLimit,
    compute_lob,
    compute_lod,
    compute_loq,
)
from interpretation.filtering import preprocess
from interpretation.method import AnalyticalMethod
from interpretation.quality_checks import QCResult, run_all_checks
from interpretation.signal_extraction import extract_current_at_time, extract_signal
from utils.formatting import format_concentration


class Verdict(Enum):
    """Outcome of a chronoamperometry measurement interpretation."""

    POSITIVE = "POSITIVE"
    NEGATIVE = "NEGATIVE"
    INCONCLUSIVE = "INCONCLUSIVE"


# Minimum number of data points required for a meaningful interpretation.
_MIN_POINTS = 10


@dataclass
class VerdictReport:
    """Rich result from the :func:`interpret` function.

    Attributes
    ----------
    verdict : Verdict
        The qualitative outcome.
    explanation : str
        Human-readable reason for the verdict.
    mean_current : float
        Mean steady-state current (µA) from the final window.
    qc_results : list[QCResult]
        Individual quality-control check outcomes.
    lod : DetectionLimit | None
        Limit of detection, if blank stats were available.
    loq : DetectionLimit | None
        Limit of quantitation, if blank stats were available.
    lob : float | None
        Limit of blank (µA), if blank stats were available.
    predicted_concentration : float | None
        Predicted analyte concentration, if a valid calibration exists.
    concentration_unit : str
        Unit for predicted_concentration.
    mode : str
        ``"blank_aware"`` or ``"legacy"`` — indicates which decision
        path was used.
    sampling_time : float | None
        Time in seconds at which the stabilized current was sampled (e.g. 185.0 s),
        or None if final-window mean was used.
    """

    verdict: Verdict
    explanation: str
    mean_current: float = 0.0
    qc_results: list[QCResult] = field(default_factory=list)
    lod: DetectionLimit | None = None
    loq: DetectionLimit | None = None
    lob: float | None = None
    predicted_concentration: float | None = None
    concentration_unit: str = ""
    mode: str = "legacy"
    sampling_time: float | None = None

    def as_tuple(self) -> tuple[Verdict, str]:
        """Backward-compatible ``(Verdict, explanation)`` pair."""
        return self.verdict, self.explanation


def interpret(
    data_points: list[DataPoint],
    config: MeasurementConfig,
    *,
    blank_stats: BlankStats | None = None,
    calibration: CalibrationResult | None = None,
    run_preprocessing: bool = True,
) -> tuple[Verdict, str]:
    """Interpret a completed measurement and return a verdict.

    This is the main entry point.  It runs the full analytical pipeline:

    1. **Preprocess** the raw data (trim transient, Hampel, Savitzky-Golay).
    2. **Quality-control checks** (steady-state, drift, SNR, %CV).
    3. **Decision**: blank-aware (if blank stats available) or legacy cutoff.
    4. **Concentration prediction** (if a valid calibration exists).

    Parameters
    ----------
    data_points : list[DataPoint]
        All data points collected during the measurement, ordered by time.
    config : MeasurementConfig
        The measurement configuration used for the run.
    blank_stats : BlankStats | None
        Blank characterization statistics.  When provided, the decision
        switches from the legacy hardcoded cutoff to a statistically
        grounded blank-aware mode using LOD.
    calibration : CalibrationResult | None
        Calibration curve fit result.  When provided (and valid), the
        report includes a predicted analyte concentration.
    run_preprocessing : bool
        If ``True`` (default), data is preprocessed before evaluation.
        Set to ``False`` if data has already been cleaned.

    Returns
    -------
    tuple[Verdict, str]
        A ``(verdict, explanation)`` pair for backward compatibility.
        Use :func:`interpret_full` for the rich :class:`VerdictReport`.
    """
    report = interpret_full(
        data_points, config,
        blank_stats=blank_stats,
        calibration=calibration,
        run_preprocessing=run_preprocessing,
    )
    return report.as_tuple()


def interpret_full(
    data_points: list[DataPoint],
    config: MeasurementConfig,
    *,
    blank_stats: BlankStats | None = None,
    calibration: CalibrationResult | None = None,
    run_preprocessing: bool = True,
) -> VerdictReport:
    """Full analytical interpretation returning a :class:`VerdictReport`.

    See :func:`interpret` for parameter documentation.
    """
    # -- Guard: too few raw points ------------------------------------------
    if len(data_points) < _MIN_POINTS:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=(
                f"Too few data points collected ({len(data_points)}). "
                f"At least {_MIN_POINTS} are required for a reliable result."
            ),
        )

    # -- Step 1: Preprocessing ----------------------------------------------
    if run_preprocessing:
        cleaned = preprocess(data_points)
    else:
        cleaned = list(data_points)

    # After preprocessing we may have fewer points (transient trimming).
    if len(cleaned) < _MIN_POINTS:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=(
                f"Too few data points remain after preprocessing "
                f"({len(cleaned)}). Measurement may be too short."
            ),
        )

    # -- Step 2: Extract analytical signal -----------------------------------
    # PRIMARY: Use the stabilized current at the target sampling time (185 s).
    # This is the value that gets interpolated into the calibration curve.
    # FALLBACK: If the measurement is too short to reach the target time,
    # use the final-window mean instead.
    max_time = max(dp.time for dp in cleaned)
    sampled_time: float | None = None

    if max_time >= TARGET_SAMPLING_TIME_S:
        # Measurement is long enough — sample at the stabilized point.
        analytical_signal = extract_current_at_time(
            cleaned, target_time=TARGET_SAMPLING_TIME_S, run_preprocessing=False,
        )
        sampled_time = TARGET_SAMPLING_TIME_S
    else:
        # Measurement too short — fall back to final-window mean.
        n_total = len(cleaned)
        window_size = max(1, math.floor(n_total * FINAL_WINDOW_PERCENTAGE))
        final_points = cleaned[-window_size:]
        currents = [dp.current for dp in final_points]
        analytical_signal = statistics.mean(currents)
        # sampled_time stays None → signals that fallback was used.

    # -- Step 3: Quality-control checks -------------------------------------
    qc_results = run_all_checks(cleaned, blank_stats)
    # A low SNR is an analytical outcome (analyte not detected), not a structural
    # failure of the measurement. We don't block the pipeline for it.
    qc_failures = [r for r in qc_results if not r.passed and r.name != "snr"]

    if qc_failures:
        # Report the first failure as the primary reason.
        first_fail = qc_failures[0]
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=first_fail.message,
            mean_current=analytical_signal,
            qc_results=qc_results,
            mode="qc_gated",
            sampling_time=sampled_time,
        )

    # -- Step 4: Plausible-range guard --------------------------------------
    if analytical_signal < PLAUSIBLE_CURRENT_MIN_UA or analytical_signal > PLAUSIBLE_CURRENT_MAX_UA:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=(
                f"Analytical signal ({analytical_signal:.4f} µA) is outside the plausible "
                f"range [{PLAUSIBLE_CURRENT_MIN_UA}, {PLAUSIBLE_CURRENT_MAX_UA}] µA. "
                "This may indicate a sensor fault or open circuit."
            ),
            mean_current=analytical_signal,
            qc_results=qc_results,
            sampling_time=sampled_time,
        )

    # -- Step 5: Decision ---------------------------------------------------
    # Compute detection limits if blank stats available.
    lob_val: float | None = None
    lod_val: DetectionLimit | None = None
    loq_val: DetectionLimit | None = None
    predicted_conc: float | None = None
    conc_unit = ""

    if blank_stats is not None:
        lob_val = compute_lob(blank_stats)
        lod_val = compute_lod(blank_stats, calibration)
        loq_val = compute_loq(blank_stats, calibration)

    # Concentration prediction — uses the stabilized current at 185 s
    # (or the fallback mean) as the value interpolated into the calibration curve.
    if calibration is not None:
        predicted_conc = calibration.predict_concentration(analytical_signal)
        conc_unit = calibration.concentration_unit

    # Build signal description for human-readable explanations.
    if sampled_time is not None:
        _sig_desc = f"at t={sampled_time:.0f} s"
    else:
        _sig_desc = "final-window mean"

    # -- Blank-aware mode ---------------------------------------------------
    if blank_stats is not None and lod_val is not None:
        mode = "blank_aware"
        is_neg_slope = bool(calibration and calibration.slope < 0)

        if is_neg_slope:
            lob_threshold = blank_stats.mean - 1.645 * blank_stats.stdev if lob_val is not None else None
            lod_threshold = blank_stats.mean - 3.0 * blank_stats.stdev
            is_positive = analytical_signal <= lod_threshold
            is_negative = lob_threshold is not None and analytical_signal >= lob_threshold
        else:
            lob_threshold = lob_val
            lod_threshold = lod_val.current_ua
            is_positive = analytical_signal >= lod_threshold
            is_negative = lob_threshold is not None and analytical_signal <= lob_threshold

        if is_positive:
            # POSITIVE: signal beyond LOD.
            cmp_sym = "≤" if is_neg_slope else "≥"
            explanation = (
                f"Signal above LOD ({analytical_signal:.4f} µA {cmp_sym} "
                f"{lod_threshold:.4f} µA, {_sig_desc})."
            )
            if predicted_conc is not None:
                formatted = format_concentration(predicted_conc, unit=conc_unit)
                explanation += f" Predicted concentration: {formatted}."
            return VerdictReport(
                verdict=Verdict.POSITIVE,
                explanation=explanation,
                mean_current=analytical_signal,
                qc_results=qc_results,
                lod=lod_val, loq=loq_val, lob=lob_val,
                predicted_concentration=predicted_conc,
                concentration_unit=conc_unit,
                mode=mode,
                sampling_time=sampled_time,
            )
        elif is_negative:
            # NEGATIVE: indistinguishable from blank.
            cmp_sym = "≥" if is_neg_slope else "≤"
            return VerdictReport(
                verdict=Verdict.NEGATIVE,
                explanation=(
                    f"Signal indistinguishable from blank "
                    f"({analytical_signal:.4f} µA {cmp_sym} LoB {lob_threshold:.4f} µA, {_sig_desc})."
                ),
                mean_current=analytical_signal,
                qc_results=qc_results,
                lod=lod_val, loq=loq_val, lob=lob_val,
                predicted_concentration=predicted_conc,
                concentration_unit=conc_unit,
                mode=mode,
                sampling_time=sampled_time,
            )
        else:
            # Between LoB and LOD — inconclusive grey zone.
            low = min(lob_threshold, lod_threshold)
            high = max(lob_threshold, lod_threshold)
            return VerdictReport(
                verdict=Verdict.INCONCLUSIVE,
                explanation=(
                    f"Signal in grey zone between LoB and LOD "
                    f"({low:.4f} < {analytical_signal:.4f} < {high:.4f} µA, "
                    f"{_sig_desc}). Detection is uncertain."
                ),
                mean_current=analytical_signal,
                qc_results=qc_results,
                lod=lod_val, loq=loq_val, lob=lob_val,
                predicted_concentration=predicted_conc,
                concentration_unit=conc_unit,
                mode=mode,
                sampling_time=sampled_time,
            )

    # -- Legacy mode (no blank stats) ---------------------------------------
    mode = "legacy"
    if analytical_signal >= POSITIVE_CUTOFF_UA:
        explanation = (
            f"Signal above threshold ({analytical_signal:.4f} µA ≥ "
            f"{POSITIVE_CUTOFF_UA} µA, {_sig_desc})."
        )
        if predicted_conc is not None:
            formatted = format_concentration(predicted_conc, unit=conc_unit)
            explanation += f" Predicted concentration: {formatted}."
        verdict = Verdict.POSITIVE
    else:
        explanation = (
            f"Signal below threshold ({analytical_signal:.4f} µA < "
            f"{POSITIVE_CUTOFF_UA} µA, {_sig_desc})."
        )
        verdict = Verdict.NEGATIVE

    return VerdictReport(
        verdict=verdict,
        explanation=explanation,
        mean_current=analytical_signal,
        qc_results=qc_results,
        lod=lod_val, loq=loq_val, lob=lob_val,
        predicted_concentration=predicted_conc,
        concentration_unit=conc_unit,
        mode=mode,
        sampling_time=sampled_time,
    )


def interpret_with_method(
    data_points: list[DataPoint],
    config: MeasurementConfig,
    method: AnalyticalMethod,
) -> VerdictReport:
    """Interpret a measurement using a predefined Analytical Method.

    This workflow bypasses the legacy cutoffs and instead uses the explicit
    preprocessing, quality configuration, and signal extraction metric
    defined in the ``AnalyticalMethod``.

    It provides enhanced verdict granularity based on the analytical limits:
    - Signal < LOB → NEGATIVE
    - LOB < Signal < LOD → INCONCLUSIVE (grey zone)
    - LOD ≤ Signal < LOQ → POSITIVE (Detected but not quantifiable)
    - LOQ ≤ Signal ≤ cal_max → POSITIVE (Quantifiable)
    - Signal > cal_max → POSITIVE (Above range)
    """
    # -- Guard: too few raw points ------------------------------------------
    if len(data_points) < _MIN_POINTS:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=(
                f"Too few data points collected ({len(data_points)}). "
                f"At least {_MIN_POINTS} are required."
            ),
        )

    # -- Step 1: Extract Signal using Method parameters ----------------------
    try:
        # extract_signal runs the preprocessing as configured in the method
        signal_val = extract_signal(
            data_points,
            metric=method.signal_metric,
            config=method.preprocessing_config,
        )
    except ValueError as exc:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=f"Signal extraction failed: {exc}",
        )

    # For QC checks, we still need the preprocessed points.
    cleaned = preprocess(
        data_points,
        trim_seconds=method.preprocessing_config.trim_seconds,
        hampel_window=method.preprocessing_config.hampel_window,
        hampel_sigma=method.preprocessing_config.hampel_sigma,
        sg_window=method.preprocessing_config.sg_window,
        sg_order=method.preprocessing_config.sg_order,
    )

    # -- Step 2: Quality-control checks -------------------------------------
    # Override settings with method's quality config
    qc_results = run_all_checks(cleaned, method.blank_stats)
    
    # We could theoretically filter the qc_results based on the method.quality_config,
    # but the checks currently read from global settings. For this phase, we
    # just accept the global checks, or we'd need to refactor run_all_checks.
    # We will assume for now the method config matches global settings or 
    # we just pass the results through.
    
    sampled_time = (
        method.preprocessing_config.sampling_time_s
        if method.signal_metric in (SignalMetric.POINT_AT_TIME, SignalMetric.STABILIZED_POINT)
        else None
    )

    qc_failures = [r for r in qc_results if not r.passed and r.name != "snr"]
    if qc_failures:
        first_fail = qc_failures[0]
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=first_fail.message,
            mean_current=signal_val,
            qc_results=qc_results,
            mode="method_gated",
            sampling_time=sampled_time,
        )

    # -- Step 3: Plausible-range guard --------------------------------------
    if signal_val < PLAUSIBLE_CURRENT_MIN_UA or signal_val > PLAUSIBLE_CURRENT_MAX_UA:
        return VerdictReport(
            verdict=Verdict.INCONCLUSIVE,
            explanation=(
                f"Signal ({signal_val:.4f} µA) is outside the plausible "
                f"range [{PLAUSIBLE_CURRENT_MIN_UA}, {PLAUSIBLE_CURRENT_MAX_UA}] µA."
            ),
            mean_current=signal_val,
            qc_results=qc_results,
            sampling_time=sampled_time,
        )

    # -- Step 4: Decision against Method limits -----------------------------
    cal = method.calibration_result
    lob = method.lob
    lod = method.lod.current_ua if method.lod else None
    loq = method.loq.current_ua if method.loq else None
    
    # Detect negative slope (cathodic reduction / signal-off)
    is_neg_slope = bool(cal and cal.slope < 0)

    # If method stats had positive offsets for a negative slope, re-align them
    if is_neg_slope and method.blank_stats is not None:
        if lob is not None and lod is not None and lob < lod:
            lob = method.blank_stats.mean - 1.645 * method.blank_stats.stdev
            lod = method.blank_stats.mean - 3.0 * method.blank_stats.stdev
            loq = method.blank_stats.mean - 10.0 * method.blank_stats.stdev
    
    cal_max = None
    if method.calibration_range:
        cal_max_conc = method.calibration_range[1]
        if cal:
            cal_max = cal.predict_signal(cal_max_conc)

    predicted_conc: float | None = None
    if cal:
        predicted_conc = cal.predict_concentration(signal_val)

    conc_unit = method.concentration_unit
    mode = "method_aware"

    # Evaluate enhanced limits
    if lob is not None and lod is not None:
        if is_neg_slope:
            # Negative slope: signal moves in -I direction
            if signal_val >= lob:
                return VerdictReport(
                    verdict=Verdict.NEGATIVE,
                    explanation=f"Signal indistinguishable from blank ({signal_val:.4f} µA ≥ LoB {lob:.4f} µA).",
                    mean_current=signal_val, qc_results=qc_results, mode=mode,
                    lod=method.lod, loq=method.loq, lob=lob,
                    predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                    sampling_time=sampled_time,
                )
            elif lob > signal_val > lod:
                return VerdictReport(
                    verdict=Verdict.INCONCLUSIVE,
                    explanation=f"Signal in grey zone between LoB and LOD ({lod:.4f} < {signal_val:.4f} < {lob:.4f} µA). Detection uncertain.",
                    mean_current=signal_val, qc_results=qc_results, mode=mode,
                    lod=method.lod, loq=method.loq, lob=lob,
                    predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                    sampling_time=sampled_time,
                )
            elif signal_val <= lod:
                if loq is not None and signal_val > loq:
                    _loq_expl = "Analyte detected but below LOQ"
                    if method.loq and method.loq.concentration is not None:
                        _loq_fmt = format_concentration(method.loq.concentration, unit=conc_unit)
                        _loq_expl += f" (LOQ = {_loq_fmt})"
                    _loq_expl += "."
                    if predicted_conc is not None:
                        _est_fmt = format_concentration(predicted_conc, unit=conc_unit)
                        _loq_expl += f" Estimated concentration: {_est_fmt} (not reliable)."
                    else:
                        _loq_expl += " Concentration not reliable."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=_loq_expl,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )
                elif cal_max is not None and signal_val < cal_max:
                    explanation = f"Signal above calibration range (< {cal_max:.4f} µA)."
                    if predicted_conc is not None:
                        formatted = format_concentration(predicted_conc, unit=conc_unit)
                        explanation += f" Extrapolated concentration: {formatted}."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=explanation,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )
                else:
                    explanation = f"Analyte detected ({signal_val:.4f} µA)."
                    if predicted_conc is not None:
                        formatted = format_concentration(predicted_conc, unit=conc_unit)
                        explanation += f" Concentration: {formatted}."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=explanation,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )
        else:
            # Positive slope: signal moves in +I direction
            if signal_val <= lob:
                return VerdictReport(
                    verdict=Verdict.NEGATIVE,
                    explanation=f"Signal indistinguishable from blank ({signal_val:.4f} µA ≤ LoB {lob:.4f} µA).",
                    mean_current=signal_val, qc_results=qc_results, mode=mode,
                    lod=method.lod, loq=method.loq, lob=lob,
                    predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                    sampling_time=sampled_time,
                )
            elif lob < signal_val < lod:
                return VerdictReport(
                    verdict=Verdict.INCONCLUSIVE,
                    explanation=f"Signal in grey zone between LoB and LOD ({lob:.4f} < {signal_val:.4f} < {lod:.4f} µA). Detection uncertain.",
                    mean_current=signal_val, qc_results=qc_results, mode=mode,
                    lod=method.lod, loq=method.loq, lob=lob,
                    predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                    sampling_time=sampled_time,
                )
            elif lod <= signal_val:
                if loq is not None and signal_val < loq:
                    _loq_expl = "Analyte detected but below LOQ"
                    if method.loq and method.loq.concentration is not None:
                        _loq_fmt = format_concentration(method.loq.concentration, unit=conc_unit)
                        _loq_expl += f" (LOQ = {_loq_fmt})"
                    _loq_expl += "."
                    if predicted_conc is not None:
                        _est_fmt = format_concentration(predicted_conc, unit=conc_unit)
                        _loq_expl += f" Estimated concentration: {_est_fmt} (not reliable)."
                    else:
                        _loq_expl += " Concentration not reliable."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=_loq_expl,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )
                elif cal_max is not None and signal_val > cal_max:
                    explanation = f"Signal above calibration range (> {cal_max:.4f} µA)."
                    if predicted_conc is not None:
                        formatted = format_concentration(predicted_conc, unit=conc_unit)
                        explanation += f" Extrapolated concentration: {formatted}."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=explanation,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )
                else:
                    explanation = f"Analyte detected ({signal_val:.4f} µA)."
                    if predicted_conc is not None:
                        formatted = format_concentration(predicted_conc, unit=conc_unit)
                        explanation += f" Concentration: {formatted}."
                    return VerdictReport(
                        verdict=Verdict.POSITIVE,
                        explanation=explanation,
                        mean_current=signal_val, qc_results=qc_results, mode=mode,
                        lod=method.lod, loq=method.loq, lob=lob,
                        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
                        sampling_time=sampled_time,
                    )

    # Fallback if method lacks proper stats (shouldn't happen for VALID methods)
    explanation = f"Analyte detected ({signal_val:.4f} µA) using method '{method.name}'."
    if predicted_conc is not None:
        formatted = format_concentration(predicted_conc, unit=conc_unit)
        explanation += f" Concentration: {formatted}."
    
    return VerdictReport(
        verdict=Verdict.POSITIVE if signal_val >= POSITIVE_CUTOFF_UA else Verdict.NEGATIVE,
        explanation=explanation,
        mean_current=signal_val,
        qc_results=qc_results,
        mode=mode,
        lod=method.lod, loq=method.loq, lob=lob,
        predicted_concentration=predicted_conc, concentration_unit=conc_unit,
        sampling_time=sampled_time,
    )
