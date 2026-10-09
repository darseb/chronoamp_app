"""Run chronoamperometry measurements and stream real-time current samples.

This module provides :class:`AcquisitionEngine`, which wraps the low-level
PalmSens SDK measurement call in a background thread and feeds each new
data point into a :class:`queue.Queue` for thread-safe consumption by any
consumer (UI, logger, file writer, etc.).
"""

from __future__ import annotations

import ctypes
import logging
import queue
import threading
from typing import Any, Callable

try:
    import pypalmsens as ps
except ImportError:
    ps = None  # type: ignore[assignment]

from core.device_manager import DeviceManager
from core.models import DataPoint, MeasurementConfig

logger = logging.getLogger(__name__)


class AcquisitionEngine:
    """Run a chronoamperometry measurement and stream data via a queue.

    Parameters
    ----------
    device_manager : DeviceManager
        An already-connected :class:`DeviceManager`.
    config : MeasurementConfig
        Measurement parameters (potential, run_time, interval_time).

    Usage::

        engine = AcquisitionEngine(dm, config)
        engine.start()

        while engine.is_running or not engine.data_queue.empty():
            try:
                dp = engine.data_queue.get(timeout=0.2)
                print(dp)
            except queue.Empty:
                continue

        engine.finished_event.wait()
        print("Measurement complete")
    """

    def __init__(
        self,
        device_manager: DeviceManager,
        config: MeasurementConfig,
    ) -> None:
        self._dm = device_manager
        self._config = config

        #: Thread-safe queue of :class:`DataPoint` objects produced during
        #: the measurement.  Consumers should drain this as points arrive.
        self.data_queue: queue.Queue[DataPoint] = queue.Queue()

        #: Set when the measurement finishes (either normally or via stop).
        self.finished_event = threading.Event()

        self._thread: threading.Thread | None = None
        self._stop_requested = threading.Event()
        self._error: BaseException | None = None
        self._last_index: int = 0  # tracks cumulative array position

        #: Optional callback invoked once when the measurement finishes.
        #: Signature: ``on_finished(error: BaseException | None) -> None``.
        #: Called from the background measurement thread.
        self.on_finished: Callable[[BaseException | None], None] | None = None

    # -- public API ---------------------------------------------------------

    def start(self) -> None:
        """Begin the measurement in a background thread.

        Raises
        ------
        RuntimeError
            If the engine is already running or the device is not connected.
        """
        if self._thread is not None and self._thread.is_alive():
            raise RuntimeError("A measurement is already in progress.")
        if not self._dm.is_connected:
            raise RuntimeError("Device is not connected.")

        # Reset state for a fresh run.
        self.finished_event.clear()
        self._stop_requested.clear()
        self._error = None
        self._last_index = 0  # reset for fresh run
        # Don't clear the queue — it's the consumer's job to drain it.

        # Instantiating the measurement method in the main thread is often required
        # for .NET COM object event dispatching in the PalmSens SDK.
        self._method = ps.ChronoAmperometry(
            interval_time=self._config.interval_time,
            potential=self._config.potential,
            run_time=self._config.run_time,
        )

        self._thread = threading.Thread(
            target=self._run,
            name="AcquisitionEngine-worker",
            daemon=True,
        )
        self._thread.start()
        logger.info("Measurement started (potential=%.3f V, run_time=%.1f s, "
                     "interval=%.4f s).",
                     self._config.potential,
                     self._config.run_time,
                     self._config.interval_time)

    def stop(self) -> None:
        """Request an early stop of the running measurement.

        This is a *request* — the SDK may still deliver a few more data
        points before the measurement thread actually terminates.  Wait on
        :attr:`finished_event` for confirmation.
        """
        if self._thread is None or not self._thread.is_alive():
            logger.debug("stop() called but no measurement is running.")
            return
        self._stop_requested.set()
        logger.info("Stop requested. Injecting KeyboardInterrupt to worker thread...")
        
        # pypalmsens measure() blocks and relies on KeyboardInterrupt to abort cleanly.
        if self._thread.ident is not None:
            res = ctypes.pythonapi.PyThreadState_SetAsyncExc(
                ctypes.c_long(self._thread.ident), 
                ctypes.py_object(KeyboardInterrupt)
            )
            if res != 1:
                # If it failed, clear the exception state
                ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(self._thread.ident), 0)
                logger.warning("Failed to inject KeyboardInterrupt into worker thread.")

    @property
    def is_running(self) -> bool:
        """``True`` while the background measurement thread is alive."""
        return self._thread is not None and self._thread.is_alive()

    @property
    def error(self) -> BaseException | None:
        """The exception that caused the measurement to fail, or ``None``."""
        return self._error

    # -- internals ----------------------------------------------------------

    def _on_new_data(self, callback_data: Any) -> None:
        """SDK callback: fires on a background thread with new points.

        The callback_data arrays (x_array, y_array) are cumulative — they
        contain every point collected so far, not just the new ones.  We
        track _last_index so we only enqueue the fresh tail.
        """
        try:
            x_all = list(callback_data.x_array)
            y_all = list(callback_data.y_array)

            # Slice out only the points we haven't seen yet.
            new_x = x_all[self._last_index:]
            new_y = y_all[self._last_index:]
            self._last_index = len(x_all)

            for t, i_ua in zip(new_x, new_y):
                # SDK callback_data.y_array (via PalmSens .NET CurrentReading.Value)
                # already returns current in µA (MicroAmperes).
                self.data_queue.put(
                    DataPoint(time=float(t), current=float(i_ua))
                )
        except Exception:
            logger.exception("Error inside measurement callback.")

    def _run(self) -> None:
        """Background thread body — configure and execute the measurement."""
        try:
            manager = self._dm.manager  # the low-level SDK handle

            # manager.measure() is *blocking* — it returns only when the
            # measurement finishes or the device is told to abort.
            # The callback fires on a background thread with new points.
            manager.measure(self._method, callback=self._on_new_data)

            logger.info("Measurement finished normally.")

        except BaseException as exc:
            # KeyboardInterrupt will be caught here
            if self._stop_requested.is_set():
                logger.info("Measurement stopped by user request.")
            else:
                self._error = exc if isinstance(exc, Exception) else Exception(str(exc))
                logger.exception("Measurement failed.")

        finally:
            self.finished_event.set()
            if self.on_finished is not None:
                try:
                    self.on_finished(self._error)
                except Exception:
                    logger.exception("Error in on_finished callback.")
