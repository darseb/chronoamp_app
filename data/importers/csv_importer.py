"""CSV importer — thin wrapper reusing the same column-mapping concept
as the Excel importer.

Reads a CSV file and returns normalised :class:`ImportedMeasurement` objects.
"""

from __future__ import annotations

import csv
import logging
from pathlib import Path
from typing import Any

from data.importer_models import ColumnMapping, ImportedMeasurement
from data.importers.excel_importer import (
    ExcelImportError,
    _is_unit_row,
    _to_float,
    detect_column_mapping,
)

logger = logging.getLogger(__name__)


class CsvImportError(Exception):
    """Raised when a CSV import fails."""


def import_from_csv(
    path: str | Path,
    mapping: ColumnMapping | None = None,
    delimiter: str = ",",
    encoding: str = "utf-8",
) -> list[ImportedMeasurement]:
    """Import measurements from a CSV file.

    Parameters
    ----------
    path : str | Path
        Path to the CSV file.
    mapping : ColumnMapping | None
        Column assignments.  If ``None``, auto-detection is attempted.
    delimiter : str
        Field delimiter.
    encoding : str
        File encoding.

    Returns
    -------
    list[ImportedMeasurement]
        One or more normalised measurements.
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    with path.open("r", newline="", encoding=encoding) as fh:
        # Sniff delimiter if possible.
        sample = fh.read(4096)
        fh.seek(0)

        try:
            dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
            delimiter = dialect.delimiter
        except csv.Error:
            pass  # use the provided delimiter

        reader = csv.reader(fh, delimiter=delimiter)
        all_rows = list(reader)

    if len(all_rows) < 2:
        raise CsvImportError("CSV file has fewer than 2 rows.")

    # Strip leading comment rows (e.g. "sep=," or "# metadata").
    while all_rows and all_rows[0] and all_rows[0][0].startswith(("#", "sep=")):
        all_rows.pop(0)

    if len(all_rows) < 2:
        raise CsvImportError("No data rows after stripping comments.")

    header = all_rows[0]
    columns = [str(c).strip() for c in header]
    data_rows = all_rows[1:]

    # Skip unit row if detected.
    if data_rows and _is_unit_row(tuple(data_rows[0])):
        data_rows = data_rows[1:]

    if not data_rows:
        raise CsvImportError("No data rows found after header.")

    if mapping is None:
        mapping = detect_column_mapping(columns)

    # Resolve indices.
    time_col = mapping.time
    current_col = mapping.current

    time_idx = columns.index(time_col) if time_col in columns else None
    current_idx = columns.index(current_col) if current_col in columns else None

    if time_idx is None or current_idx is None:
        raise CsvImportError(
            f"Cannot identify time/current columns. "
            f"Mapping: time={mapping.time}, current={mapping.current}. "
            f"Available: {columns}"
        )

    times: list[float] = []
    currents: list[float] = []
    for row in data_rows:
        t = _to_float(row[time_idx]) if time_idx < len(row) else None
        c = _to_float(row[current_idx]) if current_idx < len(row) else None
        if t is not None and c is not None:
            times.append(t)
            currents.append(c)

    if not times:
        raise CsvImportError("No valid numeric data in time/current columns.")

    return [ImportedMeasurement(
        source_file=path.name,
        source_format="csv",
        measurement_name=path.stem,
        measurement_index=0,
        time_s=times,
        current_ua=currents,
        metadata={"columns": columns, "delimiter": delimiter},
    )]
