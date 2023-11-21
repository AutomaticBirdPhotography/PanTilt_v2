import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidgetItem

from form_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.listHeader.setVisible(False)
        self.ui.listWidget.setVisible(False)


        self.ip_address = ""
        self.attempted_addresses = []

        self.spinBoxNames = ["spinBox1", "spinBox2", "spinBox3"]

        self.ui.spinEdit1.textChanged.connect(lambda text: self.handle_spinEdit_value(text, 0))
        self.ui.spinEdit2.textChanged.connect(lambda text: self.handle_spinEdit_value(text, 1))
        
        self.ui.comboBox.currentTextChanged.connect(self.handle_combo_value)

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
            if spin_values[1] > 5: spin_values[1] = 5
            if spin_values[2] > 5: spin_values[2] = 5

        else:
            self.update_spinBox_max([self.spinBoxNames[1],self.spinBoxNames[2]], 9)

        print("Spin Box Values:", spin_values)

    def handle_combo_value(self, text):
        print("ComboBox Index Changed:", text)

    def handle_spinEdit_value(self, text, index):
        print(f"{index} Text Changed:", text)

    def connect(self):
        spin_values = [self.ui.__dict__[name].value() for name in self.spinBoxNames]
        combo_value = self.ui.comboBox.currentText()
        line_edit_values = [self.ui.spinEdit1.text(), self.ui.spinEdit2.text()]

        self.ip_address = ".".join(line_edit_values) + "." + combo_value + "." + "".join(map(str, spin_values))
        
        print(self.ip_address)
        self.failed_connect()

    def failed_connect(self):
        self.ui.listHeader.setVisible(True)
        self.ui.listWidget.setVisible(True)
        self.ui.info_text.setText(f"Error {self.ip_address}")
        self.attempted_addresses.append(self.ip_address)


        self.ui.listWidget.insertItem(0,self.ip_address) 
    
    def reconnect(self, ip_address):
        print(f"Reconnecting to {ip_address}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())