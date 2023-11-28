# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ip_connect.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(787, 496)
        Form.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(260, 60, 401, 46))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.spinEdit1 = QSpinBox(self.layoutWidget)
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

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.spinEdit2 = QSpinBox(self.layoutWidget)
        self.spinEdit2.setObjectName(u"spinEdit2")
        self.spinEdit2.setMinimumSize(QSize(40, 0))
        self.spinEdit2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinEdit2.setMinimum(0)
        self.spinEdit2.setMaximum(255)
        self.spinEdit2.setValue(168)

        self.horizontalLayout.addWidget(self.spinEdit2)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.comboBox = QComboBox(self.layoutWidget)
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

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.spinBox1 = QSpinBox(self.layoutWidget)
        self.spinBox1.setObjectName(u"spinBox1")
        self.spinBox1.setMinimum(0)
        self.spinBox1.setMaximum(2)
        self.spinBox1.setStepType(QAbstractSpinBox.DefaultStepType)
        self.spinBox1.setValue(1)

        self.horizontalLayout.addWidget(self.spinBox1)

        self.spinBox2 = QSpinBox(self.layoutWidget)
        self.spinBox2.setObjectName(u"spinBox2")
        self.spinBox2.setMinimum(0)
        self.spinBox2.setMaximum(9)
        self.spinBox2.setValue(9)

        self.horizontalLayout.addWidget(self.spinBox2)

        self.spinBox3 = QSpinBox(self.layoutWidget)
        self.spinBox3.setObjectName(u"spinBox3")
        self.spinBox3.setMinimum(0)
        self.spinBox3.setMaximum(9)
        self.spinBox3.setValue(2)

        self.horizontalLayout.addWidget(self.spinBox3)

        self.checkButton = QPushButton(Form)
        self.checkButton.setObjectName(u"checkButton")
        self.checkButton.setGeometry(QRect(370, 220, 121, 71))
        self.listWidget = QListWidget(Form)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setEnabled(True)
        self.listWidget.setGeometry(QRect(30, 270, 256, 192))
        self.listHeader = QLabel(Form)
        self.listHeader.setObjectName(u"listHeader")
        self.listHeader.setEnabled(True)
        self.listHeader.setGeometry(QRect(70, 240, 201, 31))
        self.listHeader.setStyleSheet(u"font: 13pt \"Segoe UI\";")
        self.info_text = QLabel(Form)
        self.info_text.setObjectName(u"info_text")
        self.info_text.setGeometry(QRect(40, 120, 721, 51))
        self.info_text.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"text-align: center;")

        self.retranslateUi(Form)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u".", None))
        self.label_5.setText(QCoreApplication.translate("Form", u".", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"4", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"10", None))

        self.label_6.setText(QCoreApplication.translate("Form", u".", None))
        self.checkButton.setText(QCoreApplication.translate("Form", u"Check", None))
        self.listHeader.setText(QCoreApplication.translate("Form", u"Attempted ip addresses", None))
        self.info_text.setText("")
    # retranslateUi

