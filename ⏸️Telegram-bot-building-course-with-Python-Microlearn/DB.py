import sqlite3

connection = sqlite3.connect("user.db")
cursor = connection.cursor() 

create_table_query = """
    CREATE TABLE IF NOT EXISTS users(
        id integer primary key,
        first_name text,
        last_name text,
        phone_number text
    );
"""

cursor.execute(create_table_query)
connection.commit()
connection.close()

sample_data_query = """
    INSERT INTO users (id, first_name, last_name, phone_number)
    VALUES (?, ?, ?, ?)
"""

sample_data = [(8759, 'Ehsan', 'Abd', '987456138576'),
               (5432, 'Jack', 'Abd', '987456138576'),
               (8745, 'Sarah', 'Abd', '987456138576'),
               (9856, 'Maryam', 'Abd', '987456138576')]

# with sqlite3.connect('user.db') as connection:
#     cursor = connection.cursor()
#     cursor.executemany(sample_data_query, sample_data)

fetch_data_query = """
    SELECT id, first_name, last_name, phone_number FROM users
"""
rows = []

with sqlite3.connect('user.db') as connection:
    cursor = connection.cursor()
    cursor.execute(fetch_data_query)
    rows = cursor.fetchall()

for row in rows:
    print(f'ID:{row[0]}, FN:{row[1]}, LN:{row[2]}, PN:{row[3]}')