from PyQt5 import QtWidgets

class User_control:
    def __init__(self, ui_user_find):
        self.ui_user_find = ui_user_find  # 保存 UI 引用
        self.account = None
        self.password = None
    
    def user_login(self):
        self.ssn = str(self.ui_user_find.lineEdit.text()).strip()
        self.password = str(self.ui_user_find.lineEdit_2.text()).strip()
        print("Input ssn: " + str(self.ssn))
        print("Input password: "+ str(self.password))

        user_query = "SELECT * FROM users WHERE ssn = %s AND password = %s"
        self.mycursor.execute(user_query, (self.ssn, self.password))
        
        # Fetch the result
        result = self.mycursor.fetchone()
        # check result!
        if result:
            print("Login successful!")
            user_info = f"帳號: {result[0]}\n姓名: {result[1]}\n電子郵件: {result[3]}"  # 假設 result[0] 是帳號，result[1] 是姓名，result[2] 是電子郵件
            self.ui_user_find.user_info_label.setText(user_info)  # 顯示用戶資料

            vehicle_query = "SELECT * FROM vehicles WHERE user_ssn = %s"
            self.mycursor.execute(vehicle_query, (self.ssn,))
            vehicles = self.mycursor.fetchall()
            if vehicles:
                vehicle_info = ""
                for vehicle in vehicles:
                    vehicle_info += f"車輛牌照: {vehicle[1]}\n"  # 假設 vehicle[1] 是車輛牌照
                self.ui_user_find.vehicle_info_label.setText(vehicle_info)  # 顯示車輛資料
            else:
                self.ui_user_find.vehicle_info_label.setText("沒有找到該用戶的車輛。")
        else:
            print("Invalid username or password.")
            self.ui_user_find.user_info_label.setText("無效的帳號或密碼。")
            self.ui_user_find.vehicle_info_label.setText("")  # 清空車輛信息
    def violation_infor(self, vehicle_license):
        violation_query = "SELECT * FROM violation WHERE vehicle_license = %s"
        self.mycursor.execute(violation_query, (vehicle_license))
        violation_record = self.mycursor.fetchall()
        if violation_record:
            for violation in violation_record:
                print("The car violation record:")
                print(violation)
                violation_detail_query = "SELECT * FROM violate_status WHERE violation_no = %s"
                self.mycursor.execute(violation_detail_query, violation[1])
                violation_detail = self.mycursor.fetchone()
                print("The event more information:")
                print(violation_detail)