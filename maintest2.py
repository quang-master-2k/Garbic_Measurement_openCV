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
        self.graphicsView_2.setGeometry(QtCore.QRect(740, 110, 451, 301))
        self.graphicsView_2.setObjectName("graphicsView_2")

        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(740, 470, 451, 421))
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
        self.tableView_2.setGeometry(QtCore.QRect(10, 600, 291, 281))
        self.tableView_2.setObjectName("tableView_2")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 580, 191, 21))
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
        self.label_7.setGeometry(QtCore.QRect(1210, 470, 200, 17))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1210, 500, 200, 17))
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(320, 620, 200, 17))
        self.label_9.setObjectName("label_9")

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(320, 650, 200, 17))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 680, 200, 21))
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAlignment(QtCore.Qt.AlignLeft)
        self.label_11.setObjectName("label_11")

        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(445, 680, 200, 21))
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(740, 85, 451, 21))
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
        self.label_14.setGeometry(QtCore.QRect(740, 440, 451, 21))
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
        self.label_15.setGeometry(QtCore.QRect(10, 580, 291, 21))
        fontDes = QtGui.QFont()
        fontDes.setFamily("Ubuntu")
        fontDes.setPointSize(13)
        fontDes.setBold(True)
        fontDes.setWeight(75)
        self.label_15.setFont(fontDes)
        self.label_15.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")

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
        self.label_8.setText(_translate("MainWindow", "Checking: 0"))
        self.label_9.setText(_translate("MainWindow", "OK: 0/0 - 0%"))
        self.label_10.setText(_translate("MainWindow", "NG: 0/0 - 0%"))
        self.label_11.setText(_translate("MainWindow", "Final Result:"))
        self.label_12.setText(_translate("MainWindow", ""))
        self.label_13.setText(_translate("MainWindow", "Egde Description"))
        self.label_14.setText(_translate("MainWindow", "Measured Table"))
        self.label_15.setText(_translate("MainWindow", "Checking Result Table"))
        # self.pushButton_4.setText(_translate("MainWindow", "Export"))
        self.menuMeasurement.setTitle(_translate("MainWindow", "Measurement"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionDimension.setText(_translate("MainWindow", "Dimension"))
        self.actionComparison.setText(_translate("MainWindow", "Comparison"))
        self.actionSetting.setText(_translate("MainWindow", "Setting"))

    ### Camera function
    def start_webcam(self):
        self.cap = cv2.VideoCapture(0)
        self.timer.start(0)  # Update frame every 30 milliMeasurements

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

    def take_photo(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame

    ### Visualization function
    imgComparison = None
    error_dis_and_point = []
    imgDimension = None
    finalLengthList = []
    def imgprocess(self): 
        self.imgComparison, self.error_dis_and_point, self.imgDimension, self.finalLengthList = self.cam_process()

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

    #Comparison method
    def Result_comparison_method(self):
        error_list = self.error_dis_and_point
        error_edges = []
        error_dis = []
        max_dis = []
        dfMea = pd.DataFrame()
        for i in error_list:
            error_edges.append(i[1])
            error_dis.append(i[0][0])
            max_dis.append(i[0][1])
        dfMea['Edge'] = error_edges
        dfMea['Error_Dis'] = error_dis
        dfMea['Max_Dis'] = max_dis
        dfMea = dfMea.round(3)

        headers_Mea = list(dfMea.head(0))
        modelMea = PandasModel(dfMea)
        self.tableView.setModel(modelMea)

        self.scene3 = QtWidgets.QGraphicsScene()
        pixmap = QPixmap("compa.png")
        pixmap = pixmap.scaled(450, 300)
        self.scene3.clear()
        self.scene3.addPixmap(pixmap)
        self.graphicsView_2.setScene(self.scene3)

        return dfMea

    AQL_count = 1
    OrdNum = []
    ResultAQL = []
    run = 0
    
    def Final_result_comparison(self):
        dfAQL = pd.DataFrame()
        if self.run == 0:
            self.label_8.setText("Checking: " + str(self.AQL_count))

            self.OrdNum.append(self.AQL_count)       
            text = self.get_specs_info()
            dfMea = self.Result_comparison_method()
            for i in range(len(dfMea['Error_Dis'])):
                if dfMea["Error_Dis"][i] > 0:
                    self.ResultAQL.append('NG')
                    break
                else:
                    if i == len(dfMea["Error_Dis"]):
                        self.ResultAQL.append('OK')

            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL

            headers = list(dfAQL.head(0))
            modelAQL = PandasModel(dfAQL)
            self.tableView_2.setModel(modelAQL)
            self.AQL_count += 1

            if text[1] == "BB":
                self.label_7.setText("Tolerance: 1/4")
            else:
                self.label_7.setText("Tolerance: 1/8")
        else:
            dfAQL['Cut-part No'] = self.OrdNum
            dfAQL['Result'] = self.ResultAQL
            return dfAQL
        
    
    #Dimension method
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

        return df
    
    def Final_result_dimension(self):
        dfAQL = pd.DataFrame()
        if self.run == 0:
            self.label_8.setText("Checking: " + str(self.AQL_count))

            self.OrdNum.append(self.AQL_count)       
            df = self.Result_dimension_method()
            for i in range(len(df["Dimension"])):
                if df["Dimension"][i] > df["Specs UL"][i] or df["Dimension"][i] < df["Specs LL"][i]:
                    self.ResultAQL.append('NG')
                    break
                else:
                    if i == len(df["Dimension"]):
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


    def display_image_measurement(self):
        self.imgprocess()
        self.imgResult_show()
        if self.label_5.text() == "Dimension Method":
            self.Result_dimension_method()
            self.Final_result_dimension()
        elif self.label_5.text() == "Comparison Method":
            # self.Result_comparison_method()
            self.Final_result_comparison()

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
    def set_start(self):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.textEdit_3.setText("")
        self.textEdit_4.setText("")
        self.tableView.setModel(None)
        self.tableView_2.setModel(None)
        self.scene = QtWidgets.QGraphicsScene()
        self.graphicsView.setScene(self.scene)
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
        self.label_7.setText("Tolerance: 0")
        self.label_8.setText("Checking: 0")
        self.label_9.setText("Accepted: 0/0 - 0%")
        self.label_10.setText("Not Accepted: 0/0 - 0%")
        self.label_11.setText("Final Result: ")
        self.label_12.setText("")


    ### Camera processing
    def hardpattern_points_process(self):
        image_path_hard = 'hardpart1.jpg'
        input_image_hard = cv2.imread(image_path_hard)
        Yolo = YoloModel()
        Yolo.process(input_image_hard)
        yolo_corners = Yolo.keypoints_yolo

        TradCV = TraditionalCV(thresholdType = cv2.THRESH_BINARY, numCorners = 6, positionThatHaveTwoCorners=[1,4])
        TradCV.process(input_image_hard)
        cv_corners, mask = TradCV.finalCorner, TradCV.maskAccurate

        ### Thickness is 23. Modify it to suitable with torelance
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
        print(tolerance[0])

        MeasurementMethod_hardP = secondMethod(mask, TradCV.cnt, 23)
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

    def cutpart_points_process(self):
        ### Modify to frame from camera
        image_path_cut = 'image_11.jpg'
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

    def cam_process(self):
        roi_hardP, white_tor_cor_newlist, center_point_hardP, edges_hardP = self.hardpattern_points_process()
        cnts_cor_newlist, center_point_cut, imgDimension, finalLengthList = self.cutpart_points_process()
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
        self.label_9.setText('OK: ' + str(self.countAccepted) + '/' + str(self.AQL_count - 1) + ' - ' + str(P_pass*100) + '%')
        self.label_10.setText('NG: ' + str(self.AQL_count- 1 - self.countAccepted) + '/' + str(self.AQL_count - 1) + ' - ' + str((1-P_pass)*100) + '%')
        if (P_pass < 0.95):
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
