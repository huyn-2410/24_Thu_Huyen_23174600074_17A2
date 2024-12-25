import sqlite3
def connect_to_memory_database():
    # Kết nối tới cơ sở dữ liệu trong bộ nhớ
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Lấy phiên bản SQLite
    cursor.execute('SELECT sqlite_version()')
    version = cursor.fetchone()

    print(f"SQLite Version (In-Memory): {version[0]}")

    # Đóng kết nối
    conn.close()

# Gọi hàm để kết nối và in phiên bản SQLite
connect_to_memory_database()