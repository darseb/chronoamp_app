"""High-visibility result panel displayed after a measurement completes.

Shows the outcome (POSITIVE / NEGATIVE / INCONCLUSIVE / Awaiting measurement)
with a prominent status indicator, large bold verdict label, readable explanation
text, and a dedicated concentration readout badge.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel, QVBoxLayout, QWidget

from interpretation.verdict import Verdict
from ui.theme import (
    ACCENT_CYAN,
    BORDER,
    ERROR,
    PANEL_SECONDARY_BG,
    SUCCESS,
    TEXT_SECONDARY,
    WARNING,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class _BannerStyle:
    """Visual parameters for a single verdict state."""

    icon: str
    label: str
    bg: str
    border: str
    left_border: str
    title_color: str
    exp_color: str
    badge_bg: str
    badge_border: str
    badge_title: str
    badge_val: str


_STYLES: dict[Verdict | None, _BannerStyle] = {
    Verdict.POSITIVE: _BannerStyle(
        icon="●",
        label="POSITIVE",
        bg="#EDF8F0",
        border="#B7E4C7",
        left_border="#16A34A",
        title_color="#15803D",
        exp_color="#166534",
        badge_bg="#DCFCE7",
        badge_border="#86EFAC",
        badge_title="#15803D",
        badge_val="#14532D",
    ),
    Verdict.NEGATIVE: _BannerStyle(
        icon="●",
        label="NEGATIVE",
        bg="#FEF2F2",
        border="#FECACA",
        left_border="#DC2626",
        title_color="#B91C1C",
        exp_color="#991B1B",
        badge_bg="#FEE2E2",
        badge_border="#FCA5A5",
        badge_title="#B91C1C",
        badge_val="#7F1D1D",
    ),
    Verdict.INCONCLUSIVE: _BannerStyle(
        icon="●",
        label="INCONCLUSIVE",
        bg="#FFFBEB",
        border="#FDE68A",
        left_border="#D97706",
        title_color="#B45309",
        exp_color="#92400E",
        badge_bg="#FEF3C7",
        badge_border="#FCD34D",
        badge_title="#B45309",
        badge_val="#78350F",
    ),
    None: _BannerStyle(
        icon="○",
        label="Awaiting measurement",
        bg=PANEL_SECONDARY_BG,
        border=BORDER,
        left_border=ACCENT_CYAN,
        title_color="#475569",
        exp_color=TEXT_SECONDARY,
        badge_bg="#EDF8FC",
        badge_border="#88D4EE",
        badge_title="#0284C7",
        badge_val="#0369A1",
    ),
}

_CONC_PATTERN = re.compile(
    r"(?:(Extrapolated concentration|Predicted concentration|Concentration)):\s*([0-9eE.+-]+(?:\s*[a-zA-Z/%µμ]+)?)",
    re.IGNORECASE,
)


class ResultBanner(QFrame):
    """High-visibility result panel that prominently displays measurement verdicts."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._build_ui()
        self.set_verdict(None, "")

    def _build_ui(self) -> None:
        self.setObjectName("resultBanner")
        self.setMinimumHeight(74)
        self.setFixedHeight(78)

        # Prominent Verdict Readout Badge (matching concentration badge)
        self._verdict_badge = QFrame()
        self._verdict_badge.setObjectName("verdictBadge")
        verdict_layout = QVBoxLayout(self._verdict_badge)
        verdict_layout.setContentsMargins(14, 6, 14, 6)
        verdict_layout.setSpacing(1)
        verdict_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._verdict_title = QLabel("VERDICT")
        verdict_title_font = QFont()
        verdict_title_font.setPointSize(8)
        verdict_title_font.setBold(True)
        self._verdict_title.setFont(verdict_title_font)
        self._verdict_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._verdict_val = QLabel("")
        verdict_val_font = QFont()
        verdict_val_font.setPointSize(14)
        verdict_val_font.setBold(True)
        self._verdict_val.setFont(verdict_val_font)
        self._verdict_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        verdict_layout.addWidget(self._verdict_title)
        verdict_layout.addWidget(self._verdict_val)

        # Retain _title_label as alias to _verdict_val for compatibility
        self._title_label = self._verdict_val

        # Explanation text
        self._explanation_label = QLabel()
        explanation_font = QFont()
        explanation_font.setPointSize(9.5)
        self._explanation_label.setFont(explanation_font)
        self._explanation_label.setWordWrap(True)

        # Prominent right-side Concentration Readout Badge
        self._conc_badge = QFrame()
        self._conc_badge.setObjectName("concBadge")
        conc_layout = QVBoxLayout(self._conc_badge)
        conc_layout.setContentsMargins(14, 6, 14, 6)
        conc_layout.setSpacing(1)
        conc_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._conc_title = QLabel("CONCENTRATION")
        conc_title_font = QFont()
        conc_title_font.setPointSize(8)
        conc_title_font.setBold(True)
        self._conc_title.setFont(conc_title_font)
        self._conc_title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._conc_val = QLabel("")
        conc_val_font = QFont()
        conc_val_font.setPointSize(14)
        conc_val_font.setBold(True)
        self._conc_val.setFont(conc_val_font)
        self._conc_val.setAlignment(Qt.AlignmentFlag.AlignCenter)

        conc_layout.addWidget(self._conc_title)
        conc_layout.addWidget(self._conc_val)
        self._conc_badge.hide()

        root = QHBoxLayout(self)
        root.setContentsMargins(14, 8, 14, 8)
        root.setSpacing(14)
        root.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        root.addWidget(self._verdict_badge)
        root.addWidget(self._explanation_label, stretch=1)
        root.addWidget(self._conc_badge)

    def set_verdict(
        self,
        verdict: Verdict | None,
        explanation: str,
    ) -> None:
        """Update the banner to reflect the given verdict."""
        style = _STYLES.get(verdict, _STYLES[None])

        # Update Verdict Badge with matching styling
        v_title = "STATUS" if verdict is None else "VERDICT"
        v_val = "READY" if verdict is None else style.label
        self._verdict_title.setText(v_title)
        self._verdict_title.setStyleSheet(
            f"color: {style.badge_title}; background: transparent; letter-spacing: 0.5px;"
        )
        self._verdict_val.setText(v_val)
        self._verdict_val.setStyleSheet(
            f"color: {style.badge_val}; background: transparent;"
        )
        self._verdict_badge.setStyleSheet(
            f"""
            QFrame {{
                background-color: {style.badge_bg};
                border: 1px solid {style.badge_border};
                border-radius: 6px;
            }}
            """
        )

        display_exp = (
            explanation
            if (explanation and explanation.strip())
            else ("Awaiting measurement." if verdict is None else "")
        )
        self._explanation_label.setText(display_exp)
        self._explanation_label.setVisible(bool(display_exp))
        self._explanation_label.setStyleSheet(
            f"color: {style.exp_color}; background: transparent; border: none;"
        )

        self.setStyleSheet(
            f"""
            QFrame#resultBanner {{
                background-color: {style.bg};
                border: 1px solid {style.border};
                border-left: 6px solid {style.left_border};
                border-radius: 6px;
            }}
            """
        )

        # Check for extracted concentration to display in the dedicated badge
        match = _CONC_PATTERN.search(explanation or "")
        if match and verdict == Verdict.POSITIVE:
            badge_title = (
                "EXTRAPOLATED"
                if "extrapolated" in match.group(1).lower()
                else "CONCENTRATION"
            )
            self._conc_title.setText(badge_title)
            self._conc_title.setStyleSheet(
                f"color: {style.badge_title}; background: transparent; letter-spacing: 0.5px;"
            )
            self._conc_val.setText(match.group(2).strip())
            self._conc_val.setStyleSheet(
                f"color: {style.badge_val}; background: transparent;"
            )
            self._conc_badge.setStyleSheet(
                f"""
                QFrame {{
                    background-color: {style.badge_bg};
                    border: 1px solid {style.badge_border};
                    border-radius: 6px;
                }}
                """
            )
            self._conc_badge.show()
        else:
            self._conc_badge.hide()

        logger.debug("Banner updated: verdict=%s", verdict)
