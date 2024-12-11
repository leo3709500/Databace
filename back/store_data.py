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

users_file_path = '/home/jimmylin0979/Desktop/db_proj/data/Users_Table__V8_.csv'
vehicles_file_path = '/home/jimmylin0979/Desktop/db_proj/data/Vehicles_Table__V8_.csv'
violate_status_file_path = '/home/jimmylin0979/Desktop/db_proj/data/Violate_Status_Table__V8_.csv'
inspection_status_file_path = '/home/jimmylin0979/Desktop/db_proj/data/Inspection_Status_Table__V8_.csv'
violation_file_path = '/home/jimmylin0979/Desktop/db_proj/data/Violation_Table__V8_.csv'

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
    sql = """INSERT INTO users (name, ssn, password, mail, regis_year, regis_month, regis_date, 
             address, cellphone, birth_year, birth_month, birth_date) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['name'], 
        row['ssn'], 
        row['password'], 
        row['mail'],
        row['regis_year'],
        row['regis_month'],
        row['regis_date'],
        row['address'],
        row['cellphone'],
        row['birth_year'],
        row['birth_month'],
        row['birth_date']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in vehicles_data.iterrows():
    sql = """INSERT INTO vehicles (type, license_plate, car_year, car_month, car_date, inspect_no, user_ssn) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['type'], 
        row['license_plate'], 
        row['car_year'],
        row['car_month'],
        row['car_date'], 
        row['inspect_no'],
        row['user_ssn']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in violate_status_data.iterrows():
    sql = """INSERT INTO violate_status (status, fine, violate_year, violate_month, violate_date, violation_no, violation_type) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['status'], 
        row['fine'], 
        row['violate_year'],
        row['violate_month'],
        row['violate_date'], 
        row['violation_no'],
        row['violation_type']
    )
    try:
        mycursor.execute(sql, values)
    except Exception as e:
        print(f"Error inserting row {index}: {e}")

for index, row in inspection_status_data.iterrows():
    sql = """INSERT INTO inspection_status (status, inspect_no, next_year, next_month, next_date, inspect_fee, inspect_type) 
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (
        row['status'], 
        row['inspect_no'], 
        row['next_year'],
        row['next_month'],
        row['next_date'], 
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