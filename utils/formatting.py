"""Formatting utilities and display preferences for ChronoAmp."""

from __future__ import annotations

from PySide6.QtCore import QSettings

from config.settings import DEFAULT_USE_SCIENTIFIC_NOTATION

_SETTINGS_KEY = "use_scientific_notation"


def get_scientific_notation_preference() -> bool:
    """Retrieve the user's display preference for scientific notation.
    
    Persisted via QSettings across application sessions.
    """
    settings = QSettings("ChronoAmp", "ChronoAmp")
    val = settings.value(_SETTINGS_KEY, DEFAULT_USE_SCIENTIFIC_NOTATION)
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.lower() in ("true", "1", "yes")
    return bool(val)


def set_scientific_notation_preference(enabled: bool) -> None:
    """Save the user's display preference for scientific notation."""
    settings = QSettings("ChronoAmp", "ChronoAmp")
    settings.setValue(_SETTINGS_KEY, enabled)


def format_concentration(
    value: float | None,
    use_scientific: bool | None = None,
    unit: str = "",
    decimals: int = 3,
) -> str:
    """Format a concentration value in scientific notation or plain decimal.

    Parameters
    ----------
    value : float | None
        The numeric concentration value to format.
    use_scientific : bool | None
        If True, use scientific notation (e.g., '1.000e-06').
        If False, use plain decimal notation (e.g., '0.000001').
        If None, automatically use the persisted user preference.
    unit : str
        Optional unit string to append (e.g., 'nM', 'µM', 'ng/mL').
    decimals : int
        Number of decimal digits to display (default: 3).

    Returns
    -------
    str
        Formatted concentration string.
    """
    if value is None:
        return ""

    if use_scientific is None:
        use_scientific = get_scientific_notation_preference()

    if use_scientific:
        formatted = f"{value:.{decimals}e}"
    else:
        if value == 0:
            formatted = "0"
        elif abs(value) >= 1:
            # Round to given decimals, stripping unnecessary trailing zeros after decimal point
            formatted = f"{value:.{decimals}f}".rstrip("0").rstrip(".")
        else:
            # For small fractional values (< 1), format with enough precision to show significant digits
            formatted = f"{value:.8f}".rstrip("0").rstrip(".")
            if not formatted or formatted == "-":
                formatted = "0"

    if unit:
        return f"{formatted} {unit}".strip()
    return formatted
