# import important libraries
import sqlite3

# Connect to database
pathSQL = 'northwind_small.sqlite3'
conn = sqlite3.connect(pathSQL)
curs = conn.cursor()

# write code to answer questions
print(curs.execute(
    'SELECT * FROM product ORDER BY UnitPrice DESC LIMIT 10'
).fetchall())

averageAge = curs.execute(
    'SELECT AVG(HireDate - BirthDate) FROM Employee'
).fetchall()
print(averageAge)
