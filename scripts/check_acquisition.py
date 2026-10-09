#!/usr/bin/env python
"""Smoke-test: run a 10-second chronoamperometry measurement at 0 V and print
every data point as it arrives from the device.

Run from the project root::

    python -m scripts.check_acquisition

Or directly::

    python scripts/check_acquisition.py
"""

from __future__ import annotations

import logging
import queue
import sys
from pathlib import Path

# Ensure the project root is importable when running the script directly.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.acquisition import AcquisitionEngine
from core.device_manager import DeviceManager, DeviceNotFoundError
from core.models import MeasurementConfig


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%H:%M:%S",
    )

    dm = DeviceManager()

    # --- Discover & connect -------------------------------------------------
    try:
        devices = dm.list_devices()
    except DeviceNotFoundError as exc:
        print(f"\n{exc}")
        sys.exit(1)

    target = devices[0]
    print(f"\nConnecting to {target} …")
    dm.connect(target)
    print(f"Connected: {dm.is_connected}\n")

    # --- Configure & run measurement ----------------------------------------
    config = MeasurementConfig(
        potential=0.0,       # 0 V
        run_time=10.0,       # 10 seconds
        interval_time=0.1,   # 100 ms between samples
    )

    engine = AcquisitionEngine(dm, config)
    engine.start()

    print(f"{'Time (s)':>10}  {'Current (µA)':>14}")
    print("-" * 26)

    # Drain the queue until the measurement finishes and all points are
    # consumed.
    while engine.is_running or not engine.data_queue.empty():
        try:
            dp = engine.data_queue.get(timeout=0.25)
        except queue.Empty:
            continue
        print(f"{dp.time:10.4f}  {dp.current:14.6f}")

    # --- Wait for thread exit & check for errors ----------------------------
    engine.finished_event.wait(timeout=5.0)

    if engine.error is not None:
        print(f"\nMeasurement FAILED: {engine.error}")
    else:
        print("\nMeasurement complete ✓")

    # --- Cleanup ------------------------------------------------------------
    dm.disconnect()
    print(f"Disconnected: {not dm.is_connected}")


if __name__ == "__main__":
    main()
