import sqlite3
def count_records():
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Đếm số bản ghi trong bảng 'users'
    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    print(f"Số bản ghi trong bảng 'users': {count}")

    # Đóng kết nối
    conn.close()

# Gọi hàm để đếm số bản ghi
count_records()