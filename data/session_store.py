"""Persist and retrieve measurement sessions as CSV files.

Each session is stored as a single CSV file whose first rows contain metadata
(timestamp, config, verdict) followed by the raw time/current data.

CSV layout::

    # metadata
    # timestamp,2025-06-15T14:30:00
    # applied_potential,0.000
    # run_time,10.0
    # verdict,POSITIVE
    # explanation,Signal above threshold (1.234 µA ≥ -0.0001 µA).
    time,current
    0.0000,1.2345
    0.1000,1.2340
    ...
"""

from __future__ import annotations

import csv
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

from config.settings import SESSIONS_FOLDER
from core.models import DataPoint, MeasurementConfig
from interpretation.verdict import Verdict

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data structure returned by load_session
# ---------------------------------------------------------------------------

@dataclass
class SessionData:
    """All data and metadata recovered from a saved session CSV."""

    timestamp: str
    applied_potential: float
    run_time: float
    verdict: Verdict
    explanation: str
    data_points: list[DataPoint]


# -- Metadata key constants -------------------------------------------------
_META_PREFIX = "# "
_META_KEYS = ("timestamp", "applied_potential", "run_time", "verdict", "explanation")


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def save_session(
    config: MeasurementConfig,
    data_points: list[DataPoint],
    verdict: Verdict,
    explanation: str,
    timestamp: datetime | str | None = None,
    *,
    sessions_folder: str | Path | None = None,
) -> Path:
    """Save a measurement session to a CSV file.

    Parameters
    ----------
    config : MeasurementConfig
        Measurement configuration used for the run.
    data_points : list[DataPoint]
        Collected data points.
    verdict : Verdict
        Interpretation result.
    explanation : str
        Human-readable explanation of the verdict.
    timestamp : datetime | str | None
        Session timestamp.  Defaults to ``datetime.now()``.
        If a ``datetime`` object is passed it is formatted to ISO-8601.
    sessions_folder : str | Path | None
        Override the default sessions directory (mainly for testing).

    Returns
    -------
    Path
        Absolute path to the created CSV file.
    """
    # Resolve timestamp.
    if timestamp is None:
        timestamp = datetime.now()
    if isinstance(timestamp, datetime):
        ts_str = timestamp.strftime("%Y%m%dT%H%M%S")
        ts_meta = timestamp.isoformat()
    else:
        ts_str = str(timestamp).replace(":", "").replace("-", "")
        ts_meta = str(timestamp)

    # Ensure target directory exists.
    folder = Path(sessions_folder) if sessions_folder else Path(SESSIONS_FOLDER)
    folder.mkdir(parents=True, exist_ok=True)

    filename = f"{ts_str}_{verdict.value}.csv"
    filepath = folder / filename

    with filepath.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)

        # Force Excel to use comma separator regardless of system locale.
        writer.writerow(["sep=,"])

        # -- Metadata rows (prefixed with '# ') ----------------------------
        writer.writerow([f"{_META_PREFIX}metadata"])
        writer.writerow([f"{_META_PREFIX}timestamp", ts_meta])
        writer.writerow([f"{_META_PREFIX}applied_potential", f"{config.potential:.4f}"])
        writer.writerow([f"{_META_PREFIX}run_time", f"{config.run_time:.1f}"])
        writer.writerow([f"{_META_PREFIX}verdict", verdict.value])
        writer.writerow([f"{_META_PREFIX}explanation", explanation])

        # -- Data header + rows ---------------------------------------------
        writer.writerow(["time", "current"])
        for dp in data_points:
            writer.writerow([f"{dp.time:.4f}", f"{dp.current:.6f}"])

    logger.info("Session saved: %s", filepath)
    return filepath.resolve()


def load_session(filepath: str | Path) -> SessionData:
    """Load a previously saved session CSV.

    Parameters
    ----------
    filepath : str | Path
        Path to the session CSV file.

    Returns
    -------
    SessionData
        Parsed metadata and data points.

    Raises
    ------
    FileNotFoundError
        If *filepath* does not exist.
    ValueError
        If the file cannot be parsed.
    """
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"Session file not found: {filepath}")

    meta: dict[str, str] = {}
    data_points: list[DataPoint] = []
    header_seen = False

    with filepath.open("r", newline="", encoding="utf-8") as fh:
        reader = csv.reader(fh)
        for row in reader:
            if not row:
                continue

            # Metadata rows start with "# ".
            first = row[0]
            if first.startswith(_META_PREFIX):
                key = first[len(_META_PREFIX):].strip()
                if key == "metadata":
                    continue  # skip the '# metadata' sentinel
                if len(row) >= 2:
                    meta[key] = row[1].strip()
                continue

            # Data header row.
            if first.strip().lower() == "time":
                header_seen = True
                continue

            # Data rows.
            if header_seen and len(row) >= 2:
                data_points.append(
                    DataPoint(time=float(row[0]), current=float(row[1]))
                )

    # Build SessionData from parsed metadata.
    try:
        return SessionData(
            timestamp=meta.get("timestamp", ""),
            applied_potential=float(meta.get("applied_potential", "0")),
            run_time=float(meta.get("run_time", "0")),
            verdict=Verdict(meta.get("verdict", "INCONCLUSIVE")),
            explanation=meta.get("explanation", ""),
            data_points=data_points,
        )
    except (KeyError, ValueError) as exc:
        raise ValueError(f"Failed to parse session file {filepath}: {exc}") from exc
