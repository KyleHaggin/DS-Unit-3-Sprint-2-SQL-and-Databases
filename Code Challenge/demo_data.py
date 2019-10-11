# import important libraries
import sqlite3
import pandas as pd

# Part 1 Code

# Open connection to blank SQL file
pathSQL = 'demo_data.sqlite3'
conn = sqlite3.connect(pathSQL)
curs = conn.cursor()

# Create a blank table in demo_data
create_table = """
    CREATE TABLE demo (
        s VARCHAR(1),
        x INT,
        y INT
    );
    """
# Commented out to prevent errors when rerunning the code, uncomment to create
# the table anew
# curs.execute(create_table)

# Create the data
data = {'s': ['g', 'v', 'f'],
        'x': [3, 5, 8],
        'y': [9, 7, 7]
        }
df = pd.DataFrame(data)
print(df.head(3))

# Insert data into the table
# Commented out to prevent errors when rerunning the code, uncomment to insert
# the data anew
# df.to_sql('demo', con=conn)

print(curs.execute('SELECT COUNT(*) FROM demo').fetchall())
print(curs.execute('SELECT COUNT(*) FROM demo WHERE x>=5 AND y>=5').fetchall())
print(curs.execute('SELECT COUNT(DISTINCT y) FROM demo').fetchall())
