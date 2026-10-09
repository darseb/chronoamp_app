#!/usr/bin/env python
"""Quick smoke-test: discover a PalmSens device, connect, print its name, disconnect.

Run from the project root:

    python -m scripts.check_device

Or directly:

    python scripts/check_device.py
"""

from __future__ import annotations

import logging
import sys

# Ensure the project root is importable when running the script directly.
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from core.device_manager import DeviceManager, DeviceNotFoundError


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    dm = DeviceManager()

    # --- Discover -----------------------------------------------------------
    try:
        devices = dm.list_devices()
    except DeviceNotFoundError as exc:
        print(f"\n{exc}")
        sys.exit(1)

    print(f"\nFound {len(devices)} device(s):")
    for i, dev in enumerate(devices):
        print(f"  [{i}] {dev}")

    if len(devices) > 1:
        print(
            "\nMultiple devices detected — this script auto-selects the first one.\n"
            "In the full app you will be able to choose."
        )

    target = devices[0]

    # --- Connect ------------------------------------------------------------
    print(f"\nConnecting to {target} …")
    dm.connect(target)
    print(f"Connected: {dm.is_connected}")

    # --- Disconnect ---------------------------------------------------------
    print("Disconnecting …")
    dm.disconnect()
    print(f"Connected: {dm.is_connected}")
    print("\nDone — device lifecycle check passed ✓")


if __name__ == "__main__":
    main()
