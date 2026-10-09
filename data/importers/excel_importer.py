"""Flexible Excel importer with heuristic column detection and user mapping.

Supports arbitrary Excel layouts — the importer does **not** hard-code
column names, positions, row counts, or sheet indices.  Instead it:

1. Lists available sheets.
2. Reads a preview of the data (first N rows).
3. Auto-suggests column mappings based on header names and data patterns.
4. Imports measurements using a user-confirmed :class:`ColumnMapping`.

Supported layout strategies:

- **Layout A / raw signal**: Two columns (time, current) — one measurement.
- **Layout C / multi-column**: Time column + one current column per
  measurement — each column is a separate measurement.
- **Layout D / summarized table**: Rows with sample-id, concentration,
  replicate, and a single signal value per row.
"""

from __future__ import annotations

import logging
import re
from pathlib import Path
from typing import Any

import openpyxl

from data.importer_models import ColumnMapping, ImportedMeasurement

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Sheet discovery
# ---------------------------------------------------------------------------

def list_sheets(path: str | Path) -> list[str]:
    """Return the sheet names in an Excel workbook.

    Raises
    ------
    FileNotFoundError
        If *path* does not exist.
    ValueError
        If the file cannot be opened as an Excel workbook.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Excel file not found: {path}")
    try:
        wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
        names = wb.sheetnames
        wb.close()
        return names
    except Exception as exc:
        raise ValueError(f"Cannot open {path.name} as Excel: {exc}") from exc


# ---------------------------------------------------------------------------
# Preview
# ---------------------------------------------------------------------------

def read_sheet_preview(
    path: str | Path,
    sheet: str | None = None,
    max_rows: int = 20,
) -> dict[str, Any]:
    """Read column headers and a sample of rows for UI preview.

    Returns
    -------
    dict
        ``{"columns": [str, ...], "data": [[value, ...], ...], "total_rows": int}``
    """
    path = Path(path)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.active
    if ws is None:
        wb.close()
        raise ValueError("No active sheet found.")

    rows_iter = ws.iter_rows(values_only=True)
    header_row = next(rows_iter, None)
    if header_row is None:
        wb.close()
        return {"columns": [], "data": [], "total_rows": 0}

    columns = [str(c) if c is not None else f"Column_{i}" for i, c in enumerate(header_row)]

    data: list[list[Any]] = []
    total = 0
    for row in rows_iter:
        total += 1
        if total <= max_rows:
            data.append([v for v in row])

    # Count remaining rows (if read_only, ws.max_row may be available).
    total_rows = total
    wb.close()
    return {"columns": columns, "data": data, "total_rows": total_rows}


# ---------------------------------------------------------------------------
# Heuristic column detection
# ---------------------------------------------------------------------------

# Canonical patterns for column identification (case-insensitive).
_PATTERNS: dict[str, list[str]] = {
    "time": [r"time", r"^t$", r"^t\s*\(", r"^s$", r"elapsed"],
    "current": [r"current", r"^i$", r"^i\s*\(", r"µa", r"ua", r"microamp"],
    "potential": [r"potential", r"^e$", r"^e\s*\(", r"^v$", r"volt"],
    "sample_id": [r"sample", r"id$", r"name", r"label", r"identifier"],
    "concentration": [r"conc", r"level", r"amount", r"quantity"],
    "replicate": [r"replic", r"rep$", r"^n$", r"trial", r"repeat"],
    "measurement_type": [r"type", r"role", r"kind", r"category"],
    "concentration_unit": [r"unit", r"conc.*unit"],
}


def detect_column_mapping(
    columns: list[str],
    sample_data: list[list[Any]] | None = None,
) -> ColumnMapping:
    """Suggest a :class:`ColumnMapping` based on column names and data patterns.

    This is a **heuristic** — the user must be able to override every
    suggestion in the UI.
    """
    mapping: dict[str, str | None] = {}
    used: set[str] = set()  # prevent assigning one column to multiple fields

    # Priority order: assign more specific fields first.
    priority_order = [
        "concentration", "concentration_unit", "sample_id", "replicate",
        "measurement_type", "potential", "current", "time",
    ]

    for field in priority_order:
        patterns = _PATTERNS[field]
        best: str | None = None
        for col in columns:
            if col in used:
                continue
            col_lower = col.lower().strip()
            for pat in patterns:
                if re.search(pat, col_lower):
                    best = col
                    break
            if best:
                break
        mapping[field] = best
        if best:
            used.add(best)

    # -- Fallback: if we have unit-row data, use it as a secondary signal ----
    if sample_data and len(sample_data) > 0:
        first_row = sample_data[0]
        unit_hints: dict[str, str] = {}
        for i, cell in enumerate(first_row):
            if cell is None or i >= len(columns):
                continue
            cell_str = str(cell).strip().lower()
            if cell_str in ("s", "sec", "seconds"):
                unit_hints[columns[i]] = "time"
            elif cell_str in ("µa", "ua", "a", "ma"):
                unit_hints[columns[i]] = "current"
            elif cell_str in ("v", "mv"):
                unit_hints[columns[i]] = "potential"

        for col, field in unit_hints.items():
            if mapping.get(field) is None and col not in used:
                mapping[field] = col
                used.add(col)

    # -- PSTrace fallback: "CA i vs t" pattern → time is first col ----------
    # PSTrace exports use "CA i vs t" as header for time and unnamed for current.
    if mapping.get("time") is None and mapping.get("current") is None:
        for col in columns:
            if "vs t" in col.lower() or "vs. t" in col.lower():
                mapping["time"] = col
                used.add(col)
                # The next non-used column is likely the current.
                for col2 in columns:
                    if col2 not in used:
                        mapping["current"] = col2
                        used.add(col2)
                        break
                break

    return ColumnMapping(**mapping)  # type: ignore[arg-type]


# ---------------------------------------------------------------------------
# Import logic
# ---------------------------------------------------------------------------

class ExcelImportError(Exception):
    """Raised when an Excel import fails."""


def import_from_excel(
    path: str | Path,
    sheet: str | None = None,
    mapping: ColumnMapping | None = None,
) -> list[ImportedMeasurement]:
    """Import measurements from an Excel file using a column mapping.

    Parameters
    ----------
    path : str | Path
        Path to the ``.xlsx`` / ``.xls`` file.
    sheet : str | None
        Sheet name.  ``None`` uses the active sheet.
    mapping : ColumnMapping | None
        Column assignments.  If ``None``, auto-detection is attempted.

    Returns
    -------
    list[ImportedMeasurement]
        One or more normalised measurements.

    Raises
    ------
    ExcelImportError
        If the required columns (time + current) cannot be identified.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Excel file not found: {path}")

    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    ws = wb[sheet] if sheet else wb.active
    if ws is None:
        wb.close()
        raise ExcelImportError("No active sheet found.")

    # Read all rows.
    all_rows = list(ws.iter_rows(values_only=True))
    wb.close()

    if len(all_rows) < 2:
        raise ExcelImportError("Sheet has fewer than 2 rows (header + data).")

    header_row = all_rows[0]
    columns = [str(c) if c is not None else f"Column_{i}" for i, c in enumerate(header_row)]
    data_rows = all_rows[1:]

    # Skip unit row if it looks like units (e.g. "s", "µA", "V").
    if data_rows and _is_unit_row(data_rows[0]):
        data_rows = data_rows[1:]

    if not data_rows:
        raise ExcelImportError("No data rows found after header.")

    # Auto-detect mapping if not provided.
    if mapping is None:
        # Pass the first data row (which may be a unit row) as sample_data
        # so the heuristic can use unit hints.
        sample_preview = [list(r) for r in all_rows[1:min(3, len(all_rows))]]
        mapping = detect_column_mapping(columns, sample_data=sample_preview)

    # Resolve column indices.
    col_idx: dict[str, int | None] = {}
    for field_name in ("time", "current", "potential", "sample_id",
                       "concentration", "replicate", "measurement_type",
                       "concentration_unit"):
        col_name = getattr(mapping, field_name)
        if col_name is not None and col_name in columns:
            col_idx[field_name] = columns.index(col_name)
        else:
            col_idx[field_name] = None

    time_idx = col_idx.get("time")
    current_idx = col_idx.get("current")

    # If no time + current columns, try multi-column layout (Layout C).
    if time_idx is not None and current_idx is None:
        return _import_multi_column(path, columns, data_rows, time_idx, mapping)

    if time_idx is None or current_idx is None:
        raise ExcelImportError(
            f"Cannot identify required columns (time, current) in sheet. "
            f"Detected mapping: time={mapping.time}, current={mapping.current}. "
            f"Available columns: {columns}"
        )

    # Check if this is a summarized table (Layout D) or raw signal (Layout A).
    sample_idx = col_idx.get("sample_id")
    conc_idx = col_idx.get("concentration")

    if sample_idx is not None or conc_idx is not None:
        # Looks like a table with one row per sample/replicate.
        return _import_summarized_table(
            path, columns, data_rows, col_idx, mapping,
        )

    # Layout A — single raw signal.
    return _import_raw_signal(path, columns, data_rows, time_idx, current_idx, mapping)


# ---------------------------------------------------------------------------
# Layout A — raw signal (time + current)
# ---------------------------------------------------------------------------

def _import_raw_signal(
    path: Path,
    columns: list[str],
    data_rows: list[tuple],
    time_idx: int,
    current_idx: int,
    mapping: ColumnMapping,
) -> list[ImportedMeasurement]:
    """Import a sheet with time and current columns as a single measurement."""
    times: list[float] = []
    currents: list[float] = []

    for row_num, row in enumerate(data_rows, start=2):
        t = _to_float(row[time_idx] if time_idx < len(row) else None)
        c = _to_float(row[current_idx] if current_idx < len(row) else None)
        if t is not None and c is not None:
            times.append(t)
            currents.append(c)

    if not times:
        raise ExcelImportError("No valid numeric data found in time/current columns.")

    return [ImportedMeasurement(
        source_file=path.name,
        source_format="excel",
        measurement_name=path.stem,
        measurement_index=0,
        time_s=times,
        current_ua=currents,
        metadata={"columns": columns},
    )]


# ---------------------------------------------------------------------------
# Layout C — multi-column (time + one column per measurement)
# ---------------------------------------------------------------------------

def _import_multi_column(
    path: Path,
    columns: list[str],
    data_rows: list[tuple],
    time_idx: int,
    mapping: ColumnMapping,
) -> list[ImportedMeasurement]:
    """Import when each non-time numeric column is a separate measurement."""
    # Find numeric columns (excluding the time column).
    numeric_cols: list[int] = []
    for i, col in enumerate(columns):
        if i == time_idx:
            continue
        # Check if the column contains numeric data.
        sample_vals = [_to_float(row[i]) for row in data_rows[:5] if i < len(row)]
        if any(v is not None for v in sample_vals):
            numeric_cols.append(i)

    if not numeric_cols:
        raise ExcelImportError("No numeric data columns found besides time.")

    results: list[ImportedMeasurement] = []
    for meas_idx, col_i in enumerate(numeric_cols):
        times: list[float] = []
        currents: list[float] = []
        for row in data_rows:
            t = _to_float(row[time_idx] if time_idx < len(row) else None)
            c = _to_float(row[col_i] if col_i < len(row) else None)
            if t is not None and c is not None:
                times.append(t)
                currents.append(c)

        if times:
            results.append(ImportedMeasurement(
                source_file=path.name,
                source_format="excel",
                measurement_name=columns[col_i],
                measurement_index=meas_idx,
                time_s=times,
                current_ua=currents,
                metadata={"column_name": columns[col_i]},
            ))

    if not results:
        raise ExcelImportError("No valid measurements found in multi-column layout.")
    return results


# ---------------------------------------------------------------------------
# Layout D — summarized table (one row per sample/replicate)
# ---------------------------------------------------------------------------

def _import_summarized_table(
    path: Path,
    columns: list[str],
    data_rows: list[tuple],
    col_idx: dict[str, int | None],
    mapping: ColumnMapping,
) -> list[ImportedMeasurement]:
    """Import a table where each row represents a sample with a signal value.

    For summarized tables, each row produces a "measurement" with a
    single data point (the reported signal).
    """
    time_idx = col_idx["time"]
    current_idx = col_idx["current"]
    sample_idx = col_idx.get("sample_id")
    conc_idx = col_idx.get("concentration")
    rep_idx = col_idx.get("replicate")

    results: list[ImportedMeasurement] = []

    for row_num, row in enumerate(data_rows):
        # Get current value.
        if current_idx is not None and current_idx < len(row):
            current_val = _to_float(row[current_idx])
        else:
            continue

        if current_val is None:
            continue

        # Get time value (might be 0 for summarized tables).
        time_val = 0.0
        if time_idx is not None and time_idx < len(row):
            t = _to_float(row[time_idx])
            if t is not None:
                time_val = t

        # Get metadata.
        sample_name = ""
        if sample_idx is not None and sample_idx < len(row):
            sample_name = str(row[sample_idx]) if row[sample_idx] is not None else ""

        meta: dict[str, Any] = {"row": row_num + 2}
        if conc_idx is not None and conc_idx < len(row):
            meta["concentration"] = _to_float(row[conc_idx])
        if rep_idx is not None and rep_idx < len(row):
            meta["replicate"] = row[rep_idx]
        if sample_name:
            meta["sample_id"] = sample_name

        meas_name = sample_name or f"Row_{row_num + 2}"

        results.append(ImportedMeasurement(
            source_file=path.name,
            source_format="excel",
            measurement_name=meas_name,
            measurement_index=row_num,
            time_s=[time_val],
            current_ua=[current_val],
            metadata=meta,
        ))

    if not results:
        raise ExcelImportError("No valid rows found in summarized table.")

    return results


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _to_float(value: Any) -> float | None:
    """Try to convert a cell value to float, returning ``None`` on failure."""
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def _is_unit_row(row: tuple) -> bool:
    """Heuristic: is this row a unit-header row (e.g. 's', 'µA', 'V')?"""
    unit_like = {"s", "µa", "ua", "a", "v", "ma", "c", "µc"}
    count = 0
    total = 0
    for cell in row:
        if cell is None:
            continue
        total += 1
        if str(cell).strip().lower() in unit_like:
            count += 1
    return total > 0 and count / total >= 0.5
