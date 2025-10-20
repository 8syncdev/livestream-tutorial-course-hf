# str_a = 'a'
# str_b = 'a'

# print(id(str_a))
# print(id(str_b))

# str_example = 'Python là ngôn ngữ lập trình'

# print(str_example[0])
# print(str_example[-len(str_example)])
# print(str_example[-str_example.__len__()])


# original = "Ví dụ về chuỗi chuỗi"

# new_str = original.replace("chuỗi", "string")

# print(original)
# print(new_str)


# str1 = "hello"
# str2 = "world"

# # print(str1 + " " + str2)

# # print(str1 * 10)

# print("h" in str1)

# n = int(input())

# String Formatting định dạng chuỗi

name = "alex"
age = 30

# print("My name is %s, age is %i" % (name, age))
# print("My name is %s, age is %.10f" % (name, age))


# Format
# print("Tôi tên là {}, tuổi là {:.10f}".format(name, age))
#                                         0     1
# Định nghĩa giá trị theo vị trí

# print("Tôi tên là {1}, tuổi là {0}".format(name, age))

# f-string python 3.6+

# print(f"Tôi là {name}, {age} tuổi")

'''
Căn chỉnh format bố cục string
'''

# menu = "Menu"

# print(f"{menu:.^50}")
# print(f"{menu:.<50}")
# print(f"{menu:.>50}")


# Các phương thức xử lý chuỗi quan trọng

# text = "  nGuyen vAn a   "

# # loại bỏ khoảng trắng
# print(text.strip()) # "nGuyen vAn a"

# # Chuyển đổi chữ hoa/thường
# print(text.upper())
# print(text.lower())

# # Kiểm tra chuỗi
# print(text.isalpha())

# # chứa các giá trị là chuỗi số dạng decimal(0-9). Không chưa các unicode numeric ví dụ như là fraction, superscript, Roman numerals
# print(text.isdigit())
# print(text.isnumeric())

# words = text.split() # tách từng từ theo khoảng trắng str -> list[str]

# print(words)

# print("+".join(words))

# print(text.find("nGuyen"))
# print(text.index("nGuyen"))


# Mutiline


multi_line = '''
Đây là chuỗi
với nhiều dòng
với nhiều dòng
với nhiều dòng
với nhiều dòng
'''

print("Tên\tGiá")
print("Tên\nGiá")
print("Tên \\n Giá")


# Cách dùng raw string: vô hiệu hóa các kí tự đặc biệt

path = r"C:\WorkSpace\livestream-tutorial-course-hf\practice-py\l3\n"

print(path)
print(path)


'''
Tóm tắt:
1. Chuỗi trong python có tính bất biến (immutable) và được biểu diễn sử dụng được unicode
2. Có nhiều cách tạo chuỗi: nháy đơn, nháy kép, hoặc dấu 3 nháy tương tác trên nhiều dòng
3. Phương thức là các hàm chức năng có sẵn
4. Nhiều cách định dạng chuỗi %, format, f-string
5. Vô hiệu hóa kí tự đặc biệt trong chuỗi bằng raw string r""
'''



