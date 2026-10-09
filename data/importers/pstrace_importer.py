"""Parse PalmSens ``.pssession`` files exported by PSTrace.

A ``.pssession`` file is a **UTF-16 LE** encoded text file whose content
is a single JSON object with the following top-level structure::

    {
        "Type": "PalmSens.DataFiles.SessionFile",
        "CoreVersion": "...",
        "MethodForMeasurement": "...",
        "Measurements": [ ... ]
    }

Each element of ``Measurements`` contains a ``DataSet`` whose ``Values``
array holds typed data-arrays (time, current, potential, charge).  The
arrays are identified *semantically* by their ``Description`` and ``Type``
fields — the parser never relies on fixed positions or hard-coded lengths.

A single ``.pssession`` may hold one **or many** measurements (e.g. when
the user combines multiple runs in PSTrace).

Usage::

    measurements = parse_pssession("experiment.pssession")
    for m in measurements:
        print(m.measurement_name, m.n_points)
"""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any

from data.importer_models import ImportedMeasurement

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Encoding helpers
# ---------------------------------------------------------------------------

def _read_text(path: Path) -> str:
    """Read a ``.pssession`` file, auto-detecting encoding.

    PalmSens typically writes UTF-16 LE with a BOM.  If that fails we
    fall back to UTF-8.
    """
    raw = path.read_bytes()

    # Check for UTF-16 LE BOM (FF FE).
    if raw[:2] == b"\xff\xfe":
        return raw.decode("utf-16-le")

    # Check for UTF-16 BE BOM (FE FF).
    if raw[:2] == b"\xfe\xff":
        return raw.decode("utf-16-be")

    # Try generic utf-16 (Python handles BOM internally).
    try:
        return raw.decode("utf-16")
    except (UnicodeDecodeError, UnicodeError):
        pass

    # Fallback to UTF-8.
    return raw.decode("utf-8")


# ---------------------------------------------------------------------------
# Array extraction helpers
# ---------------------------------------------------------------------------

# Maps Description strings to the ImportedMeasurement field they populate.
_DESCRIPTION_MAP: dict[str, str] = {
    "time": "time",
    "current": "current",
    "potential": "potential",
    "charge": "charge",
}

# Maps PalmSens DataArray Type strings to the semantic key.
_TYPE_MAP: dict[str, str] = {
    "PalmSens.Data.DataArrayTime": "time",
    "PalmSens.Data.DataArrayCurrents": "current",
    "PalmSens.Data.DataArrayPotentials": "potential",
    "PalmSens.Data.DataArrayCharge": "charge",
}


def _identify_array(array_obj: dict[str, Any]) -> str | None:
    """Return the semantic key ('time', 'current', …) for a data-array object.

    Checks ``Description`` first (most reliable), then falls back to
    ``Type``.  Returns ``None`` if the array cannot be identified.
    """
    desc = array_obj.get("Description", "").strip().lower()
    if desc in _DESCRIPTION_MAP:
        return _DESCRIPTION_MAP[desc]

    type_str = array_obj.get("Type", "")
    if type_str in _TYPE_MAP:
        return _TYPE_MAP[type_str]

    return None


def _extract_values(array_obj: dict[str, Any]) -> list[float]:
    """Extract the numeric values from a DataArray's ``DataValues`` list.

    Each element is expected to be ``{"V": <float>}``.
    """
    data_values = array_obj.get("DataValues", [])
    result: list[float] = []
    for dv in data_values:
        if isinstance(dv, dict) and "V" in dv:
            result.append(float(dv["V"]))
        elif isinstance(dv, (int, float)):
            result.append(float(dv))
    return result


def _get_unit_string(array_obj: dict[str, Any]) -> str:
    """Return the unit symbol from a DataArray's ``Unit`` dict, or ``""``."""
    unit = array_obj.get("Unit", {})
    if isinstance(unit, dict):
        return unit.get("S", "")
    return ""


# ---------------------------------------------------------------------------
# Current unit conversion
# ---------------------------------------------------------------------------

def _current_to_ua(values: list[float], unit_str: str, unit_type: str) -> list[float]:
    """Convert current values to µA based on the declared unit.

    PalmSens convention: When the ``Unit.Type`` is
    ``PalmSens.Units.MicroAmpere``, the stored values are already in µA
    even though the ``S`` field reads ``"A"`` (the base SI symbol).
    This function detects that case and returns the values as-is.

    For genuine Ampere-scale values (e.g. from third-party files), it
    converts to µA correctly.
    """
    type_lower = unit_type.lower()

    if "microampere" in type_lower:
        # PalmSens stores values in µA when Type is MicroAmpere.
        return list(values)

    if "milliampere" in type_lower:
        return [v * 1e3 for v in values]

    # If unit symbol indicates the values are in Amperes.
    if unit_str == "A" or "ampere" in type_lower:
        return [v * 1e6 for v in values]

    if unit_str == "mA":
        return [v * 1e3 for v in values]

    if unit_str in ("µA", "uA"):
        return list(values)

    # Unknown unit — return as-is and log a warning.
    logger.debug("Unknown current unit (S=%s, Type=%s) — assuming µA.", unit_str, unit_type)
    return list(values)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

class PsSessionParseError(Exception):
    """Raised when a ``.pssession`` file cannot be parsed."""


def parse_pssession(path: str | Path) -> list[ImportedMeasurement]:
    """Parse a PalmSens ``.pssession`` file and return imported measurements.

    Parameters
    ----------
    path : str | Path
        Path to the ``.pssession`` file.

    Returns
    -------
    list[ImportedMeasurement]
        One entry per measurement found in the file.

    Raises
    ------
    FileNotFoundError
        If *path* does not exist.
    PsSessionParseError
        If the file cannot be decoded or parsed.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"PSTrace session file not found: {path}")

    # -- Read and decode -----------------------------------------------------
    try:
        text = _read_text(path)
    except Exception as exc:
        raise PsSessionParseError(
            f"Failed to decode {path.name}: {exc}"
        ) from exc

    # Strip BOM characters and null bytes from both ends.
    text = text.strip("\ufeff\ufffe\x00")

    # -- Parse JSON ----------------------------------------------------------
    try:
        session = json.loads(text)
    except json.JSONDecodeError as exc:
        raise PsSessionParseError(
            f"Failed to parse JSON in {path.name}: {exc}"
        ) from exc

    if not isinstance(session, dict):
        raise PsSessionParseError(
            f"Expected a JSON object at the top level of {path.name}, "
            f"got {type(session).__name__}."
        )

    # Validate top-level structure.
    session_type = session.get("Type", "")
    if "SessionFile" not in session_type and "DataFiles" not in session_type:
        logger.warning(
            "Unexpected session Type '%s' in %s — attempting to parse anyway.",
            session_type, path.name,
        )

    measurements_raw = session.get("Measurements", [])
    if not isinstance(measurements_raw, list):
        raise PsSessionParseError(
            f"'Measurements' is not a list in {path.name}."
        )

    if not measurements_raw:
        raise PsSessionParseError(
            f"No measurements found in {path.name}."
        )

    # -- Extract metadata from the method string ----------------------------
    method_str = session.get("MethodForMeasurement", "")
    core_version = session.get("CoreVersion", "")

    # -- Parse each measurement ---------------------------------------------
    results: list[ImportedMeasurement] = []
    source_name = path.name

    for idx, meas_raw in enumerate(measurements_raw):
        if not isinstance(meas_raw, dict):
            logger.warning("Measurement #%d in %s is not a dict — skipping.", idx, source_name)
            continue

        title = meas_raw.get("Title", f"Measurement [{idx}]")
        dataset = meas_raw.get("DataSet", {})
        values_list = dataset.get("Values", [])

        if not values_list:
            logger.warning(
                "Measurement '%s' (#%d) in %s has no data arrays — skipping.",
                title, idx, source_name,
            )
            continue

        # Walk the Values array and identify each channel.
        arrays: dict[str, list[float]] = {}
        units: dict[str, str] = {}
        unit_types: dict[str, str] = {}

        for arr_obj in values_list:
            if not isinstance(arr_obj, dict):
                continue
            key = _identify_array(arr_obj)
            if key is None:
                arr_type = arr_obj.get("Type", "unknown")
                arr_desc = arr_obj.get("Description", "unknown")
                logger.debug(
                    "Unrecognised array Type=%s Description=%s in '%s' — skipping.",
                    arr_type, arr_desc, title,
                )
                continue

            values = _extract_values(arr_obj)
            if not values:
                logger.debug("Array '%s' in '%s' has no data values.", key, title)
                continue

            arrays[key] = values
            units[key] = _get_unit_string(arr_obj)
            unit_obj = arr_obj.get("Unit", {})
            unit_types[key] = unit_obj.get("Type", "") if isinstance(unit_obj, dict) else ""

        # We require at least time and current.
        if "time" not in arrays:
            logger.warning(
                "Measurement '%s' (#%d) in %s has no time array — skipping.",
                title, idx, source_name,
            )
            continue
        if "current" not in arrays:
            logger.warning(
                "Measurement '%s' (#%d) in %s has no current array — skipping.",
                title, idx, source_name,
            )
            continue

        # Convert current to µA.
        current_ua = _current_to_ua(
            arrays["current"],
            units.get("current", ""),
            unit_types.get("current", ""),
        )

        # Build metadata dict.
        meta: dict[str, Any] = {
            "title": title,
            "core_version": core_version,
            "device_serial": meas_raw.get("DeviceSerial", ""),
            "device_fw": meas_raw.get("DeviceFW", ""),
            "device_used": meas_raw.get("DeviceUsed", ""),
            "timestamp": meas_raw.get("TimeStamp", ""),
            "utc_timestamp": meas_raw.get("UTCTimeStamp", ""),
            "measurement_type": meas_raw.get("Type", ""),
        }

        results.append(ImportedMeasurement(
            source_file=source_name,
            source_format="pstrace",
            measurement_name=title,
            measurement_index=idx,
            time_s=arrays["time"],
            current_ua=current_ua,
            potential_v=arrays.get("potential"),
            charge_uc=arrays.get("charge"),
            metadata=meta,
        ))

    if not results:
        raise PsSessionParseError(
            f"No usable measurements (with time + current) found in {path.name}."
        )

    logger.info(
        "Parsed %d measurement(s) from %s.", len(results), source_name,
    )
    return results
