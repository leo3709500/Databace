from PyQt5 import QtWidgets

class Admin_login:
    def __init__(self):
        self.admin_credentials = {"admin":"database123", "password":"aaa123"}
        self.message_box = QtWidgets.QMessageBox()
    
    def admin_login(self):
        username = str(self.ui_login.lineEdit.text()).strip()
        password = str(self.ui_login.lineEdit_2.text()).strip()
        print(f"Entered Username: {username}")
        print(f"Entered Password: {password}")

        if username in self.admin_credentials["admin"] and self.admin_credentials["password"] == password:
            self.stacked_widget.setCurrentWidget(self.manage_widget)
        else:
            # 顯示錯誤提示
            self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.message_box.setWindowTitle("登入失敗")
            self.message_box.setText("帳號或密碼錯誤，請重試！")
            self.message_box.exec_()
        