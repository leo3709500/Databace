import sys
import pymysql
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from connect.admin import Admin_login
from connect.manage import Manage_control
from connect.add_manage import Add_usermanage, Add_vehiclemanage, Add_violatemanage
from connect.user import User_control

from PyQt5 import QtWidgets
####
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem

####
from main_window import Ui_MainWindow as MainWindowUI
from login_window import Ui_MainWindow as LoginWindowUI
from manage_window import Ui_MainWindow as ManageWindowUI
from diagram.add_window import Ui_MainWindow as AddWindowUI
from user_find import Ui_MainWindow as UserFindWindowUI
from diagram.add_vehicle_window import Ui_MainWindow as AddVehicleUI
from diagram.add_violation_window import Ui_MainWindow as AddViolationUI
from question import Ui_MainWindow as QuestionUI
from other import Ui_MainWindow as OtherUI
from PyQt5.QtGui import QStandardItem


class MainController(Admin_login, User_control, Manage_control, Add_usermanage, Add_vehiclemanage, Add_violatemanage):
    def __init__(self):
        # 初始化應用程式
        self.app = QtWidgets.QApplication([])
        self.main_window = QtWidgets.QMainWindow()
        self.stacked_widget = QtWidgets.QStackedWidget()

        # 初始化各個UI
        self.ui_main = MainWindowUI()   #initial page
        self.ui_login = LoginWindowUI() #normal login
        self.ui_manage = ManageWindowUI()
        self.ui_add = AddWindowUI()     #add user information
        self.ui_user_find = UserFindWindowUI()
        self.ui_add_vehicle = AddVehicleUI()
        self.ui_add_violation = AddViolationUI()
        self.ui_question = QuestionUI()
        self.ui_other = OtherUI()

        # 初始化各個視窗
        self.main_widget = QtWidgets.QMainWindow()
        self.login_widget = QtWidgets.QMainWindow()
        self.manage_widget = QtWidgets.QMainWindow()
        self.add_widget = QtWidgets.QMainWindow()
        self.user_find_widget = QtWidgets.QMainWindow()
        self.add_vehicle_widget = QtWidgets.QMainWindow()
        self.add_violation_widget = QtWidgets.QMainWindow()
        self.question_widget = QtWidgets.QMainWindow()
        self.other_widget = QtWidgets.QMainWindow()

        # 設定UI到各個視窗
        self.ui_main.setupUi(self.main_widget)
        self.ui_login.setupUi(self.login_widget)
        self.ui_manage.setupUi(self.manage_widget)
        self.ui_add.setupUi(self.add_widget)
        self.ui_user_find.setupUi(self.user_find_widget)
        self.ui_add_vehicle.setupUi(self.add_vehicle_widget)
        self.ui_add_violation.setupUi(self.add_violation_widget)
        self.ui_question.setupUi(self.question_widget)
        self.ui_other.setupUi(self.other_widget)

        # 將視窗加入堆疊小部件
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.login_widget)
        self.stacked_widget.addWidget(self.manage_widget)
        self.stacked_widget.addWidget(self.add_widget)
        self.stacked_widget.addWidget(self.user_find_widget)
        self.stacked_widget.addWidget(self.add_vehicle_widget)
        self.stacked_widget.addWidget(self.add_violation_widget)
        self.stacked_widget.addWidget(self.question_widget)
        self.stacked_widget.addWidget(self.other_widget)

        # 設定主視窗的中央小部件
        self.main_window.setCentralWidget(self.stacked_widget)

        # 設定主視窗大小
        self.main_window.resize(800, 600)

        # 設定按鈕連接
        self.setup_connections()

        #database setting
        self.mydb = pymysql.connect(
                host='localhost',
                user='root',
                password='jimmylin0320',
                database='carsys'
        )
        self.mycursor = self.mydb.cursor()
        #inherit the attribute from the other controller.
        super().__init__()


    def setup_connections(self):
        # 設定按鈕點擊事件，切換不同的視窗
        self.ui_main.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.login_widget))
        self.ui_main.pushButton_2.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.user_find_widget))# user_find user account and password page
        self.ui_main.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.question_widget))
        self.ui_main.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.other_widget))
        self.ui_login.pushButton.clicked.connect(self.admin_login) # modify to judge the admin account
        self.ui_manage.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_widget))
        
        self.ui_login.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        self.ui_user_find.pushButton_3.clicked.connect(self.user_login)
        self.ui_user_find.pushButton_4.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))# return to orginal page
        # self.ui_user_find.pushButton_4.clicked.connect(self.user_login)
        
        # 新增一個按鈕來顯示查詢結果
        self.ui_manage.pushButton_2.clicked.connect(self.setup_table)
        self.ui_manage.pushButton_3.clicked.connect(self.display_query_results)
        self.ui_manage.pushButton_3.clicked.connect(self.manage_query)
        self.ui_manage.pushButton_6.clicked.connect(self.delete_item)
        self.ui_manage.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        self.ui_manage.pushButton_7.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_vehicle_widget))
        self.ui_manage.pushButton_8.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.add_violation_widget))

        self.ui_add.pushButton.clicked.connect(self.add_user)
        self.ui_add.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))

        self.ui_add_violation.pushButton.clicked.connect(self.add_violation)
        self.ui_add_violation.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        
        self.ui_add_vehicle.pushButton.clicked.connect(self.add_vehicle)
        self.ui_add_vehicle.pushButton_3.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.manage_widget))
        
        self.ui_question.pushButton_5.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))
        self.ui_other.pushButton_6.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.main_widget))

     #this should be moved to manage.py   
    def display_query_results(self):
        
        results = self.get_query_results()
        self.ui_manage.model.clear()  # 清除現有的模型數據
        self.ui_manage.model.setHorizontalHeaderLabels(self.ui_manage.columns)
        for row in results:
            items = [QStandardItem(str(field)) for field in row]
            self.ui_manage.model.appendRow(items)

    def show_main_window(self):
        # 顯示主視窗
        self.main_window.show()

    def run(self):
        # 執行應用程式
        self.show_main_window()
        self.app.exec_()

if __name__ == "__main__":
    # 創建控制器並運行
    controller = MainController()
    controller.run()
    controller.mycursor.close()
