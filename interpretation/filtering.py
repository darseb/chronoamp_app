"""Signal preprocessing pipeline for chronoamperometry data.

Provides three sequential filters that clean raw measurement data before
analytical evaluation:

1. **Transient trimming** — removes the initial capacitive charging decay.
2. **Hampel filter** — replaces outlier spikes with local median values.
3. **Savitzky-Golay smoothing** — reduces high-frequency noise while
   preserving peak shape.

The convenience function :func:`preprocess` runs all three in order.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import replace

from config.settings import (
    HAMPEL_N_SIGMA,
    HAMPEL_WINDOW_SIZE,
    SAVGOL_POLYORDER,
    SAVGOL_WINDOW_LENGTH,
    TRANSIENT_TRIM_SECONDS,
)
from core.models import DataPoint


# ---------------------------------------------------------------------------
# 1. Capacitive-transient trimming
# ---------------------------------------------------------------------------

def trim_transient(
    data_points: list[DataPoint],
    trim_seconds: float = TRANSIENT_TRIM_SECONDS,
) -> list[DataPoint]:
    """Discard data points within the initial *trim_seconds* window.

    During a chronoamperometric step the electrode double-layer charges
    exponentially (Cottrell transient, I ∝ t⁻¹/²).  Including this region
    biases steady-state metrics.

    Parameters
    ----------
    data_points : list[DataPoint]
        Raw data ordered by time.
    trim_seconds : float
        Duration (s) of the initial window to discard.

    Returns
    -------
    list[DataPoint]
        Data points with ``time >= trim_seconds``.
    """
    if not data_points or trim_seconds <= 0:
        return list(data_points)
    return [dp for dp in data_points if dp.time >= trim_seconds]


# ---------------------------------------------------------------------------
# 2. Hampel outlier filter
# ---------------------------------------------------------------------------

def hampel_filter(
    data_points: list[DataPoint],
    window_size: int = HAMPEL_WINDOW_SIZE,
    n_sigma: float = HAMPEL_N_SIGMA,
) -> list[DataPoint]:
    """Replace outlier current values with the local median.

    For each point the filter computes the median and Median Absolute
    Deviation (MAD) within a symmetric window of *window_size* neighbours
    on each side.  Points whose current deviates more than
    ``n_sigma × MAD × 1.4826`` from the local median are replaced.

    The factor 1.4826 converts MAD to a consistent estimator of the
    standard deviation for normally distributed data.

    Parameters
    ----------
    data_points : list[DataPoint]
        Ordered data points.
    window_size : int
        Number of neighbours on each side of the centre point.
    n_sigma : float
        Threshold in multiples of the estimated standard deviation.

    Returns
    -------
    list[DataPoint]
        Filtered data points (same length as input).
    """
    if len(data_points) < 3 or window_size < 1:
        return list(data_points)

    n = len(data_points)
    currents = [dp.current for dp in data_points]
    result: list[DataPoint] = []

    for i in range(n):
        lo = max(0, i - window_size)
        hi = min(n, i + window_size + 1)
        window = currents[lo:hi]

        local_median = statistics.median(window)
        deviations = [abs(v - local_median) for v in window]
        mad = statistics.median(deviations)

        deviation_from_median = abs(currents[i] - local_median)

        if mad > 0:
            # Convert MAD to estimated std-dev (consistency constant for normal).
            threshold = n_sigma * mad * 1.4826
            is_outlier = deviation_from_median > threshold
        else:
            # MAD == 0 means all neighbours are identical (or nearly so).
            # Any point that differs from the median is an outlier.
            is_outlier = deviation_from_median > 0

        if is_outlier:
            # Replace outlier with local median.
            result.append(replace(data_points[i], current=local_median))
        else:
            result.append(data_points[i])

    return result


# ---------------------------------------------------------------------------
# 3. Savitzky-Golay smoothing (pure-Python implementation)
# ---------------------------------------------------------------------------

def _savgol_coefficients(window_length: int, polyorder: int) -> list[float]:
    """Compute Savitzky-Golay convolution coefficients.

    Uses the Vandermonde-based least-squares approach so that we do not
    depend on scipy at runtime.  Only the smoothing (0th-derivative)
    coefficients are returned.
    """
    if window_length % 2 == 0:
        raise ValueError("window_length must be odd")
    if polyorder >= window_length:
        raise ValueError("polyorder must be less than window_length")

    half = window_length // 2
    # Build Vandermonde matrix J (window_length × polyorder+1).
    rows: list[list[float]] = []
    for i in range(-half, half + 1):
        rows.append([float(i) ** k for k in range(polyorder + 1)])

    # J^T J
    m = polyorder + 1
    jtj = [[0.0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            jtj[r][c] = sum(rows[i][r] * rows[i][c] for i in range(window_length))

    # Invert J^T J via Gauss-Jordan elimination.
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(m)] for i, row in enumerate(jtj)]
    for col in range(m):
        # Partial pivot.
        max_row = max(range(col, m), key=lambda r: abs(aug[r][col]))
        aug[col], aug[max_row] = aug[max_row], aug[col]
        pivot = aug[col][col]
        if abs(pivot) < 1e-15:
            raise ValueError("Singular matrix in Savitzky-Golay coefficient computation")
        for j in range(2 * m):
            aug[col][j] /= pivot
        for r in range(m):
            if r != col:
                factor = aug[r][col]
                for j in range(2 * m):
                    aug[r][j] -= factor * aug[col][j]

    inv_jtj = [row[m:] for row in aug]

    # Coefficients = first row of (J^T J)^{-1} J^T → smoothing coefficients.
    coeffs: list[float] = []
    for i in range(window_length):
        c = sum(inv_jtj[0][k] * rows[i][k] for k in range(m))
        coeffs.append(c)

    return coeffs


def savgol_smooth(
    data_points: list[DataPoint],
    window_length: int = SAVGOL_WINDOW_LENGTH,
    polyorder: int = SAVGOL_POLYORDER,
) -> list[DataPoint]:
    """Apply Savitzky-Golay smoothing to the current channel.

    Edge points that fall outside the convolution window are left unchanged
    (no extrapolation artefacts).

    Parameters
    ----------
    data_points : list[DataPoint]
        Ordered data points.
    window_length : int
        Convolution window size (must be odd and > polyorder).
    polyorder : int
        Polynomial order for the local fit.

    Returns
    -------
    list[DataPoint]
        Smoothed data points (same length as input).
    """
    n = len(data_points)
    if n < window_length or window_length < 3:
        return list(data_points)

    # Ensure odd window.
    if window_length % 2 == 0:
        window_length += 1

    coeffs = _savgol_coefficients(window_length, polyorder)
    half = window_length // 2
    currents = [dp.current for dp in data_points]

    result: list[DataPoint] = list(data_points)  # copy; edges stay unchanged
    for i in range(half, n - half):
        smoothed = sum(
            coeffs[j] * currents[i - half + j] for j in range(window_length)
        )
        result[i] = replace(data_points[i], current=smoothed)

    return result


# ---------------------------------------------------------------------------
# Convenience: full preprocessing pipeline
# ---------------------------------------------------------------------------

def preprocess(
    data_points: list[DataPoint],
    trim_seconds: float = TRANSIENT_TRIM_SECONDS,
    hampel_window: int = HAMPEL_WINDOW_SIZE,
    hampel_sigma: float = HAMPEL_N_SIGMA,
    sg_window: int = SAVGOL_WINDOW_LENGTH,
    sg_order: int = SAVGOL_POLYORDER,
) -> list[DataPoint]:
    """Run the full preprocessing pipeline: trim → Hampel → Savitzky-Golay.

    Parameters
    ----------
    data_points : list[DataPoint]
        Raw measurement data.
    trim_seconds, hampel_window, hampel_sigma, sg_window, sg_order
        Override defaults from ``config.settings`` if needed.

    Returns
    -------
    list[DataPoint]
        Cleaned data ready for analytical evaluation.
    """
    cleaned = trim_transient(data_points, trim_seconds)
    cleaned = hampel_filter(cleaned, hampel_window, hampel_sigma)
    cleaned = savgol_smooth(cleaned, sg_window, sg_order)
    return cleaned
