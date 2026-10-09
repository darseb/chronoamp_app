"""Centralized light theme configuration for ChronoAmp.

This module provides the color palette and generates the application-wide QSS stylesheet.
Incorporates Pantone 297C (#5BC2E7) as the primary light blue accent.
"""

from __future__ import annotations

# -- Semantic Colors --------------------------------------------------------

# Primary Light Blue Accent (Pantone 297C: approx. HEX #5BC2E7 / RGB 91, 194, 231)
ACCENT_CYAN = "#5BC2E7"
ACCENT_CYAN_HOVER = "#46B8E0"
ACCENT_CYAN_LIGHT = "#EDF8FC"
ACCENT_CYAN_TINT = "#DBF2FA"
ACCENT_CYAN_BORDER = "#88D4EE"
ACCENT_CYAN_DARK = "#1A7C9F"

# Primary Action Blue (high-contrast readable action color accented with cyan)
ACCENT_PRIMARY = "#1982A8"
ACCENT_PRIMARY_HOVER = "#1E96C0"
ACCENT_PRIMARY_PRESSED = "#136987"
ACCENT_PRIMARY_LIGHT = "#E1F2F9"

# Backward compatibility aliases
ACCENT = ACCENT_PRIMARY
ACCENT_HOVER = ACCENT_PRIMARY_HOVER
ACCENT_LIGHT = ACCENT_CYAN_LIGHT

# Surfaces
WINDOW_BG = "#F4F6F9"
PANEL_BG = "#FFFFFF"
PANEL_SECONDARY_BG = "#F8FAFC"
INPUT_BG = "#FFFFFF"

# Borders (crisp with subtle cool slate tone)
BORDER = "#D5DFE8"
BORDER_STRONG = "#AFC0CE"
BORDER_ACCENT = ACCENT_CYAN

# Text
TEXT = "#1C242C"
TEXT_SECONDARY = "#556473"
TEXT_DISABLED = "#94A3B3"
TEXT_ACCENT = "#136282"

# Status colors
SUCCESS = "#1E874B"
SUCCESS_LIGHT = "#EBF7F0"
SUCCESS_BORDER = "#A3D8B9"

WARNING = "#C78700"
WARNING_LIGHT = "#FFF8E6"
WARNING_BORDER = "#F5D685"

ERROR = "#C53030"
ERROR_LIGHT = "#FDE8E8"
ERROR_BORDER = "#F8B4B4"

# Plot colors
PLOT_BG = "#FFFFFF"
PLOT_GRID = "#E5ECF2"
PLOT_TRACE = "#157A9E"


# -- Stylesheet Generation --------------------------------------------------

def build_stylesheet() -> str:
    """Generate the global QSS stylesheet for the application."""
    import os
    check_icon_path = os.path.join(os.path.dirname(__file__), "check.png").replace("\\", "/")
    return f"""
        /* Global Application Background */
        QWidget {{
            background-color: {WINDOW_BG};
            color: {TEXT};
            font-family: "Segoe UI", system-ui, -apple-system, sans-serif;
            font-size: 9.5pt;
        }}

        /* Top level windows & dialogs */
        QMainWindow, QDialog, QWizard {{
            background-color: {WINDOW_BG};
        }}
        
        QSplitter::handle {{
            background-color: {BORDER};
            width: 1px;
        }}
        
        QSplitter::handle:hover {{
            background-color: {ACCENT_CYAN};
        }}

        /* Buttons */
        QPushButton {{
            background-color: {PANEL_BG};
            color: {TEXT};
            border: 1px solid {BORDER};
            border-radius: 4px;
            padding: 4px 12px;
            min-height: 22px;
            font-weight: 500;
        }}
        
        QPushButton:hover {{
            background-color: {ACCENT_CYAN_LIGHT};
            border-color: {ACCENT_CYAN};
            color: {TEXT_ACCENT};
        }}
        
        QPushButton:pressed {{
            background-color: {ACCENT_CYAN_TINT};
            border-color: {ACCENT_CYAN_HOVER};
        }}
        
        QPushButton:disabled {{
            color: {TEXT_DISABLED};
            background-color: {PANEL_SECONDARY_BG};
            border-color: {BORDER};
        }}

        /* Primary Action Buttons */
        QPushButton#btn_primary {{
            background-color: {ACCENT_PRIMARY};
            color: #FFFFFF;
            border: 1px solid {ACCENT_PRIMARY_PRESSED};
            border-radius: 4px;
            padding: 5px 14px;
            font-weight: 600;
        }}
        
        QPushButton#btn_primary:hover {{
            background-color: {ACCENT_PRIMARY_HOVER};
            border-color: {ACCENT_CYAN};
        }}
        
        QPushButton#btn_primary:pressed {{
            background-color: {ACCENT_PRIMARY_PRESSED};
        }}
        
        QPushButton#btn_primary:disabled {{
            background-color: {ACCENT_PRIMARY_LIGHT};
            color: {TEXT_DISABLED};
            border-color: {BORDER};
        }}

        /* Danger / Stop Buttons */
        QPushButton#btn_stop:enabled {{
            background-color: #FFF5F5;
            color: {ERROR};
            border: 1px solid {ERROR_BORDER};
            font-weight: 600;
        }}
        QPushButton#btn_stop:enabled:hover {{
            background-color: {ERROR_LIGHT};
            border-color: {ERROR};
        }}

        /* Inputs */
        QLineEdit, QDoubleSpinBox, QComboBox {{
            background-color: {INPUT_BG};
            color: {TEXT};
            border: 1px solid {BORDER};
            border-radius: 4px;
            padding: 3px 6px;
            min-height: 22px;
        }}
        
        QLineEdit:focus, QDoubleSpinBox:focus, QComboBox:focus {{
            border: 1.5px solid {ACCENT_CYAN};
            background-color: #FFFFFF;
        }}
        
        QLineEdit:disabled, QDoubleSpinBox:disabled, QComboBox:disabled {{
            background-color: {PANEL_SECONDARY_BG};
            color: {TEXT_DISABLED};
            border-color: {BORDER};
        }}
        
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
            border-left: 1px solid {BORDER};
        }}

        /* CheckBox */
        QCheckBox {{
            spacing: 6px;
        }}
        QCheckBox::indicator {{
            width: 14px;
            height: 14px;
            border: 1px solid {BORDER};
            border-radius: 3px;
            background-color: {PANEL_BG};
        }}
        QCheckBox::indicator:hover {{
            border-color: {ACCENT_CYAN};
        }}
        QCheckBox::indicator:checked {{
            background-color: {ACCENT_PRIMARY};
            border-color: {ACCENT_CYAN};
            image: url("{check_icon_path}");
        }}

        /* Section Group Boxes */
        QGroupBox {{
            background-color: {PANEL_BG};
            border: 1px solid {BORDER};
            border-radius: 6px;
            margin-top: 12px;
            padding-top: 6px;
            padding-bottom: 6px;
            padding-left: 8px;
            padding-right: 8px;
            font-weight: 600;
        }}
        
        QGroupBox::title {{
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 2px 8px;
            left: 10px;
            color: {TEXT_ACCENT};
            background-color: {ACCENT_CYAN_LIGHT};
            border: 1px solid {ACCENT_CYAN_BORDER};
            border-radius: 3px;
            font-size: 8pt;
            font-weight: bold;
            letter-spacing: 0.5px;
        }}

        /* Frames / Panels */
        QFrame#panel {{
            background-color: {PANEL_BG};
            border: 1px solid {BORDER};
            border-radius: 6px;
        }}
        
        QFrame#panel_secondary {{
            background-color: {PANEL_SECONDARY_BG};
            border: 1px solid {BORDER};
            border-radius: 6px;
        }}
        
        QFrame#panel_accent {{
            background-color: {ACCENT_CYAN_LIGHT};
            border: 1px solid {ACCENT_CYAN_BORDER};
            border-radius: 6px;
        }}

        /* Labels */
        QLabel {{
            background: transparent;
        }}
        
        QLabel#secondary {{
            color: {TEXT_SECONDARY};
            font-size: 8.5pt;
        }}
        
        QLabel#accent_label {{
            color: {TEXT_ACCENT};
            font-weight: bold;
        }}
        
        QLabel#status_connected {{
            color: {SUCCESS};
            font-weight: bold;
        }}
        
        QLabel#status_disconnected {{
            color: {ERROR};
            font-weight: bold;
        }}

        /* Progress Bar */
        QProgressBar {{
            border: 1px solid {BORDER};
            border-radius: 4px;
            background-color: {PANEL_SECONDARY_BG};
            text-align: center;
            font-size: 8pt;
            font-weight: bold;
            color: {TEXT_ACCENT};
            min-height: 14px;
            max-height: 14px;
        }}
        
        QProgressBar::chunk {{
            background-color: {ACCENT_CYAN};
            border-radius: 3px;
        }}

        /* Text / Log Viewer */
        QPlainTextEdit, QTextEdit {{
            background-color: {PANEL_BG};
            color: {TEXT};
            border: 1px solid {BORDER};
            border-radius: 4px;
            padding: 4px;
            font-family: "Consolas", "Cascadia Code", "Segoe UI Mono", monospace;
            font-size: 8.5pt;
        }}
        
        QPlainTextEdit:focus, QTextEdit:focus {{
            border: 1px solid {ACCENT_CYAN};
        }}

        /* Status Bar */
        QStatusBar {{
            background-color: {PANEL_BG};
            border-top: 1px solid {BORDER};
            color: {TEXT_SECONDARY};
            font-size: 8.5pt;
            padding: 2px 8px;
        }}
        
        QStatusBar::item {{
            border: none;
        }}

        /* Table Widget */
        QTableWidget {{
            background-color: {PANEL_BG};
            alternate-background-color: {PANEL_SECONDARY_BG};
            border: 1px solid {BORDER};
            gridline-color: {BORDER};
        }}
        
        QHeaderView::section {{
            background-color: {ACCENT_CYAN_LIGHT};
            color: {TEXT_ACCENT};
            border: none;
            border-right: 1px solid {BORDER};
            border-bottom: 1px solid {BORDER};
            padding: 4px 8px;
            font-weight: bold;
            font-size: 8.5pt;
        }}
        
        /* Scrollbar */
        QScrollBar:vertical {{
            border: none;
            background: {PANEL_SECONDARY_BG};
            width: 8px;
            margin: 0px;
            border-radius: 4px;
        }}
        QScrollBar::handle:vertical {{
            background: {BORDER};
            min-height: 20px;
            border-radius: 4px;
        }}
        QScrollBar::handle:vertical:hover {{
            background: {ACCENT_CYAN};
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
    """
