#!/usr/bin/env python
"""Smoke-test: open a window with LivePlotWidget, run a real 10-second CA
measurement at 0 V, and stream data to the plot in real time.

Run from the project root::

    python -m scripts.check_live_plot

Or directly::

    python scripts/check_live_plot.py
"""

from __future__ import annotations

import logging
import queue
import sys
from pathlib import Path

# Ensure the project root is importable when running the script directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication

from core.acquisition import AcquisitionEngine
from core.device_manager import DeviceManager, DeviceNotFoundError
from core.models import MeasurementConfig
from ui.live_plot_widget import LivePlotWidget


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
    )

    # --- Qt application ----------------------------------------------------
    app = QApplication(sys.argv)

    # --- Device connection --------------------------------------------------
    dm = DeviceManager()

    try:
        devices = dm.list_devices()
    except DeviceNotFoundError as exc:
        print(f"\n{exc}")
        sys.exit(1)

    target = devices[0]
    print(f"\nConnecting to {target} …")
    dm.connect(target)
    print(f"Connected: {dm.is_connected}\n")

    # --- Measurement config -------------------------------------------------
    config = MeasurementConfig(
        potential=0.0,       # 0 V
        run_time=10.0,       # 10 seconds
        interval_time=0.1,   # 100 ms between samples
    )

    # --- Widget & engine ----------------------------------------------------
    plot = LivePlotWidget(max_points=2000, update_rate=30)
    plot.setWindowTitle("ChronoAmp — Live Plot Check")
    plot.resize(900, 500)
    plot.show()

    engine = AcquisitionEngine(dm, config)

    # --- Timer to drain the queue on the GUI thread -------------------------
    # We poll the engine's data_queue every 50 ms and feed points into the
    # plot widget.  This keeps the GUI responsive while the SDK callback
    # pushes data from a background thread.
    def poll_queue() -> None:
        batch = 0
        while batch < 200:  # cap per tick to avoid blocking the event loop
            try:
                dp = engine.data_queue.get_nowait()
            except queue.Empty:
                break
            plot.add_point(dp.time, dp.current)
            batch += 1

        # Once measurement is done and queue is drained, stop the timer
        # and clean up.
        if not engine.is_running and engine.data_queue.empty():
            poll_timer.stop()
            if engine.error is not None:
                print(f"\nMeasurement FAILED: {engine.error}")
            else:
                print("\nMeasurement complete ✓")
            dm.disconnect()
            print(f"Disconnected: {not dm.is_connected}")

    poll_timer = QTimer()
    poll_timer.timeout.connect(poll_queue)
    poll_timer.start(50)  # 50 ms → ~20 Hz polling

    # --- Start measurement --------------------------------------------------
    engine.start()

    # --- Run Qt event loop --------------------------------------------------
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
