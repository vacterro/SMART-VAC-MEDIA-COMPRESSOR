def generate_stylesheet(palette: dict, font_family: str = "MS Sans Serif", font_size: int = 14) -> str:
    """
    Generate dynamic stylesheet substituting CSS variables based on the active palette.
    Vintage 1995 UI Edition, compliant with /vintage strict rules.
    """
    palette_copy = palette.copy()
    palette_copy['font_css'] = f"font-family: 'Verdana';"
    palette_copy['font_size'] = font_size

    return """
/* Global Styles - Vintage Golden Aesthetic - Compact */
QWidget {{
    background-color: {background};
    color: {textPrimary};
    font-size: {font_size}px;
    {font_css}
}}

*:focus {{
    outline: none;
    border: 1px solid {accentCursor};
}}

/* Typography */
QLabel {{
    color: {textPrimary};
    background-color: transparent;
    padding: 0;
    margin: 0;
}}

/* Data Views (List/Table) - Compact */
QListView, QTreeView, QTableWidget {{
    background-color: {surfaceRaised};
    color: {textPrimary};
    font-family: 'Verdana';
    border: 2px solid;
    border-top-color: {borderDark};
    border-left-color: {borderDark};
    border-bottom-color: {borderHighlight};
    border-right-color: {borderHighlight};
    outline: none;
    padding: 0;
}}

QListView::item:selected, QTreeView::item:selected, QTableWidget::item:selected {{
    background-color: {selection};
    color: {textPrimary};
}}

/* Buttons - Brutally Compact */
QPushButton {{
    background-color: {surface};
    color: {textPrimary};
    border: 2px solid;
    border-top-color: {borderHighlight};
    border-left-color: {borderHighlight};
    border-bottom-color: {borderDark};
    border-right-color: {borderDark};
    padding: 0px 2px;
    min-height: 18px;
    border-radius: 0px;
}}

QPushButton:hover {{
    background-color: {surfaceAlt};
}}

QPushButton:pressed, QPushButton:checked {{
    background-color: {surface};
    border-top-color: {borderDark};
    border-left-color: {borderDark};
    border-bottom-color: {borderHighlight};
    border-right-color: {borderHighlight};
    padding: 1px 1px -1px 3px; /* Minimal shift */
}}

QPushButton:disabled {{
    color: {textMuted};
    border: 1px solid {borderMuted};
    background-color: {surface};
}}

/* Inputs - Compact */
QSpinBox, QDoubleSpinBox, QLineEdit, QComboBox {{
    background-color: {surfaceRaised};
    color: {textPrimary};
    border: 2px solid;
    border-top-color: {borderDark};
    border-left-color: {borderDark};
    border-bottom-color: {borderHighlight};
    border-right-color: {borderHighlight};
    padding: 0px 2px;
    min-height: 18px;
}}

/* Group Boxes - Compact */
QGroupBox {{
    font-weight: bold;
    border: 2px solid {borderMuted};
    margin-top: 8px;
    padding-top: 8px;
}}

QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 4px;
    color: {textPrimary};
}}

/* Progress Bar - Compact */
QProgressBar {{
    border: 2px solid;
    border-top-color: {borderDark};
    border-left-color: {borderDark};
    border-bottom-color: {borderHighlight};
    border-right-color: {borderHighlight};
    background-color: {surfaceRaised};
    text-align: center;
    color: {textPrimary};
    min-height: 18px;
    margin: 0;
}}

QProgressBar::chunk {{
    background-color: {accentTealDeep};
}}

/* Tabs - Compact */
QTabWidget::pane {{
    border: 2px solid {borderMuted};
    background-color: {surface};
    top: 0;
}}

QTabBar::tab {{
    background-color: {surfaceRaised};
    color: {textPrimary};
    border: 2px solid;
    border-top-color: {borderHighlight};
    border-left-color: {borderHighlight};
    border-bottom-color: {borderDark};
    border-right-color: {borderDark};
    padding: 1px 4px;
}}

QTabBar::tab:selected {{
    background-color: {surface};
}}
    """.format(**palette_copy)
