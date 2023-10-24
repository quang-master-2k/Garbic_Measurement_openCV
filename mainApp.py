# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont, QPixmap
from Yolo import YoloModel
from TraditionalCV import TraditionalCV
from CombineModel import CombineModel
from CalculateEdge import CalculateEdgeLength
from secondMethod import secondMethod
from sqlalchemy import create_engine
import pyodbc
import math
from fractions import Fraction
import datetime

### Class create table
class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        QtCore.QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return str(self._data.columns[section])
        return None

class Ui_MainWindow(object):
    ### User interface
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1409, 927)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 42, 101, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 50, 101, 17))
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(320, 42, 101, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 50, 101, 17))
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 40, 101, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 48, 101, 17))
        self.label_4.setObjectName("label_4")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(620, 42, 101, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 50, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.set_start)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(850, 50, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.clicked.connect(self.display_image_measurement)

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 85, 722, 482))
        self.graphicsView.setObjectName("graphicsView")

        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setGeometry(QtCore.QRect(740, 85, 452, 302))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 600, 402, 302))
        self.tableView.setObjectName("tableView")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 1000, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(960, 50, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.end_measurement)

        self.tableView_2 = QtWidgets.QTableView(self.centralwidget)
        self.tableView_2.setGeometry(QtCore.QRect(740, 470, 300, 450))
        self.tableView_2.setObjectName("tableView_2")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(1060, 470, 200, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(420, 620, 200, 17))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(420, 650, 200, 17))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1060, 500, 200, 17))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(1060, 530, 200, 17))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1060, 650, 200, 21))
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1190, 650, 200, 21))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(740, 390, 451, 21))
        fontDes = QtGui.QFont()
        fontDes.setFamily("Ubuntu")
        fontDes.setPointSize(13)
        fontDes.setBold(True)
        fontDes.setWeight(75)
        self.label_13.setFont(fontDes)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(10, 580, 291, 21))
        fontDes = QtGui.QFont()
        fontDes.setFamily("Ubuntu")
        fontDes.setPointSize(13)
        fontDes.setBold(True)
        fontDes.setWeight(75)
        self.label_14.setFont(fontDes)
        self.label_14.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")

        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(740, 440, 300, 21))
        fontDes = QtGui.QFont()
        fontDes.setFamily("Ubuntu")
        fontDes.setPointSize(13)
        fontDes.setBold(True)
        fontDes.setWeight(75)
        self.label_15.setFont(fontDes)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")

        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1060, 560, 200, 17))
        self.label_16.setObjectName("label_16")

        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(1060, 590, 200, 17))
        self.label_17.setObjectName("label_17")

        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1060, 620, 200, 17))
        self.label_18.setObjectName("label_18")


        # self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_4.setGeometry(QtCore.QRect(650, 830, 89, 25))
        # self.pushButton_4.setObjectName("pushButton_4")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1409, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuMeasurement = QtWidgets.QMenu(self.menuBar)
        self.menuMeasurement.setObjectName("menuMeasurement")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionDimension = QtWidgets.QAction(MainWindow)
        self.actionDimension.setObjectName("actionDimension")
        self.actionComparison = QtWidgets.QAction(MainWindow)
        self.actionComparison.setObjectName("actionComparison")
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.menuMeasurement.addAction(self.actionDimension)
        self.menuMeasurement.addAction(self.actionComparison)
        self.menuOptions.addAction(self.actionSetting)
        self.menuBar.addAction(self.menuMeasurement.menuAction())
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.actionDimension.triggered.connect(self.changeDimensionMeasurement)
        self.actionComparison.triggered.connect(self.changeComparisonMeasurement)

        # Connect the action to open the settings dialog
        self.actionSetting.triggered.connect(self.openSettingDialog)
        self.menuMeasurement.setEnabled(False)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    ### Rename labels, buttons, menuBar
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Garment Style"))
        self.label_2.setText(_translate("MainWindow", "Pattern code"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Size"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_2.setText(_translate("MainWindow", "Measure"))
        self.label_5.setText(_translate("MainWindow", "Measurement"))
        self.pushButton_3.setText(_translate("MainWindow", "End"))
        self.label_6.setText(_translate("MainWindow", "Final result report"))
        self.label_7.setText(_translate("MainWindow", "Torelance: 0"))
        self.label_8.setText(_translate("MainWindow", "Cut-part No: 0"))
        self.label_9.setText(_translate("MainWindow", "OK: 0/0 - 0%"))
        self.label_10.setText(_translate("MainWindow", "NG: 0/0 - 0%"))
        self.label_11.setText(_translate("MainWindow", "Final Result:"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Egde Description"))
        self.label_14.setText(_translate("MainWindow", "Measured Table"))
        self.label_15.setText(_translate("MainWindow", "Inspection Result Table"))
        self.label_16.setText(_translate("MainWindow", "Total cut part: "))
        self.label_17.setText(_translate("MainWindow", "Required sample q'ty: "))
        self.label_18.setText(_translate("MainWindow", "Acceptance level: "))
        # self.pushButton_4.setText(_translate("MainWindow", "Export"))
        self.menuMeasurement.setTitle(_translate("MainWindow", "Measurement"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionDimension.setText(_translate("MainWindow", "Dimension"))
        self.actionComparison.setText(_translate("MainWindow", "Comparison"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))

    ### Camera function
    # This is webcam computer camera. If you need to connect to Jetson, you have to modify it
    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(30)  # Update frame every 30 milliMeasurements

    # Show camera on application
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            image = QImage(
                frame_rgb.data, w, h, ch * w, QImage.Format_RGB888
            )
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaled(720, 480)
            self.scene.clear()
            self.scene.addPixmap(pixmap)

    def video_streaming(self):
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.timer = QtCore.QTimer(self.graphicsView)
        self.timer.timeout.connect(self.update_frame)
        self.start_webcam()

    # Taking photo function
    def take_photo(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame


    ### Visualization function
    # Results are taken after image processing
    # imgComparison: Result image of Comparison method
    # error_dis_and point: Result error distance and max distance
    # imgDimension: Result image of Dimension method
    # finalLengthList: Pixel results are measure for each edge
    imgComparison = None
    error_dis_and_point = []
    imgDimension = None
    finalLengthList = []
    def imgprocess(self): 
        self.imgComparison, self.error_dis_and_point, self.imgDimension, self.finalLengthList = self.cam_process()
    # Show image results
    def imgResult_show(self):
        if self.label_5.text() == 'Dimension Method':
            self.scene1 = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.scene1)

            height, width, channel = self.imgDimension.shape
            bytes_per_line = channel * width    
            imageDi = QImage(self.imgDimension.data.tobytes(), width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(imageDi)
            pixmap = pixmap.scaled(720, 480)
            self.scene1.clear()
            self.scene1.addPixmap(pixmap)   
        elif self.label_5.text() == 'Comparison Method':
            self.scene1 = QtWidgets.QGraphicsScene()
            self.graphicsView.setScene(self.scene1)

            height, width, channel = self.imgComparison.shape
            bytes_per_line = channel * width    
            image = QImage(self.imgComparison.data.tobytes(), width, height, bytes_per_line, QImage.Format_RGB888)

            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaled(720, 480)
            self.scene1.clear()
            self.scene1.addPixmap(pixmap)

    # Comparison method
    # dfComparison: detailed result of each measurement
    def Result_comparison_method(self):
        error_list = self.error_dis_and_point
        error_edges = []
        error_dis = []
        max_dis = []
        dfComparison = pd.DataFrame()
        for i in error_list:
            error_edges.append(i[1])
            error_dis.append(i[0][0])
            max_dis.append(i[0][1])
        dfComparison['Edge'] = error_edges
        dfComparison['Error_Dis'] = error_dis
        dfComparison['Max_Dis'] = max_dis
        dfComparison = dfComparison.round(3)

        headers_Mea = list(dfComparison.head(0))
        modelMea = PandasModel(dfComparison)
        self.tableView.setModel(modelMea)

        self.scene3 = QtWidgets.QGraphicsScene()
        pixmap = QPixmap("compa.png")
        pixmap = pixmap.scaled(450, 300)
        self.scene3.clear()
        self.scene3.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene3)

        return dfComparison

    # AQL_count: count Order Number of cut-part is checking
    AQL_count = 1
    OrdNum = []
    ResultAQL = []
    run = 0
    
    # Display final resulf of comparison method and add result database
    def Final_result_comparison(self):
        dfAQL = pd.DataFrame()
        if self.run == 0:
            self.label_8.setText("Cut-part No: " + str(self.AQL_count))
            self.OrdNum.append(self.AQL_count)   

            dfComparison = self.Result_comparison_method()
            current_date = datetime.date.today()
            current_time = datetime.datetime.now().time()
            text = self.get_specs_info()
            server = 'quangsog-Inspiron-5570'
            database = 'HBI_app'
            username = 'sa'
            password = '123456Qa'
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
            conn = pyodbc.connect(connection_string)
            for i in range(len(dfComparison["Edge"])):
                if pd.isna(dfComparison["Error_Dis"][i]):
                    text_query_comparison_result = [current_date, current_time, text[0], text[1], text[2], text[3], None, None, None, str(dfComparison["Edge"][i]), None, dfComparison['Max_Dis'][i]]
                else:
                    text_query_comparison_result = [current_date, current_time, text[0], text[1], text[2], text[3], None, None, None, str(dfComparison["Edge"][i]), dfComparison["Error_Dis"][i], dfComparison['Max_Dis'][i]]    
                sql = '''INSERT INTO MeasuredResult (MeasureDate, MeasureTime ,Garment_Style, Pattern_Code, Piece_Name, Size, Dimension_Name, Dimension_Value, Dimension_Result, Comparison_Edge, Error_Distance, Max_Distance)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''

                conn.execute(sql, text_query_comparison_result)
            conn.commit()
            conn.close()

            for i in range(len(dfComparison['Error_Dis'])):
                if dfComparison["Error_Dis"][i] != None:
                    self.ResultAQL.append('NG')
                    break
                else:
                    if i == (len(dfComparison["Error_Dis"])-1):
                        self.ResultAQL.append('OK')

            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL

            headers = list(dfAQL.head(0))
            modelAQL = PandasModel(dfAQL)
            self.tableView_2.setModel(modelAQL)
            self.AQL_count += 1
        else:
            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL
            return dfAQL
        
    
    # Dimension method
    # df: detailed results of dimension 
    def Result_dimension_method(self):
        text_insert = self.get_specs_info()
        server = 'quangsog-Inspiron-5570'
        database = 'HBI_app'
        username = 'sa'
        password = '123456Qa'
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        engine = create_engine(f'mssql+pyodbc:///?odbc_connect={connection_string}')

        query = f"SELECT Dimension_Name, Dimension_Value FROM DimensionDatabase WHERE Garment_Style = '{text_insert[0]}' AND Pattern_Code = '{text_insert[1]}' AND Piece_Name = '{text_insert[2]}' AND Size = {text_insert[3]}"
        df = pd.read_sql(query, engine)
        new_column_names = {'Dimension_Name': 'Name', 'Dimension_Value': 'Specs LL'}
        df.rename(columns=new_column_names, inplace=True)

        # Upper limit and lower limit
        # Need to modify based on result of dimension
        df['Specs UL'] = df["Specs LL"] + 1/8
        df["Specs LL"] = df['Specs LL'] - 1/8
        listLength = self.finalLengthList
        df["Dimension"] = [listLength[6], listLength[0], listLength[1], listLength[2], listLength[3], listLength[4], listLength[5], listLength[7]]
        df["Dimension"] = df["Dimension"] / (35*2.54)
        df = df.round(3)

        headers = list(df.head(0))
        model = PandasModel(df)
        self.tableView.setModel(model)
        engine.dispose()

        self.scene3 = QtWidgets.QGraphicsScene()
        pixmap = QPixmap("dimen.png")
        pixmap = pixmap.scaled(450, 300)
        self.scene3.clear()
        self.scene3.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene3)

        return df

    # Display final resulf of dimension method and add result database
    def Final_result_dimension(self):
        dfAQL = pd.DataFrame()
        if self.run == 0:
            self.label_8.setText("Cut-part No: " + str(self.AQL_count))

            self.OrdNum.append(self.AQL_count)      

            df = self.Result_dimension_method()
            current_date = datetime.date.today()
            current_time = datetime.datetime.now().time()
            text = self.get_specs_info()
            server = 'quangsog-Inspiron-5570'
            database = 'HBI_app'
            username = 'sa'
            password = '123456Qa'
            connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
            conn = pyodbc.connect(connection_string)
            for i in range(len(df["Dimension"])):
                if df["Dimension"][i] > df["Specs UL"][i] or df["Dimension"][i] < df["Specs LL"][i]:
                    text_query_dimension_result = [current_date, current_time, text[0], text[1], text[2], text[3], df['Name'][i], df["Dimension"][i], 'NG', None, None, None]    
                else:
                    text_query_dimension_result = [current_date, current_time, text[0], text[1], text[2], text[3], df['Name'][i], df["Dimension"][i], "OK", None, None, None]
                sql = '''INSERT INTO MeasuredResult (MeasureDate, MeasureTime ,Garment_Style, Pattern_Code, Piece_Name, Size, Dimension_Name, Dimension_Value, Dimension_Result, Comparison_Edge, Error_Distance, Max_Distance)
                            VALUES (?,?,?,?,?,?,?,?,?,?,?,?)'''
                print(text_query_dimension_result)
                print(conn.execute(sql, text_query_dimension_result))
            conn.commit()
            conn.close()

            for i in range(len(df["Dimension"])):
                if df["Dimension"][i] > df["Specs UL"][i] or df["Dimension"][i] < df["Specs LL"][i]:
                    self.ResultAQL.append('NG')
                    break
                else:
                    if i == (len(df["Dimension"])-1):
                        self.ResultAQL.append('OK')

            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL

            headers = list(dfAQL.head(0))
            modelAQL = PandasModel(dfAQL)
            self.tableView_2.setModel(modelAQL)
            self.AQL_count += 1
        else:
            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL
            return dfAQL

    # Display all image and table
    def display_image_measurement(self):
        self.imgprocess()
        self.imgResult_show()
        if self.label_5.text() == "Dimension Method":
            self.Final_result_dimension()
        elif self.label_5.text() == "Comparison Method":
            self.Final_result_comparison()

    # For choose both methods in setting, this function change to Dimension when choose Dimension
    def changeDimensionMeasurement(self):
        if self.AQL_count == 1:
            self.label_5.setText("Dimension Method")
            self.actionDimension.setIcon(QtGui.QIcon("mark.png"))  # Replace with the path to your black mark icon
            self.actionComparison.setIcon(QtGui.QIcon())  # Clear the icon from the "Measurement" action
        else:
            self.label_5.setText("Dimension Method")
            self.actionDimension.setIcon(QtGui.QIcon("mark.png"))  # Replace with the path to your black mark icon
            self.actionComparison.setIcon(QtGui.QIcon())  # Clear the icon from the "Measurement" action
            self.imgResult_show()
            self.Result_dimension_method()
            self.run = 1
            dfAQL = self.Final_result_dimension()
            headers = list(dfAQL.head(0))
            modelAQL = PandasModel(dfAQL)
            self.tableView_2.setModel(modelAQL)
            self.run = 0
    ### For choose both methods in setting, this function change to Comparison when choose Comparison
    def changeComparisonMeasurement(self):
        if self.AQL_count == 1:
            self.label_5.setText("Comparison Method")
            self.actionComparison.setIcon(QtGui.QIcon("mark.png"))  # Replace with the path to your black mark icon
            self.actionDimension.setIcon(QtGui.QIcon())  # Clear the icon from the "Dimension" action
        else:
            self.label_5.setText("Comparison Method")  
            self.actionComparison.setIcon(QtGui.QIcon("mark.png"))  # Replace with the path to your black mark icon
            self.actionDimension.setIcon(QtGui.QIcon())  # Clear the icon from the "Dimension" action
            self.imgResult_show()
            self.Result_comparison_method()
            self.run = 1
            dfAQL = self.Final_result_comparison()
            headers = list(dfAQL.head(0))
            modelAQL = PandasModel(dfAQL)
            self.tableView_2.setModel(modelAQL)
            self.run = 0
    
    ### Start function
    # Setup all variables to start a measurement process
    def set_start(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_4.setText("")
        self.tableView.setModel(None)
        self.tableView_2.setModel(None)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
        self.graphicsView_2.setScene(None)
        self.timer = QtCore.QTimer(self.graphicsView)
        self.timer.timeout.connect(self.update_frame)
        self.start_webcam()
        self.AQL_count = 1
        self.OrdNum = []
        self.ResultAQL = []
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_3.setEnabled(True)
        self.run = 0
        self.countAccepted = 0
        self.label_7.setText("Tolerance: 0")
        self.label_8.setText("Cut-part No: 0")
        self.label_9.setText("Accepted: 0/0 - 0%")
        self.label_10.setText("Not Accepted: 0/0 - 0%")
        self.label_11.setText("Final Result: ")
        self.label_12.setText("")
        self.label_16.setText('Total cut part: ')
        self.label_17.setText("Required sample q'ty: ")
        self.label_18.setText("Acceptance level: ")


    ### Camera processing
    # Hard-pattern need to modify to get from database
    def hardpattern_points_process(self):
        image_path_hard = 'hardpart1.jpg'
        input_image_hard = cv2.imread(image_path_hard)
        Yolo = YoloModel()
        Yolo.process(input_image_hard)
        yolo_corners = Yolo.keypoints_yolo

        TradCV = TraditionalCV(thresholdType = cv2.THRESH_BINARY, numCorners = 6, positionThatHaveTwoCorners=[1,4])
        TradCV.process(input_image_hard)
        cv_corners, mask = TradCV.finalCorner, TradCV.maskAccurate

        ### Thickness reflect tolerance
        text_insert = self.get_specs_info()
        server = 'quangsog-Inspiron-5570'
        database = 'HBI_app'
        username = 'sa'
        password = '123456Qa'
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        sql_thickness = "SELECT Tolerance FROM ComparisonDatabase WHERE Garment_Style = ? AND Pattern_Code = ? AND Piece_Name = ?"
        text_query_thickness = [text_insert[0], text_insert[1], text_insert[2]]
        tolerance = conn.execute(sql_thickness, text_query_thickness).fetchone()
        conn.commit()
        conn.close()
        ### Tor (inches) * 2.54 * pixel/cm * 2 = thickness
        thickness = tolerance[0]* 2.54 * 35 * 2
        thickness = math.ceil(thickness)
        label7 = Fraction(float(tolerance[0])).limit_denominator()
        self.label_7.setText("Tolerance: " + str(label7))
        MeasurementMethod_hardP = secondMethod(mask, TradCV.cnt, thickness)    
        mask_tor = MeasurementMethod_hardP.drawTorContours()
        white_tor_pixels_cor = MeasurementMethod_hardP.getTorleranceArea(mask_tor)

        Combine = CombineModel(yolo_corners, cv_corners, TradCV.threshold, mask_tor)
        Combine.process(num_corners = 6, mode = 'A')
        roi_hardP, rotation_matrix, transposed_matrix, center_point_hardP = Combine.cutting_image_2ndMethod()

        Edge = CalculateEdgeLength(mask, Combine.combineCorners, TradCV.threshold)
        Edge.process()
        edges_hardP = Edge.edgePointsList
        edges_hardP_cor_newlist = []
        edge_hardP_cor_newlist = []
        for edge in edges_hardP:
            for cor in edge[0]:
                rotated_pixel_cor = np.dot(rotation_matrix, np.array([int(cor[0]), int(cor[1]), 1])).tolist()
                transposed_pixel = [int(rotated_pixel_cor[0] - transposed_matrix[0]), int(rotated_pixel_cor[1] - transposed_matrix[1])]
                edge_hardP_cor_newlist.append(transposed_pixel)
            edges_hardP_cor_newlist.append([edge_hardP_cor_newlist, edge[1]])

        white_tor_cor_newlist = []
        for pixel in white_tor_pixels_cor:
            rotated_pixel = np.dot(rotation_matrix, np.array([int(pixel[0][0]), int(pixel[0][1]), 1])).tolist()
            transposed_pixel = [int(rotated_pixel[0] - transposed_matrix[0]), int(rotated_pixel[1] - transposed_matrix[1])]
            white_tor_cor_newlist.append(transposed_pixel)

        return roi_hardP, white_tor_cor_newlist, center_point_hardP, edges_hardP_cor_newlist

    # When you run to check app you can use Image
    # When you run with Jetson Nano change to received frame from camera
    def cutpart_points_process(self):
        # Modify to take frame from Jetson camera
        image_path_cut = 'image_2.jpg'
        input_image_cut = cv2.imread(image_path_cut)

        Yolo = YoloModel()
        Yolo.process(input_image_cut)
        yolo_corners = Yolo.keypoints_yolo

        TradCV = TraditionalCV(thresholdType = cv2.THRESH_BINARY, numCorners = 6, positionThatHaveTwoCorners=[1,4])
        TradCV.process(input_image_cut)
        cv_corners, mask = TradCV.finalCorner, TradCV.maskAccurate

        Combine = CombineModel(yolo_corners, cv_corners, TradCV.threshold, mask)
        Combine.process(num_corners = 6, mode = 'A')
        imgDimension = Combine.imageWithMode
        roi_cut, rotation_matrix, transposed_matrix, center_point_cut = Combine.cutting_image_2ndMethod()

        Edge = CalculateEdgeLength(mask, Combine.combineCorners, TradCV.threshold)
        Edge.process()
        finalLengthList = Edge.finalLengthList
        edges = Edge.edgePointsList

        cnts_cor_newlist = []
        for edge in edges:
            edge_cor_newlist = []
            for pixel in edge[0]:
                rotated_pixel = np.dot(rotation_matrix, np.array([int(pixel[0]), int(pixel[1]), 1])).tolist()
                transposed_pixel = [int(rotated_pixel[0] - transposed_matrix[0]), int(rotated_pixel[1] - transposed_matrix[1])]
                edge_cor_newlist.append(transposed_pixel)
            cnts_cor_newlist.append([edge_cor_newlist, edge[1]])
        return cnts_cor_newlist, center_point_cut, imgDimension, finalLengthList

    # Final function process to get result
    def cam_process(self):
        # Result of hardpattern and cutpart
        roi_hardP, white_tor_cor_newlist, center_point_hardP, edges_hardP = self.hardpattern_points_process()
        cnts_cor_newlist, center_point_cut, imgDimension, finalLengthList = self.cutpart_points_process()
        
        # Error edge visualization
        for edge in cnts_cor_newlist:
            for cor in edge[0]:
                cor[0] = cor[0] + center_point_hardP[0] - center_point_cut[0]
                cor[1] = cor[1] + center_point_hardP[1] - center_point_cut[1]
        error_edges = []
        for i in cnts_cor_newlist:
            error_points = []
            for j in i[0]:
                if j in white_tor_cor_newlist:
                    cv2.circle(roi_hardP, j, 2, (50, 100, 255), -1)
                else:
                    cv2.circle(roi_hardP, j, 2, (255, 0, 0), -1)
                    error_points.append(j)
            error_edges.append([error_points, i[1]])

        # Error distance
        error_dis_and_point = []
        for i in range(len(error_edges)):
            if len(error_edges[i][0]) != 0:
                sort_error_edge = []
                for point in error_edges[i][0]:
                    min_dis = 1000000
                    for cor in edges_hardP[i][0]:
                        distance = ((point[0] - cor[0])**2 + (point[1] - cor[1])**2)**(1/2)
                        if distance < min_dis:
                            min_dis = distance
                    sort_error_edge.append([min_dis])
                sort_error_edge = sorted(sort_error_edge, key=lambda x:x[0], reverse=True)
                error_dis_and_point.append([sort_error_edge[0], i])
            else:
                error_dis_and_point.append([[None], i])

        # Max distance of all edge
        for i in range(len(cnts_cor_newlist)):
            sort_cal_edge = []
            for point in cnts_cor_newlist[i][0]:
                min_dis = 1000000
                for cor in edges_hardP[i][0]:
                    distance_cal = ((point[0] - cor[0])**2 + (point[1] - cor[1])**2)**(1/2)
                    if distance_cal < min_dis:
                        min_dis = distance_cal
                sort_cal_edge.append(min_dis)
            sort_cal_edge = sorted(sort_cal_edge, reverse=True)
            error_dis_and_point[i][0].append(sort_cal_edge[0])
        
        return roi_hardP, error_dis_and_point, imgDimension, finalLengthList

    ### End function
    countAccepted = 0
    def end_measurement(self):
        self.cap.release()
        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        
        self.run = 1 
        dfEnd = self.Final_result_dimension()
        for i in range(len(dfEnd['Result'])):
            if dfEnd['Result'][i] == 'OK':
                self.countAccepted += 1

        P_pass = self.countAccepted / (self.AQL_count-1)
        P_pass = round((P_pass)*100, 2)
        P_reject = round(100 - P_pass, 2)
        self.label_9.setText('OK: ' + str(self.countAccepted) + '/' + str(self.AQL_count - 1) + ' - ' + str(P_pass) + '%')
        self.label_10.setText('NG: ' + str(self.AQL_count- 1 - self.countAccepted) + '/' + str(self.AQL_count - 1) + ' - ' + str(P_reject) + '%')

        current_date = datetime.date.today()
        current_time = datetime.datetime.now().time()
        text = self.get_specs_info()
        server = 'quangsog-Inspiron-5570'
        database = 'HBI_app'
        username = 'sa'
        password = '123456Qa'
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
        conn = pyodbc.connect(connection_string)
        
        #P_Pass is AQL standard - need modify to follow AQL standard
        if (P_pass < 95):
            fontResult = QtGui.QFont()
            fontResult.setFamily("Ubuntu")
            fontResult.setPointSize(15)
            fontResult.setBold(True)
            fontResult.setWeight(75)    
            self.label_12.setFont(fontResult)
            self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.label_12.setAlignment(QtCore.Qt.AlignLeft)
            self.label_12.setStyleSheet('color: red')
            self.label_12.setText('Reject')
            text_final_query = [current_date, current_time, text[0], text[1], text[2], text[3], (self.AQL_count -1), self.countAccepted, (self.AQL_count -1 - self.countAccepted), "Reject"]
        else:
            fontResult = QtGui.QFont()
            fontResult.setFamily("Ubuntu")
            fontResult.setPointSize(15)
            fontResult.setBold(True)
            fontResult.setWeight(75)    
            self.label_12.setFont(fontResult)
            self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
            self.label_12.setAlignment(QtCore.Qt.AlignLeft)
            self.label_12.setStyleSheet('color: green')
            self.label_12.setText('Pass')
            text_final_query = [current_date, current_time, text[0], text[1], text[2], text[3], (self.AQL_count -1), self.countAccepted, (self.AQL_count -1 - self.countAccepted), "Pass"]

        sql = '''INSERT INTO FinalResult (MeasureDate, MeasureTime ,Garment_Style, Pattern_Code, Piece_Name, Size, Number_checking, Accepted, Not_Accepted, FinalResult)
            VALUES (?,?,?,?,?,?,?,?,?,?)'''
        conn.execute(sql, text_final_query)
        conn.commit()
        conn.close()

        self.label_16.setText('Total cut part: 150')
        self.label_17.setText("Required sample q'ty: 13")
        self.label_18.setText("Acceptance level: 0")
    
    ### Additional function
    def openSettingDialog(self):
        dialog = SettingDialog()
        result = dialog.exec_()
        if result == QtWidgets.QDialog.Accepted:
            # Handle settings here
            selected_option = dialog.get_selected_option()
            if selected_option == "Dimension Method":
                self.label_5.setText("Dimension Method")
                self.menuMeasurement.setEnabled(False)
                self.pushButton.setEnabled(True)
            elif selected_option == "Comparison Method":
                self.label_5.setText("Comparison Method")
                self.pushButton.setEnabled(True)
                self.menuMeasurement.setEnabled(False)
            elif selected_option == "Dimension Method & Comparison Method":
                self.label_5.setText("Dimension Method & Comparison Method")
                self.menuMeasurement.setEnabled(True)
                self.pushButton.setEnabled(True)
    
    #Get input information
    def get_specs_info(self):
        textEdits = [
            self.textEdit,
            self.textEdit_2,
            self.textEdit_3,
            self.textEdit_4
        ]

        texts = []
        for textEdit in textEdits:
            text = textEdit.toPlainText()
            texts.append(text)
   
        return texts

### Options - Setting dialog to choose what method user want to measure
class SettingDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 300, 200)

        self.okButton = QtWidgets.QPushButton("OK", self)
        self.cancelButton = QtWidgets.QPushButton("Cancel", self)
        self.radioGroupBox = QtWidgets.QGroupBox("Options:", self)

        self.dimensionRadio = QtWidgets.QRadioButton("Dimension Method", self)
        self.comparisonRadio = QtWidgets.QRadioButton("Comparison Method", self)
        self.dim_comp_radio = QtWidgets.QRadioButton("Dimension Method & Comparison Method", self)

        self.radio_layout = QtWidgets.QVBoxLayout()
        self.radio_layout.addWidget(self.dimensionRadio)
        self.radio_layout.addWidget(self.comparisonRadio)
        self.radio_layout.addWidget(self.dim_comp_radio)
        self.radioGroupBox.setLayout(self.radio_layout)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.radioGroupBox)
        layout.addWidget(self.okButton)
        layout.addWidget(self.cancelButton)
        self.setLayout(layout)

        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)

    def get_selected_option(self):
        if self.dimensionRadio.isChecked():
            return "Dimension Method"
        elif self.comparisonRadio.isChecked():
            return "Comparison Method"
        elif self.dim_comp_radio.isChecked():
            return "Dimension Method & Comparison Method"
        return ""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
