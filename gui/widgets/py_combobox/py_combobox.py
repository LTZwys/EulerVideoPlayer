# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QComboBox {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid transparent;
    padding-left: 10px;
    padding-right: 25px;  /* 预留下拉箭头空间 */
    color: {_color};
    selection-color: {_selection_color};
    selection-background-color: {_context_color};
}}
QComboBox:focus {{
    border: {_border_size}px solid {_context_color};
    background-color: {_bg_color_active};
}}
QComboBox::drop-down {{
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left-width: 0px;
    border-top-right-radius: {_radius}px;
    border-bottom-right-radius: {_radius}px;
    background-color: transparent;
}}
QComboBox::down-arrow {{
    image: url(:/icons/icons/down_arrow_white.png);  /* 可替换为自定义箭头图标 */
    width: 8px;
    height: 8px;
}}
QComboBox QAbstractItemView {{
    background-color: {_bg_color};
    border-radius: {_radius}px;
    border: {_border_size}px solid {_context_color};
    color: {_color};
    selection-color: {_selection_color};
    selection-background-color: {_context_color};
    padding: 5px;
}}
QComboBox::disabled {{
    background-color: #222222;
    color: #888888;
}}
'''

# PY COMBO BOX
# ///////////////////////////////////////////////////////////////
class PyComboBox(QComboBox):
    def __init__(
        self, 
        parent=None,
        items: list = None,  
        current_index: int = 0,  
        radius: int = 8,
        border_size: int = 2,
        color: str = "#FFF",
        selection_color: str = "#FFF",
        bg_color: str = "#333",
        bg_color_active: str = "#222",
        context_color: str = "#00ABE8"
    ):
        super().__init__(parent) 

        self._radius = radius
        self._border_size = border_size
        self._color = color
        self._selection_color = selection_color
        self._bg_color = bg_color
        self._bg_color_active = bg_color_active
        self._context_color = context_color

        # 初始化参数
        self._items = items or []
        self._current_index = current_index

        if self._items:
            self.addItems(self._items)
            if 0 <= self._current_index < len(self._items):
                self.setCurrentIndex(self._current_index)

        self.set_stylesheet(
            radius,
            border_size,
            color,
            selection_color,
            bg_color,
            bg_color_active,
            context_color
        )

        self.view().setMouseTracking(True)

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

    def add_item(self, text: str):
        self.addItem(text)
        self._items.append(text)

    def set_items(self, items: list):
        self.clear()
        self._items = items
        self.addItems(items)

    def get_current_text(self) -> str:
        return self.currentText()
