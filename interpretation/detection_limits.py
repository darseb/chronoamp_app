"""Compute Limit of Blank (LoB), Limit of Detection (LOD), and Limit of
Quantitation (LOQ) from blank characterization and calibration data.

Follows IUPAC conventions and the definitions used in the user's reference
articles:

    LoB = mean_blank + 1.645 × σ_blank                (Sankar et al. 2024)
    LOD (current) = mean_blank + 3 × σ_blank           (IUPAC / S/N = 3)
    LOQ (current) = mean_blank + 10 × σ_blank

    For LINEAR fits:
        LOD (conc.) = 3  × σ_blank / slope
        LOQ (conc.) = 10 × σ_blank / slope

    For LOGARITHMIC fits  I = m·log10(C) + b  (IUPAC criteria):
        LOD (conc.) = 10^(3σ / |m|)                     (Eq. 2)
        LOQ (conc.) = 10^(10σ / |m|)                    (Eq. 3)

    where σ = standard deviation of the blank response and
          m = slope of the calibration curve.

    Analytical sensitivity = slope / σ_blank            (Mandel & Stiehler 1954)
"""

from __future__ import annotations

import math
from dataclasses import dataclass

from interpretation.blank_store import BlankStats
from interpretation.calibration import CalibrationResult, FitType


# ---------------------------------------------------------------------------
# Data class
# ---------------------------------------------------------------------------

@dataclass
class DetectionLimit:
    """A detection limit expressed in both current and concentration units.

    Attributes
    ----------
    current_ua : float
        The detection limit in µA.
    concentration : float | None
        The detection limit in concentration units, or ``None`` if no
        calibration is available.
    concentration_unit : str
        Unit label for *concentration* (e.g. "ng/mL").
    """

    current_ua: float
    concentration: float | None
    concentration_unit: str = ""

    @property
    def concentration_value(self) -> float | None:
        """Alias for concentration to ensure compatibility."""
        return self.concentration


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def compute_lob(blank_stats: BlankStats) -> float:
    """Limit of Blank (µA).

    LoB = mean_blank + 1.645 × σ_blank

    Represents the highest apparent analyte signal expected from a blank.
    """
    return blank_stats.lob  # already computed in BlankStats


def compute_lod(
    blank_stats: BlankStats,
    calibration: CalibrationResult | None = None,
) -> DetectionLimit:
    """Limit of Detection.

    In current units:
        LOD = mean_blank + 3 × σ_blank

    In concentration units:
        Linear:       LOD = 3 × σ_blank / |slope|
        Logarithmic:  LOD = 10^(3σ / |m|)   (IUPAC Eq. 2)
    """
    lod_current = blank_stats.mean + 3.0 * blank_stats.stdev

    lod_conc: float | None = None
    conc_unit = ""
    if calibration is not None and abs(calibration.slope) > 1e-30:
        fit_type = (
            calibration.fit_type.value
            if hasattr(calibration.fit_type, "value")
            else str(calibration.fit_type)
        ).lower()
        if fit_type == FitType.LOGARITHMIC.value:
            # IUPAC Eq. 2: LOD = 10^(3σ / |m|)
            exponent = (3.0 * blank_stats.stdev) / abs(calibration.slope)
            lod_conc = 10.0 ** exponent if abs(exponent) < 300 else None
        else:
            lod_conc = 3.0 * blank_stats.stdev / abs(calibration.slope)
        conc_unit = calibration.concentration_unit

    return DetectionLimit(
        current_ua=lod_current,
        concentration=lod_conc,
        concentration_unit=conc_unit,
    )


def compute_loq(
    blank_stats: BlankStats,
    calibration: CalibrationResult | None = None,
) -> DetectionLimit:
    """Limit of Quantitation.

    In current units:
        LOQ = mean_blank + 10 × σ_blank

    In concentration units:
        Linear:       LOQ = 10 × σ_blank / |slope|
        Logarithmic:  LOQ = 10^(10σ / |m|)   (IUPAC Eq. 3)
    """
    loq_current = blank_stats.mean + 10.0 * blank_stats.stdev

    loq_conc: float | None = None
    conc_unit = ""
    if calibration is not None and abs(calibration.slope) > 1e-30:
        fit_type = (
            calibration.fit_type.value
            if hasattr(calibration.fit_type, "value")
            else str(calibration.fit_type)
        ).lower()
        if fit_type == FitType.LOGARITHMIC.value:
            # IUPAC Eq. 3: LOQ = 10^(10σ / |m|)
            exponent = (10.0 * blank_stats.stdev) / abs(calibration.slope)
            loq_conc = 10.0 ** exponent if abs(exponent) < 300 else None
        else:
            loq_conc = 10.0 * blank_stats.stdev / abs(calibration.slope)
        conc_unit = calibration.concentration_unit

    return DetectionLimit(
        current_ua=loq_current,
        concentration=loq_conc,
        concentration_unit=conc_unit,
    )


def compute_analytical_sensitivity(
    calibration: CalibrationResult,
    blank_stats: BlankStats,
) -> float | None:
    """Analytical sensitivity (Mandel & Stiehler definition).

    sensitivity = slope / σ_blank

    Higher values indicate better discrimination between small concentration
    differences.  Returns ``None`` if σ_blank is zero.
    """
    if blank_stats.stdev <= 0:
        return None
    return abs(calibration.slope) / blank_stats.stdev
