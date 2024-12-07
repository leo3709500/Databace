####this program is used to initialize the table.####
####And it will retrieve the data from the .csv file####

import pymysql
import pandas as pd

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='jimmylin0320',
    database='carsys'
)
mycursor = mydb.cursor()

users_file_path = '/home/jimmylin0979/Desktop/db_proj/Users_Table__V6_.csv'
vehicles_file_path = '/home/jimmylin0979/Desktop/db_proj/Vehicles_Table__V6_.csv'
violate_status_file_path = '/home/jimmylin0979/Desktop/db_proj/Violate_Status_Table__V6_.csv'
inspection_status_file_path = '/home/jimmylin0979/Desktop/db_proj/Inspection_Status_Table__V6_.csv'
violation_file_path = '/home/jimmylin0979/Desktop/db_proj/Violation_Table__V6_.csv'

users_data = pd.read_csv(users_file_path)
vehicles_data = pd.read_csv(vehicles_file_path)
violate_status_data = pd.read_csv(violate_status_file_path)
inspection_status_data = pd.read_csv(inspection_status_file_path)
violation_data = pd.read_csv(violation_file_path)

# 清空各個表格
tables = ['violation', 'inspection_status', 'violate_status', 'vehicles', 'users']
try:
    for table in tables:
        mycursor.execute(f"TRUNCATE TABLE {table};")
    print("All tables have been cleared.")
except Exception as e:
    print(f"Error clearing tables: {e}")


for index, row in users_data.iterrows():
    sql = """INSERT INTO users (name, ssn, password, mail, regis_date, address, cellphone, year, month, date) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['name'], 
        row['ssn'], 
        row['password'], 
        row['mail'],
        row['regis_date'],
        row['address'],
        row['cellphone'],
        row['year'],
        row['month'],
        row['date']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in vehicles_data.iterrows():
    sql = """INSERT INTO vehicles (type, license_plate, register_date, inspect_No, user_ssn) 
             VALUES (%s, %s, %s, %s, %s)"""
    values = (
        row['type'], 
        row['license_plate'], 
        row['register_date'], 
        row['inspect_No'],
        row['user_ssn']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in violate_status_data.iterrows():
    sql = """INSERT INTO violate_status (status, fine, date, violation_no, violation_type) 
             VALUES (%s, %s, %s, %s, %s)"""
    values = (
        row['status'], 
        row['fine'], 
        row['date'], 
        row['violation_no'],
        row['violation_type']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in inspection_status_data.iterrows():
    sql = """INSERT INTO inspection_status (status, inspect_no, next_time, inspect_fee, inspect_type) 
             VALUES (%s, %s, %s, %s, %s)"""
    values = (
        row['status'], 
        row['inspect_no'], 
        row['next_time'], 
        row['inspect_fee'],
        row['inspect_type']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in violation_data.iterrows():
    sql = """INSERT INTO violation (vehicle_license, violation_no) 
             VALUES (%s, %s)"""
    values = (
        row['vehicle_license'], 
        row['violation_no']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

# 確認變更
mydb.commit()

# 關閉資料庫連線
mycursor.close()
mydb.close()
print('All the table had been initialized successfully!!')