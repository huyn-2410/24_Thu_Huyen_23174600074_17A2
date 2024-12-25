import sqlite3
def print_sqlite_version():
    conn=sqlite3.connect('example.db')
    cursor=conn.cursor()
    cursor.execute('SELECT sqlite_version()')
    version=cursor.fetchone()
    print(f"SQLite Version: {version[0]}")
    conn.close()
print_sqlite_version()