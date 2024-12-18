import pymysql

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='leo030102' # 請修改為你的 MySQL 密碼
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS carsys;")
print("資料庫 'carsys' 已成功創建或已存在。")

mycursor.close()