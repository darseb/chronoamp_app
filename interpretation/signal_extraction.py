"""Extract a single analytical signal value from a measurement trace.

This module bridges imported measurements into the **existing** filtering
pipeline (:mod:`interpretation.filtering`) so that historical calibration
data and live PalmSens data share one authoritative signal-processing path.

Supported metrics (see :class:`SignalMetric`):

- Mean of the final window (default — matches existing verdict logic).
- Median of the final window.
- Peak current (maximum absolute value).
- Last data point.
"""

from __future__ import annotations

import math
import statistics

from config.settings import (
    FINAL_WINDOW_PERCENTAGE,
    HAMPEL_N_SIGMA,
    HAMPEL_WINDOW_SIZE,
    SAVGOL_POLYORDER,
    SAVGOL_WINDOW_LENGTH,
    TARGET_SAMPLING_TIME_S,
    TRANSIENT_TRIM_SECONDS,
)
from core.models import DataPoint
from data.importer_models import ImportedMeasurement, SignalMetric
from interpretation.filtering import preprocess


from dataclasses import asdict, dataclass, fields


# ---------------------------------------------------------------------------
# Preprocessing configuration
# ---------------------------------------------------------------------------

@dataclass
class PreprocessingConfig:
    """Signal preprocessing parameters stored in an Analytical Method.

    These mirror the defaults in ``config.settings`` but can be overridden
    per-method.
    """

    trim_seconds: float = TRANSIENT_TRIM_SECONDS
    hampel_window: int = HAMPEL_WINDOW_SIZE
    hampel_sigma: float = HAMPEL_N_SIGMA
    sg_window: int = SAVGOL_WINDOW_LENGTH
    sg_order: int = SAVGOL_POLYORDER
    final_window_pct: float = FINAL_WINDOW_PERCENTAGE
    sampling_time_s: float = TARGET_SAMPLING_TIME_S

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "PreprocessingConfig":
        valid_keys = {f.name for f in fields(cls)}
        return cls(**{k: v for k, v in d.items() if k in valid_keys})


# ---------------------------------------------------------------------------
# Conversion helper
# ---------------------------------------------------------------------------

def imported_to_datapoints(measurement: ImportedMeasurement) -> list[DataPoint]:
    """Convert an :class:`ImportedMeasurement` to a list of :class:`DataPoint`.

    Maps ``time_s`` → ``time`` and ``current_ua`` → ``current``.
    """
    n = min(len(measurement.time_s), len(measurement.current_ua))
    return [
        DataPoint(time=measurement.time_s[i], current=measurement.current_ua[i])
        for i in range(n)
    ]


# ---------------------------------------------------------------------------
# Signal extraction
# ---------------------------------------------------------------------------

def extract_current_at_time(
    data_points: list[DataPoint],
    target_time: float = TARGET_SAMPLING_TIME_S,
    run_preprocessing: bool = True,
    config: PreprocessingConfig | None = None,
) -> float:
    """Extract interpolated current at a specific time point from a measurement.

    Parameters
    ----------
    data_points : list[DataPoint]
        Measurement data points.
    target_time : float
        Target time in seconds (e.g. 185.0 s for stabilized current).
    run_preprocessing : bool
        Whether to filter/smooth data before extraction.
    config : PreprocessingConfig | None
        Preprocessing configuration.

    Returns
    -------
    float
        Current in µA at target_time.
    """
    if config is None:
        config = PreprocessingConfig()

    if run_preprocessing:
        cleaned = preprocess(
            data_points,
            trim_seconds=config.trim_seconds,
            hampel_window=config.hampel_window,
            hampel_sigma=config.hampel_sigma,
            sg_window=config.sg_window,
            sg_order=config.sg_order,
        )
    else:
        cleaned = list(data_points)

    if not cleaned:
        raise ValueError("No data points available to extract current at target time.")

    pts = sorted(cleaned, key=lambda p: p.time)
    if target_time <= pts[0].time:
        return pts[0].current
    if target_time >= pts[-1].time:
        return pts[-1].current

    # Linear interpolation between adjacent points
    for i in range(len(pts) - 1):
        t1, t2 = pts[i].time, pts[i + 1].time
        if t1 <= target_time <= t2:
            if abs(t2 - t1) < 1e-12:
                return pts[i].current
            frac = (target_time - t1) / (t2 - t1)
            return pts[i].current + frac * (pts[i + 1].current - pts[i].current)

    return pts[-1].current


def extract_signal(
    data_points: list[DataPoint],
    metric: SignalMetric = SignalMetric.MEAN_FINAL_WINDOW,
    config: PreprocessingConfig | None = None,
    run_preprocessing: bool = True,
) -> float:
    """Extract a single analytical signal value from a measurement trace.

    Parameters
    ----------
    data_points : list[DataPoint]
        Raw or pre-cleaned data points.
    metric : SignalMetric
        Which metric to compute from the processed data.
    config : PreprocessingConfig | None
        Preprocessing parameters.  ``None`` uses global defaults.
    run_preprocessing : bool
        If ``True``, data is preprocessed before extraction.

    Returns
    -------
    float
        The extracted signal value in µA.

    Raises
    ------
    ValueError
        If fewer than 3 data points remain after preprocessing.
    """
    if config is None:
        config = PreprocessingConfig()

    if run_preprocessing:
        cleaned = preprocess(
            data_points,
            trim_seconds=config.trim_seconds,
            hampel_window=config.hampel_window,
            hampel_sigma=config.hampel_sigma,
            sg_window=config.sg_window,
            sg_order=config.sg_order,
        )
    else:
        cleaned = list(data_points)

    if len(cleaned) < 3:
        raise ValueError(
            f"Too few data points ({len(cleaned)}) after preprocessing "
            f"for signal extraction."
        )

    # -- Extract based on metric --------------------------------------------
    if metric in (SignalMetric.POINT_AT_TIME, SignalMetric.STABILIZED_POINT):
        target_t = config.sampling_time_s
        return extract_current_at_time(cleaned, target_time=target_t, run_preprocessing=False)

    if metric == SignalMetric.PEAK_CURRENT:
        currents = [dp.current for dp in cleaned]
        # Peak = maximum absolute value (preserving sign).
        return max(currents, key=abs)

    if metric == SignalMetric.LAST_POINT:
        return cleaned[-1].current

    # Final-window metrics.
    n_total = len(cleaned)
    window_size = max(1, math.floor(n_total * config.final_window_pct))
    final_points = cleaned[-window_size:]
    currents = [dp.current for dp in final_points]

    if metric == SignalMetric.MEDIAN_FINAL_WINDOW:
        return statistics.median(currents)

    # Default: MEAN_FINAL_WINDOW.
    return statistics.mean(currents)


def extract_signal_from_imported(
    measurement: ImportedMeasurement,
    metric: SignalMetric = SignalMetric.MEAN_FINAL_WINDOW,
    config: PreprocessingConfig | None = None,
    run_preprocessing: bool = True,
) -> float:
    """Convenience: convert imported measurement and extract signal."""
    data_points = imported_to_datapoints(measurement)
    return extract_signal(data_points, metric, config, run_preprocessing)
