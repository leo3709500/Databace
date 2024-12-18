# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DBMS\ui\manage_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from img_set.img_set import Img_setting

class Ui_MainWindow(Img_setting):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 612)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
       # 設定表格視圖
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 180, 751, 390))
        self.tableView.setObjectName("tableView")
        self.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        

        self.columns = [
            "type", "license_plate", "car_year", "car_month", "car_date", 
            "inspect_no", "user_ssn", "vehicle_license", "violation_no", 
            "status", "fine", "violate_year", "violate_month", "violate_date", 
            "violation_no", "violation_type", "status", "inspect_no", 
            "next__inspect_year", "next_inspect_month", "next_inspect_date", "inspect_fee", "inspect_type"
        ]
        # 設定模型
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(self.columns)
        self.tableView.setModel(self.model)
        
        # 添加圓角樣式
        self.tableView.setStyleSheet("""
            QTableView {
                border: 5px solid #444444;
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
            QTableView::item {
                background-color: #3C3C3C;
                color: #FFFFFF;
            }
            QTableView::item:selected {
                background-color: #0080FF;
                color: #FFFFFF;
            }
            QHeaderView::section {
                background-color: #444444;
                color: #FFFFFF;
            }
            QTableView::indicator {
                background-color: #444444;
                color: #FFFFFF;
            }
            QScrollBar:vertical {
                border: none;
                background: #444444; /* 滾動條背景顏色 */
                width: 10px; /* 滾動條寬度 */
                margin: 22px 0 22px 0; /* 上下邊距 */
            }
            QScrollBar::handle:vertical {
                background: #ADADAD; /* 滾動條滑塊顏色 */
                min-height: 20px; /* 滑塊最小高度 */
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none; /* 隱藏上下箭頭 */
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none; /* 隱藏滾動條的頁面 */
            }
            QScrollBar:horizontal {
                border: none;
                background: #444444; /* 滾動條背景顏色 */
                height: 10px; /* 滾動條高度 */
                margin: 0 22px 0 22px; /* 左右邊距 */
            }
            QScrollBar::handle:horizontal {
                background: #ADADAD; /* 滾動條滑塊顏色 */
                min-width: 20px; /* 滑塊最小寬度 */
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                background: none; /* 隱藏左右箭頭 */
            }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
                background: none; /* 隱藏滾動條的頁面 */
            }
            Q
        """)
        
        # 設定按鈕的佈局小工具
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 751, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # 設定水平佈局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 設定各個按鈕
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout.addWidget(self.pushButton_7)
        
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout.addWidget(self.pushButton_8)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        
        # 設定網格佈局小工具
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(120, 90, 551, 41))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        # 設定網格佈局
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 設定下拉選單和標籤
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)
        
        # 美化下拉選單
        self.comboBox.setStyleSheet("""
            QComboBox {
                background-color: #444444;
                color: #ffffff;
                border: 2px solid #444444;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        self.comboBox_3 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 0, 3, 1, 1)
        
        # 美化下拉選單
        self.comboBox_3.setStyleSheet("""
            QComboBox {
                background-color: #444444;
                color: #ffffff;
                border: 2px solid #444444;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Microsoft JhengHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)
        
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Microsoft JhengHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        
        self.comboBox_2 = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 0, 5, 1, 1)
        
        # 美化下拉選單
        self.comboBox_2.setStyleSheet("""
            QComboBox {
                background-color: #444444;
                color: #ffffff;
                border: 2px solid #444444;
                border-radius: 5px;
                padding: 5px;
            }
        """)
        
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Microsoft JhengHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 設定標題標籤
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 260, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setFamily("Microsoft JhengHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-weight: bold;
                font-size: 40px;
            }
        """)
        
        # 設定主視窗的中央小工具
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設定選單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設定狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        # 隱藏視窗邊框
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        # 添加 Mac OS 風格的紅橘綠按鈕
        self.button_close = QtWidgets.QPushButton(self.centralwidget)
        self.button_close.setGeometry(QtCore.QRect(10, 10, 15, 15))
        self.button_close.setStyleSheet("""
            QPushButton {
                background-color: #FF605C;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #FF1F1F;
            }
        """)
        self.button_minimize = QtWidgets.QPushButton(self.centralwidget)
        self.button_minimize.setGeometry(QtCore.QRect(30, 10, 15, 15))
        self.button_minimize.setStyleSheet("""
            QPushButton {
                background-color: #FFBD44;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #FFAA00;
            }
        """)
        self.button_maximize = QtWidgets.QPushButton(self.centralwidget)
        self.button_maximize.setGeometry(QtCore.QRect(50, 10, 15, 15))
        self.button_maximize.setStyleSheet("""
            QPushButton {
                background-color: #00CA4E;
                border: none;
                border-radius: 7px;
            }
            QPushButton:hover {
                background-color: #00B324;
            }
        """)

        # 連接按鈕的點擊事件
        self.button_close.clicked.connect(MainWindow.close)
        self.button_minimize.clicked.connect(MainWindow.showMinimized)
        self.button_maximize.clicked.connect(MainWindow.showMaximized)

        # 設定視窗圓角和背景半透明
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget.setStyleSheet(f"""
            QWidget#centralwidget {{
                background-image: url({self.background_2});
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 15px;
                opacity: 0.25;
            }}
        """)

        # 設定整體深色主題和圓角按鈕的樣式
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2b2b2b;
            }
            QLabel {
                color: #ffffff;
            }
            QPushButton {
                background-color: #444444;
                color: #ffffff;
                border: 3px solid #444444;
                border-radius: 11px;
                padding: 1px;
                font-family: "Microsoft JhengHei";
            }
            QPushButton:hover {
                background-color: #0080FF;
            }
        """)

        # 重新翻譯UI文字
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設定UI文字的翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_6.setText(_translate("MainWindow", "刪除"))
        self.pushButton_3.setText(_translate("MainWindow", "查詢"))
        self.pushButton_4.setText(_translate("MainWindow", "新增使用者"))
        self.pushButton_7.setText(_translate("MainWindow", "新增車輛"))
        self.pushButton_8.setText(_translate("MainWindow", "新增違規狀態"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.pushButton_5.setText(_translate("MainWindow", "返回主畫面"))
        self.comboBox.setItemText(0, _translate("MainWindow", "所有車種"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SUV"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Coupe"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Truck"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Sedan"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Van"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "所有檢驗項目"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "101"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "102"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "103"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "104"))
        self.comboBox_3.setItemText(5, _translate("MainWindow", "105"))
        
        self.label_2.setText(_translate("MainWindow", "違規項目："))
        self.label_2.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_3.setText(_translate("MainWindow", "檢驗項目："))
        self.label_3.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.comboBox_2.setItemText(0, _translate("MainWindow", "所有違規"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1001"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1002"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1003"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1004"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "1005"))
        self.label.setText(_translate("MainWindow", "車輛種類："))
        self.label.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        
        self.label_4.setText(_translate("MainWindow", "狀態查詢系統"))
        self.label_4.setGeometry(QtCore.QRect(280, 30, 260, 51))
        self.label_4.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-weight: bold;
                font-size: 40px;
            }
        """)


if __name__ == "__main__":
    import sys
    # 創建應用程式
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 執行應用程式
    sys.exit(app.exec_())