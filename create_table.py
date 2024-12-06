import pymysql
#### the function of this program is to create a table used to store the infor in the future. #### 
mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='jimmylin0320',
    database='carsys'
)

mycursor = mydb.cursor()
# mycursor.execute("""CREATE TABLE users (name VARCHAR(40), ssn VARCHAR(10), password VARCHAR(40), 
#                  mail VARCHAR(255), regis_date DATETIME, address VARCHAR(50), cellphone VARCHAR(10),
#                  year VARCHAR(4), month VARCHAR(2), date VARCHAR(2), admin_ssn VARCHAR(10),
#                  PRIMARY KEY(ssn))""")

# mycursor.execute("""CREATE TABLE vehicles (type VARCHAR(20), license_plate VARCHAR(8), register_date DATETIME, 
#                  inspect_No VARCHAR(20), user_ssn VARCHAR(10),
#                  PRIMARY KEY(license_plate))""")

# mycursor.execute("""CREATE TABLE violate_status (status VARCHAR(2), fine INTEGER(5), date DATETIME, violation_no VARCHAR(10),
#                 PRIMARY KEY(violation_no))""")

# mycursor.execute("""CREATE TABLE inspection_status (status VARCHAR(2), inspect_no VARCHAR(10), next_time DATETIME, inspect_fee INTEGER(4),
#                 PRIMARY KEY(inspect_no))""")

# mycursor.execute("""CREATE TABLE violation (vehicle_license VARCHAR(8), violation_no VARCHAR(10),
#                 PRIMARY KEY (vehicle_license, violation_no))""")

# mydb.close()

####this is modification of the original table
mycursor.execute("ALTER TABLE users MODIFY COLUMN regis_date DATE")
mycursor.execute("ALTER TABLE vehicles MODIFY COLUMN register_date DATE")
mycursor.execute("ALTER TABLE violate_status MODIFY COLUMN date DATE")
mycursor.execute("ALTER TABLE inspection_status MODIFY COLUMN next_time DATE")