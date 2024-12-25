import sqlite3
# Kết nối tới cơ sở dữ liệu SQLite
def delete_specific_row():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # Nhập ID của hàng cần xóa
    row_id = input("Nhập ID của hàng cần xóa: ")

    # Xóa hàng cụ thể trong bảng 'users'
    cursor.execute('DELETE FROM users WHERE id = ?', (row_id,))

    if cursor.rowcount > 0:
        print(f"Đã xóa thành công hàng có ID = {row_id}.")
    else:
        print(f"Không tìm thấy hàng có ID = {row_id}.")

    # Hiển thị các bản ghi còn lại
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("Danh sách các bản ghi còn lại:")
    for row in rows:
        print(row)

    # Đóng kết nối
    conn.commit()
    conn.close()

# Gọi hàm để xóa hàng cụ thể
delete_specific_row()
