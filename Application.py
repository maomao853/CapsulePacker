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

import sys
import re
import json

## Add Patient WINDOW ##
class Ui_AddPatient(QWidget):

    submitted = Signal(str, str)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(400, 305)
        self.setMinimumSize(QSize(400, 305))
        self.setMaximumSize(QSize(400, 305))
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(90, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(90, 50))
        self.label.setStyleSheet(u"font: 25 16pt \"Segoe UI Light\";")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(200, 35))
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_2)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(200, 35))
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(90, 50))
        self.label_2.setStyleSheet(u"font: 25 16pt \"Segoe UI Light\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        self.pushButton.setStyleSheet(u"font: 14pt \"Segoe UI Light\";")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 50))
        self.pushButton_2.setStyleSheet(u"font: 14pt \"Segoe UI Light\";")
        self.horizontalLayout.addWidget(self.pushButton_2)

        QWidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)

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
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"First Name...", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name...", None))

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

    confirmed = Signal(str, str, str, str)

    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()

    def setupUi(self):
        self.resize(400, 300)
        self.setMaximumSize(400, 300)
        self.setMinimumSize(400, 300)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 50))
        self.label.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMinimumSize(QSize(0, 50))
        self.spinBox.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.spinBox)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(200, 50))
        self.label_2.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setMinimumSize(QSize(0, 50))
        self.spinBox_2.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.spinBox_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(200, 50))
        self.label_3.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(200, 50))
        self.label_4.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.spinBox_3 = QSpinBox(self.frame)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setMinimumSize(QSize(0, 50))
        self.spinBox_3.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.spinBox_3)

        self.spinBox_4 = QSpinBox(self.frame)
        self.spinBox_4.setObjectName(u"spinBox_4")
        self.spinBox_4.setMinimumSize(QSize(0, 50))
        self.spinBox_4.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.spinBox_4)

        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
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
    def yes(self):
        morning = self.spinBox.text()
        noon = self.spinBox_2.text()
        evening = self.spinBox_3.text()
        bedtime = self.spinBox_4.text()
        self.confirmed.emit(morning, noon, evening, bedtime)
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
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(850, 0))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 40))
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(40, 40))
        self.pushButton_3.setMaximumSize(QSize(40, 40))
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setColumnCount(7)
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
        font: 48pt "Segoe UI";
        border: 4px solid rgb(212, 212, 212);
        border-radius: 20px;
        background-color: rgb(255, 255, 255);
        """)
        self.label.setAlignment(Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(420, 0))
        self.frame_3.setMaximumSize(QSize(420, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        # Medication Lookup
        rows, meds = self.getMeds()
        model = QStandardItemModel(len(meds), 3)
        model.setHorizontalHeaderLabels([
            "DIN",
            "Medication",
            "Strength",
        ])
        for row, value in enumerate(meds):
            for column, item in enumerate(value):
                model.setItem(row, column, QStandardItem(str(item)))
            
        filter_proxy_model = QSortFilterProxyModel()
        filter_proxy_model.setSourceModel(model)
        filter_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        filter_proxy_model.setFilterKeyColumn(1)

        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView.setModel(filter_proxy_model)
        self.gridLayout_3.addWidget(self.tableView, 1, 0, 1, 5)
        self.tableView.setColumnWidth(0, 70)
        self.tableView.setColumnWidth(1, 200)
        self.tableView.setColumnWidth(2, 85)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(400, 40))
        self.lineEdit.textChanged.connect(filter_proxy_model.setFilterRegExp)
        self.gridLayout_3.addWidget(self.lineEdit, 0, 0, 1, 5)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(50, 50))
        self.pushButton_6.setMaximumSize(QSize(50, 50))
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 4, 1, 1)

        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 50))
        self.pushButton_5.setMaximumSize(QSize(50, 50))
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 3, 1, 1)

        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 50))
        self.gridLayout_3.addWidget(self.pushButton, 2, 0, 1, 3)

        self.gridLayout.addWidget(self.frame_3, 0, 0, 2, 1)
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        # STARTUP EVENTS
        self.loadPatientDropdown()
        self.loadPatientTable()


## BUTTON EVENTS ##
        # Dropdown Menu
        self.comboBox.currentIndexChanged.connect(self.loadPatientTable)
        # Med_lookup BUTTON
        self.pushButton.clicked.connect(self.buttonEvent_1)
        #self.pushButton_4.clicked.connect()
        #self.pushButton_5.clicked.connect()
        self.pushButton_6.clicked.connect(self.buttonEvent_6)

        # Patient_data BUTTON
        self.pushButton_2.clicked.connect(self.buttonEvent_2)
        self.pushButton_3.clicked.connect(self.buttonEvent_3)

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        # Med lookup
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search...", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"-", None))
        
        # Patient Data
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Blister Pack", None))


## Button Functions ##
    # add med
    def buttonEvent_1(self):
        self.addMedWindow = Ui_AddMedication()
        self.addMedWindow.show()
        self.addMedWindow.confirmed.connect(self.addMedication)

    # add patient
    def buttonEvent_2(self):
        self.addPatientWindow = Ui_AddPatient()
        self.addPatientWindow.show()
        self.addPatientWindow.submitted.connect(self.addPatient)

    # delete patient
    def buttonEvent_3(self):
        index = self.comboBox.currentIndex()
        pid_temp = self.pidCache
        pid = pid_temp[index]

        query = "delete from patient where pid={} if exists".format(pid)
        print(query)
        self.executeData(query)
        self.loadPatientDropdown()

    # delete med
    def buttonEvent_6(self):
        row = self.tableWidget.currentRow()

        if (row >= 0):
            index = self.comboBox.currentIndex()
            pid_temp = self.pidCache
            pid = pid_temp[index]

            query = "delete prescriptions[{}] from patient where pid={}".format(row, pid)
            self.executeData(query)
            self.loadPatientTable()
        elif (row < 0):
            pass
        

## Custom Functions ##
    # Initialize Medication Lookup
    def getMeds(self):
        query = "select * from medication"
        meds = self.getAllData(query)
       
        counter = 0
        medList = []
        for item in meds:
            medList.append(item)
            counter += 1

        return(counter, medList)

    # Initialize patient data
    def loadPatientDropdown(self):
        self.comboBox.clear()
        self.pidCache = []
        query = "select * from patient"
        data = self.getAllData(query)
        for item in data:
            name = "{}, {}".format(item[1], item[2])
            self.pidCache.append(item[0])
            self.comboBox.addItem(name)

    def loadPatientTable(self):
        self.tableWidget.setRowCount(0)
        index = self.comboBox.currentIndex()
        pid_temp = self.pidCache
        pid = pid_temp[index]

        query = "select prescriptions from patient where pid={}".format(pid)
        data = self.getSingleData(query)
        print(data)
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
    @Slot(str, str, str, str)
    def addMedication(self, morning, noon, evening, bedtime):
        row = self.tableView.selectionModel().currentIndex().row()
        din = self.tableView.model().index(row, 0).data()
        index = self.comboBox.currentIndex()
        pid_temp = self.pidCache
        pid = pid_temp[index]

        medInfo = "{}:{}:{}:{}:{}".format(din, morning, noon, evening, bedtime)
        medList = []
        medList.append(medInfo)

        query = "update patient set prescriptions = prescriptions + {} where pid = {}".format(medList, pid)
        self.executeData(query)
        self.loadPatientTable()

    # Add Patient
    @Slot(str, str)
    def addPatient(self, fname, lname):
        query = "insert into patient(pid, fname, lname) values (uuid(), '{}', '{}')".format(fname, lname)
        print(query)
        self.executeData(query)
        self.loadPatientDropdown()


## DATABASE FUNCTIONS ##
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
