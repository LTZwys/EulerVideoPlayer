# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget

from gui.uis.windows.main_window.functions_main_window import *

from gui.widgets.py_plain_text_edit.py_plain_text_edit import  PyPlainTextEdit
import tempfile
from pathlib import Path
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from gui.uis.windows.main_window.functions_main_window import *


class SetupPageTools(QObject):
    def __init__(self):
        super().__init__()

    # SETUP PAGE_VIDEOPLAYER
    # ///////////////////////////////////////////////////////////////
    def setup_tools(self):
        # CHECK LOAD UI
        # ///////////////////////////////////////////////////////////////
        if self.ui is None:
            self.ui = UI_MainWindow()
            self.ui.setup_ui(self)
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items
        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items
        # SET THEME 
        # ///////////////////////////////////////////////////////////////
        self.setup_push_buttons_style()
        self.ui.load_pages.lineEdit1.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )
        self.ui.load_pages.lineEdit2.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )
        self.ui.load_pages.lineEdit3.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )
        self.ui.load_pages.lineEdit1.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )

        self.ui.load_pages.comboBox.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]

        )

        self.ui.load_pages.checkBox.set_stylesheet(
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        self.ui.load_pages.checkBox_2.set_stylesheet(
            bg_color = self.themes["app_color"]["dark_two"],
            circle_color = self.themes["app_color"]["icon_color"],
            active_color = self.themes["app_color"]["context_color"]
        )

        self.ui.load_pages.plainTextEdit.set_stylesheet(
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

    
    def setup_push_buttons_style(self):
        btn_style = {
            "radius": 10,
            "color": self.themes["app_color"]["text_foreground"],
            "bg_color": self.themes["app_color"]["dark_one"],
            "bg_color_hover": self.themes["app_color"]["dark_three"],
            "bg_color_pressed": self.themes["app_color"]["dark_four"]
        }
        for btn_num in range(1, 11):
            btn_attr_name = f"pushButton_{btn_num}"

            if hasattr(self.ui.load_pages, btn_attr_name):
                btn = getattr(self.ui.load_pages, btn_attr_name)
                btn.set_style(**btn_style)
                btn.setMinimumHeight(80)
                btn.setText("KEYWORD")
            else:
                print(f"Warning: Button {btn_attr_name} not found in load_pages!")

    

    



