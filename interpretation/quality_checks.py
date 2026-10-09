"""Quality-control checks for chronoamperometry measurements.

Validates that a measurement has reached steady-state equilibrium and
meets quality criteria before the data is interpreted.  Each check
returns a :class:`QCResult` indicating pass/fail, and :func:`run_all_checks`
aggregates them.

Quality gates (IUPAC / electrochemical best-practice):
    1. Steady-state — |dI/dt| must be below a threshold.
    2. Electrode drift — no monotonic drift beyond tolerance.
    3. Signal-to-noise ratio (SNR ≥ 3, per IUPAC S/N convention).
    4. Coefficient of variation (%CV < 10 %).
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass

from config.settings import (
    FINAL_WINDOW_PERCENTAGE,
    MAX_CV_PERCENT,
    MAX_DRIFT_FRACTION,
    MAX_STEADY_STATE_SLOPE_UA_PER_S,
    MIN_SNR,
)
from core.models import DataPoint
from interpretation.blank_store import BlankStats


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------

@dataclass
class QCResult:
    """Outcome of a single quality-control check.

    Attributes
    ----------
    passed : bool
        ``True`` if the check passed.
    name : str
        Short identifier for the check (e.g. ``"steady_state"``).
    message : str
        Human-readable explanation of the result.
    value : float
        The computed metric value (e.g. slope, SNR, %CV).
    """

    passed: bool
    name: str
    message: str
    value: float


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def _final_window(data_points: list[DataPoint]) -> list[DataPoint]:
    """Extract the final-window slice (last FINAL_WINDOW_PERCENTAGE)."""
    n = len(data_points)
    window_size = max(1, math.floor(n * FINAL_WINDOW_PERCENTAGE))
    return data_points[-window_size:]


def check_steady_state(
    data_points: list[DataPoint],
    max_slope: float = MAX_STEADY_STATE_SLOPE_UA_PER_S,
) -> QCResult:
    """Verify the current is not still changing at the end of the run.

    Computes |dI/dt| via linear regression over the final window.
    """
    window = _final_window(data_points)
    if len(window) < 3:
        return QCResult(
            passed=False,
            name="steady_state",
            message="Too few points in the final window for steady-state check.",
            value=float("nan"),
        )

    times = [dp.time for dp in window]
    currents = [dp.current for dp in window]
    slope = _slope(times, currents)

    passed = abs(slope) <= max_slope
    return QCResult(
        passed=passed,
        name="steady_state",
        message=(
            f"Steady-state OK (|dI/dt| = {abs(slope):.6f} µA/s ≤ {max_slope} µA/s)."
            if passed
            else f"Signal has not stabilized (|dI/dt| = {abs(slope):.6f} µA/s > {max_slope} µA/s)."
        ),
        value=abs(slope),
    )


def check_drift(
    data_points: list[DataPoint],
    max_drift_fraction: float = MAX_DRIFT_FRACTION,
) -> QCResult:
    """Detect monotonic electrode drift in the final window.

    Compares the mean current of the first half vs. the second half of the
    final window.  If the fractional difference exceeds *max_drift_fraction*,
    the check fails.
    """
    window = _final_window(data_points)
    if len(window) < 4:
        return QCResult(
            passed=False,
            name="drift",
            message="Too few points in the final window for drift check.",
            value=float("nan"),
        )

    mid = len(window) // 2
    first_half = [dp.current for dp in window[:mid]]
    second_half = [dp.current for dp in window[mid:]]

    mean_first = statistics.mean(first_half)
    mean_second = statistics.mean(second_half)

    # Avoid division by zero — use the larger absolute mean as the reference.
    ref = max(abs(mean_first), abs(mean_second), 1e-30)
    drift_frac = abs(mean_second - mean_first) / ref

    passed = drift_frac <= max_drift_fraction
    return QCResult(
        passed=passed,
        name="drift",
        message=(
            f"Drift OK (fractional drift = {drift_frac:.4f} ≤ {max_drift_fraction})."
            if passed
            else f"Excessive electrode drift detected "
                 f"(fractional drift = {drift_frac:.4f} > {max_drift_fraction})."
        ),
        value=drift_frac,
    )


def check_snr(
    data_points: list[DataPoint],
    blank_stats: BlankStats | None,
    min_snr: float = MIN_SNR,
) -> QCResult:
    """Evaluate the signal-to-noise ratio.

    SNR = |mean_signal − mean_blank| / σ_blank

    If no blank statistics are available the check is skipped (passes
    automatically).
    """
    if blank_stats is None or blank_stats.stdev <= 0:
        return QCResult(
            passed=True,
            name="snr",
            message="SNR check skipped (no blank statistics available).",
            value=float("nan"),
        )

    window = _final_window(data_points)
    if not window:
        return QCResult(
            passed=False, name="snr",
            message="No data in final window.", value=0.0,
        )

    mean_signal = statistics.mean([dp.current for dp in window])
    snr = abs(mean_signal - blank_stats.mean) / blank_stats.stdev

    passed = snr >= min_snr
    return QCResult(
        passed=passed,
        name="snr",
        message=(
            f"SNR OK ({snr:.2f} ≥ {min_snr})."
            if passed
            else f"Signal-to-noise ratio too low ({snr:.2f} < {min_snr}). "
                 f"Result may not be distinguishable from blank."
        ),
        value=snr,
    )


def check_cv(
    data_points: list[DataPoint],
    max_cv_percent: float = MAX_CV_PERCENT,
) -> QCResult:
    """Check the coefficient of variation in the final window.

    %CV = (σ / |mean|) × 100
    """
    window = _final_window(data_points)
    currents = [dp.current for dp in window]

    if len(currents) < 2:
        return QCResult(
            passed=False, name="cv",
            message="Too few points to compute %CV.", value=float("nan"),
        )

    mean_c = statistics.mean(currents)
    std_c = statistics.stdev(currents)

    if abs(mean_c) < 1e-30:
        # Near-zero mean makes %CV meaningless.
        return QCResult(
            passed=True, name="cv",
            message="%CV check skipped (mean ≈ 0).", value=float("nan"),
        )

    cv_pct = (std_c / abs(mean_c)) * 100.0

    passed = cv_pct <= max_cv_percent
    return QCResult(
        passed=passed,
        name="cv",
        message=(
            f"%CV OK ({cv_pct:.2f}% ≤ {max_cv_percent}%)."
            if passed
            else f"Coefficient of variation too high ({cv_pct:.2f}% > {max_cv_percent}%)."
        ),
        value=cv_pct,
    )


# ---------------------------------------------------------------------------
# Aggregate
# ---------------------------------------------------------------------------

def run_all_checks(
    data_points: list[DataPoint],
    blank_stats: BlankStats | None = None,
) -> list[QCResult]:
    """Run all quality-control checks and return the results.

    Parameters
    ----------
    data_points : list[DataPoint]
        Preprocessed data (transient already trimmed).
    blank_stats : BlankStats | None
        Blank characterization; ``None`` skips the SNR check.

    Returns
    -------
    list[QCResult]
        One entry per check, in order: steady_state, drift, snr, cv.
    """
    return [
        check_steady_state(data_points),
        check_drift(data_points),
        check_snr(data_points, blank_stats),
        check_cv(data_points),
    ]


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _slope(xs: list[float], ys: list[float]) -> float:
    """Simple linear-regression slope."""
    n = len(xs)
    if n < 2:
        return 0.0
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    sum_x2 = sum(x * x for x in xs)
    denom = n * sum_x2 - sum_x * sum_x
    if abs(denom) < 1e-30:
        return 0.0
    return (n * sum_xy - sum_x * sum_y) / denom
