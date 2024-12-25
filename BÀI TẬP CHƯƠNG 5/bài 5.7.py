import sqlite3
def update_column_values():
    # Kết nối tới cơ sở dữ liệu SQLite
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Giá trị mới cho cột cụ thể
    new_value = input("Nhập giá trị mới cho cột age: ")

    # Cập nhật tất cả các giá trị trong cột 'age' của bảng 'users'
    cursor.execute('UPDATE users SET age = ?', (new_value,))

    print(f"Cập nhật tất cả các giá trị của cột 'age' thành {new_value} thành công.")

    # Hiển thị các bản ghi sau khi cập nhật
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Danh sách các bản ghi sau khi cập nhật:")
    for row in rows:
        print(row)

    # Đóng kết nối
    conn.commit()
    conn.close()

# Gọi hàm để cập nhật cột
update_column_values()
