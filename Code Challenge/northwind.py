# import important libraries
import sqlite3

# Connect to database
pathSQL = 'northwind_small.sqlite3'
conn = sqlite3.connect(pathSQL)
curs = conn.cursor()

# Part2
# write code to answer questions
print(curs.execute(
    'SELECT * FROM product ORDER BY UnitPrice DESC LIMIT 10'
).fetchall())

averageAge = curs.execute(
    'SELECT AVG(HireDate - BirthDate) FROM Employee'
).fetchall()
print(averageAge)

# Part3
query = """
SELECT Supplier.CompanyName, Product.UnitPrice, Product.ProductName
FROM Product
INNER JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""
print(curs.execute(query).fetchall())

print(curs.execute(
    """
    SELECT CategoryName
    FROM Product
    INNER JOIN Category ON Product.CategoryId = Category.Id
    GROUP BY CategoryId
    ORDER BY COUNT(*) DESC
    LIMIT 1
    """
).fetchall())
