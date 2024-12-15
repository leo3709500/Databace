# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\DBMS\ui\user_find.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設定查詢按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(620, 40, 81, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        
        # 設定返回按鈕
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(620, 80, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        
        # 設定群組框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        ##
        self.groupBox.setGeometry(QtCore.QRect(100, 30, 491, 90)) #改外框大小
        ##
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("""
            QGroupBox {
                border: 2px solid #444444;  /* 設置邊框顏色和寬度 */
                border-radius: 10px;        /* 設置圓角 */
                padding: 10px;              /* 設置內邊距 */
            }
        """)
        
        # 設定網格佈局小工具
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        ##
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 13, 441, 67)) #改內容大小
        ##
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        
        # 設定網格佈局
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setRowMinimumHeight(0, 80)  # 設置第一行的最小高度
        self.gridLayout.setRowMinimumHeight(1, 80)  # 設置第二行的最小高度
        self.gridLayout.setObjectName("gridLayout")
        
        # 設定密碼標籤
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 設定帳號標籤
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 設定帳號輸入框
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumSize(200, 30)  # 設置最小寬度和高度
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        # 設定密碼輸入框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setMinimumSize(200, 30)  # 設置最小寬度和高度
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
        # 設定用戶資料群組框
        self.user_info_group = QtWidgets.QGroupBox(self.centralwidget)
        self.user_info_group.setGeometry(QtCore.QRect(100, 130, 600, 90))
        self.user_info_group.setTitle("用戶資料")
        self.user_info_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #444444;  /* 設置邊框顏色和寬度 */
                border-radius: 10px;        /* 設置圓角 */
                padding: 10px;              /* 設置內邊距 */
            }
            QGroupBox:title {
                color: #000000;             /* 設置標題顏色 */
            }
        """)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.user_info_group.setFont(font)
        
        # 設定用戶資料標籤
        self.user_info_label = QtWidgets.QLabel(self.user_info_group)
        self.user_info_label.setGeometry(QtCore.QRect(10, 20, 280, 120))
        self.user_info_label.setWordWrap(True)
        self.user_info_label.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.user_info_label.setStyleSheet("font-size: 12pt; color: #333;")
        self.user_info_label.setObjectName("user_info_label")
        
        # 設定用戶車輛群組框
        self.vehicle_info_group = QtWidgets.QGroupBox(self.centralwidget)
        self.vehicle_info_group.setGeometry(QtCore.QRect(100, 230, 600, 150))
        self.vehicle_info_group.setTitle("用戶的車輛")
        self.vehicle_info_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #444444;  /* 設置邊框顏色和寬度 */
                border-radius: 10px;        /* 設置圓角 */
                padding: 10px;              /* 設置內邊距 */
            }
            QGroupBox:title {
                color: #000000;             /* 設置標題顏色 */
            }
        """)
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei")
        self.vehicle_info_group.setFont(font)
        

        # 新增 QTableView 來顯示車輛資訊
        self.vehicle_info_table = QtWidgets.QTableView(self.vehicle_info_group)
        self.vehicle_info_table.setGeometry(QtCore.QRect(10, 20, 580, 120))
        self.vehicle_info_table.setObjectName("vehicle_info_table")
        
        # 添加圓角樣式
        self.vehicle_info_table.setStyleSheet("""
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
        """)

        # 設定模型
        self.vehicle_info_model = QStandardItemModel()
        self.vehicle_info_model.setHorizontalHeaderLabels(
            ["車輛類型", "車輛牌照", "車輛年份", "車輛月份", "車輛日期", "檢查號"]
        )
        self.vehicle_info_table.setModel(self.vehicle_info_model)

        # 禁止編輯
        self.vehicle_info_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        #modify
        # 設定用戶違規狀態群組框
        self.violate_status_group = QtWidgets.QGroupBox(self.centralwidget)
        self.violate_status_group.setGeometry(QtCore.QRect(100, 400, 600, 150))
        self.violate_status_group.setTitle("用戶違規狀態")
        self.violate_status_group.setStyleSheet("""
            QGroupBox {
                border: 2px solid #444444;  /* 設置邊框顏色和寬度 */
                border-radius: 10px;        /* 設置圓角 */
                padding: 10px;              /* 設置內邊距 */
            }
            QGroupBox:title {
                color: #000000;             /* 設置標題顏色 */
            }
        """)

        # 新增 QTableView 來顯示違規狀態
        self.violate_status_table = QtWidgets.QTableView(self.violate_status_group)
        self.violate_status_table.setGeometry(QtCore.QRect(10, 20, 580, 120))
        self.violate_status_table.setObjectName("violate_status_table")
        
        # 添加圓角樣式
        self.violate_status_table.setStyleSheet("""
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
        """)

        # 設定模型
        self.violate_status_model = QStandardItemModel()
        self.violate_status_model.setHorizontalHeaderLabels(
            ["車牌號碼", "違規類型", "違規日期", "罰款金額", "狀態"]
        )
        self.violate_status_table.setModel(self.violate_status_model)

        # 設置列寬
        self.violate_status_table.setColumnWidth(0, 120)  # 車牌號碼
        self.violate_status_table.setColumnWidth(1, 120)  # 違規類型
        self.violate_status_table.setColumnWidth(2, 120)  # 違規日期
        self.violate_status_table.setColumnWidth(3, 120)  # 罰款金額
        self.violate_status_table.setColumnWidth(4, 120)  # 狀態

        # 禁止編輯
        self.violate_status_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # 設定主視窗的中央小工具
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設定選單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設定狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
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
                border: none;
                border-radius: 10px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)
        
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
        self.centralwidget.setStyleSheet("""
            QWidget#centralwidget {
                background-image: url('C:/github/Databace-brian/background/background_2.png');
                background-repeat: no-repeat;
                background-position: center;
                border-radius: 15px;
                opacity: 0.25;
            }
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
                border: 2px solid #444444;
                border-radius: 15px;
                padding: 70px;
                font-family: "Microsoft JhengHei";
            }
            QPushButton:hover {
                background-color: #0080FF;
            }
            QLineEdit {
                border: 2px solid #444444;
                border-radius: 15px;
                padding: 5px;
                background-color: #FFFFFF;
                color: 	#000000;
            }
        """)

        # 重新翻譯UI文字
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設定UI文字的翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "查詢"))
        self.pushButton_4.setText(_translate("MainWindow", "返回"))
        self.groupBox.setTitle(_translate("MainWindow", "登入"))
        self.label_2.setText(_translate("MainWindow", "密碼："))
        self.label_2.setStyleSheet("color: #000000;")
        self.label.setText(_translate("MainWindow", "帳號："))
        self.label.setStyleSheet("color: #000000;")


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