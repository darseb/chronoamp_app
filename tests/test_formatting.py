"""Unit tests for utils.formatting — concentration formatting and display preferences."""

from __future__ import annotations

import pytest
from utils.formatting import (
    format_concentration,
    get_scientific_notation_preference,
    set_scientific_notation_preference,
)


class TestFormatConcentration:
    def test_none_returns_empty_string(self) -> None:
        assert format_concentration(None) == ""
        assert format_concentration(None, use_scientific=True) == ""
        assert format_concentration(None, unit="nM") == ""

    def test_zero_formatting(self) -> None:
        assert format_concentration(0.0, use_scientific=False) == "0"
        assert format_concentration(0.0, use_scientific=True) == "0.000e+00"
        assert format_concentration(0.0, use_scientific=False, unit="µM") == "0 µM"

    def test_decimal_mode(self) -> None:
        # Standard values >= 1
        assert format_concentration(1.234, use_scientific=False) == "1.234"
        assert format_concentration(10.5, use_scientific=False) == "10.5"
        assert format_concentration(100.0, use_scientific=False) == "100"

        # Fractional values < 1
        assert format_concentration(0.005, use_scientific=False) == "0.005"
        assert format_concentration(0.000123, use_scientific=False) == "0.000123"

        # With unit
        assert format_concentration(2.5, use_scientific=False, unit="ng/mL") == "2.5 ng/mL"

    def test_scientific_mode(self) -> None:
        assert format_concentration(1.234e-6, use_scientific=True) == "1.234e-06"
        assert format_concentration(5.0e3, use_scientific=True) == "5.000e+03"
        assert format_concentration(1.234e-6, use_scientific=True, unit="M") == "1.234e-06 M"
        assert format_concentration(0.05, use_scientific=True, decimals=2) == "5.00e-02"

    def test_preference_toggle(self) -> None:
        # Set preference to True
        set_scientific_notation_preference(True)
        assert get_scientific_notation_preference() is True
        # format_concentration without use_scientific should respect preference
        formatted = format_concentration(1.234e-5)
        assert "e" in formatted.lower()

        # Set preference to False
        set_scientific_notation_preference(False)
        assert get_scientific_notation_preference() is False
        formatted = format_concentration(1.234)
        assert formatted == "1.234"
