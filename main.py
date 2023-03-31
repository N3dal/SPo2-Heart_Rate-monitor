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


class Plotter:
    """
        Custom Plotter;
    """


class DataViewer(QFrame):
    """
        Docstring;
    """

    WIDTH, HEIGHT = 240, 180

    STYLESHEET = """
        background-color: #5ba2f4;
        color: black;
        font-size: 22px;
        border-radius: 10px;
    """

    TITLE_LABEL_STYLESHEET = """
        color: black;
        font-size: 22px;
    """

    DATA_LABEL_STYLESHEET = """
        color: white;
        font-size: 30px;
    """

    def __init__(self,
                 name: str,
                 title: str = None,
                 measurement_unit: str = "",
                 min_value: int = None,
                 max_value: int = None,
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.setFixedSize(DataViewer.WIDTH, DataViewer.HEIGHT)
        self.setStyleSheet(DataViewer.STYLESHEET)
        self.__name = name

        if title is None:
            self.title = self.name
        else:
            self.title = title

        # default data simply out when we don't have any,
        # data we want to view three dashes;
        self.data = "---"
        self.measurement_unit = measurement_unit

        self.__min_value = min_value
        self.__max_value = max_value

        self.__setup_ui()

        self.show()

    def __setup_ui(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                setup all the ui for the DataViewer;  

        """

        self.__title_label = QLabel(parent=self, text=self.title.title())
        self.__title_label.setStyleSheet(DataViewer.TITLE_LABEL_STYLESHEET)
        self.__title_label.setFixedSize(DataViewer.WIDTH-10, 40)
        self.__title_label.setAlignment(Qt.AlignCenter)
        self.__title_label.move(5, 5)

        self.__data_label = QLabel(parent=self, text=str(self.data))
        self.__data_label.setStyleSheet(DataViewer.DATA_LABEL_STYLESHEET)
        self.__data_label.setFixedSize(
            DataViewer.WIDTH-10, DataViewer.HEIGHT-50)
        self.__data_label.setAlignment(Qt.AlignCenter)
        self.__data_label.move(5, 45)

        return None

    def update_data(self, new_value: str):
        """
            :ARGS:
                new_value:str => new data;

            :RETURNS:
                return None;

            :INFO:
                update the DataViewer with new data;

        """

        self.data = new_value

        self.__data_label.setText(f"{self.data} {self.measurement_unit}")

        return None

    def set_min_value(self, value: int):
        """
            :ARGS:
                value:int => the new min value;

            :RETURNS:
                return None;

            :INFO:
                change the min value for the alert;
        """

        self.__min_value = value

        return None

    def set_max_value(self, value: int):
        """
            :ARGS:
                value:int => the new max value;

            :RETURNS:
                return None;

            :INFO:
                change the max value for the alert;
        """

        self.__max_value = value

        return None

    def alert(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                start the alarm;
        """

        return None

    @property
    def name(self):
        return self.__name

    @property
    def min_value(self):
        return self.__min_value

    @property
    def max_value(self):
        return self.__max_value


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
        background-color: #5ba2f4;
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

    WIDTH, HEIGHT = 900, 670
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

        # create the DataViewers;
        self.heart_rate_viewer = DataViewer(
            parent=self, name="heart-rate", measurement_unit="bpm")
        self.spo2_level_viewer = DataViewer(
            parent=self, name="spo2-level", measurement_unit="%")
        self.temperature_viewer = DataViewer(
            parent=self, name="temperature", measurement_unit="°C")

        self.heart_rate_viewer.move(
            40, MainWindow.HEIGHT - DataViewer.HEIGHT - 30)
        self.spo2_level_viewer.move(
            45*2 + DataViewer.WIDTH, MainWindow.HEIGHT - DataViewer.HEIGHT - 30)
        self.temperature_viewer.move(
            45*3 + DataViewer.WIDTH * 2, MainWindow.HEIGHT - DataViewer.HEIGHT - 30)


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
