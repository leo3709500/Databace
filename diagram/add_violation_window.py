# -*- coding: utf-8 -*-

# 這個檔案是由 PyQt5 UI 代碼生成器生成的，從 'C:\DBMS\ui\add_violation.ui' 讀取
# 警告：任何手動更改都會在重新運行 pyuic5 時丟失。除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from img_set.img_set import Img_setting

class Ui_MainWindow(Img_setting):
    def setupUi(self, MainWindow):
        # 設置主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
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
                padding: 30px;
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
        
        # 創建中央小部件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設置輸入欄位的網格佈局
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(170, 120, 431, 321))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 車牌號碼標籤
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 違規類型標籤
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        
        # 違規狀態標籤
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        
        # 違規編號標籤
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 違規日期標籤
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        
        # 車牌號碼輸入欄位
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        
        # 違規編號輸入欄位
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)
        
        # 罰金標籤
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setFamily("Microsoft JhengHei")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        
        # 罰金輸入欄位
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        
        # 違規日期輸入欄位
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.gridLayout.addWidget(self.dateEdit, 5, 1, 1, 1)
        
        self.dateEdit.setStyleSheet("""
            QDateEdit {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #444444;
                border-radius: 4px;
                padding: 5px;
            }
            QDateEdit::drop-down {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #444444;
                border-radius: 4px;
                padding: 5px;
            }
        """)
        
        # 違規類型下拉選單
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout.addWidget(self.comboBox_2, 4, 1, 1, 1)
        
        self.comboBox_2.setStyleSheet("""
            QComboBox {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #444444;
                border-radius: 4px;
                padding: 5px;
            }
            QComboBox::drop-down {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #FFFFFF;
                border-radius: 6px;
                padding: 10px;
                font-size: 15px;
                font-weight: bold;
                font-family: "Microsoft JhengHei";
                
            }
        """)
        
        # 違規狀態下拉選單
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 2, 1, 1, 1)
        self.comboBox_3.setStyleSheet("""
            QComboBox {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #444444;
                border-radius: 4px;
                padding: 5px;
            }
            QComboBox::drop-down {
                background-color: #FFFFFF;
                color: #000000;
                border: 2px solid #FFFFFF;
                border-radius: 6px;
                padding: 10px;
                font-size: 15px;
                font-weight: bold;
                font-family: "Microsoft JhengHei";
                
            }
        """)
        
        # 標題標籤
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 60, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setFamily("Microsoft JhengHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # 設置按鈕的水平佈局
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(170, 460, 431, 31))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 新增按鈕
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        # 清除按鈕
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        # 上一頁按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        # 設置主視窗的中央小部件
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設置菜單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設置狀態欄
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

        # 重新翻譯 UI 元素
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 設置清除按鈕的功能
        self.pushButton_2.clicked.connect(self.clear_fields)

    def clear_fields(self):
        # 清除所有輸入欄位的內容
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())

    def retranslateUi(self, MainWindow):
        # 設置 UI 元素的文字
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "車牌號碼："))
        self.label.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_5.setText(_translate("MainWindow", "違規類型："))
        self.label_5.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_4.setText(_translate("MainWindow", "違規狀態："))
        self.label_4.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_2.setText(_translate("MainWindow", "違規編號："))
        self.label_2.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_6.setText(_translate("MainWindow", "違規日期："))
        self.label_6.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.label_7.setText(_translate("MainWindow", "罰金："))
        self.label_7.setStyleSheet("""
            QLabel {
                color: #000000;
            }
        """)
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1001"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1002"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "1003"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "1004"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "1005"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Y"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "N"))
        self.label_3.setText(_translate("MainWindow", "請輸入欲新增的違規資訊"))
        self.label_3.setGeometry(QtCore.QRect(240, 40, 350, 101))
        self.label_3.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 30px;
                font-weight: bold;
                font-family: "Microsoft JhengHei";
            }
        """)    
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "上一頁"))

if __name__ == "__main__":
    import sys
    # 創建應用程序對象
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    # 進入應用程序的主循環
    sys.exit(app.exec_())
