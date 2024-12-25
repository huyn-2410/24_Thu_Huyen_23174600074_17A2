import sqlite3
def create_database_and_table():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')
    print("Database and table 'users' have been created successfully.")
    conn.commit()
    conn.close()


create_database_and_table()