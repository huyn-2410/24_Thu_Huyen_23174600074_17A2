import sqlite3
def list_tables():
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Truy vấn danh sách các bảng trong cơ sở dữ liệu
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()

    print("Danh sách các bảng trong cơ sở dữ liệu:")
    for table in tables:
        print(f"- {table[0]}")

    # Đóng kết nối
    conn.close()

# Gọi hàm để liệt kê các bảng
list_tables()