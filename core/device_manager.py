"""Manage discovery, connection, and lifecycle of PalmSens potentiostat devices.

This module owns the full connection lifecycle — discover, connect, disconnect —
and nothing else.  Measurement logic lives in ``core.acquisition``.
"""

from __future__ import annotations

import logging
from typing import Any

try:
    import pypalmsens as ps
except ImportError:  # SDK not installed — UI can still launch
    ps = None  # type: ignore[assignment]

logger = logging.getLogger(__name__)



# ---------------------------------------------------------------------------
# Custom exceptions
# ---------------------------------------------------------------------------

class DeviceNotFoundError(Exception):
    """Raised when no PalmSens potentiostat can be found on any port.

    The default message is written so a non-programmer can understand what
    went wrong and what to try next.
    """

    def __init__(self, message: str | None = None) -> None:
        super().__init__(
            message
            or (
                "No potentiostat was detected.\n"
                "\n"
                "Please check the following:\n"
                "  1. The device is powered on.\n"
                "  2. The USB cable is securely connected to both the\n"
                "     potentiostat and your computer.\n"
                "  3. The correct driver is installed (see the PalmSens\n"
                "     documentation for your operating system).\n"
                "\n"
                "If the problem persists, try a different USB port or cable."
            )
        )


# ---------------------------------------------------------------------------
# DeviceManager
# ---------------------------------------------------------------------------

class DeviceManager:
    """Discover, connect to, and safely disconnect from a PalmSens device.

    Usage::

        dm = DeviceManager()
        devices = dm.list_devices()      # may raise DeviceNotFoundError
        dm.connect(devices[0])
        # … use dm.manager for low-level calls …
        dm.disconnect()                  # safe even if cable was yanked
    """

    def __init__(self) -> None:
        self._instrument: Any | None = None
        self._context: Any | None = None  # context-manager object from ps.connect
        self._manager: Any | None = None  # the yielded manager inside the CM

    # -- public API ---------------------------------------------------------

    def list_devices(self) -> list:
        """Return available PalmSens instruments.

        Returns
        -------
        list
            One or more ``Instrument`` objects discovered by the SDK.

        Raises
        ------
        DeviceNotFoundError
            If **no** devices are found on any port.
        """
        if ps is None:
            raise DeviceNotFoundError(
                "The PalmSens SDK (pypalmsens) is not installed.\n"
                "Install it and restart the application."
            )
        devices = ps.discover()
        if not devices:
            raise DeviceNotFoundError()
        logger.info("Discovered %d device(s): %s", len(devices), devices)
        return devices

    def connect(self, device: Any) -> None:
        """Open a connection to *device*.

        Parameters
        ----------
        device
            An ``Instrument`` object previously returned by :meth:`list_devices`.

        Raises
        ------
        RuntimeError
            If a connection is already open (call :meth:`disconnect` first).
        """
        if self._manager is not None:
            raise RuntimeError(
                "Already connected to a device. "
                "Call disconnect() before connecting to another one."
            )

        self._instrument = device
        self._context = ps.connect(instrument=device)
        # Enter the context manager to obtain the live manager handle.
        self._manager = self._context.__enter__()
        logger.info("Connected to %s", device)

    def disconnect(self) -> None:
        """Close the current connection.

        This method is **safe to call at any time** — it will not raise even
        if the device was physically unplugged, the connection was already
        closed, or no connection was ever opened.
        """
        # Nothing to do if we never connected.
        if self._context is None:
            return

        # Try the clean SDK exit path first.
        try:
            self._manager.disconnect()
        except Exception:
            logger.debug("SDK disconnect() failed (device may already be gone).",
                         exc_info=True)

        # Always exit the context manager so resources are freed.
        try:
            self._context.__exit__(None, None, None)
        except Exception:
            logger.debug("Context-manager exit failed.", exc_info=True)

        instrument_name = self._instrument
        self._instrument = None
        self._context = None
        self._manager = None
        logger.info("Disconnected from %s", instrument_name)


    # -- properties ---------------------------------------------------------

    @property
    def is_connected(self) -> bool:
        """``True`` when a live connection to a device exists."""
        return self._manager is not None

    @property
    def manager(self) -> Any:
        """The low-level SDK manager handle (available only while connected).

        Raises
        ------
        RuntimeError
            If accessed when no device is connected.
        """
        if self._manager is None:
            raise RuntimeError("No device is connected.")
        return self._manager
