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
import pyqtgraph as pg
from utils import *
from settings import (SettingsWindow)
from defaults import *
import os
import sys

# wipe terminal screen;
clear()


class Plotter(pg.PlotWidget):
    """
        Custom Plotter;
    """

    BACKGROUND_COLOR = "black"

    STYLESHEET = """
        border: 8px solid #5ba2f4;
        border-radius: 10px;
    """

    def __init__(self, width: int, height: int, name: str, pen_color: str = "#cd1b5b", *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__width = width
        self.__height = height
        self.__name = name

        self.pen = pg.mkPen(color=pen_color, width=2.4)

        self.setGeometry(0, 0, self.__width, self.__height)

        # hold the x data axis data;
        # self.x = [0 for _ in range(100)]

        # # hold the y data axis data;
        # self.y = [*self.x]

        # # we need line reference to update the plot,
        # # and we can get the line reference when we,
        # # first plot the data;
        # self.line_ref = self.plot(self.x, self.y, pen=self.pen)

        # now hide the axises values;
        self.getAxis("bottom").setStyle(showValues=False)
        self.getAxis("left").setStyle(showValues=False)

        self.showGrid(x=True, y=True, alpha=1.0)

        self.setContentsMargins(0, 0, 0, 0)

        self.setBackground(Plotter.BACKGROUND_COLOR)

        self.setStyleSheet(Plotter.STYLESHEET)

    def update(self, data: list):
        """
            :ARGS:
                data:list => the new data;

            :RETURNS:
                return None;

            :INFO:
                update the plot data;
        """

        return None

    @property
    def name(self):
        return self.__name


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

        # create the settings Window;
        self.__settings_window = SettingsWindow()

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

        self.__settings_window.show()
        self.__settings_window.activateWindow()

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
    START_BUTTON_STYLESHEET = """
        QPushButton{
            background-color: #f0f0f0;
            color: black;
            border: 1px solid black;
            border-radius: 8px;
        }
        
        QPushButton:hover{
            border: 2px solid black;
            
        }
    
    """
    TITLE = "Arduino HST Monitor"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(MainWindow.WIDTH, MainWindow.HEIGHT)
        self.setStyleSheet(MainWindow.STYLESHEET)
        self.setWindowTitle(MainWindow.TITLE)

        menu_bar = MenuBar(parent=self)
        self.setMenuBar(menu_bar)

        # create the plotters;
        self.heart_rate_plotter = Plotter(
            parent=self, name="heart-rate", width=MainWindow.WIDTH-85, height=200)
        self.spo2_level_plotter = Plotter(
            parent=self, name="spo2-level", width=450, height=200)
        self.temperature_plotter = Plotter(
            parent=self, name="temperature", width=MainWindow.WIDTH - 545, height=200)

        self.heart_rate_plotter.move(30, 40)
        self.spo2_level_plotter.move(30, 250)
        self.temperature_plotter.move(490, 250)

        # create the DataViewers;
        self.heart_rate_viewer = DataViewer(
            parent=self, name="heart-rate", measurement_unit="bpm")
        self.spo2_level_viewer = DataViewer(
            parent=self, name="spo2-level", measurement_unit="%")
        self.temperature_viewer = DataViewer(
            parent=self, name="temperature", measurement_unit="°C")

        self.heart_rate_viewer.move(
            30, MainWindow.HEIGHT - DataViewer.HEIGHT - 25)
        self.spo2_level_viewer.move(
            40*2 + DataViewer.WIDTH, MainWindow.HEIGHT - DataViewer.HEIGHT - 25)
        self.temperature_viewer.move(
            40*3 + DataViewer.WIDTH * 2, MainWindow.HEIGHT - DataViewer.HEIGHT - 25)

        # create play and stop pictures for the button;
        self.__play_picture = QIcon(UI.PLAY_PICTURE_PATH)
        self.__stop_picture = QIcon(UI.STOP_PICTURE_PATH)

        # create an indicator for button status;
        self.__start_button_status = False

        self.start_button = QPushButton(parent=self)
        self.start_button.setFixedSize(43, 35)
        self.start_button.setIcon(self.__play_picture)
        self.start_button.setStyleSheet(MainWindow.START_BUTTON_STYLESHEET)
        self.start_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.start_button.clicked.connect(self.__start_button_click_event)
        self.start_button.move(MainWindow.WIDTH - 48, 40)

    def __start_button_click_event(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                start button event;
        """
        self.__start_button_status = False if self.__start_button_status else True

        if self.__start_button_status:
            # we want to stop;
            # set the icon to stop;
            self.start_button.setIcon(self.__stop_picture)

        else:
            # we want to start;
            # set the icon to play;
            self.start_button.setIcon(self.__play_picture)

        return None


def main():

    app = QApplication(sys.argv)

    root = MainWindow()

    root.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
