from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox
class Manage_control:
    def __init__(self, is_edit=False):
        # 初始化狀態變量
        self.is_edit = is_edit

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

    def get_query_results(self):
        car_type = str(self.ui_manage.comboBox.currentText()).strip()
        violation_type = str(self.ui_manage.comboBox_2.currentText()).strip()
        inspection_type = str(self.ui_manage.comboBox_3.currentText()).strip()
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
        return self.mycursor.fetchall()  # 返回查詢結果
    def setup_table(self):
        self.is_edit = not self.is_edit
        if self.is_edit:
            self.ui_manage.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        else:
            self.ui_manage.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # 根據當前模式設置表格的編輯觸發器
        if self.is_edit:
            self.ui_manage.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
            self.ui_manage.tableView.setSelectionBehavior(self.ui_manage.tableView.SelectRows)
            self.ui_manage.tableView.setSelectionMode(self.ui_manage.tableView.SingleSelection)
        for row in range(self.ui_manage.model.rowCount()):
            for column in range(self.ui_manage.model.columnCount()):
                item = self.ui_manage.model.item(row, column)
                if item: 
                    item.setFlags(item.flags() | Qt.ItemIsEditable)
        self.ui_manage.model.itemChanged.connect(self.on_item_changed)


    def on_item_changed(self, item):
        original_value = self.ui_manage.model.data(item.index(), Qt.EditRole)
        new_value = item.text()
        row = item.row()
        column = item.column()
        column_name = self.ui_manage.model.horizontalHeaderItem(column).text()
        if column_name  == "license_plate":
            reply = QMessageBox.question(
                self.ui_manage.tableView, 
                "Error", 
                f"The license_plate can not be changed!!",
                QMessageBox.Yes
            )
            if reply:
                item.setText(original_value)    #reset to origin.
                return  #halt the process.

        #get the primary key
        license_plate = self.ui_manage.model.item(row, 1).text()  
        # update database
        update_query = f"UPDATE vehicles SET {column_name} = %s WHERE license_plate = %s"

        try:
            self.mycursor.execute(update_query, (new_value, license_plate))
            self.mydb.commit()
            print(f"Successfully updated {column_name} to {new_value} for license_plate {license_plate}")
        except Exception as e:
            print(f"Failed to update database: {e}")
            self.mydb.rollback()
    def delete_item(self):
        # Get the index of the selected row
        selected_indexes = self.ui_manage.tableView.selectionModel().selectedRows()
        
        if not selected_indexes:
            # No row selected
            QMessageBox.warning(self.ui_manage.tableView, "Warning", "No row selected.")
            return

        # Assuming license_plate is in the second column (index 1)
        row = selected_indexes[0].row()
        license_plate = self.ui_manage.model.item(row, 1).text()
        
        # Confirm deletion
        reply = QMessageBox.question(
            self.ui_manage.tableView, 
            "Confirm Deletion", 
            f"Are you sure you want to delete the row with license plate {license_plate}?",
            QMessageBox.Yes | QMessageBox.No
        )
        
        if reply == QMessageBox.No:
            return  # User canceled the deletion

        # Delete from database
        delete_query = "DELETE FROM vehicles WHERE license_plate = %s"
        try:
            self.mycursor.execute(delete_query, (license_plate,))
            self.mydb.commit()
            print(f"Successfully deleted row with license_plate {license_plate}")
            
            # Remove the row from the table view
            self.ui_manage.model.removeRow(row)
            
        except Exception as e:
            print(f"Failed to delete row from database: {e}")
            self.mydb.rollback()
            QMessageBox.critical(self.ui_manage.tableView, "Error", "Failed to delete the row from the database.")

    def toggle_edit_mode(self):
        # 切換編輯模式
        self.is_edit = not self.is_edit
        if self.is_edit:
            self.ui_manage.tableView.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        else:
            self.ui_manage.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setup_table()  # 更新表格設置
