# -*- coding: utf-8 -*-

# 這個檔案是從 'C:\github\station_ui\ui\add_vehicle.ui' 讀取後生成的表單實作
# 由 PyQt5 UI 代碼生成器 5.15.11 創建
# 警告：任何對此文件的手動更改將在再次運行 pyuic5 時丟失。除非您知道自己在做什麼，否則不要編輯此文件。

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設定主視窗的名稱和大小
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # 設定中央小工具
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 設定按鈕的佈局
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 470, 431, 31))
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
        
        # 設定表單的佈局
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(190, 130, 431, 321))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        
        # 身分證字號輸入框
        self.ssn = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.ssn.setObjectName("ssn")
        self.gridLayout.addWidget(self.ssn, 0, 1, 1, 1)
        
        # 車牌號碼標籤
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        
        # 車牌號碼輸入框
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        
        # 身分證字號標籤
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        
        # 註冊日期選擇框
        self.dateEdit = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.gridLayout.addWidget(self.dateEdit, 1, 1, 1, 1)
        
        # 檢驗費用輸入框
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 7, 1, 1, 1)
        
        # 檢驗狀態標籤
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        
        # 註冊日期標籤
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        
        # 下次檢驗日期選擇框
        self.dateEdit_2 = QtWidgets.QDateEdit(self.layoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setDisplayFormat("yyyy-MM-dd")
        self.gridLayout.addWidget(self.dateEdit_2, 6, 1, 1, 1)
        
        # 檢驗費用標籤
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 7, 0, 1, 1)
        
        # 檢驗狀態下拉選單
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout.addWidget(self.comboBox_3, 5, 1, 1, 1)
        
        # 下次檢驗日期標籤
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        
        # 檢驗號碼標籤
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        
        # 檢驗號碼輸入框
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        
        # 車輛種類標籤
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        
        # 檢驗項目標籤
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 8, 0, 1, 1)
        
        # 檢驗項目下拉選單
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.gridLayout.addWidget(self.comboBox_4, 8, 1, 1, 1)
        
        # 車輛種類下拉選單
        self.car_typ_comboBox = QtWidgets.QComboBox(self.layoutWidget_2)
        self.car_typ_comboBox.setObjectName("car_typ_comboBox")
        self.car_typ_comboBox.addItem("")
        self.car_typ_comboBox.addItem("")
        self.car_typ_comboBox.addItem("")
        self.car_typ_comboBox.addItem("")
        self.car_typ_comboBox.addItem("")
        self.gridLayout.addWidget(self.car_typ_comboBox, 2, 1, 1, 1)
        
        # 標題標籤
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 70, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
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

        # 重新翻譯 UI
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # 設定清除按鈕的功能
        self.pushButton_2.clicked.connect(self.clear_fields)

    def clear_fields(self):
        # 清除所有輸入欄位的內容
        self.ssn.clear()
        self.lineEdit_6.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.lineEdit_7.clear()
        self.comboBox_3.setCurrentIndex(0)
        self.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def retranslateUi(self, MainWindow):
        # 設定翻譯
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "新增"))
        self.pushButton_2.setText(_translate("MainWindow", "清除"))
        self.pushButton_3.setText(_translate("MainWindow", "上一頁"))
        self.label_7.setText(_translate("MainWindow", "車牌號碼："))
        self.label_2.setText(_translate("MainWindow", "身分證字號："))
        self.label_8.setText(_translate("MainWindow", "檢驗狀態："))
        self.label_6.setText(_translate("MainWindow", "註冊日期："))
        self.label_10.setText(_translate("MainWindow", "檢驗費用："))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Y"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "N"))
        self.label_9.setText(_translate("MainWindow", "下次檢驗日期："))
        self.label_5.setText(_translate("MainWindow", "檢驗號碼："))
        self.label_4.setText(_translate("MainWindow", "車輛種類："))
        self.label_11.setText(_translate("MainWindow", "檢驗項目："))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "101"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "102"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "103"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "104"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "105"))
        self.car_typ_comboBox.setItemText(0, _translate("MainWindow", "SUV"))
        self.car_typ_comboBox.setItemText(1, _translate("MainWindow", "Coupe"))
        self.car_typ_comboBox.setItemText(2, _translate("MainWindow", "Truck"))
        self.car_typ_comboBox.setItemText(3, _translate("MainWindow", "Sedan"))
        self.car_typ_comboBox.setItemText(4, _translate("MainWindow", "Van"))
        self.label_3.setText(_translate("MainWindow", "請輸入欲新增的車輛資訊"))

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
