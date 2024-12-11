

import pymysql

def initialize_database():
    # 連接資料庫
    mydb = pymysql.connect(
        host='localhost',
        user='root',
        password='jimmylin0320',
        database='carsys'
    )
    mycursor = mydb.cursor()
    
    # 刪除已存在的表
    mycursor.execute("DROP TABLE IF EXISTS users")
    mycursor.execute("DROP TABLE IF EXISTS vehicles")
    mycursor.execute("DROP TABLE IF EXISTS violate_status")
    mycursor.execute("DROP TABLE IF EXISTS inspection_status")
    mycursor.execute("DROP TABLE IF EXISTS violation")
    
    # 重新建立表
    mycursor.execute("""CREATE TABLE users (
                        name VARCHAR(40), 
                        ssn VARCHAR(10), 
                        password VARCHAR(40), 
                        mail VARCHAR(255), 
                        regis_year VARCHAR(4),
                        regis_month VARCHAR(2),
                        regis_date VARCHAR(2), 
                        address VARCHAR(50), 
                        cellphone VARCHAR(10),
                        birth_year VARCHAR(4), 
                        birth_month VARCHAR(2), 
                        birth_date VARCHAR(2), 
                        PRIMARY KEY(ssn))""")
    
    mycursor.execute("""CREATE TABLE vehicles (
                        type VARCHAR(20), 
                        license_plate VARCHAR(8), 
                        car_year VARCHAR(4),
                        car_month VARCHAR(2),
                        car_date VARCHAR(2), 
                        inspect_no VARCHAR(20), 
                        user_ssn VARCHAR(10),
                        PRIMARY KEY(license_plate))""")
    
    mycursor.execute("""CREATE TABLE violate_status (
                        status VARCHAR(1), 
                        fine INTEGER(5), 
                        violate_year VARCHAR(4),
                        violate_month VARCHAR(2),
                        violate_date VARCHAR(2), 
                        violation_no VARCHAR(10),
                        violation_type VARCHAR(4),
                        PRIMARY KEY(violation_no))""")
    
    mycursor.execute("""CREATE TABLE inspection_status (
                        status VARCHAR(2), 
                        inspect_no VARCHAR(10), 
                        next_year VARCHAR(4),
                        next_month VARCHAR(2),
                        next_date VARCHAR(2), 
                        inspect_fee INTEGER(4),
                        inspect_type VARCHAR(3),
                        PRIMARY KEY(inspect_no))""")
    
    mycursor.execute("""CREATE TABLE violation (
                        vehicle_license VARCHAR(8), 
                        violation_no VARCHAR(10),
                        PRIMARY KEY (vehicle_license, violation_no))""")
    

    # 提交更改並關閉連接
    mydb.commit()
    mydb.close()

# 執行初始化函式
initialize_database()
