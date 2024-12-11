
class Manage_control:
    def manage_query(self):
        car_type = str(self.ui_manage.comboBox.currentText()).strip()
        violation_type = str(self.ui_manage.comboBox_2.currentText()).strip()    #1001, 1002, 1003, 1004, all
        inspection_type = str(self.ui_manage.comboBox_3.currentText()).strip()   #101, 102, 103, 104, 104, all
        query_conditions = []
        query_params = []

        if car_type.lower() != "所有車種":
            query_conditions.append("vehicles.type = %s")
            query_params.append(car_type)

        if violation_type.lower() != "所有違規":
            query_conditions.append("violate_status.violation_type = %s")
            query_params.append(violation_type)

        if inspection_type.lower() != "所有檢驗項目":
            query_conditions.append("inspection_status.inspect_type = %s")
            query_params.append(inspection_type)

        vehicles_query = """
        SELECT *
        FROM vehicles
        JOIN violation ON vehicles.license_plate = violation.vehicle_license
        JOIN violate_status ON violation.violation_no = violate_status.violation_no
        JOIN inspection_status ON vehicles.inspect_no = inspection_status.inspect_no
        """
        if query_conditions:
            vehicles_query += " WHERE " + " AND ".join(query_conditions)

        self.mycursor.execute(vehicles_query, tuple(query_params))

        # 打印欄位名稱
        column_names = [desc[0] for desc in self.mycursor.description]
        print("欄位名稱:")
        print(", ".join(column_names))
        print("============================")

        information = self.mycursor.fetchall()
        warning = 1
        for infor in information:
            warning = 0
            print(infor)
            print("============================")
        if warning:
            print("No result!!")