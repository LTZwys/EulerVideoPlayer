# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPlainTextEdit {{
	background-color: {_bg_color};
	border-radius: {_radius}px;
	border: {_border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
    padding-top: 8px;
    padding-bottom: 8px;
	selection-color: {_selection_color};
	selection-background-color: {_context_color};
    color: {_color};
}}
QPlainTextEdit:focus {{
	border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
QPlainTextEdit QScrollBar {{
    background-color: {_bg_color};
    width: 8px;
    height: 8px;
}}
QPlainTextEdit QScrollBar::handle {{
    background-color: {_context_color};
    border-radius: 4px;
}}
QPlainTextEdit QScrollBar::handle:hover {{
    background-color: {_context_color};
    opacity: 0.8;
}}
QPlainTextEdit QScrollBar::add-line, QScrollBar::sub-line {{
    height: 0px;
    width: 0px;
}}
'''

# PY PLAIN TEXT EDIT
# ///////////////////////////////////////////////////////////////
class PyPlainTextEdit(QPlainTextEdit):
    def __init__(
        self, 
        parent=None,  
        text = "",
        place_holder_text = "",
        radius = 8,
        border_size = 2,
        color = "#FFF",
        selection_color = "#FFF",
        bg_color = "#333",
        bg_color_active = "#222",
        context_color = "#00ABE8"
    ):
        super().__init__(parent) 

        # PARAMETERS
        if text:
            self.setPlainText(text)
        if place_holder_text:
            self._placeholder_text = place_holder_text
            self._placeholder_color = "#888"
            self._normal_color = color
            self.textChanged.connect(self._on_text_changed)
            self._draw_placeholder()

        self.setFrameStyle(QFrame.NoFrame) 
        self.setCursorWidth(2)  
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # SET STYLESHEET
        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color
        )

    def _draw_placeholder(self):
        if not self.toPlainText() and hasattr(self, "_placeholder_text"):
            self.setStyleSheet(
                self.styleSheet() + f"\nQPlainTextEdit {{ color: {self._placeholder_color}; }}"
            )
            self.setPlainText(self._placeholder_text)
        elif hasattr(self, "_normal_color"):
            self.setStyleSheet(
                self.styleSheet().replace(f"color: {self._placeholder_color};", f"color: {self._normal_color};")
            )

    def _on_text_changed(self):
        current_text = self.toPlainText()
        if current_text == self._placeholder_text:
            self.setPlainText("")
            self.setStyleSheet(
                self.styleSheet().replace(f"color: {self._placeholder_color};", f"color: {self._normal_color};")
            )
        elif not current_text:
            self._draw_placeholder()

    def setPlainText(self, text):
        if hasattr(self, "_placeholder_text") and text == self._placeholder_text:
            super().setPlainText(text)
        else:

            if hasattr(self, "_placeholder_text") and self.toPlainText() == self._placeholder_text:
                super().setPlainText("")
            super().setPlainText(text)
        self._draw_placeholder()

    # SET STYLESHEET
    def set_stylesheet(
        self,
        radius,
        border_size,
        color,
        selection_color,
        bg_color,
        bg_color_active,
        context_color
    ):
        if hasattr(self, "_normal_color"):
            self._normal_color = color
        
        # APPLY STYLESHEET
        style_format = style.format(
            _radius = radius,
            _border_size = border_size,           
            _color = color,
            _selection_color = selection_color,
            _bg_color = bg_color,
            _bg_color_active = bg_color_active,
            _context_color = context_color
        )
        self.setStyleSheet(style_format)
        
        if hasattr(self, "_placeholder_text"):
            self._draw_placeholder()