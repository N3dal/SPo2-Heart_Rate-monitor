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


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
