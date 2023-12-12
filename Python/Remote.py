"""
This file contains the implementation of a remote control application for a Pan-Tilt camera system.
The application allows the user to configure the IP address and establish a connection to the camera system.
It also displays a live video feed from the camera and provides controls for pan and tilt movements.
"""
# TODO: Add the functionality to move to point clicked on. Ie. also add ability in menu to change camera parameters

import sys, cv2
from PySide6.QtCore import QThread, Signal, Slot, Qt, QObject, QPoint
from PySide6.QtGui import QImage, QPixmap, QMouseEvent, QPainter, QPen
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QListWidgetItem, QDialog, QLabel

from application_ui import Ui_MainWindow
from IPGui_ui import Ui_Form
from focalGui_ui import Ui_Dialog

from vidTransfer import VideoClient
from joyinput import Controller
import time
import logging

MAX_DISCONNECT_TIME = 60  # Maximum time in seconds to wait for tripod connection before reconnecting

# Set global logging level
LOGGING_LEVEL = logging.DEBUG  # Change this to INFO, WARNING, ERROR, CRITICAL as per your requirement
# If logger is set to level DEBUG it does not connect to the tripod


logging.basicConfig(level=LOGGING_LEVEL, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def setup_logger():
    # Create a logger for this module
    logger = logging.getLogger(__name__)

    # Create a stream handler
    handler = logging.StreamHandler()

    # Create a file handler
    file_handler = logging.FileHandler("remote_error_log.txt", mode='w')  # Change mode to 'w' to clear the file

    # Set the logging level for the file handler to ERROR
    file_handler.setLevel(logging.ERROR)

    # Add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(file_handler)

    return logger

# Create a logger for this module
logger = setup_logger()


# Create a VideoClient instance for video streaming
if logger.isEnabledFor(logging.DEBUG):
    tripod = VideoClient(clientAddress="auto", port="5454", logging=True, debug=True)
else:
    tripod = VideoClient(clientAddress="auto", port="5454", logging=True, debug=False)

joy = Controller(0)

class IPConfigWindow(QDialog):
    """
    A QWidget subclass that represents the IP configuration window.
    This window allows the user to configure the IP address and establish a connection to the camera system.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.listHeader.setVisible(False)
        self.ui.listWidget.setVisible(False)

        self.logger = logging.getLogger(__name__)


        self.ip_address = ""

        self.spinBoxNames = ["spinBox1", "spinBox2", "spinBox3"]

        for name in self.spinBoxNames:
            self.ui.__dict__[name].valueChanged.connect(self.handle_spinBox_value)

        self.ui.checkButton.clicked.connect(self.check_ip)

    def update_spinBox_max(self, names, max_value):
        """
        Update the maximum value of the spin boxes.

        Args:
            names (list): List of spin box names.
            max_value (int): The new maximum value for the spin boxes.
        """
        for name in names:
            spin_box = self.ui.__dict__[name]

            # Disconnect valueChanged signal temporarily
            spin_box.valueChanged.disconnect(self.handle_spinBox_value)

            spin_box.setMaximum(max_value)

            # Reconnect valueChanged signal
            spin_box.valueChanged.connect(self.handle_spinBox_value)

    def handle_spinBox_value(self):
        """
        Handle the value change of the spin boxes.
        """
        spin_values = []
        for name in self.spinBoxNames:
            spin_box = self.ui.__dict__[name]
            spin_values.append(spin_box.value())
        if spin_values[0] == 2:
            self.update_spinBox_max([self.spinBoxNames[1], self.spinBoxNames[2]], 5)
            spin_values[1] = min(spin_values[1], 5)
            spin_values[2] = min(spin_values[2], 5)

        else:
            self.update_spinBox_max([self.spinBoxNames[1], self.spinBoxNames[2]], 9)

    def check_ip(self):
        """
        Check the IP address configuration and establish a connection to the camera system.
        """
        spin_values = [self.ui.__dict__[name].value() for name in self.spinBoxNames]
        combo_value = self.ui.comboBox.currentText()
        line_edit_values = [self.ui.spinEdit1.text(), self.ui.spinEdit2.text()]

        self.ip_address = ".".join(line_edit_values) + "." + combo_value + "." + "".join(map(str, spin_values))
        
        if not self.logger.isEnabledFor(logging.DEBUG):
            self.connect(self.ip_address)
        else:
            self.close_window()

    def connect(self, ip_address):
        """
        Establish a connection to the camera system using the specified IP address.

        Args:
            ip_address (str): The IP address of the camera system.
        """
        try:
            tripod.establish_connection(ip_address)
            self.close_window()
        except:
            self.failed_connect()

    def failed_connect(self):
        """
        Handle the case when the connection to the camera system fails.
        Display an error message and provide options for reconnecting.
        """
        self.ui.listHeader.setVisible(True)
        self.ui.listWidget.setVisible(True)
        self.ui.info_text.setText(f"Error {self.ip_address}")

        # Create a custom widget for each item in the list
        item_widget = QWidget()
        item_layout = QVBoxLayout(item_widget)

        # Label for displaying the IP address
        ip_label = QPushButton(self.ip_address)

        ip_label.setStyleSheet("font-size: 15pt;")  # Adjust the size as needed

        ip_label.clicked.connect(self.handle_ip_label_click)
        item_layout.addWidget(ip_label)

        # Create a list widget item and set the widget for it
        listWidgetItem = QListWidgetItem()
        listWidgetItem.setSizeHint(item_widget.sizeHint())

        # Insert the item at the top of the list
        self.ui.listWidget.insertItem(0, listWidgetItem)
        self.ui.listWidget.setItemWidget(listWidgetItem, item_widget)

    def handle_ip_label_click(self):
        """
        Handle the click event of the IP address label.
        Reconnect to the camera system using the clicked IP address.
        """
        sender_button = self.sender()
        if sender_button is not None:
            ip_address = sender_button.text()
            self.reconnect(ip_address)

    def reconnect(self, ip_address):
        """
        Reconnect to the camera system using the specified IP address.

        Args:
            ip_address (str): The IP address of the camera system.
        """
        print(f"Reconnecting to {ip_address}")
        self.connect(ip_address)

    def close_window(self):
        """
        Close the IP configuration window.
        """
        self.close()

class FocalConfigWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

class VideoThread(QThread):
    """
    A QThread subclass that handles video streaming from the camera system.
    """

    change_pixmap_signal = Signal(QImage)

    def run(self):
        """
        Run the video streaming thread.
        """
        while True:
            frame = tripod.grabFrame()
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
            self.change_pixmap_signal.emit(qt_image)
            time.sleep(0.1)

class DataThread(QThread):
    def __init__(self, parent=None, joy=None, tripod=None, ui=None):
        super().__init__(parent)
        self.joy = joy
        self.tripod = tripod
        self.ui = ui
        self.last_button = self.last_data = None
        self.move_factors = [0.1, 0.5, 1]
        self.move_factor_index = 1

        self.ui.enableCheckBox.clicked.connect(self.handle_enable)
        self.ui.homeButton.clicked.connect(self.handle_home)
        self.ui.alignButton.clicked.connect(self.handle_align)

        # Create a logger for the class
        self.logger = logging.getLogger(__name__)

        # Set move factors in moveFactor combobox
        self.ui.moveFactor.clear()
        self.ui.moveFactor.addItems([str(factor) for factor in self.move_factors])
        self.ui.moveFactor.setCurrentIndex(self.move_factor_index)


    def toggle_joy_input(self):
        """
        Toggle the joyInputCheckBox.
        """
        self.ui.joyInputCheckBox.setChecked(not self.ui.joyInputCheckBox.isChecked())
       
    def toggle_enable(self):
        """
        Toggle the enableCheckBox.
        """
        self.ui.enableCheckBox.setChecked(not self.ui.enableCheckBox.isChecked())
        self.handle_enable()

    def handle_enable(self):
        """
        Handle the enableCheckBox.
        """
        if self.ui.enableCheckBox.isChecked():
            if not self.logger.isEnabledFor(logging.DEBUG):
                self.tripod.sendData("e")

            self.logger.info("Sent 'e' command to tripod")
        else:
            if not self.logger.isEnabledFor(logging.DEBUG):
                self.tripod.sendData("d")
            self.logger.info("Sent 'd' command to tripod")
    
    def handle_home(self):
        """
        Handle the homeButton.
        """
        if not self.logger.isEnabledFor(logging.DEBUG):
            self.tripod.sendData("h")
        self.logger.info("Sent 'h' command to tripod")

    def handle_align(self):
        """
        Handle the alignButton.
        """
        if not self.logger.isEnabledFor(logging.DEBUG):
            self.tripod.sendData("a")
        self.logger.info("Sent 'a' command to tripod")

    def buttonAction(self, button):
        match button:
            case "BACK":
                pass

            case "X":
                self.toggle_joy_input()
                self.logger.info("Joystick toggled joy input")

            case "B":
                self.toggle_enable()
                self.logger.info("Joystick toggled enable")

            case "Y":
                self.handle_home()

            case "A":
                self.handle_align()

            case "UP":
                if self.move_factor_index < len(self.move_factors) - 1:
                    self.move_factor_index += 1
                    self.ui.moveFactor.setCurrentIndex(self.move_factor_index)
                    self.logger.info(f"Joystick changed move factor to {self.move_factors[self.move_factor_index]}")
                
            case "DOWN":
                if self.move_factor_index >= 1:
                    self.move_factor_index -= 1
                    self.ui.moveFactor.setCurrentIndex(self.move_factor_index)
                    self.logger.info(f"Joystick changed move factor to {self.move_factors[self.move_factor_index]}")

    def run(self):
        while True:
            if tripod.is_connected or self.logger.isEnabledFor(logging.DEBUG):
                last_connected = time.time()
            else:
                if time.time() - last_connected > MAX_DISCONNECT_TIME:
                    self.logger.error(f"Connection to tripod has been lost for more than {MAX_DISCONNECT_TIME} seconds. Reconnecting...")
                    if not self.logger.isEnabledFor(logging.DEBUG):
                        tripod.establish_connection("auto")

            clicked_button = self.joy.get_active_button()
            if (clicked_button != self.last_button):
                self.last_button = clicked_button
                self.buttonAction(clicked_button)
            
            if self.ui.joyInputCheckBox.isChecked() and (self.tripod.is_connected or self.logger.isEnabledFor(logging.DEBUG)):
                move_factor = float(self.ui.moveFactor.currentText())
                data = f"{self.joy.get_joystick_position(0, move_factor)}, {self.joy.get_joystick_position(1, move_factor)}"
                if (data != self.last_data):
                    self.last_data = data
                    if not self.logger.isEnabledFor(logging.DEBUG):
                        self.tripod.sendData(data)
                    self.logger.debug(f"Sent '{data}' to tripod")
                self.last_data = data
            time.sleep(0.1)

class MainWindow(QMainWindow):
    """
    A QMainWindow subclass that represents the main application window.
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initProcess()


    def initProcess(self):
        """
        Initialize the user interface.
        """
        self.video_thread = VideoThread()
        self.video_thread.change_pixmap_signal.connect(self.update_video_frame)
        self.video_thread.start()

        self.data_thread = DataThread(joy=joy, tripod=tripod, ui=self.ui)
        self.data_thread.start()
        
        self.ui.actionIP_Config.triggered.connect(self.show_ip_dialog)
        self.ui.actionChange_camera.triggered.connect(self.show_focal_dialog)
        self.focal_length = 500

        #self.show_ip_dialog()


    def mousePressEvent(self, event: QMouseEvent):
        mousePos = self.ui.videoFrame.mapFrom(self, event.position().toPoint())
        if (mousePos.x() < 0 or mousePos.x() > self.image_size.width() or mousePos.y() < 0 or mousePos.y() > self.image_size.height()):
            return
        image_center = QPoint(self.image_size.width()/2, self.image_size.height()/2)
        
        self.toPointPos = image_center - mousePos
        self.drawPoint(mousePos, self.ui.videoFrame.pixmap().toImage())
        print(f"Offset: {self.toPointPos.x()}, {self.toPointPos.y()}")
    
    def drawPoint(self, point, image):
        painter = QPainter(image)
        painter.setPen(QPen(Qt.red))
        painter.drawPoint(point)

    def show_ip_dialog(self):
        """
        Show the IP configuration dialog.
        """
        widget = IPConfigWindow(self)
        widget.exec()

    def show_focal_dialog(self):
        """
        Show the camera configuration dialog.
        """
        dialog = FocalConfigWindow(self)
        if dialog.exec() == QDialog.Accepted:
            self.focal_length = int(dialog.ui.comboBox.currentText())
            logger.info(f"Changed focal length to {self.focal_length}")

    @Slot(QImage)
    def update_video_frame(self, image):
        """
        Update the video frame in the UI.

        Args:
            image (QImage): The new video frame image.
        """
        label_width = self.ui.videoFrame.width()
        label_height = self.ui.videoFrame.height()
        pixmap = QPixmap.fromImage(image).scaled(label_width, label_height, Qt.KeepAspectRatio)
        self.image_size = pixmap.size()
        self.ui.videoFrame.setPixmap(pixmap)

    def closeEvent(self, event):
        """
        Clean up threads when the window is closed.
        """
        self.video_thread.quit()

        self.data_thread.quit()

        event.accept()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        widget = MainWindow()
        widget.show()
        sys.exit(app.exec())

    except Exception as e:
        logger.error("An error occurred", exc_info=True)

    finally:
        try:
            joy.stop()
            tripod.stop()   #Tar seg av å sende "s"
        except Exception as e:
            logger.error("An error occurred", exc_info=True)
                
            raise Exception("Alvorlige programfeil oppstod")