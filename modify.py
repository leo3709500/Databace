import pandas as pd

user_df = pd.read_csv('/home/jimmylin0979/Desktop/db_proj/Users_Table__Updated_.csv')

user_df = user_df.drop(['admin_ssn'], axis=1)
print(user_df.columns)
user_df.to_csv('/home/jimmylin0979/Desktop/db_proj/Users_Table__Updated_.csv')
print('The admin_ssn in user infor had be removed.')