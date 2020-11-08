# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Pharmacy.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import tuple_factory

from multiprocessing.pool import ThreadPool

import sys
import re
import json

# Thread Class
class WorkerThread(QThread):
    
    finished = Signal(object)

    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        try:
            result = self.fn(
                *self.args, **self.kwargs
            )
        except Exception as e:
            print(e)
        else:
            self.finished.emit(result)

class Ui_DeleteWindow(QWidget):

    accepted = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(400, 340)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyleSheet(u"background-color: rgb(250, 251, 254);")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(239, 241, 248);\nborder-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(0, 210))
        self.label.setStyleSheet(u"font: 12 24pt \"JetBrains Mono ExtraLight\";")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText("Are you sure you \nwant to delete:\n")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(62, 74, 89);border-radius: 3px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton_2:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton_2:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.frame_2)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

## Button Events ##
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Yes", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"No", None))

## Custom Functions ##
    def yes(self):
        self.accepted.emit()
        self.close()
    
    def no(self):
        self.close()

## Add Patient WINDOW ##
class Ui_AddPatient(QWidget):

    submitted = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.lineEditQSS = ("""
        font: 25 14pt "JetBrains Mono Light";
        background-color: rgb(220, 221, 252);
        padding: 5px;
        """)

        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(400, 340)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyleSheet(u"background-color: rgb(250, 251, 254);")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: rgb(239, 241, 248);border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignCenter)
        self.formLayout.setFormAlignment(Qt.AlignCenter)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 20pt \"JetBrains Mono Extra Bold\";color: rgb(112, 0, 168);")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"font: 20pt \"JetBrains Mono Extra Bold\";color: rgb(112, 0, 168);")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit_2")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setStyleSheet(self.lineEditQSS)
        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.lineEdit)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit")
        self.lineEdit_2.setStyleSheet(self.lineEditQSS)
        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.lineEdit_2)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(62, 74, 89);border-radius: 3px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton_2:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton_2:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.frame_2)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

## Button Events ##
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Last Name", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add Patient", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Discard", None))

## CUSTOM FUNCTIONS ##
    # Button Functions
    def yes(self):
        fname = self.lineEdit.text()
        lname = self.lineEdit_2.text()
        self.submitted.emit(fname, lname)
        self.close()

    def no(self):
        self.close()

## Add Medication WINDOW ##
class Ui_AddMedication(QWidget):

    confirmed = Signal(bool, str, str, str, str)

    def __init__(self):
        super().__init__()
        self.spinBoxQSS = """
        font: 20pt "Segoe UI";
        background-color: rgb(220, 221, 252);font: 20pt "Segoe UI";
        """
        self.labelQSS = """
        font: 20pt "JetBrains Mono Extra Bold";
        color: rgb(112, 0, 168);
        """

        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(400, 300)
        self.setMaximumSize(400, 300)
        self.setMinimumSize(400, 300)
        self.setWindowModality(Qt.ApplicationModal)
        self.setStyleSheet("background-color: rgb(250, 251, 254);")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setStyleSheet("background-color: rgb(239, 241, 248);border-radius: 5px;")
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 50))
        self.label.setAlignment(Qt.AlignHCenter)
        self.label.setStyleSheet(self.labelQSS)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)    

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 50))
        self.label_2.setAlignment(Qt.AlignHCenter)
        self.label_2.setStyleSheet(self.labelQSS)
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)    

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 50))
        self.label_3.setAlignment(Qt.AlignHCenter)
        self.label_3.setStyleSheet(self.labelQSS)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 50))
        self.label_4.setAlignment(Qt.AlignHCenter)
        self.label_4.setStyleSheet(self.labelQSS)
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 40))
        self.spinBox.setStyleSheet(self.spinBoxQSS)
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(0, 40))
        self.spinBox_2.setStyleSheet(self.spinBoxQSS)
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_2)

        self.spinBox_3 = QSpinBox(self.frame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(0, 40))
        self.spinBox_3.setStyleSheet(self.spinBoxQSS)
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.frame)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(0, 40))
        self.spinBox_4.setStyleSheet(self.spinBoxQSS)
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBox_4)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 80))
        self.frame_2.setStyleSheet("background-color: rgb(62, 74, 89);border-radius: 3px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 12pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton_2:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton_2:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.frame_2)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

## BUTTON EVENTS ##
        # Button Box
        self.pushButton.clicked.connect(self.yes)
        self.pushButton_2.clicked.connect(self.no)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Morning", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Noon", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Evening", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Bedtime", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add Medication", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Discard", None))

## CUSTOM FUNCTIONS ##
    def addEdit(self, value):
        self.isEdit = value

    def yes(self):
        morning = self.spinBox.text()
        noon = self.spinBox_2.text()
        evening = self.spinBox_3.text()
        bedtime = self.spinBox_4.text()
        self.confirmed.emit(self.isEdit, morning, noon, evening, bedtime)
        self.close()

    def no(self):
        self.close()

## MAIN WINDOW ##
class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        # INITIALIZE UI
        self.resize(1600, 900)
        self.setMinimumSize(QSize(1600, 900))
        self.setStyleSheet("background-color: rgb(250, 251, 254);")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(750, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.comboBox.setStyleSheet("""
        QComboBox {
            background-color: rgb(239, 241, 248);
            border-radius: 5px;
        }
        QComboBox:on {
            background-color: rgb(228, 224, 255)
        }
        QComboBox::drop-down {
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 20px;
        
            border-top-right-radius: 3px;
            border-bottom-right-radius: 3px;
        }
        QComboBox QAbstractView{
            font: 12pt "Segoe UI Light";
            background-color: rgb(239, 215, 245);
            color: #999999;
            selection-background-color: #999999;
            selection-color: #4f4f4f;
        }
        """)
        font2 = QFont()
        font2.setFamily(u"Segoe UI Light")
        font2.setPointSize(14)
        self.comboBox.setFont(font2)
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 30pt "Montserrat Alternates ExtraBold";
        }
        QPushButton#pushButton_2:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton_2:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.pushButton_3.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
			font: 30pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton_3:hover {
            background-color: rgb(82, 86, 238);
			border-radius: 3px;
        }
        QPushButton#pushButton_3:pressed {
            background-color: rgb(82, 86, 238);
			border: 3px solid rgbrgb(214, 203, 255);
			border-radius: 3px;
        }
        """)
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet("""
        QTableWidget {	
            background-color: rgb(239, 241, 248);
            padding: 10px;
            border-radius: 5px;
            gridline-color: rgb(192, 192, 192);
            font: 25 12pt "Segoe UI Semilight";
        }
        QTableWidget::item{
            border-color: rgb(44, 49, 60);
            padding-left: 3px;
            padding-right: 3px;
            gridline-color: rgb(192, 192, 192);
        }
        QTableWidget::item:selected{
            background-color: rgb(85, 170, 255, 200);
        }
        QTableWidget::horizontalHeader{	
            background-color: rgb(220, 221, 252);
            font: 25 18pt "Segoe UI Light";
        }
        QHeaderView::section:horizontal{
            border: 1px solid rgb(170, 170, 255);
            background-color: rgb(220, 221, 252);
            font: 25 12pt "Segoe UI Semibold";
            padding: 3px;
        }
        """)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 90)
        self.tableWidget.setColumnWidth(4, 90)
        self.tableWidget.setColumnWidth(5, 90)
        self.tableWidget.setColumnWidth(6, 90)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.Fixed)
        self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.Fixed)
        self.tableWidget.setHorizontalHeaderLabels([
            "DIN",
            "Medication",
            "Strength",
            "Morning",
            "Noon",
            "Evening",
            "Bedtime"
        ])
        self.gridLayout_2.addWidget(self.tableWidget, 1, 0, 1, 3)

        self.gridLayout.addWidget(self.frame_2, 1, 1, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"""
        font: 48pt "JetBrains Mono";
        color: rgb(10, 10, 10);
        border: 4px solid rgb(170, 170, 255);
        border-radius: 15px;
        background-color: rgb(220, 221, 252);
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(420, 0))
        self.frame_3.setMaximumSize(QSize(500, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setStyleSheet("""
        background-color: rgb(62, 74, 89);
        border-radius: 10px;
        padding: 5px;
        """)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # Medication Lookup
        self.model = QStandardItemModel(0, 3)
        self.model.setHorizontalHeaderLabels([
            "DIN",
            "Medication",
            "Strength",
        ])
            
        self.filter_proxy_model = QSortFilterProxyModel()
        self.filter_proxy_model.setSourceModel(self.model)
        self.filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.filter_proxy_model.setFilterKeyColumn(1)


        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(241, 243, 250);border-radius: 10px;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.tableView = QTableView(self.frame_4)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet("""
        QTableView {
            background-color: rgb(239, 241, 248);
            border-radius: 3px;
            font: 12pt 'Segoe UI Light';
        }
        QTableView::horizontalHeader{	
            background-color: rgb(220, 221, 252);
            font: 14pt 'Segoe UI';
        }
        QHeaderView::section:horizontal{
            border: 1px solid rgb(170, 170, 255);
            background-color: rgb(220, 221, 252);
            font: 12pt 'Segoe UI Semibold';
            padding: 3px;
            border-radius: 2px;
        }
        QTableView::item:selected{
            background-color: rgb(85, 170, 255, 200);
        }
        """)
        self.tableView.setModel(self.filter_proxy_model)
        self.verticalLayout.addWidget(self.tableView)
        self.tableView.horizontalHeader().setFixedHeight(35)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setColumnWidth(0, 70)
        self.tableView.setColumnWidth(2, 95)
        self.tableView.horizontalHeader().setMinimumHeight(45)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)
        self.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.Fixed)
        self.gridLayout_3.addWidget(self.frame_4, 1, 0, 1, 5)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 3, 1)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(350, 40))
        self.lineEdit.setStyleSheet("""
        QLineEdit {
            background-color: rgb(241, 243, 250);
            border-radius: 10px;
        }
        QLineEdit:hover {
            border: 2px solid rgb(187, 150, 224);
        }
        QLineEdit:focus {
            border: 2px solid rgb(85, 170, 255);
        }
        """)
        self.lineEdit.textChanged.connect(self.filter_proxy_model.setFilterRegExp)
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 5)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.pushButton_6.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
            font: 81 30pt "JetBrains Mono Extra Bold";
        }
        QPushButton#pushButton_6:hover {
            background-color: rgb(82, 86, 238);
            border-radius: 3px;
        }
        QPushButton#pushButton_6:pressed {
            background-color: rgb(82, 86, 238);
            border: 3px solid rgbrgb(214, 203, 255);
            border-radius: 3px;
        }
        """)
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(100, 50))
        self.pushButton_5.setStyleSheet("""
        QPushButton {
            font: 25pt "Segoe UI semi-bold";
            color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
            border-radius: 3px;
        }
        QPushButton#pushButton_5:hover {
            background-color: rgb(82, 86, 238);
            border-radius: 3px;
        }
        QPushButton#pushButton_5:pressed {
            background-color: rgb(82, 86, 238);
            border: 3px solid rgbrgb(214, 203, 255);
            border-radius: 3px;
        }
        """)
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 40))
        self.pushButton.setStyleSheet("""
        QPushButton {
			color: rgb(255, 255, 255);
            background-color: rgb(117, 122, 242);
			border-radius: 3px;
            font: 26pt "Segoe UI Semibold";
        }
        QPushButton#pushButton:hover {
            background-color: rgb(82, 86, 238);
            border-radius: 3px;
        }
        QPushButton#pushButton:pressed {
            background-color: rgb(82, 86, 238);
            border: 3px solid rgbrgb(214, 203, 255);
            border-radius: 3px;
        }
        """)
        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 3)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 2, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        # STARTUP EVENTS
        self.initMedTable()
        self.initPatientDropdown()
        #self.loadPatientTable()


## BUTTON EVENTS ##
        # Dropdown Menu
        self.comboBox.currentIndexChanged.connect(self.initPatientTable)
        # Med_lookup BUTTON
        self.pushButton.clicked.connect(self.buttonEvent_1)
        self.pushButton_5.clicked.connect(self.buttonEvent_5)
        self.pushButton_6.clicked.connect(self.buttonEvent_6)

        # Patient_data BUTTON
        self.pushButton_2.clicked.connect(self.buttonEvent_2)
        self.pushButton_3.clicked.connect(self.buttonEvent_3)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        # Med lookup
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        
        # Patient Data
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"CapsulePacker", None))


## Button Functions ##
    # add med
    def buttonEvent_1(self):
        x = self.tableView.currentIndex()
        print(x)
        self.addMedWindow = Ui_AddMedication()
        self.addMedWindow.addEdit(False)
        self.addMedWindow.show()
        self.addMedWindow.confirmed.connect(self.addMedication)

    # add patient
    def buttonEvent_2(self):
        self.addPatientWindow = Ui_AddPatient()
        self.addPatientWindow.submitted.connect(self.addPatient)

    # delete patient
    def buttonEvent_3(self):
        name = self.comboBox.currentText()
        self.deleteWindow = Ui_DeleteWindow()
        text = self.deleteWindow.label.text()
        newText = text + name
        self.deleteWindow.label.setText(newText)
        self.deleteWindow.accepted.connect(self.buttonUpdate_3)
        self.deleteWindow.show()
        
    def buttonUpdate_3(self):
        index = self.comboBox.currentIndex()
        pid_temp = self.pidCache
        pid = pid_temp[index]

        query = "delete from patient where pid={} if exists".format(pid)
        print(query)
        self.executeData(query)
        self.initPatientDropdown()

    # edit patient
    def buttonEvent_5(self):
        self.editMedWindow = Ui_AddMedication()
        self.editMedWindow.addEdit(True)

        row = int(self.tableWidget.currentRow())
        morning = int(self.tableWidget.item(row, 3).text())
        noon = int(self.tableWidget.item(row, 4).text())
        evening = int(self.tableWidget.item(row, 5).text())
        bedtime = int(self.tableWidget.item(row, 6).text())
        print(morning, noon, evening, bedtime)

        self.editMedWindow.spinBox.setValue(morning)
        self.editMedWindow.spinBox_2.setValue(noon)
        self.editMedWindow.spinBox_3.setValue(evening)
        self.editMedWindow.spinBox_4.setValue(bedtime)
        
        self.editMedWindow.show()
        self.editMedWindow.confirmed.connect(self.addMedication)

    # delete med
    def buttonEvent_6(self):
        row = self.tableWidget.currentRow()
        name = self.tableWidget.item(row, 1).text()
        strength = self.tableWidget.item(row, 2).text()
        self.deleteWindow = Ui_DeleteWindow()
        text = self.deleteWindow.label.text()
        newText = text + name + " " + strength
        self.deleteWindow.label.setText(newText)
        self.deleteWindow.accepted.connect(self.buttonUpdate_6)
        self.deleteWindow.show()

    def buttonUpdate_6(self):
        row = self.tableWidget.currentRow()

        if (row >= 0):
            index = self.comboBox.currentIndex()
            pid_temp = self.pidCache
            pid = pid_temp[index]

            query = "delete prescriptions[{}] from patient where pid={}".format(row, pid)
            self.executeData(query)
            self.initPatientTable()
        elif (row < 0):
            pass
        

## Custom Functions ##
    # Initialize Medication Table
    def initMedTable(self):
        query = "select * from medication"
        self.worker = WorkerThread(self.getAllData, query)
        self.worker.finished.connect(self.updateMedTable)
        self.worker.start()

    # Update Medication Table
    def updateMedTable(self, meds):
        print("UPDATE")
        medList = []
        for item in meds:
            medList.append(item)

        self.model = QStandardItemModel(len(medList), 3)
        for row, value in enumerate(medList):
            for column, item in enumerate(value):
                self.model.setItem(row, column, QStandardItem(str(item)))
        
        self.model.setHorizontalHeaderLabels([
            "DIN",
            "Medication",
            "Strength",
        ])
        self.filter_proxy_model.setSourceModel(self.model)
        self.tableView.setModel(self.filter_proxy_model)

    # Initialize patient data
    def initPatientDropdown(self):
        query = "select * from patient"
        self.worker = WorkerThread(self.getAllData, query)
        self.worker.finished.connect(self.updatePatientDropdown)
        self.worker.start()

    def updatePatientDropdown(self, data):
        self.comboBox.clear()
        self.pidCache = []
        for item in data:
            name = "{}, {}".format(item[1], item[2])
            self.pidCache.append(item[0])
            self.comboBox.addItem(name)
        
    def initPatientTable(self):
        self.tableWidget.setRowCount(0)
        index = self.comboBox.currentIndex()
        pid_temp = self.pidCache
        pid = pid_temp[index]

        query = "select prescriptions from patient where pid={}".format(pid)
        self.worker = WorkerThread(self.getSingleData, query)
        self.worker.finished.connect(self.updatePatientTable)
        self.worker.start()

    def updatePatientTable(self, data):
        try:
            for i, item in enumerate(data[0]):
                print(item)
                self.tableWidget.insertRow(i)
                medList = item
                try:
                    meds = re.split(":", item)

                    query = "select name, strength from medication where din={}".format(meds[0])
                    med_info = self.getSingleData(query)
                    
                    self.tableWidget.setItem(i, 0, QTableWidgetItem(str(meds[0])))
                    self.tableWidget.setItem(i, 1, QTableWidgetItem(str(med_info[0])))
                    self.tableWidget.setItem(i, 2, QTableWidgetItem(str(med_info[1])))
                    self.tableWidget.setItem(i, 3, QTableWidgetItem(str(meds[1])))
                    self.tableWidget.setItem(i, 4, QTableWidgetItem(str(meds[2])))
                    self.tableWidget.setItem(i, 5, QTableWidgetItem(str(meds[3])))
                    self.tableWidget.setItem(i, 6, QTableWidgetItem(str(meds[4])))
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            print(e)
            pass

    # Add Selected Medication
    @Slot(bool, str, str, str, str)
    def addMedication(self, isEdit, morning, noon, evening, bedtime):
        print(isEdit)
        if isEdit:
            row = self.tableWidget.currentRow()
            din = self.tableView.model().index(row, 0).data()
            index = self.comboBox.currentIndex()
            pid_temp = self.pidCache
            pid = pid_temp[index]

            medInfo = "{}:{}:{}:{}:{}".format(din, morning, noon, evening, bedtime)

            query = "update patient set prescriptions[{}] = '{}' where pid = {}".format(row, medInfo, pid)
            print(query)
            self.executeData(query)
            self.initPatientTable()
        elif not isEdit:
            row = self.tableView.selectionModel().currentIndex().row()
            din = self.tableView.model().index(row, 0).data()
            index = self.comboBox.currentIndex()
            pid_temp = self.pidCache
            pid = pid_temp[index]

            medInfo = "{}:{}:{}:{}:{}".format(din, morning, noon, evening, bedtime)
            medList = []
            medList.append(medInfo)

            query = "update patient set prescriptions = prescriptions + {} where pid = {}".format(medList, pid)
            print(query)
            self.executeData(query)
            self.initPatientTable()

    # Add Patient
    @Slot(str, str)
    def addPatient(self, fname, lname):
        query = "insert into patient(pid, fname, lname) values (uuid(), '{}', '{}')".format(fname, lname)
        print(query)
        self.executeData(query)
        self.initPatientDropdown()


## DATABASE FUNCTIONS ##

    # Get all data from database
    def getMedTableData(self, query):
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-pharmacydb.zip',
            'use_default_tempdir': True
        }
        auth_provider = PlainTextAuthProvider('maomao853', 'admin')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        session.row_factory = tuple_factory
        session.execute('use pharmacy_db')

        data = session.execute(query)
        x = [i for i in data]
        print(query)
        print(data)
        print(x)
        return(data)

    # Get all data from database
    def getAllData(self, query):
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-pharmacydb.zip',
            'use_default_tempdir': True
        }
        auth_provider = PlainTextAuthProvider('maomao853', 'admin')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        session.row_factory = tuple_factory
        session.execute('use pharmacy_db')

        data = session.execute(query)
        print(query)
        return(data)
    
    # Get one line of data from database
    def getSingleData(self, query):
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-pharmacydb.zip',
            'use_default_tempdir': True
        }
        auth_provider = PlainTextAuthProvider('maomao853', 'admin')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        session.row_factory = tuple_factory
        session.execute('use pharmacy_db')

        data = session.execute(query).one()
        return(data)

    # Execute query from database
    def executeData(self, query):
        cloud_config= {
            'secure_connect_bundle': 'secure-connect-pharmacydb.zip',
            'use_default_tempdir': True
        }
        auth_provider = PlainTextAuthProvider('maomao853', 'admin')
        cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
        session = cluster.connect()
        session.execute('use pharmacy_db')
        session.execute(query)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    sys.exit(app.exec_())
