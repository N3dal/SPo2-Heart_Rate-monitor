"""
    Docstring;
"""
import serial
from serial.tools import list_ports
from PyQt5.QtCore import QObject
from PyQt5.QtCore import pyqtSignal


class SerialHandler:
    """
        Custom Serial handler for the arduino;
    """

    BUAD_RATES = [300,
                  600,
                  750,
                  1200,
                  2400,
                  4800,
                  9600,
                  19200,
                  31250,
                  38400,
                  57600,
                  74880,
                  115200,
                  230400,
                  250000,
                  460800,
                  500000,
                  921600,
                  1000000,
                  2000000]

    class Signals(QObject):
        """
            Docstring;
        """

        received_data = pyqtSignal(str)
        closed = pyqtSignal()
        opened = pyqtSignal()

    def __init__(self):

        self.__available_ports = []
        self.__active_connections = []
        self.signals = SerialHandler.Signals()
        self.data = None

    def check_for_available_ports(self):
        """
            :ARGS:
                None;

            :INFO:
                check out from the available ports on the machine;

            :RETURNS:
                return list;
        """

        self.__available_ports = list_ports.comports()
        # print(self.__available_ports)

        return self.__available_ports

    def open_connection(self, device_name: str, buad_rate: int = 9600, timeout: int = 1):
        """
            :ARGS:
                device_name: str => the device name or path;
                buad_rate: int => data buad rate;
                timeout:int => timeout;

            :INFO:
                create a serial connection simply out open serial communication;

            :RETURNS:
                return None;
        """

        try:
            conn = serial.Serial(device_name, int(buad_rate), timeout=timeout)
            self.__active_connections.append(conn)
            self.signals.opened.emit()

        except:
            raise Exception(
                f"Can't open the port {device_name=} with buad_rate {buad_rate=}")

        return None

    def close_connection(self, device_name: str):
        """
            :ARGS:
                device_name:str => the device that we want to close;

            :INFO:
                close the serial connection for specific device;

            :RETURNS:
                return bool;

                return True if the device closed, other wise it returns False;
        """

        if not self.__active_connections:
            # if theres no connections;
            return False

        for conn in self.__active_connections.copy():
            if conn.name == device_name:
                conn.close()

                # now remove the conn from the active list;
                self.__active_connections.remove(conn)

                self.signals.closed.emit()
                return True

        return False

    def close_all(self):
        """
            :ARGS:
                None;

            :INFO:
                close all the active connections;

            :RETURNS:
                return None;

        """

        for conn in self.__active_connections.copy():
            self.close_connection(conn.name)

        self.__active_connections.clear()

        return None

    def read(self, device_name: str):
        """
            :ARGS:
                device_name:str => the port that you want to read data from it;

            :RETURNS:
                return the data that capture from the serial port;
                return the str;

            :INFO:
                read full line a specific port;
                make sure that your line ends with '\n';
        """

        # if not self.__active_connections:
        #     # if theres no port available;
        #     raise Exception("Theres no port to read from it!!!")

        for device in self.__active_connections:
            if device.name == device_name:
                self.data = device.readline().decode()
                self.signals.received_data.emit(self.data)

        return self.data

    @property
    def available_ports(self):
        """
            Docstring;
        """

        # first check out for available ports;
        self.check_for_available_ports()

        return self.__available_ports

    @property
    def active_connections(self):
        """
            View all available connections;
        """

        return self.__active_connections


s = SerialHandler()
s.open_connection(device_name="/dev/ttyACM0")
print(s.read("/dev/ttyACM0"))

# s.read("fine")
