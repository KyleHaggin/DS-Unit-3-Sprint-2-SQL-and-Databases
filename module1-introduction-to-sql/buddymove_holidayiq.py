# import important libraries
import pandas as pd
import sqlite3 as sq


# import the data with pandas
pathCSV = 'module1-introduction-to-sql/buddymove_holidayiq.csv'
pathSQL = 'module1-introduction-to-sql/buddymove_holidayiq.sqlite3'
df = pd.read_csv(pathCSV)

# create user_id instead of user id
df['User_Id'] = df['User Id']
df.head(10)

# create connection and transfer data to SQL
conn = sq.connect(pathSQL)
df.to_sql('review', con=conn)
curs = conn.cursor()

# execute code to find length of file, should be 249
curs.execute('SELECT COUNT(User_Id) FROM review;').fetchall()

# execute code to find the number of users who reviewed 100+ in both nature
# and shopping
curs.execute('SELECT COUNT(DISTINCT "User_Id") FROM review WHERE Nature >= '
             '100 AND Shopping >= 100').fetchall()
