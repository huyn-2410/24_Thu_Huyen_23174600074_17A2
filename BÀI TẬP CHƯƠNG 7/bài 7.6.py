word = input("Nhập một từ: ")

# Đảo ngược từ bằng cách sử dụng vòng lặp
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word

# Hiển thị từ ngược lại
print("Từ ngược lại là:", reversed_word)