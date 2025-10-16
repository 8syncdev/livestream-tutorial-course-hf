# str_val = "hello"

# print(str_val[:3])
# print(str_val[:])

# # Sử dụng Negative indexing (vị trí âm)

# text = "Python is fun"



# # print(text[-4:])

# print(text[::-1])


# text = "fkdsflksdfsmkfj"
# print(text[::2])

# print(text[3:0])
# print(text[:text.__len__()+10])

text = "Python is great"

# print(text[10: 5: -1]) # start -> stop + 1 đối với step âm

full_name = "John Doe"
# first_name = full_name[:full_name.index(" ")]
# last_name = full_name[full_name.index(" ")+1:]

# print(first_name, last_name)


# first_name, last_name = full_name.split()

# print(first_name, last_name)


# email = "user@example.com" # example.com
# print(email[email.index('@')+1:])


# Các lỗi hay gặp trong xử lí chuỗi

# IndexError: truy cập vào vị trí mà vượt phạm vi cho phép
# text = "hello" 
# print(text[10])


# Tóm tắt các ý về string slicing
'''
1. Cú pháp: [start: stop: step]. Mặc định start=0, stop=n, step=1
2. Indexing bắt đầu từ 0->n-1, -n->-1
3. step có thể là dương hoặc âm. Lưu ý trong trường hợp step là số âm start->stop+1
'''

# Thao tác với String - String Manipulation

# uper, lower, replace, split, join


# s = "hello"
# # s[0] = "H" # Sai vì cố tình thay đổi giá trị trong vùng nhớ ban đầu
# new_str = s.replace('h', "H")
# print(new_str)


# s = "hello"
# char_list = list(s)

# char_list.insert(3, "HI")

# join_str = "".join(char_list)

# print(join_str)

#  Ửu điểm:
'''
- Dễ dàng thao tác với các ký tự riêng lẻ
- Phù hợp với các thao tác phức tập

Nhược điểm:
- Tốn bộ nhớ hơn so với cách dùng chuỗi mới
'''


# Sử dụng module array Cách 2

# import array as arr

# s = "Word"

# # Chuyển đổi chuỗi thành mảng Unicode
# char_array = arr.array('u', s) # array('u', ['W','o', 'r', 'd'])

# char_array.insert(3, "L") # Chèn kí tự L vào vị trí số 3

# join_str = char_array.tounicode() # Kết tất cả phần tử lại

# print(join_str)

# '''
# Khi nào cần sử dụng:
# - Khi cần tối ưu hóa bộ nhớ với chuỗi dài
# - Khi làm việc với các kiểu dữ liệu khác nhau trong một mảng
# '''


# import io

# s = "Worldaaa"
# #           ......
# #       3
# #       LDD : lda -> LDD
# sio = io.StringIO(s)

# sio.seek(s.__len__()) # Di chuyển tới vị trí số 3 là chữ cái L

# sio.write("LDD") # Thay thế chữ l bằng LDD

# val = sio.getvalue()

# print(val)


# Đảo ngược chuỗi 

# s = "Python"

# char_list = list(s)
# char_list.reverse()

# rev_str = ''.join(char_list)
# print(rev_str)


s = "Hello World"

trans_table = s.maketrans("HW", "JZ")
'''
H-J
W-Z
'''

res = s.translate(trans_table)

print(res)


