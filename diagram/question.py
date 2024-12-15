# -*- coding: utf-8 -*-

# 這個文件是由 PyQt5 UI 代碼生成器生成的，從 'C:\DBMS\ui\question.ui' 讀取 UI 文件
# 警告：任何手動更改都會在再次運行 pyuic5 時丟失

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 設置主窗口的基本屬性
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # 創建中央小部件
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # 創建 Tab Widget 並設置其位置和大小
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(40, 40, 720, 490))
        self.tabWidget.setObjectName("tabWidget")
        
        # 添加美化 Tab 的樣式
        self.tabWidget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #444444;
                background-color: #7B7B7B;
            }
            QTabBar::tab {
                background: #444444;
                color: #ffffff;
                padding: 10px;
                border: 1px solid #444444;
                border-bottom: none;
                border-top-left-radius: 5px;
                border-top-right-radius: 5px;
                min-width: 158px;
                max-width: 158px;
            }
            QTabBar::tab:selected {
                background: #7B7B7B;
                font-weight: bold;
            }
            QTabBar::tab:hover {
                background: #555555;
            }
            QTabBar {
                alignment: center;
            }
            QLabel {
                font-family: "Microsoft JhengHei";
                color: #ffffff;
            }
            QPushButton {
                font-family: "Microsoft JhengHei";
                background-color: #444444;
                color: #ffffff;
                border: 3px solid #444444;
                border-radius: 11px;
                padding: 1px;
            }
            QPushButton:hover {
                background-color: #0080FF;
            }
        """)
        
        # 創建第一個 Tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        
        # 在第一個 Tab 中添加標籤
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 120, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Microsoft JhengHei")
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        
        # 添加第二個標籤
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 681, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        
        # 將第一個 Tab 添加到 Tab Widget
        self.tabWidget.addTab(self.tab, "")
        
        # 創建第二個 Tab
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        
        # 在第二個 Tab 中添加標籤
        self.label_3 = QtWidgets.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 170, 681, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
        
        # 添加第二個標籤
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 110, 641, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Microsoft JhengHei")
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setObjectName("label_4")
        
        # 將第二個 Tab 添加到 Tab Widget
        self.tabWidget.addTab(self.tab_2, "")
        
        # 創建第三個 Tab
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        
        # 在第三個 Tab 中添加標籤
        self.label_5 = QtWidgets.QLabel(self.tab_3)
        self.label_5.setGeometry(QtCore.QRect(20, 180, 771, 261))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setObjectName("label_5")
        
        # 添加第二個標籤
        self.label_6 = QtWidgets.QLabel(self.tab_3)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 711, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Microsoft JhengHei")
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(False)
        self.label_6.setObjectName("label_6")
        
        # 將第三個 Tab 添加到 Tab Widget
        self.tabWidget.addTab(self.tab_3, "")
        
        # 創建第四個 Tab
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        
        # 在第四個 Tab 中添加標籤
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 681, 291))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setObjectName("label_7")
        
        # 添加第二個標籤
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 581, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        font.setFamily("Microsoft JhengHei")
        self.label_8.setFont(font)
        self.label_8.setAutoFillBackground(False)
        self.label_8.setObjectName("label_8")
        
        # 將第四個 Tab 添加到 Tab Widget
        self.tabWidget.addTab(self.tab_4, "")
        
        # 創建返回主畫面的按鈕
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(340, 542, 102, 23))
        self.pushButton_5.setObjectName("pushButton_6")
        self.pushButton_5.setStyleSheet("""
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
        
        # 設置主窗口的中央小部件
        MainWindow.setCentralWidget(self.centralwidget)
        
        # 創建菜單欄
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        # 創建狀態欄
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # 設置 UI 的翻譯文本
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
                border: none;
                border-radius: 10px;
                padding: 10px;
                font-family: "Microsoft JhengHei";
            }
            QPushButton:hover {
                background-color: #555555;
            }
        """)

    def retranslateUi(self, MainWindow):
        # 設置窗口標題和各個標籤的文本
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Q1：汽車定期檢驗次數之規定如何？"))
        self.label_2.setText(_translate("MainWindow", "1.自用小客車（LPG車、租賃車除外）新領牌照後出廠未滿5年者免檢驗，出廠\n"
"2.出廠年份逾10年之營業大客車或高壓罐槽車每年至少檢驗3次。\n"
"3.拖車每年檢驗1次。\n"
"4.其他汽車出廠未滿5年者每年檢驗1次，5年以上者每年檢驗2次。\n"
"5年以上未滿10年者每年檢驗1次，10年以上者每年檢驗2次。\n"
""))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Q1"))
        self.label_3.setText(_translate("MainWindow", "1.檢驗不合格者，應於1個月內整修完善，申請覆驗。\n"
"2.凡於7日內覆驗免收費1次，第8日起覆驗應收覆驗費。\n"
"3.覆驗時，只檢驗不合格項目。\n"
""))
        self.label_4.setText(_translate("MainWindow", "Q2.：檢驗不合格之汽車，如何辦理覆驗？\n"
"覆驗時是否應再繳納檢驗費？"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Q2"))
        self.label_5.setText(_translate("MainWindow", "依據道路交通安全規則第52條規定駕照有效期間：\n"
"1. 自中華民國102年7月1日起，新領或已領有之各類普通駕駛執照，免定期申請換發；其已領有之駕駛執照\n"
"有效期間屆滿後，仍屬有效，並得免換發之；外國人取得外僑永久居留證者，亦同。\n"
"2. 受終身不得考領駕駛執照處分重新申請考驗合格後領有1年有效期間駕駛執照。\n"
"3. 外國人、大陸地區人民、香港或澳門居民或臺灣地區無戶籍之國民考領換領我國汽車駕駛執照應每滿6年換發。\n"
"4. 特定年齡以上之汽車駕駛人另有規定其普通駕駛執照有效期間及申請換發新照規定時，應依規定辦理之。\n"
"5. 汽車駕駛人應於有效期限屆滿前後1個月內向公路監理機關申請換發。除前項免再依規定申請換發之情形外，\n"
"汽車駕駛執照逾期未換發新照者，不得駕駛汽車。\n"
"依據道路交通管理處罰條例第22條規定：\n"
"駕駛執照逾有效期間仍駕車者，處新臺幣1800元以上3600元以下罰鍰，並禁止其駕駛； 駕駛執照並應扣繳之。\n"
""))
        self.label_6.setText(_translate("MainWindow", "Q3：汽(機)車駕駛執照換發之處罰條款\n"
"或相關法規之規定如何？"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Q3"))
        self.label_7.setText(_translate("MainWindow", "(一)應備文件\n"
"1.國民身分證或戶口名簿（佐以其他貼有本人相片之足資證明其 身分之證件，\n"
"如全民健保卡、護照、軍人身分證或駕駛執照等）或僑民居留證正本。\n"
"2.原新領之駕駛執照正本。\n"
"(二)連同應備文件，至各公路監理機關服務台抽取號碼單等候叫號辦理，或用郵寄\n"
"通信方式辦理。\n"
"(三)注意事項：\n"
"1.若有違反道路交通管理事件，應結清罰鍰，\n"
"或辦理分期付款並繳納第一期罰鍰金額。\n"
"2.駕照背面之「住址變更」欄已填滿者應換發新照，並繳納規費\n"
"新臺幣50元；駕照已到期應同時辦理換照者，繳納規費新臺幣200元。\n"
""))
        self.label_8.setText(_translate("MainWindow", "Q4：汽(機)車駕駛人住址變更，應如何辦理？"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Q4"))
        self.pushButton_5.setText(_translate("MainWindow", "返回主畫面"))

if __name__ == "__main__":
    import sys
    # 創建應用程序對象
    app = QtWidgets.QApplication(sys.argv)
    # 創建主窗口對象
    MainWindow = QtWidgets.QMainWindow()
    # 創建 UI 對象並設置 UI
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # 顯示主窗口
    MainWindow.show()
    # 進入應用程序主循環
    sys.exit(app.exec_())
