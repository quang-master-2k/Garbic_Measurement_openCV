import sqlite3
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc
from fractions import Fraction

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
        MainWindow.setEnabled(True)
        MainWindow.resize(1600, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 17))
        self.label.setObjectName("label")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(110, 3, 131, 31))
        self.textEdit.setObjectName("textEdit")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(355, 3, 131, 31))
        self.textEdit_2.setObjectName("textEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 101, 17))
        self.label_2.setObjectName("label_2")

        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(600, 3, 131, 31))
        self.textEdit_3.setObjectName("textEdit_3")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 10, 101, 17))
        self.label_3.setObjectName("label_3")

        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(840, 3, 131, 31))
        self.textEdit_5.setObjectName("textEdit_5")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(760, 10, 101, 17))
        self.label_5.setObjectName("label_5")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.label_4.setObjectName("label_4")

        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(130, 50, 571, 31))
        self.textEdit_4.setObjectName("textEdit_4")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 121, 31))
        self.label_6.setObjectName("label_6")

        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(130, 100, 571, 31))
        self.textEdit_6.setObjectName("textEdit_6")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(1000, 10, 101, 17))
        self.label_8.setObjectName("label_8")

        self.textEdit_8 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(1060, 3, 121, 31))
        self.textEdit_8.setObjectName("textEdit_8")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(720, 50, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.open_file_dialog)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(720, 100, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.open_file_dialog_hardImg)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 140, 121, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.add_database)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(1300, 3, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.show_database)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(1200, 3, 89, 25))
        self.pushButton_5.setObjectName("pushButton_5")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 200, 521, 31))
        self.label_7.setObjectName("label_7")

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 250, 1000, 500))
        self.tableView.setObjectName("tableView")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Garment Style"))
        self.label_2.setText(_translate("MainWindow", "Pattern Code"))
        self.label_3.setText(_translate("MainWindow", "Piece Name"))
        self.label_4.setText(_translate("MainWindow", "Dimension Data"))
        self.label_5.setText(_translate("MainWindow", "Tolerance"))
        self.label_6.setText(_translate("MainWindow", "HardImg"))
        self.label_7.setText(_translate("MainWindow", ""))
        self.label_8.setText(_translate("MainWindow", "Corners"))  
        self.pushButton.setText(_translate("MainWindow", "Browse"))
        self.pushButton_2.setText(_translate("MainWindow", "Add Database"))
        self.pushButton_3.setText(_translate("MainWindow", "Show"))
        self.pushButton_4.setText(_translate("MainWindow", "Browse"))
        self.pushButton_5.setText(_translate("MainWindow", "Capture"))

    def open_file_dialog(self):
        file_dialog = QtWidgets.QFileDialog()
        file_path = file_dialog.getOpenFileName(None, "Select File")[0]
        self.textEdit_4.setText(file_path)

    def open_file_dialog_hardImg(self):
        file_dialog_hardImg = QtWidgets.QFileDialog()
        file_path_hardImg = file_dialog_hardImg.getOpenFileName(None, "Select File")[0]
        self.textEdit_6.setText(file_path_hardImg)

    def add_database(self):
        file_path_DimensionData = self.textEdit_4.toPlainText()
        file_path_HardImg = self.textEdit_6.toPlainText()
        text_insert = self.get_specs_info()
        server = 'quangsog-Inspiron-5570'
        database = 'HBI_app'
        username = 'sa'
        password = '123456Qa'
        connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


        if file_path_DimensionData:
            try:
                conn = pyodbc.connect(connection_string)
                wb = pd.read_excel(file_path_DimensionData)
                for index, row in wb.iterrows():
                    size = row['Size']
                    size = int(size)
                    for column_name, value in row.items():
                        if column_name != 'Size': 
                            dimension_name = column_name
                            dimension_value = value
                            text_query_dimension = [text_insert[0], text_insert[1], text_insert[2], int(text_insert[3])]
                            text_query_dimension.append(size)
                            text_query_dimension.append(dimension_name)
                            text_query_dimension.append(dimension_value)
                            sql = '''INSERT INTO DimensionDatabase (Garment_Style, Pattern_Code, Piece_Name, Num_Corners, Size, Dimension_Name, Dimension_Value)
                            VALUES (?,?,?,?,?,?,?)'''

                            conn.execute(sql, text_query_dimension)
                            conn.commit()

                conn.close()
                
                conn_show = sqlite3.connect('databaseShow.db')  # Replace 'database.db' with your desired database name
                wb = pd.read_excel(file_path_DimensionData)
                table_name = text_insert[0]+text_insert[1]+text_insert[2]  # Replace 'my_table' with your desired table name

                wb.to_sql(table_name, conn_show, if_exists='replace', index=False)

                conn_show.commit()
                conn_show.close()

                self.show_database()

                print("Succesful")
            except Exception as e:
                print(e)

        elif file_path_HardImg:
            try:
                conn = pyodbc.connect(connection_string)
                text_query_comparison = text_insert.copy()
                text_query_comparison[3] = int(text_query_comparison[3])
                fraction = Fraction(text_query_comparison[4])
                text_query_comparison[4] = float(fraction)
                text_query_comparison.append(file_path_HardImg)
                sql_Comparison = '''INSERT INTO ComparisonDatabase (Garment_Style, Pattern_Code, Piece_Name, Num_Corners, Tolerance, Hard_patternImg)
                                VALUES (?,?,?,?,?,?)'''   
                conn.execute(sql_Comparison, text_query_comparison)
                conn.commit()
                conn.close()    
            except Exception as e:
                print(e)
        else:
            print("No file selected")
        

    def get_specs_info(self):
        textEdits = [
            self.textEdit,
            self.textEdit_2,
            self.textEdit_3,
            self.textEdit_8,
            self.textEdit_5
        ]

        texts = []
        for textEdit in textEdits:
            text = textEdit.toPlainText()
            texts.append(text)

        return texts

    def show_database(self):
        conn = sqlite3.connect('databaseShow.db')  # Replace 'database.db' with your desired database name
        cursor = conn.cursor()
        text_insert = self.get_specs_info()
        table_name = text_insert[0]+text_insert[1]+text_insert[2]  # Replace 'my_table' with your desired table name
        # Display the data table
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        
        headers = list(df.head(0))
        model = PandasModel(df)
        self.tableView.setModel(model)
        conn.close()
        self.label_7.setText('Data: ' + text_insert[0]+text_insert[1]+text_insert[2])
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        self.label_7.setFont(font)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
