# Khởi tạo một list rỗng
empty_list = []
empty_list = list()

# [] khác list(), list() ép kiểu dữ liệu về kiểu dữ liệu list

# List chứa các phần tử khác nhau

mixed_list = ["Python", 3.14, 42, True, [1,2,3]]

# print(empty_list, mixed_list)

'''
Lưu ý:
- Các phần tử trong list thì được đặt cách nhau bởi dấu phẩy.
- List có thể chứa các list khác (nested list)
- Khởi tạo bằng dấu ngoặc vuông[], dùng cấu trúc ép kiểu list()
'''

# Truy cập vào bên trong list

'''
list_name[index]
index: 0->n-1, -n->-1
'''

# day_so = [1,2,3,4,5]
# #         0 1 2 3 4

# # Phần tử đầu tiên
# print(day_so[0])
# print(day_so[-day_so.__len__()])
# print(day_so[-len(day_so)])

# # Phần tử cuối cùng
# print(day_so[-1])


# # Phần tử bất kì
# print(day_so[1])

'''
Các built-in function: append, remove, pop, sort, reverse, insert, copy, count, index
'''


# Count: là hàm chức năng đếm số lần xuất hiện của 1 giá trị

numbers = [1,2,3,2,4,2,5]
#          0 1 2 3 4 5 6

# count = numbers.count(2)

# print(count)


# Index: tìm vị trí xuất hiện đầu tiên

# print(numbers.index(2)) # tìm số lần xuất hiện của 2 toàn bộ vị trí

# def list_all_index(_list: list, value):
#     ds = []
#     while value in set(_list): # dừng khi mà value không còn nằm trong list nữa
#         ds.append(_list.index(value)) # thêm giá trị vào bên trong list
#         _list[_list.index(value)] = None # thay giá trị tại vị trí đã tìm thấy bằng 1 giá trị khác

#     return ds


# print(list_all_index(numbers, 2))


# Reverse(): đảo ngược thứ tự của list, hàm chức năng built sẵn trong python là hàm reversed()


# numbers.reverse()

# new_numbers = reversed(numbers)

# print(numbers)
# print(list(new_numbers))


# a=[]
# b=a.copy()
# b.append(1)

# print(a)


# Sort và sorted

# numbers.sort()


def solve(item):
    if item % 2 == 1:
        return -item # giãm dần là số âm
    return item # tăng là số dương

# tại sao giá trị item dương là tăng dần còn âm là giãm dần
# item là từng giá trị duyệt qua trong list
# new_nb = sorted(numbers, key=solve) 

# '''
# def sorted(list, key):
#     for item in list:
#         key(item)
#         ...
# '''

# print(numbers)
# print(new_nb)


str_ = list(input())

# dùng join để kết lại, dùng array tối ưu hơn



