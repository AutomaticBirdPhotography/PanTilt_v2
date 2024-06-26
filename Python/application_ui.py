# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'application.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(819, 648)
        MainWindow.setStyleSheet(u"\n"
"/* Set the background color to a dark shade */\n"
"QWidget {\n"
"	font: 14pt \"Segoe UI\";\n"
"    background-color: #333333; /* You can adjust the color code as needed */\n"
"    color: #ffffff; /* Set the text color to white or a contrasting color */\n"
"}\n"
"\n"
"/* Set the background color of QComboBox */\n"
"QComboBox {\n"
"    background-color: #444444;\n"
"    color: #ffffff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Set the background color of QSpinBox */\n"
"QSpinBox {\n"
"    background-color: #444444;\n"
"    color: #ffffff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"\n"
"/* Set the background color of QListView */\n"
"QListView {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QLineEdit */\n"
"QLineEdit {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"/* Set the background color of QPlainTextEdit */\n"
"QPlainTextEdit {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"/* Set the background color of QTabWidget */\n"
"QTabWidget {\n"
"    background-color"
                        ": #444444;\n"
"}\n"
"\n"
"/* Set the background color of QTableWidget */\n"
"QTableWidget {\n"
"    background-color: #444444;\n"
"}\n"
"\n"
"/* Set the background color of QHeaderView */\n"
"QHeaderView {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QScrollBar */\n"
"QScrollBar:vertical {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QScrollBar handle */\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"/* Set the background color of QScrollBar handle when pressed */\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #999999;\n"
"}\n"
"\n"
"/* Set the background color of QScrollBar add and subtract buttons */\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QScrollBar add and subtract buttons when pressed */\n"
"QScrollBar::add-line:vertical:pressed,\n"
"QScrollBar::sub-line:vertical:pressed {\n"
""
                        "    background: #777777;\n"
"}\n"
"\n"
"/* Set the background color of QMenuBar */\n"
"QMenuBar {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"/* Set the background color of QMenuBar items */\n"
"QMenuBar::item {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Set the background color of QMenuBar items when hovered */\n"
"QMenuBar::item:selected {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QMenuBar items when pressed */\n"
"QMenuBar::item:pressed {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"/* Set the background color of QMenu */\n"
"QMenu {\n"
"    background-color: #333333;\n"
"    color: #ffffff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"/* Set the background color of QMenu items */\n"
"QMenu::item {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* Set the background color of QMenu items when hovered */\n"
"QMenu::item:selected {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QMenu items when p"
                        "ressed */\n"
"QMenu::item:pressed {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"/* Set the background color of QMenu items when checked */\n"
"QMenu::item:checked {\n"
"    background-color: #555555;\n"
"}\n"
"\n"
"/* Set the background color of QMenu items when checked and hovered */\n"
"QMenu::item:checked:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"/* Set the background color of QPushButton */\n"
"QPushButton {\n"
"    background-color: #296968;\n"
"    color: #ffffff;\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"\n"
"/* Set the background color of QPushButton when hovered */\n"
"QPushButton:hover {\n"
"    background-color: #1a4848;\n"
"\n"
"}\n"
"\n"
"/* Set the background color of QPushButton when pressed */\n"
"QPushButton:pressed {\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"/* Set the background color of QPushButton when focused */\n"
"QPushButton:selected {\n"
"    background-color: #777777;\n"
"}\n"
"\n"
"QCheckBox:indicator {\n"
"	background-color : #555555;\n"
""
                        "	border-radius: 5px;\n"
"    width: 16px; /* Adjust the size as needed */\n"
"    height: 16px; /* Adjust the size as needed */\n"
"}\n"
"\n"
"QCheckBox:indicator:checked {\n"
"	background-color : #f58900;\n"
"}\n"
"")
        self.actionChange_camera = QAction(MainWindow)
        self.actionChange_camera.setObjectName(u"actionChange_camera")
        self.actionIP_Config = QAction(MainWindow)
        self.actionIP_Config.setObjectName(u"actionIP_Config")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.videoFrame = QLabel(self.centralwidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setGeometry(QRect(40, 80, 741, 431))
        self.videoFrame.setStyleSheet(u"")
        self.joyInputCheckBox = QCheckBox(self.centralwidget)
        self.joyInputCheckBox.setObjectName(u"joyInputCheckBox")
        self.joyInputCheckBox.setGeometry(QRect(30, 530, 101, 21))
        self.joyInputCheckBox.setIconSize(QSize(16, 16))
        self.joyInputCheckBox.setChecked(True)
        self.enableCheckBox = QCheckBox(self.centralwidget)
        self.enableCheckBox.setObjectName(u"enableCheckBox")
        self.enableCheckBox.setGeometry(QRect(150, 530, 81, 20))
        self.enableCheckBox.setChecked(True)
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(250, 520, 81, 41))
        self.alignButton = QPushButton(self.centralwidget)
        self.alignButton.setObjectName(u"alignButton")
        self.alignButton.setGeometry(QRect(340, 520, 81, 41))
        self.moveFactor = QComboBox(self.centralwidget)
        self.moveFactor.setObjectName(u"moveFactor")
        self.moveFactor.setGeometry(QRect(697, 41, 81, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 819, 32))
        self.menuProperties = QMenu(self.menubar)
        self.menuProperties.setObjectName(u"menuProperties")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProperties.menuAction())
        self.menuProperties.addAction(self.actionChange_camera)
        self.menuProperties.addAction(self.actionIP_Config)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionChange_camera.setText(QCoreApplication.translate("MainWindow", u"Change camera", None))
        self.actionIP_Config.setText(QCoreApplication.translate("MainWindow", u"IP Config", None))
        self.videoFrame.setText(QCoreApplication.translate("MainWindow", u"DSLR_video", None))
        self.joyInputCheckBox.setText(QCoreApplication.translate("MainWindow", u"Joy Input", None))
        self.enableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.alignButton.setText(QCoreApplication.translate("MainWindow", u"Align", None))
        self.menuProperties.setTitle(QCoreApplication.translate("MainWindow", u"Properties", None))
    # retranslateUi

