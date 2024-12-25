import sqlite3 
def create_table_and_insert_records():
    # Kết nối hoặc tạo cơ sở dữ liệu SQLite
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Tạo bảng mới
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
    ''')

    # Chèn một số bản ghi vào bảng
    users = [
        (1, 'Alice', 30),
        (2, 'Bob', 25),
        (3, 'Charlie', 35)
    ]
    cursor.executemany('INSERT OR IGNORE INTO users (id, name, age) VALUES (?, ?, ?)', users)

    # Truy vấn tất cả các hàng trong bảng
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    print("Danh sách các bản ghi trong bảng 'users':")
    for row in rows:
        print(row)

    # Đóng kết nối
    conn.commit()
    conn.close()

# Gọi hàm để tạo bảng, chèn dữ liệu và hiển thị các bản ghi
create_table_and_insert_records()
