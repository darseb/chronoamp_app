"""Export measurement data to CSV, Excel, or PDF report formats.

Currently supports Excel (.xlsx) export via pandas + openpyxl.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import pandas as pd

from data.session_store import load_session

logger = logging.getLogger(__name__)


def export_to_excel(
    session_filepath: str | Path,
    output_path: str | Path,
) -> Path:
    """Read a session CSV and write a formatted Excel spreadsheet.

    Parameters
    ----------
    session_filepath : str | Path
        Path to the session CSV created by :func:`data.session_store.save_session`.
    output_path : str | Path
        Destination ``.xlsx`` file path.

    Returns
    -------
    Path
        Absolute path to the created Excel file.
    """
    session = load_session(session_filepath)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # -- Build PSTrace compatible DataFrame --------------------------------
    # PSTrace format:
    # A1: "CA i vs t", B1: "" (empty, pandas reads as "Unnamed: 1")
    # A2: "s", B2: "µA"
    # A3+: data
    data: list[dict[str, Any]] = [
        {"CA i vs t": "s", "": "µA"}
    ]
    for dp in session.data_points:
        data.append({"CA i vs t": dp.time, "": dp.current})

    data_df = pd.DataFrame(data)

    report_data = [
        {"Parameter": "Timestamp", "Value": session.timestamp},
        {"Parameter": "Applied Potential (V)", "Value": session.applied_potential},
        {"Parameter": "Run Time (s)", "Value": session.run_time},
        {"Parameter": "Verdict", "Value": session.verdict.value if hasattr(session.verdict, "value") else str(session.verdict)},
        {"Parameter": "Explanation", "Value": session.explanation},
    ]
    report_df = pd.DataFrame(report_data)

    # -- Write to Excel with formatting -------------------------------------
    with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
        data_df.to_excel(writer, sheet_name="Sheet1", index=False)
        report_df.to_excel(writer, sheet_name="Report", index=False)

        # Auto-fit column widths for readability on all sheets.
        for sheetname in writer.sheets:
            ws = writer.sheets[sheetname]
            for col_cells in ws.columns:
                max_len = 0
                col_letter = col_cells[0].column_letter
                for cell in col_cells:
                    try:
                        cell_len = len(str(cell.value or ""))
                    except TypeError:
                        cell_len = 0
                    max_len = max(max_len, cell_len)
                # Add a small margin and cap at 80 chars.
                ws.column_dimensions[col_letter].width = min(max_len + 4, 80)

    logger.info("Excel export saved: %s", output_path)
    return output_path.resolve()
