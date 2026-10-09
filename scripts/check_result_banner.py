#!/usr/bin/env python
"""Visual smoke-test for the ResultBanner widget.

Opens a window with the banner and four buttons so you can cycle through
every verdict state and inspect the styling without any hardware attached.

Run from the project root::

    python -m scripts.check_result_banner

Or directly::

    python scripts/check_result_banner.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root is importable when running the script directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from interpretation.verdict import Verdict
from ui.result_banner import ResultBanner


_SAMPLE_EXPLANATIONS = {
    Verdict.POSITIVE: "Signal above threshold (1.2340 µA ≥ -0.0001 µA).",
    Verdict.NEGATIVE: "Signal below threshold (-3.4500 µA < -0.0001 µA).",
    Verdict.INCONCLUSIVE: (
        "Signal is too noisy (std dev 12.3456 µA exceeds threshold 5.0 µA). "
        "The result cannot be determined reliably."
    ),
    None: "",
}


def main() -> None:
    app = QApplication(sys.argv)

    # -- Dark palette for the container so the banner pops -----------------
    root = QWidget()
    root.setWindowTitle("ChronoAmp — Result Banner Check")
    root.setStyleSheet("background-color: #11111b; color: #cdd6f4;")
    root.resize(640, 260)

    banner = ResultBanner()

    # -- Control buttons ---------------------------------------------------
    btn_layout = QHBoxLayout()
    btn_layout.setSpacing(8)

    btn_font = QFont()
    btn_font.setPointSize(10)

    btn_style = (
        "QPushButton {"
        "  background-color: #313244; color: #cdd6f4; border: 1px solid #45475a;"
        "  border-radius: 6px; padding: 8px 18px;"
        "}"
        "QPushButton:hover { background-color: #45475a; }"
    )

    for label, verdict in [
        ("Positive", Verdict.POSITIVE),
        ("Negative", Verdict.NEGATIVE),
        ("Inconclusive", Verdict.INCONCLUSIVE),
        ("Reset", None),
    ]:
        btn = QPushButton(label)
        btn.setFont(btn_font)
        btn.setStyleSheet(btn_style)
        btn.clicked.connect(
            lambda _checked, v=verdict: banner.set_verdict(
                v, _SAMPLE_EXPLANATIONS[v]
            )
        )
        btn_layout.addWidget(btn)

    # -- Assemble ----------------------------------------------------------
    layout = QVBoxLayout(root)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(20)
    layout.addWidget(banner)
    layout.addLayout(btn_layout)
    layout.addStretch()

    root.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
