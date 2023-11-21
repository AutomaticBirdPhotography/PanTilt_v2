# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.checkButton = QPushButton(self.centralwidget)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(320, 280, 121, 71))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(185, 144, 391, 48))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spinEdit1 = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinEdit1.setObjectName(u"spinEdit1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinEdit1.sizePolicy().hasHeightForWidth())
        self.spinEdit1.setSizePolicy(sizePolicy)
        self.spinEdit1.setMinimumSize(QSize(45, 0))
        self.spinEdit1.setStyleSheet(u"")
        self.spinEdit1.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinEdit1.setMinimum(0)
        self.spinEdit1.setMaximum(255)
        self.spinEdit1.setValue(192)

        self.horizontalLayout.addWidget(self.spinEdit1)

        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.spinEdit2 = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinEdit2.setObjectName(u"spinEdit2")
        self.spinEdit2.setMinimumSize(QSize(40, 0))
        self.spinEdit2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinEdit2.setMinimum(0)
        self.spinEdit2.setMaximum(255)
        self.spinEdit2.setValue(168)

        self.horizontalLayout.addWidget(self.spinEdit2)

        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.horizontalLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setMinimumSize(QSize(60, 0))

        self.horizontalLayout.addWidget(self.comboBox)

        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.spinBox1 = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox1.setObjectName(u"spinBox1")
        self.spinBox1.setMinimum(0)
        self.spinBox1.setMaximum(2)
        self.spinBox1.setStepType(QAbstractSpinBox.DefaultStepType)
        self.spinBox1.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox1)

        self.spinBox2 = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox2.setObjectName(u"spinBox2")
        self.spinBox2.setMinimum(0)
        self.spinBox2.setMaximum(9)
        self.spinBox2.setValue(9)

        self.horizontalLayout.addWidget(self.spinBox2)

        self.spinBox3 = QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox3.setObjectName(u"spinBox3")
        self.spinBox3.setMinimum(0)
        self.spinBox3.setMaximum(9)
        self.spinBox3.setValue(2)

        self.horizontalLayout.addWidget(self.spinBox3)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.info_text = QLabel(self.centralwidget)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setGeometry(QRect(40, 210, 721, 51))
        self.info_text.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QRect(40, 350, 256, 192))
        self.listHeader = QLabel(self.centralwidget)
        self.listHeader.setObjectName(u"listHeader")
        self.listHeader.setEnabled(True)
        self.listHeader.setGeometry(QRect(60, 320, 201, 31))
        self.listHeader.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.checkButton.setText(QCoreApplication.translate("MainWindow", u"Check", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"10", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.info_text.setText("")
        self.listHeader.setText(QCoreApplication.translate("MainWindow", u"Attempted ip addresses", None))
    # retranslateUi

