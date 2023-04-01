"""
    Docstring;
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class SettingsWindow(QMainWindow):
    """
        Docstring;
    """

    WIDTH, HEIGHT = 400, 250
    STYLESHEET = """
        background-color: #ffffff;
    """

    TITLE = "Settings"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(SettingsWindow.WIDTH, SettingsWindow.HEIGHT)
        self.setStyleSheet(SettingsWindow.STYLESHEET)
        self.setWindowTitle(SettingsWindow.TITLE)
