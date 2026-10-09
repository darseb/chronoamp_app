"""Calibration curve engine for electrochemical biosensors.

Builds a linear calibration curve from user-provided standard measurements
(known concentration → measured steady-state current), performs least-squares
regression, and uses the inverse equation to predict analyte concentration
from unknown samples.

Persistence is handled via JSON so the calibration survives between app
sessions.

Theoretical basis (IUPAC / ACS Sensors conventions):
    Sensitivity = slope of the calibration curve (µA per concentration unit)
    Linear range = [C_min, C_max] over which R² ≥ MIN_R_SQUARED
    Predicted concentration = (I_measured − intercept) / slope
"""

from __future__ import annotations

import json
import logging
import math
import statistics
from dataclasses import asdict, dataclass
from pathlib import Path

from config.settings import MIN_CALIBRATION_POINTS, MIN_R_SQUARED, SESSIONS_FOLDER

logger = logging.getLogger(__name__)


from enum import Enum

# ---------------------------------------------------------------------------
# Fit Type enum
# ---------------------------------------------------------------------------

class FitType(str, Enum):
    """Supported mathematical fit models for calibration."""
    LINEAR = "linear"
    LOGARITHMIC = "logarithmic"


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class CalibrationResult:
    """Output of a regression fit on calibration data.

    Attributes
    ----------
    slope : float
        Calibration sensitivity (µA per concentration unit, or µA per decade for log).
    intercept : float
        Y-intercept of the regression line (µA).
    r_squared : float
        Coefficient of determination (R²).
    concentration_min : float
        Lowest standard concentration used.
    concentration_max : float
        Highest standard concentration used.
    n_points : int
        Number of calibration points used in the fit.
    concentration_unit : str
        User-specified unit string for concentrations.
    fit_type : str
        The regression model used: 'linear' or 'logarithmic'.
    """

    slope: float
    intercept: float
    r_squared: float
    concentration_min: float
    concentration_max: float
    n_points: int
    concentration_unit: str = ""
    fit_type: str = "linear"

    def predict_concentration(self, current: float) -> float | None:
        """Predict concentration from measured current based on fit_type."""
        if abs(self.slope) < 1e-30:
            return None
        if self.fit_type == FitType.LOGARITHMIC.value or self.fit_type == FitType.LOGARITHMIC:
            # current = slope * log10(C) + intercept
            # log10(C) = (current - intercept) / slope
            # C = 10 ** ((current - intercept) / slope)
            exponent = (current - self.intercept) / self.slope
            if exponent > 100:
                return float("inf")
            if exponent < -100:
                return 0.0
            return 10.0 ** exponent
        else:
            # Linear: current = slope * C + intercept -> C = (current - intercept) / slope
            return (current - self.intercept) / self.slope

    def predict_signal(self, concentration: float) -> float | None:
        """Predict expected current (µA) for a known concentration."""
        if self.fit_type == FitType.LOGARITHMIC.value or self.fit_type == FitType.LOGARITHMIC:
            if concentration <= 0:
                return None
            return self.slope * math.log10(concentration) + self.intercept
        else:
            return self.slope * concentration + self.intercept


@dataclass(frozen=True)
class CalibrationPoint:
    """A single calibration standard: known concentration and measured current."""

    concentration: float
    current: float


# ---------------------------------------------------------------------------
# CalibrationCurve
# ---------------------------------------------------------------------------

_DEFAULT_PATH = object()


class CalibrationCurve:
    """Build, fit, persist, and apply a calibration curve.

    Parameters
    ----------
    path : str | Path | None
        Path to the ``calibration.json`` file.  Defaults to
        ``<SESSIONS_FOLDER>/calibration.json``. If explicitly ``None``,
        the curve operates strictly in-memory without persistence.
    concentration_unit : str
        Label for concentration units (e.g. "ng/mL", "µM", "U/mL").
    fit_type : FitType | str
        Fit strategy ('linear' or 'logarithmic'). Defaults to 'linear'.
    """

    def __init__(
        self,
        path: str | Path | None = _DEFAULT_PATH,
        concentration_unit: str = "",
        fit_type: FitType | str = FitType.LINEAR,
    ) -> None:
        if path is _DEFAULT_PATH:
            self._path: Path | None = Path(SESSIONS_FOLDER) / "calibration.json"
        elif path is not None:
            self._path = Path(path)
        else:
            self._path = None

        self._points: list[CalibrationPoint] = []
        self._result: CalibrationResult | None = None
        self._concentration_unit = concentration_unit
        self._fit_type = FitType(fit_type)
        self._load()

    @property
    def fit_type(self) -> FitType:
        """Currently active fit strategy."""
        return self._fit_type

    @fit_type.setter
    def fit_type(self, value: FitType | str) -> None:
        self._fit_type = FitType(value)
        self._result = None  # invalidate cached fit

    # -- Public API ---------------------------------------------------------

    def add_point(self, concentration: float, current: float) -> None:
        """Add a calibration standard measurement.

        Parameters
        ----------
        concentration : float
            Known analyte concentration.
        current : float
            Measured steady-state current (µA) for that concentration.
        """
        self._points.append(CalibrationPoint(concentration, current))
        self._result = None  # invalidate cached fit
        self._save()
        logger.info(
            "Calibration point added (n=%d): conc=%.6g, current=%.6f µA",
            len(self._points), concentration, current,
        )

    def fit(self) -> CalibrationResult | None:
        """Perform regression according to the selected fit_type.

        Returns
        -------
        CalibrationResult | None
            ``None`` if fewer than ``MIN_CALIBRATION_POINTS`` exist.
            Otherwise the fit result.

        Raises
        ------
        ValueError
            If ``fit_type == FitType.LOGARITHMIC`` and any standard calibration
            point has concentration <= 0.
        """
        if self._fit_type == FitType.LOGARITHMIC:
            # Exclude blank points (C == 0)
            valid_points = [p for p in self._points if p.concentration != 0.0]

            # Check for non-positive concentrations (e.g. negative values)
            non_positive = [p.concentration for p in valid_points if p.concentration <= 0]
            if non_positive:
                raise ValueError(
                    f"Logarithmic calibration requires all concentrations to be strictly positive (> 0). "
                    f"Found non-positive value: {non_positive[0]}"
                )

            n = len(valid_points)
            if n < MIN_CALIBRATION_POINTS:
                return None

            xs = [math.log10(p.concentration) for p in valid_points]
            ys = [p.current for p in valid_points]
            raw_concs = [p.concentration for p in valid_points]

            slope, intercept = _linear_regression(xs, ys)
            r_sq = _r_squared(xs, ys, slope, intercept)

            self._result = CalibrationResult(
                slope=slope,
                intercept=intercept,
                r_squared=r_sq,
                concentration_min=min(raw_concs),
                concentration_max=max(raw_concs),
                n_points=n,
                concentration_unit=self._concentration_unit,
                fit_type=self._fit_type.value,
            )
        else:
            n = len(self._points)
            if n < MIN_CALIBRATION_POINTS:
                return None

            xs = [p.concentration for p in self._points]
            ys = [p.current for p in self._points]

            slope, intercept = _linear_regression(xs, ys)
            r_sq = _r_squared(xs, ys, slope, intercept)

            self._result = CalibrationResult(
                slope=slope,
                intercept=intercept,
                r_squared=r_sq,
                concentration_min=min(xs),
                concentration_max=max(xs),
                n_points=n,
                concentration_unit=self._concentration_unit,
                fit_type=self._fit_type.value,
            )

        self._save()
        logger.info(
            "Calibration fit (%s): slope=%.6g, intercept=%.6g, R²=%.4f (n=%d)",
            self._fit_type.value, self._result.slope, self._result.intercept,
            self._result.r_squared, self._result.n_points,
        )
        return self._result

    @property
    def result(self) -> CalibrationResult | None:
        """Most recent fit result, or ``None``."""
        return self._result

    @property
    def points(self) -> list[CalibrationPoint]:
        """Copy of the raw calibration points."""
        return list(self._points)

    @property
    def count(self) -> int:
        """Number of calibration points recorded."""
        return len(self._points)

    @property
    def is_valid(self) -> bool:
        """``True`` if a fit exists with R² ≥ ``MIN_R_SQUARED``."""
        return self._result is not None and self._result.r_squared >= MIN_R_SQUARED

    def predict_concentration(self, current: float) -> float | None:
        """Predict analyte concentration from a measured current.

        Returns
        -------
        float | None
            Predicted concentration, or ``None`` if no valid calibration
            exists or the slope is zero.
        """
        if self._result is None:
            return None
        return self._result.predict_concentration(current)

    def reset(self) -> None:
        """Discard all calibration data and delete the storage file."""
        self._points.clear()
        self._result = None
        if self._path is not None and self._path.exists():
            self._path.unlink()
            logger.info("Calibration store reset: %s deleted.", self._path)

    @property
    def concentration_unit(self) -> str:
        return self._concentration_unit

    @concentration_unit.setter
    def concentration_unit(self, value: str) -> None:
        old_unit = self._concentration_unit
        self._concentration_unit = value
        if old_unit and value and old_unit.strip().lower() != value.strip().lower():
            from utils.units import convert_concentration
            self._points = [
                CalibrationPoint(
                    concentration=convert_concentration(p.concentration, old_unit, value),
                    current=p.current,
                )
                for p in self._points
            ]
            if self._points:
                self.fit()
        elif self._result is not None:
            self._result = CalibrationResult(
                slope=self._result.slope,
                intercept=self._result.intercept,
                r_squared=self._result.r_squared,
                concentration_min=self._result.concentration_min,
                concentration_max=self._result.concentration_max,
                n_points=self._result.n_points,
                concentration_unit=value,
                fit_type=self._result.fit_type,
            )
        self._save()

    # -- Persistence --------------------------------------------------------

    def _save(self) -> None:
        if self._path is None:
            return
        self._path.parent.mkdir(parents=True, exist_ok=True)
        data: dict = {
            "concentration_unit": self._concentration_unit,
            "fit_type": self._fit_type.value,
            "points": [
                {"concentration": p.concentration, "current": p.current}
                for p in self._points
            ],
        }
        if self._result is not None:
            data["result"] = asdict(self._result)
        with self._path.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=2)

    def _load(self) -> None:
        if self._path is None or not self._path.exists():
            return
        try:
            with self._path.open("r", encoding="utf-8") as fh:
                data = json.load(fh)
            self._concentration_unit = data.get("concentration_unit", "")
            fit_type_str = data.get("fit_type", "linear")
            self._fit_type = FitType(fit_type_str)
            self._points = [
                CalibrationPoint(
                    concentration=float(p["concentration"]),
                    current=float(p["current"]),
                )
                for p in data.get("points", [])
            ]
            if "result" in data:
                r = data["result"]
                self._result = CalibrationResult(
                    slope=float(r["slope"]),
                    intercept=float(r["intercept"]),
                    r_squared=float(r["r_squared"]),
                    concentration_min=float(r["concentration_min"]),
                    concentration_max=float(r["concentration_max"]),
                    n_points=int(r["n_points"]),
                    concentration_unit=r.get("concentration_unit", ""),
                    fit_type=r.get("fit_type", fit_type_str),
                )
            logger.info(
                "Loaded %d calibration points from %s",
                len(self._points), self._path,
            )
        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            logger.warning("Corrupt calibration file %s — starting fresh.", self._path)
            self._points = []
            self._result = None


# ---------------------------------------------------------------------------
# Private helpers — pure-Python linear regression
# ---------------------------------------------------------------------------

def _linear_regression(xs: list[float], ys: list[float]) -> tuple[float, float]:
    """Ordinary least-squares fit: y = slope * x + intercept."""
    n = len(xs)
    sum_x = sum(xs)
    sum_y = sum(ys)
    sum_xy = sum(x * y for x, y in zip(xs, ys))
    sum_x2 = sum(x * x for x in xs)

    denom = n * sum_x2 - sum_x * sum_x
    if abs(denom) < 1e-30:
        return 0.0, sum_y / n if n else 0.0

    slope = (n * sum_xy - sum_x * sum_y) / denom
    intercept = (sum_y - slope * sum_x) / n
    return slope, intercept


def _r_squared(
    xs: list[float], ys: list[float], slope: float, intercept: float
) -> float:
    """Coefficient of determination for a linear fit."""
    n = len(xs)
    if n < 2:
        return 0.0
    y_mean = sum(ys) / n
    ss_tot = sum((y - y_mean) ** 2 for y in ys)
    ss_res = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(xs, ys))
    if ss_tot < 1e-30:
        return 1.0 if ss_res < 1e-30 else 0.0
    return 1.0 - ss_res / ss_tot
