#!/usr/bin/python3
# -----------------------------------------------------------------
#
#
#
#
# Author:N84.
#
# Create Date:Fri Mar 31 15:57:21 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils import *
import os
import sys

# wipe terminal screen;
clear()


class Menu(QMenu):
    """
        Custom Menu that add clicked signal;
    """

    class Signals(QObject):
        """
            Docstring;
        """

        clicked = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.signals = Menu.Signals()

    def mousePressEvent(self, e):
        """
            Docstring;
        """

        self.signals.clicked.emit()

        return None


class MenuBar(QMenuBar):
    """
        Custom Menu Bar;
    """

    STYLESHEET = """
        background-color: #c9bbaa;
        color: black;
        font-size: 15px;
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setStyleSheet(MenuBar.STYLESHEET)

        # create the MenuBar options;
        file_menu = self.addMenu("&File")

        settings_menu = Menu("Settings", parent=self)
        self.addMenu(settings_menu)

        info_menu = Menu("Info", parent=self)
        self.addMenu(info_menu)

        # add option to the File Menu;
        file_menu.addAction("Export")
        file_menu.addAction("Generate Report")
        file_menu.addAction("Save")
        file_menu.addAction("Exit")

        file_menu.triggered[QAction].connect(
            self.file_menu_action_process_trigger
        )

        settings_menu.signals.clicked.connect(
            self.settings_menu_action_process_trigger
        )

        info_menu.signals.clicked.connect(
            self.info_menu_action_process_trigger
        )

    def file_menu_action_process_trigger(self, menu: QMenu):
        """
            :ARGS:
                menu:QMenu=>the clicked QMenu; 

            :RETURNS:
                return None;

            :INFO:
                process file menu action when its clicked;;
        """

        clicked_action_name = menu.text()

        if clicked_action_name == "Export":
            pass

        elif clicked_action_name == "Generate Report":
            pass

        elif clicked_action_name == "Save":
            pass

        else:
            # in case of action name is "Exit" or any thing not included;
            sys.exit(0)

        return None

    def settings_menu_action_process_trigger(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                process settings menu action when its clicked;;
        """

        print("Settings Menu Clicked")

        return None

    def info_menu_action_process_trigger(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                process info menu action when its clicked;;
        """

        print("Info Menu Clicked")

        return None


class MainWindow(QMainWindow):
    """
        Docstring;
    """

    WIDTH, HEIGHT = 850, 600
    STYLESHEET = """
        background-color: #ffffff;
    """
    TITLE = "Arduino HST Monitor"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setStyleSheet(MainWindow.STYLESHEET)
        self.setWindowTitle(MainWindow.TITLE)

        menu_bar = MenuBar(parent=self)
        self.setMenuBar(menu_bar)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
