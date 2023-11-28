import sys, cv2
from PySide6.QtCore import QThread, Signal, Slot, Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QListWidgetItem
from ip_connect_ui import Ui_Form
from core_connect import ConnectionModule



connection = ConnectionModule(clientAddress="auto", port="5454", logging=True)


class IPConfigWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.listHeader.setVisible(False)
        self.ui.listWidget.setVisible(False)

        self.ip_address = ""

        self.spinBoxNames = ["spinBox1", "spinBox2", "spinBox3"]

        for name in self.spinBoxNames:
            self.ui.__dict__[name].valueChanged.connect(self.handle_spinBox_value)

        self.ui.checkButton.clicked.connect(self.connect)

    def update_spinBox_max(self, names, max_value):
        for name in names:
            spin_box = self.ui.__dict__[name]

            # Disconnect valueChanged signal temporarily
            spin_box.valueChanged.disconnect(self.handle_spinBox_value)

            spin_box.setMaximum(max_value)

            # Reconnect valueChanged signal
            spin_box.valueChanged.connect(self.handle_spinBox_value)

    def handle_spinBox_value(self):
        spin_values = []
        for name in self.spinBoxNames:
            spin_box = self.ui.__dict__[name]
            spin_values.append(spin_box.value())
        if spin_values[0] == 2:
            self.update_spinBox_max([self.spinBoxNames[1],self.spinBoxNames[2]], 5)
            spin_values[1] = min(spin_values[1], 5)
            spin_values[2] = min(spin_values[2], 5)

        else:
            self.update_spinBox_max([self.spinBoxNames[1],self.spinBoxNames[2]], 9)

    def connect(self):
        spin_values = [self.ui.__dict__[name].value() for name in self.spinBoxNames]
        combo_value = self.ui.comboBox.currentText()
        line_edit_values = [self.ui.spinEdit1.text(), self.ui.spinEdit2.text()]

        self.ip_address = ".".join(line_edit_values) + "." + combo_value + "." + "".join(map(str, spin_values))
        try:
            connection.establish_connection(self.ip_address)
        except:
            self.failed_connect()

    def failed_connect(self):
        self.ui.listHeader.setVisible(True)
        self.ui.listWidget.setVisible(True)
        self.ui.info_text.setText(f"Error {self.ip_address}")

        # Create a custom widget for each item in the list
        item_widget = QWidget()
        item_layout = QVBoxLayout(item_widget)

        # Label for displaying the IP address
        ip_label = QPushButton(self.ip_address)
        
        ip_label.setStyleSheet("font-size: 15pt;") # Adjust the size as needed
        
        ip_label.clicked.connect(self.handle_ip_label_click)
        item_layout.addWidget(ip_label)

        # Create a list widget item and set the widget for it
        listWidgetItem = QListWidgetItem()
        listWidgetItem.setSizeHint(item_widget.sizeHint())
        
        # Insert the item at the top of the list
        self.ui.listWidget.insertItem(0, listWidgetItem)
        self.ui.listWidget.setItemWidget(listWidgetItem, item_widget)

    def handle_ip_label_click(self):
        sender_button = self.sender()
        if sender_button is not None:
            ip_address = sender_button.text()
            self.reconnect(ip_address)

    def reconnect(self, ip_address):
        print(f"Reconnecting to {ip_address}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = IPConfigWindow()
    widget.show()
    sys.exit(app.exec())