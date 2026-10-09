"""Persist and summarize blank (zero-analyte) measurements.

A *blank* measurement is one performed without analyte present.  Running
multiple blanks and recording their steady-state current allows the app to
compute the statistical baseline needed for LOD / LOQ calculations
(IUPAC standard: 20–30 replicates recommended).

Blank statistics are persisted to ``blanks.json`` inside the sessions folder
so they survive between application restarts.
"""

from __future__ import annotations

import json
import logging
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path

from config.settings import (
    LOB_K_FACTOR,
    MIN_BLANK_REPLICATES,
    RECOMMENDED_BLANK_REPLICATES,
    SESSIONS_FOLDER,
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class BlankStats:
    """Summary statistics computed from recorded blank measurements.

    Attributes
    ----------
    mean : float
        Mean blank current (µA).
    stdev : float
        Standard deviation of blank currents (µA).
    count : int
        Number of blank replicates recorded.
    lob : float
        Limit of Blank = mean + k × stdev  (µA).
    """

    mean: float
    stdev: float
    count: int
    lob: float


# ---------------------------------------------------------------------------
# BlankStore
# ---------------------------------------------------------------------------

class BlankStore:
    """Record, persist, and query blank measurement statistics.

    Parameters
    ----------
    path : str | Path | None
        Path to the ``blanks.json`` file.  Defaults to
        ``<SESSIONS_FOLDER>/blanks.json``.
    """

    def __init__(self, path: str | Path | None = None) -> None:
        if path is None:
            path = Path(SESSIONS_FOLDER) / "blanks.json"
        self._path = Path(path)
        self._currents: list[float] = []
        self._load()

    # -- Public API ---------------------------------------------------------

    def add_blank(self, mean_current: float) -> None:
        """Append a blank measurement (preprocessed mean steady-state current).

        Parameters
        ----------
        mean_current : float
            Mean current (µA) from the final window of a blank run.
        """
        self._currents.append(mean_current)
        self._save()
        logger.info(
            "Blank recorded (n=%d): %.6f µA", len(self._currents), mean_current
        )

    def get_stats(self) -> BlankStats | None:
        """Compute summary statistics from all recorded blanks.

        Returns
        -------
        BlankStats | None
            ``None`` if fewer than ``MIN_BLANK_REPLICATES`` have been recorded.
        """
        n = len(self._currents)
        if n < MIN_BLANK_REPLICATES:
            return None

        mean = statistics.mean(self._currents)
        stdev = statistics.stdev(self._currents) if n >= 2 else 0.0
        lob = mean + LOB_K_FACTOR * stdev

        return BlankStats(mean=mean, stdev=stdev, count=n, lob=lob)

    @property
    def count(self) -> int:
        """Number of blank replicates currently stored."""
        return len(self._currents)

    @property
    def currents(self) -> list[float]:
        """Copy of the raw blank current values."""
        return list(self._currents)

    @property
    def has_enough(self) -> bool:
        """``True`` if at least ``MIN_BLANK_REPLICATES`` blanks are stored."""
        return len(self._currents) >= MIN_BLANK_REPLICATES

    @property
    def is_recommended(self) -> bool:
        """``True`` if at least ``RECOMMENDED_BLANK_REPLICATES`` blanks exist."""
        return len(self._currents) >= RECOMMENDED_BLANK_REPLICATES

    def reset(self) -> None:
        """Discard all recorded blanks and delete the storage file."""
        self._currents.clear()
        if self._path.exists():
            self._path.unlink()
            logger.info("Blank store reset: %s deleted.", self._path)

    # -- Persistence --------------------------------------------------------

    def _save(self) -> None:
        """Write current state to ``blanks.json``."""
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data = {"currents": self._currents}
        with self._path.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)

    def _load(self) -> None:
        """Load previously recorded blanks from ``blanks.json``."""
        if not self._path.exists():
            return
        try:
            with self._path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            self._currents = [float(v) for v in data.get("currents", [])]
            logger.info("Loaded %d blanks from %s", len(self._currents), self._path)
        except (json.JSONDecodeError, KeyError, TypeError):
            logger.warning("Corrupt blanks file %s — starting fresh.", self._path)
            self._currents = []
