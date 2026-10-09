"""Domain data models (measurement parameters, sample points, session metadata)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MeasurementConfig:
    """Parameters for a single chronoamperometry measurement.

    Attributes
    ----------
    potential : float
        Applied potential in volts (V).
    run_time : float
        Total measurement duration in seconds (s).
    interval_time : float
        Time between successive data points in seconds (s).
    """

    potential: float
    run_time: float
    interval_time: float


@dataclass(frozen=True)
class DataPoint:
    """A single time–current sample from a running measurement.

    Attributes
    ----------
    time : float
        Elapsed time in seconds since the measurement started.
    current : float
        Measured current in µA at this time point.
    """

    time: float
    current: float
