# -*- coding: utf-8 -*-

# 這個檔案是從 'C:\DBMS\ui\add.ui' 讀取的 UI 文件生成的表單實現
#
# 由 PyQt5 UI 代碼生成器 5.15.10 創建
#
# 警告：任何對此文件的手動更改將在再次運行 pyuic5 時丟失。
# 除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 600)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設定佈局小工具
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 110, 431, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        
        # 設定網格佈局
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 設定姓名輸入框
        self.name = QtWidgets.QLineEdit(self.layoutWidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 0, 1, 1, 1)
        
        # 設定信箱輸入框
        self.email = QtWidgets.QLineEdit(self.layoutWidget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 5, 1, 1, 1)
        
        # 設定地址輸入框
        self.address = QtWidgets.QLineEdit(self.layoutWidget)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 4, 1, 1, 1)
        
        # 設定密碼輸入框
        self.password = QtWidgets.QLineEdit(self.layoutWidget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 2, 1, 1, 1)
        
        # 設定出生年月日標籤
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        
        # 設定身分證字號輸入框
        self.ssn = QtWidgets.QLineEdit(self.layoutWidget)
        self.ssn.setObjectName("ssn")
        self.gridLayout.addWidget(self.ssn, 1, 1, 1, 1)
        
        # 設定日期編輯器
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy/MM/dd")
        self.gridLayout.addWidget(self.dateEdit, 7, 1, 1, 1)
        
        # 設定電話標籤
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        
        # 設定電話輸入框
        self.phone_number = QtWidgets.QLineEdit(self.layoutWidget)
        self.phone_number.setObjectName("phone_number")
        self.gridLayout.addWidget(self.phone_number, 6, 1, 1, 1)
        
        # 設定姓名標籤
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        
        # 設定信箱標籤
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)
        
        # 設定身分證字號標籤
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        
        # 設定地址標籤
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        
        # 設定密碼標籤
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        
        # 設定註冊日期標籤
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)
        
        # 設定註冊日期輸入框
        self.reg_date = QtWidgets.QDateEdit(self.layoutWidget)
        self.reg_date.setObjectName("reg_date")
        self.reg_date.setDisplayFormat("yyyy/MM/dd")
        self.gridLayout.addWidget(self.reg_date, 3, 1, 1, 1)
        
        # 設定按鈕佈局小工具
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(190, 450, 431, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        
        # 設定水平佈局
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        # 設定新增按鈕
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        
        # 設定清除按鈕
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        
        # 設定上一頁按鈕
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        
        # 設定標題標籤
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 50, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        # 設定主視窗的中央小工具
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 設定選單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 設定狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 重新翻譯 UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # 設置清除按鈕的功能
        self.pushButton_2.clicked.connect(self.clear_fields)

    def clear_fields(self):
        # 清除所有輸入欄位的內容
        self.name.clear()
        self.email.clear()
        self.address.clear()
        self.password.clear()
        self.ssn.clear()
        self.phone_number.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())

    def retranslateUi(self, MainWindow):
        # 設定翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "出生年月日："))
        self.label_5.setText(_translate("MainWindow", "電話："))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_7.setText(_translate("MainWindow", "信箱："))
        self.label_2.setText(_translate("MainWindow", "身分證字號："))
        self.label_4.setText(_translate("MainWindow", "地址："))
        self.label_8.setText(_translate("MainWindow", "密碼："))
        self.label_9.setText(_translate("MainWindow", "註冊日期："))
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "上一頁"))
        self.label_3.setText(_translate("MainWindow", "請輸入欲新增的使用者資訊"))

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
