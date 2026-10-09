"""Activity and event log panel for ChronoAmp.

Displays timestamped events, state transitions, acquisition milestones,
and system messages in a clean, compact scientific viewer.
"""

from __future__ import annotations

import logging
from datetime import datetime

from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtGui import QFont, QTextCursor
from PySide6.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QPlainTextEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QApplication,
)

logger = logging.getLogger(__name__)


class _LogSignalEmitter(QObject):
    """Helper to emit log messages safely across threads."""
    message_logged = Signal(str, str)


class ActivityLogPanel(QGroupBox):
    """Dockable panel showing real-time system and acquisition event logs."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__("ACTIVITY LOG", parent)
        self._emitter = _LogSignalEmitter()
        self._emitter.message_logged.connect(self._append_message)
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(10, 12, 10, 8)
        layout.setSpacing(6)

        # Log viewer
        self._log_view = QPlainTextEdit()
        self._log_view.setReadOnly(True)
        self._log_view.setMaximumBlockCount(1000)
        self._log_view.setMinimumHeight(70)
        
        font = QFont("Consolas")
        font.setStyleHint(QFont.StyleHint.Monospace)
        font.setPointSize(8)
        self._log_view.setFont(font)
        self._log_view.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

        # Footer toolbar
        toolbar = QHBoxLayout()
        toolbar.setContentsMargins(0, 0, 0, 0)
        toolbar.setSpacing(6)

        self._auto_scroll_cb = QCheckBox("Auto-scroll")
        self._auto_scroll_cb.setChecked(True)
        self._auto_scroll_cb.setObjectName("secondary")

        self._btn_copy = QPushButton("Copy")
        self._btn_copy.setFixedHeight(22)
        self._btn_copy.clicked.connect(self._copy_log)

        self._btn_clear = QPushButton("Clear")
        self._btn_clear.setFixedHeight(22)
        self._btn_clear.clicked.connect(self._clear_log)

        toolbar.addWidget(self._auto_scroll_cb)
        toolbar.addStretch()
        toolbar.addWidget(self._btn_copy)
        toolbar.addWidget(self._btn_clear)

        layout.addWidget(self._log_view, stretch=1)
        layout.addLayout(toolbar)

    def log(self, message: str, level: str = "INFO") -> None:
        """Post a log entry (safe from any thread)."""
        self._emitter.message_logged.emit(message, level)

    def _append_message(self, message: str, level: str) -> None:
        now_str = datetime.now().strftime("%H:%M:%S")
        prefix = f"[{now_str}]"
        
        if level == "ERROR":
            formatted = f"{prefix} [ERR] {message}"
        elif level == "WARNING":
            formatted = f"{prefix} [WARN] {message}"
        else:
            formatted = f"{prefix} {message}"

        self._log_view.appendPlainText(formatted)

        if self._auto_scroll_cb.isChecked():
            self._log_view.moveCursor(QTextCursor.MoveOperation.End)

    def _clear_log(self) -> None:
        self._log_view.clear()

    def _copy_log(self) -> None:
        text = self._log_view.toPlainText()
        if text:
            clipboard = QApplication.clipboard()
            if clipboard:
                clipboard.setText(text)


class QtLogHandler(logging.Handler):
    """Logging handler that pipes Python log records directly into the UI log."""

    def __init__(self, log_panel: ActivityLogPanel) -> None:
        super().__init__()
        self._log_panel = log_panel

    def emit(self, record: logging.LogRecord) -> None:
        try:
            msg = self.format(record)
            self._log_panel.log(msg, level=record.levelname)
        except Exception:
            self.handleError(record)
