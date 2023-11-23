import sys
from IPconfigurator import IPconfigGUI
from PySide6.QtWidgets import QApplication

app = QApplication(sys.argv)
IPGui = IPconfigGUI.MainWindow()
IPGui.show()

sys.exit(app.exec())