# -*- coding: utf-8 -*-

# 這個檔案是由 PyQt5 UI 代碼生成器生成的，從 'C:\DBMS\ui\login_window.ui' 讀取
# 警告：任何手動更改都會在重新運行 pyuic5 時丟失。除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設置主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # 創建中央小部件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設置按鈕的水平佈局
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 350, 441, 33))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 登入按鈕
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        # 返回主畫面按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        # 標題標籤
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 100, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(32)
        font.setFamily("Microsoft JhengHei")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # 設置帳號和密碼的網格佈局
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(190, 190, 441, 141))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 密碼標籤
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Microsoft JhengHei")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 帳號標籤
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setFamily("Microsoft JhengHei")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 帳號輸入欄位
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        # 密碼輸入欄位
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        
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

        # 重新翻譯 UI 元素
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        # 設置 UI 元素的文字
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "登入"))
        self.pushButton_3.setText(_translate("MainWindow", "返回主畫面"))
        self.label_3.setText(_translate("MainWindow", "管理員登入"))
        self.label_3.setStyleSheet("""
            QLabel {
                color: #000000;
                font-weight: bold;
                font-size: 40px;
            }
        """)
        self.label_2.setText(_translate("MainWindow", "密碼："))
        self.label_2.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 20px;
            }
        """)
        self.label.setText(_translate("MainWindow", "帳號："))
        self.label.setStyleSheet("""
            QLabel {
                color: #000000;
                font-size: 20px;
            }
        """)

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
