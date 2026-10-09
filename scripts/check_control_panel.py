#!/usr/bin/env python
"""Standalone smoke-test for the ControlPanel widget.

Opens the panel in a minimal window — no device or acquisition engine needed.
Prints to console whenever ``start_requested`` or ``stop_requested`` fires so
you can verify the signals work by clicking the buttons.

Run from the project root::

    python -m scripts.check_control_panel

Or directly::

    python scripts/check_control_panel.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure the project root is importable when running the script directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PySide6.QtWidgets import QApplication

from ui.control_panel import ControlPanel


def _on_start(potential: float, run_time: float) -> None:
    print(f"[signal] start_requested  potential={potential:.3f} V, "
          f"run_time={run_time:.1f} s")


def _on_stop() -> None:
    print("[signal] stop_requested")


def main() -> None:
    app = QApplication(sys.argv)

    panel = ControlPanel()
    panel.setWindowTitle("ChronoAmp — Control Panel Check")
    panel.resize(320, 200)

    # Wire signals to console-printing slots.
    panel.start_requested.connect(_on_start)
    panel.stop_requested.connect(_on_stop)

    # Simulate the measurement finishing 3 s after Start is clicked,
    # so we can verify the panel re-enables properly.
    from PySide6.QtCore import QTimer

    def _simulate_finish() -> None:
        print("[sim]    Measurement finished → re-enabling controls")
        panel.set_running(False)

    def _on_start_with_sim(potential: float, run_time: float) -> None:
        QTimer.singleShot(3000, _simulate_finish)

    panel.start_requested.connect(_on_start_with_sim)

    panel.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
