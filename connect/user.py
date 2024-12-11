from PyQt5 import QtWidgets

class User_control:
    def __init__(self):
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
            print("User personal information:")

            self.mycursor.execute(user_query, (self.ssn, self.password))
            user_infor = self.mycursor.fetchall()
            for infor in user_infor:
                print(infor)
            
            vehicle_query = "SELECT * FROM vehicles WHERE user_ssn = %s"
            self.mycursor.execute(vehicle_query, (self.ssn))
            vehicles = self.mycursor.fetchall()
            if vehicles:
                for vehicle in vehicles:
                    print("User's Vehicles:")
                    print(vehicle)  # 逐行列印每一筆資料
                    self.violation_infor(vehicle[1])
            else:
                print("No vehicles found for this user.")
            # 這裡可以進一步處理登錄成功後的動作
        else:
            print("Invalid username or password.")
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