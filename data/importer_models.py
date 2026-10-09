"""Normalized data structures for imported measurements and calibration assignments.

These models decouple **file-format-specific** parsing (PSTrace, Excel, CSV)
from **analytical** calibration logic.  The calibration system only ever
receives :class:`CalibrationMeasurement` objects — it never needs to know
whether the signal came from a ``.pssession`` file, an Excel spreadsheet,
or a future source.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


# ---------------------------------------------------------------------------
# Signal metric enum
# ---------------------------------------------------------------------------

class SignalMetric(Enum):
    """Method for extracting a single analytical signal value from a trace."""

    MEAN_FINAL_WINDOW = "mean_final_window"
    MEDIAN_FINAL_WINDOW = "median_final_window"
    PEAK_CURRENT = "peak_current"
    LAST_POINT = "last_point"
    POINT_AT_TIME = "point_at_time"
    STABILIZED_POINT = "stabilized_point"


# ---------------------------------------------------------------------------
# Measurement role
# ---------------------------------------------------------------------------

class MeasurementRole(Enum):
    """Analytical role assigned to an imported measurement."""

    BLANK = "blank"
    STANDARD = "standard"
    SAMPLE = "sample"
    IGNORE = "ignore"


# ---------------------------------------------------------------------------
# Imported measurement (format-agnostic)
# ---------------------------------------------------------------------------

@dataclass
class ImportedMeasurement:
    """A single measurement imported from any supported file format.

    All signal arrays are stored in SI-consistent units used internally
    by ChronoAmp:

    - **time** — seconds (s)
    - **current** — microamperes (µA)
    - **potential** — volts (V)
    - **charge** — microcoulombs (µC)

    Attributes
    ----------
    source_file : str
        Original filename or path of the imported file.
    source_format : str
        Format identifier (``"pstrace"``, ``"excel"``, ``"csv"``).
    measurement_name : str
        Human-readable label (e.g. ``"Chronoamperometry [1]"``).
    measurement_index : int
        Zero-based index of this measurement within the source file.
    time_s : list[float]
        Time values in seconds.
    current_ua : list[float]
        Current values in µA.
    potential_v : list[float] | None
        Potential values in V, if available.
    charge_uc : list[float] | None
        Charge values in µC, if available.
    metadata : dict[str, Any]
        Arbitrary key-value metadata preserved from the source.
    """

    source_file: str
    source_format: str
    measurement_name: str
    measurement_index: int
    time_s: list[float]
    current_ua: list[float]
    potential_v: list[float] | None = None
    charge_uc: list[float] | None = None
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def n_points(self) -> int:
        """Number of data points in the measurement."""
        return len(self.time_s)


# ---------------------------------------------------------------------------
# Source file provenance
# ---------------------------------------------------------------------------

@dataclass
class SourceFileInfo:
    """Provenance record for one imported file used to build a method.

    Attributes
    ----------
    filename : str
        Original filename (basename).
    format : str
        Format identifier.
    file_hash : str
        SHA-256 hex digest of the file, or ``""`` if not computed.
    import_date : str
        ISO-8601 timestamp of the import.
    measurement_ids : list[str]
        Identifiers of the measurements used from this file.
    """

    filename: str
    format: str
    file_hash: str = ""
    import_date: str = ""
    measurement_ids: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Calibration measurement (with role assignment)
# ---------------------------------------------------------------------------

@dataclass
class CalibrationMeasurement:
    """A measurement with its analytical role and concentration assigned.

    This is the normalized input to the calibration-fitting pipeline.

    Attributes
    ----------
    source : ImportedMeasurement
        Reference to the full imported measurement data.
    measurement_id : str
        Unique identifier (e.g. ``"file_0_meas_1"``).
    role : MeasurementRole
        Analytical role: blank, standard, or sample.
    concentration : float | None
        Known analyte concentration (only for standards).
    concentration_unit : str
        Unit string for *concentration* (e.g. ``"pg/mL"``).
    replicate : int
        Replicate number (1-based).
    signal_value : float
        Extracted analytical signal (µA), computed by the signal
        extraction module.
    signal_unit : str
        Unit of *signal_value* (always ``"µA"`` for current).
    """

    source: ImportedMeasurement
    measurement_id: str
    role: MeasurementRole
    concentration: float | None = None
    concentration_unit: str = ""
    replicate: int = 1
    signal_value: float = 0.0
    signal_unit: str = "µA"


# ---------------------------------------------------------------------------
# Column mapping (for Excel / CSV imports)
# ---------------------------------------------------------------------------

@dataclass
class ColumnMapping:
    """User-confirmed column assignments for tabular imports.

    Each field is either a column name/index or ``None`` if the column
    is not present in the data.
    """

    time: str | None = None
    current: str | None = None
    potential: str | None = None
    sample_id: str | None = None
    concentration: str | None = None
    concentration_unit: str | None = None
    replicate: str | None = None
    measurement_type: str | None = None
