from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem
from PyQt5.QtGui import QStandardItemModel
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
                # 清空現有的模型數據
                self.ui_user_find.vehicle_info_model.clear()
                self.ui_user_find.vehicle_info_model.setHorizontalHeaderLabels(
                    ["車輛類型", "車輛牌照", "車輛年份", "車輛月份", "車輛日期", "檢查號"]
                )

                for vehicle in vehicles:
                    items = [QStandardItem(str(field)) for field in vehicle[:6]]  # 只取前 6 個欄位
                    self.ui_user_find.vehicle_info_model.appendRow(items)
                    # 清空舊的 QLabel 顯示
                # self.ui_user_find.vehicle_info_model.setText("")
                self.ui_user_find.vehicle_info_table.setModel(self.ui_user_find.vehicle_info_model)
            else:
                self.ui_user_find.vehicle_info_label.setText("沒有找到該用戶的車輛。")
        else:
            print("Invalid username or password.")
            #self.ui_user_find.user_info_label.setText("無效的帳號或密碼。")
            #self.ui_user_find.vehicle_info_label.setText("")  # 清空車輛信息
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
                
    def display_violation_status(self):
        # 從 vehicles_table 中獲取車牌號碼
        vehicle_query = "SELECT license_plate FROM vehicles WHERE user_ssn = %s"
        self.mycursor.execute(vehicle_query, (self.ssn,))
        vehicle_records = self.mycursor.fetchall()

        if not vehicle_records:
            print("No vehicles found for this user.")
            self.ui_user_find.violate_status_model.clear()
            self.ui_user_find.violate_status_model.setHorizontalHeaderLabels(
                ["車牌號碼", "違規類型", "違規日期", "罰款金額", "狀態"]
            )
            return

        # 查詢違規狀態
        for vehicle in vehicle_records:
            license_plate = vehicle[0]
            violation_query = """
            SELECT v.vehicle_license, vs.violation_type, vs.violate_date, vs.fine, vs.status
            FROM violation v
            JOIN violate_status vs ON v.violation_no = vs.violation_no
            WHERE v.vehicle_license = %s
            """
            self.mycursor.execute(violation_query, (license_plate,))
            violation_records = self.mycursor.fetchall()

            if violation_records:
                # 清空現有的模型數據
                self.ui_user_find.violate_status_model.clear()
                self.ui_user_find.violate_status_model.setHorizontalHeaderLabels(
                    ["車牌號碼", "違規類型", "違規日期", "罰款金額", "狀態"]
                )

                for record in violation_records:
                    items = [QStandardItem(str(field)) for field in record]
                    self.ui_user_find.violate_status_model.appendRow(items)

                self.ui_user_find.violate_status_table.setModel(self.ui_user_find.violate_status_model)
            else:
                print(f"No violation records found for vehicle {license_plate}.")