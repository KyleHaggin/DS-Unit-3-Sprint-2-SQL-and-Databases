# import important libraries
import psycopg2
import sqlite3

# setup connection information
dbname = 'xefhbwxp'
user = 'xefhbwxp'
password = '5pK_L2dDC1zRHmIrqGxMu1D8cR95vaRK'  # password here
host = 'salt.db.elephantsql.com'

# connect to elephantsql
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
print('Connection to ElephantSQL made.')
del conn
print('Connection terminated.')

# reconnect to elephantsql
pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password,
                           host=host)
print('Connection to ElephantSQL made.')
pg_curs = pg_conn.cursor()

# create character table in ElephantSQL
create_character_table = """
    CREATE TABLE charactercreator_character (
        character_id SERIAL PRIMARY KEY,
        name VARCHAR(30),
        level INT,
        exp INT,
        hp INT,
        strength INT,
        intelligence INT,
        dexterity INT,
        wisdom INT
    );
    """
# commented out due to creation already occuring
# pg_curs.execute(create_character_table)

# check that the tables are in ElephantSQL
show_tables = """
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname != 'pg_catalog'
AND schemaname != 'information_schema';
"""
pg_curs.execute(show_tables)
print(pg_curs.fetchall())

# connect to the rpg database
pathSQL = 'module1-introduction-to-sql/rpg_db.sqlite3'
sl_conn = sqlite3.connect(pathSQL)
sl_curs = sl_conn.cursor()
characters = sl_curs.execute(
    'SELECT * from charactercreator_character;'
    ).fetchall()
print(characters[0])

# insert all the data from rpg into ElephantSQL
for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom)
        VALUES """ + str(character[1:]) + ';'
    pg_curs.execute(insert_character)
    # test commented out to streamline load times, uncomment if using
# pg_curs.execute('SELECT * FROM charactercreator_character;')
# print(pg_curs.fetchall())
pg_curs.close()
pg_conn.commit()

# assert
pg_curs = pg_conn.cursor()
pg_curs.execute('SELECT * FROM charactercreator_character;')
pg_characters = pg_curs.fetchall()
for character, pg_character in zip(characters, pg_characters):
    assert character == pg_character
