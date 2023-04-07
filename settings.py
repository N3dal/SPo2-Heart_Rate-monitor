"""
    Docstring;
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from serial_handler import SerialHandler


class SettingsWindow(QMainWindow):
    """
        Docstring;
    """

    WIDTH, HEIGHT = 400, 250
    STYLESHEET = """
        background-color: #ffffff;
    """

    SAVE_BUTTON_STYLESHEET = """
        QPushButton{
            background-color: #5ba2f4;
            color: black;
            border-radius: 8px;
        }
        
        QPushButton:hover{
            background-color: #2ca3fa;
            
        }
    
    """

    PORT_SELECTION_STYLESHEET = """
        color: black;
    """

    BUAD_RATE_SELECTION_STYLESHEET = """
        color: black;
    """

    LABEL_STYLESHEET = """
        color: black;
        font-size: 15px;
    """

    TITLE = "Settings"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFixedSize(SettingsWindow.WIDTH, SettingsWindow.HEIGHT)
        self.setStyleSheet(SettingsWindow.STYLESHEET)
        self.setWindowTitle(SettingsWindow.TITLE)

        self.serial_handler = SerialHandler()

        self.save_button = QPushButton(parent=self, text="Save")
        self.save_button.setFixedSize(110, 45)
        self.save_button.setStyleSheet(SettingsWindow.SAVE_BUTTON_STYLESHEET)
        self.save_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.save_button.clicked.connect(self.__save_button_click_event)
        self.save_button.move(SettingsWindow.WIDTH - 120,
                              SettingsWindow.HEIGHT - 60)

        self.port_label = QLabel(parent=self, text="Port:")
        self.port_label.setStyleSheet(SettingsWindow.LABEL_STYLESHEET)
        self.port_label.move(10, 10)
        self.port_selection = QComboBox(parent=self)
        self.port_selection.setStyleSheet(
            SettingsWindow.PORT_SELECTION_STYLESHEET)
        self.port_selection.addItems(
            port.device for port in self.serial_handler.available_ports)
        self.port_selection.move(55, 10)

        self.buad_rate_label = QLabel(parent=self, text="Buad-Rate:")
        self.buad_rate_label.setStyleSheet(SettingsWindow.LABEL_STYLESHEET)
        self.buad_rate_label.move(10, 50)
        self.buad_rate_selection = QComboBox(parent=self)
        self.buad_rate_selection.setStyleSheet(
            SettingsWindow.PORT_SELECTION_STYLESHEET)
        self.buad_rate_selection.addItems(
            str(buad_rate) for buad_rate in self.serial_handler.BUAD_RATES)
        self.buad_rate_selection.move(100, 50)

    def __save_button_click_event(self):
        """
            :ARGS:
                None;

            :RETURNS:
                return None;

            :INFO:
                save button event;
        """

        return None
