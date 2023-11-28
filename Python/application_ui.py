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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.videoFrame = QLabel(self.centralwidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setGeometry(QRect(120, 80, 461, 281))
        self.joyInputCheckBox = QCheckBox(self.centralwidget)
        self.joyInputCheckBox.setObjectName(u"joyInputCheckBox")
        self.joyInputCheckBox.setGeometry(QRect(70, 380, 81, 51))
        self.joyInputCheckBox.setIconSize(QSize(16, 16))
        self.joyInputCheckBox.setChecked(True)
        self.enableCheckBox = QCheckBox(self.centralwidget)
        self.enableCheckBox.setObjectName(u"enableCheckBox")
        self.enableCheckBox.setGeometry(QRect(70, 430, 75, 20))
        self.enableCheckBox.setChecked(True)
        self.homeButton = QPushButton(self.centralwidget)
        self.homeButton.setObjectName(u"homeButton")
        self.homeButton.setGeometry(QRect(220, 420, 75, 24))
        self.alignButton = QPushButton(self.centralwidget)
        self.alignButton.setObjectName(u"alignButton")
        self.alignButton.setGeometry(QRect(320, 420, 75, 24))
        self.moveFactor = QComboBox(self.centralwidget)
        self.moveFactor.setObjectName(u"moveFactor")
        self.moveFactor.setGeometry(QRect(120, 50, 68, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.videoFrame.setText(QCoreApplication.translate("MainWindow", u"DSLR_video", None))
        self.joyInputCheckBox.setText(QCoreApplication.translate("MainWindow", u"Joy Input", None))
        self.enableCheckBox.setText(QCoreApplication.translate("MainWindow", u"Enable", None))
        self.homeButton.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.alignButton.setText(QCoreApplication.translate("MainWindow", u"Align", None))
    # retranslateUi

