from PyQt5 import QtWidgets

class Add_usermanage:
    
    def add_user(self):
        name = str(self.ui_add.name.text()).strip()
        ssn = str(self.ui_add.ssn.text()).strip()
        password = str(self.ui_add.password.text()).strip()
        mail = str(self.ui_add.email.text()).strip()
        regis_day = str(self.ui_add.reg_date.date().toString("yyyy-MM-dd")).strip()
        regis_year, regis_month, regis_date = regis_day.split('-')
        address = str(self.ui_add.address.text()).strip()
        phone = str(self.ui_add.phone_number.text()).strip()
        birth_day = str(self.ui_add.dateEdit.date().toString("yyyy-MM-dd")).strip()
        birth_year, birth_month, birth_date = birth_day.split('-')
        if not ssn:
            QtWidgets.QMessageBox.warning(None, "警告", "身份證字號不能為空！")
            return
        
        try:
            # 檢查使用者是否已存在
            if not self.check_user_exists(ssn):
                # 插入新使用者資料
                user_insert = '''
                    INSERT INTO users (name, ssn, password, mail, regis_year, regis_month, regis_date, address, cellphone, 
                    birth_year, birth_month, birth_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    '''
                self.mycursor.execute(user_insert, (name, ssn, password, mail, regis_year, regis_month, regis_date, address, phone, birth_year, birth_month, birth_date))
                self.mydb.commit()
                QtWidgets.QMessageBox.information(None, "成功", "資料已成功保存！")
            else:
                QtWidgets.QMessageBox.warning(None, "警告", "該ssn已存在！")
        except:
            QtWidgets.QMessageBox.critical(None, "錯誤無法插入資料:")
            print(f"插入資料失敗")

    def check_user_exists(self, ssn):
        """
        檢查使用者是否存在
        """
        try:
            user_query = "SELECT * FROM users WHERE ssn = %s"
            self.mycursor.execute(user_query, (ssn))
            exists = self.mycursor.fetchone()
            return exists is not None
        except:
            QtWidgets.QMessageBox.critical(None, "錯誤檢查使用者失敗")
            print("檢查使用者失敗")
            return False
        
class Add_vehiclemanage:

    def add_vehicle(self):
        type = str(self.ui_add_vehicle.car_typ_comboBox.currentText()).strip()
        license_plate = str(self.ui_add_vehicle.lineEdit_6.text()).strip()
        car_day = str(self.ui_add_vehicle.dateEdit.date().toString("yyyy-MM-dd")).strip()
        car_year, car_month, car_date = car_day.split('-')
        inspect_no = str(self.ui_add_vehicle.lineEdit_5.text()).strip()
        user_ssn = str(self.ui_add_vehicle.ssn.text()).strip()

        inspect_status = str(self.ui_add_vehicle.comboBox_3.currentText()).strip()
        next_inspect_day = str(self.ui_add_vehicle.dateEdit_2.date().toString("yyyy-MM-dd")).strip()
        next_year, next_month, next_date = next_inspect_day.split('-')
        inspect_fee = str(self.ui_add_vehicle.lineEdit_7.text()).strip()
        inspect_type = str(self.ui_add_vehicle.comboBox_4.currentText()).strip()

        ssn_exist_check = "SELECT ssn FROM users WHERE ssn = %s"
        license_check = "SELECT license_plate FROM vehicles WHERE license_plate = %s"
        inspect_no_check = "SELECT inspect_no FROM inspection_status WHERE inspect_no = %s"
        if len(inspect_no)!= 6:
            QtWidgets.QMessageBox.warning(None, "Warning", "The inspect_no must include 6 characters!")
        try:
            self.mycursor.execute(ssn_exist_check, (user_ssn,))
            ssn_exist = self.mycursor.fetchone()
            self.mycursor.execute(inspect_no_check, (inspect_no,))
            inspect_no_exist = self.mycursor.fetchone()
            if not ssn_exist:
                QtWidgets.QMessageBox.warning(None, "Warning", "The user does not exist!")
            elif inspect_no_exist:
                QtWidgets.QMessageBox.warning(None, "Warning", "The inspect_no already exist!")
            else:
                self.mycursor.execute(license_check, (license_plate,))
                license_exist = self.mycursor.fetchone()
                if not license_exist:
                    if len(license_plate) != 8: 
                        QtWidgets.QMessageBox.warning(None, "Warning", "Error: The license plate must include 8 characters!")
                    else:
                        vehicle_insert = '''
                            INSERT INTO vehicles (type, license_plate, car_year, car_month, car_date, inspect_no, user_ssn)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        '''
                        self.mycursor.execute(vehicle_insert, (type, license_plate, car_year, car_month, car_date, inspect_no, user_ssn))
                        self.mydb.commit()
                        inspect_insert = '''
                            INSERT INTO inspection_status (status, inspect_no, next_year, next_month, next_date, inspect_fee, inspect_type)
                            VALUES (%s, %s, %s, %s, %s, %s, %s)
                        '''
                        self.mycursor.execute(inspect_insert, (inspect_status, inspect_no, next_year, next_month, next_date, inspect_fee, inspect_type))
                        self.mydb.commit()
                        QtWidgets.QMessageBox.information(None, "Success", "Data has been saved successfully!")
                else:
                    QtWidgets.QMessageBox.warning(None, "Warning", "Error: The license plate has already exists!!")
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

class Add_violatemanage:
    def add_violation(self):
        vehicle_license = str(self.ui_add_violation.lineEdit_2.text()).strip()
        violation_no = str(self.ui_add_violation.lineEdit_3.text()).strip()
        status = str(self.ui_add_violation.comboBox_3.currentText()).strip()
        fine = str(self.ui_add_violation.lineEdit_6.text()).strip()
        violate_day = str(self.ui_add_violation.dateEdit.date().toString("yyyy-MM-dd")).strip()
        violate_year, violate_month, violate_date = violate_day.split('-')
        violation_type = str(self.ui_add_violation.comboBox_2.currentText()).strip()

        if len(violation_no) != 6:
            QtWidgets.QMessageBox.warning(None, "Warning", "Error: The violation_no must have 4 characters!")
            return
        elif len(vehicle_license) != 8:
            QtWidgets.QMessageBox.warning(None, "Warning", "Error: The vehicle_license must have 8 characters!")
            return
        
        try:
            # 檢查車牌是否存在
            license_check = "SELECT license_plate FROM vehicles WHERE license_plate = %s"
            self.mycursor.execute(license_check, (vehicle_license,))
            license_exist = self.mycursor.fetchone()

            # 檢查違規編號是否存在
            violation_no_check = "SELECT violation_no FROM violation WHERE violation_no = %s"
            self.mycursor.execute(violation_no_check, (violation_no,))
            violation_no_exist = self.mycursor.fetchone()

            if not license_exist:
                QtWidgets.QMessageBox.warning(None, "Warning", "The license of the car does not exist!")
            elif violation_no_exist:
                QtWidgets.QMessageBox.warning(None, "Warning", "The violation_no has been used!")
            else:
                # 開始插入資料
                violation_insert = '''
                    INSERT INTO violation (vehicle_license, violation_no)
                    VALUES (%s, %s)
                '''
                violate_status_insert = '''
                    INSERT INTO violate_status (status, fine, violate_year, violate_month, violate_date, violation_no, violation_type)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
                self.mycursor.execute(violation_insert, (vehicle_license, violation_no))
                self.mycursor.execute(violate_status_insert, (status, fine, violate_year, violate_month, violate_date, violation_no, violation_type))
                self.mydb.commit()
                QtWidgets.QMessageBox.information(None, "Success", "Data has been saved successfully!")
        except Exception as e:
            self.mydb.rollback()
            QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")

# class Add_violatemanage:
#     def add_violation(self):
#         vehicle_license = str(self.ui_add_violation.lineEdit_2.text()).strip()
#         violation_no = str(self.ui_add_violation.lineEdit_3.text()).strip()

#         status = str(self.ui_add_violation.comboBox_3.currentText()).strip()
#         fine = str(self.ui_add_violation.lineEdit_6.text()).strip()
#         violate_day = str(self.ui_add_violation.dateEdit.date().toString("yyyy-MM-dd")).strip()
#         violate_year, violate_month, violate_date = violate_day.split('-')
#         violation_no = str(self.ui_add_violation.comboBox_3.currentText()).strip()
#         violation_type = str(self.ui_add_violation.comboBox_2.currentText()).strip()

#         if len(violation_no) != 4:
#             QtWidgets.QMessageBox.warning(None, "Warning", "Error: The violation_no must have 4 characters!!")
#         elif len(vehicle_license) != 8:
#             QtWidgets.QMessageBox.warning(None, "Warning", "Error: The vehicle_license must have 8 characters!!")
#         try:
#             license_check = "SELECT license_plate FROM vehicles WHERE license_plate = %s"
#             self.mycursor.execute(license_check, (vehicle_license,))
#             license_exist = self.mycursor.fetchone()
#             violation_no_check = "SELECT violation_no FROM violation WHERE violation_no = %s"
#             violation_no = self.mycursor.execute(violation_no_check, (violation_no,))
#             violation_no_exist = self.mycursor.fetchone()
#             if not license_exist:
#                 QtWidgets.QMessageBox.warning(None, "Warning", "The license of car does not exist!")
#             elif violation_no_exist:
#                 QtWidgets.QMessageBox.warning(None, "Warning", "The violation_no has been used!")
#             else:
#                 violation_insert = '''
#                         INSERT INTO violation (vehicle_license, violation_no)
#                         VALUES (%s, %s)
#                         '''
#                 violate_status_insert = '''
#                     INSERT INTO violate_status (status, fine, violate_year, violate_month, violate_date, violation_no, violation_type)
#                     VALUES (%s, %s, %s, %s, %s, %s, %s)
#                     '''
#                 self.mycursor.execute(violation_insert, (vehicle_license, violation_no))
#                 self.mycursor.commit()
#                 self.mycursor.execute(violate_status_insert, (status, fine, violate_year, violate_month, violation_no, violation_type))
#                 self.mycursor.commit()
#         except Exception as e:
#             QtWidgets.QMessageBox.critical(None, "Error", f"An error occurred: {str(e)}")