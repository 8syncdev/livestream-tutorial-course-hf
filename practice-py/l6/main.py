day_so = [1, 2, 3, 4, 5]
#         0  1  2  3  4

# print(day_so[1: 4])

#  Chèn: chèn vào đầu tiên, chèn vào vị trí kết thúc, chèn vào vị trí bất kì ở giữa

# Chèn vào vị trí đầu tiên

day_so[:0] = [100]


day_so[day_so.__len__():] = [100]


day_so[1:1] = [1000, 10,4,3]
# print(day_so)

# [start: stop: step] , start==stop


# List Comprehension

'''
new_list = [expression for item in iterable if condition]

expression: biểu thức hoặc là phép toán, chức năng có giá trị trả về
item: biến đại diện mỗi phần từ trong iterable khi duyệt qua
iterable: Cấu trúc dữ liệu lưu tập hợp các phần tử (list, tuple, string, ...)
'''

# a=[]
# b=[]
# print(id(a))
# print(id(b))


# def my_func(item):
#     return item * item

# day_so = [1,2,3,4,5]

# print([my_func(item) for item in day_so if item % 2 == 0])

# Phân loại số chẵn lẻ bằng list comp


# Map, filter, reduce


# Nhập giá trị list

# n = int(input())

# ds = []
# for _ in range(n):
#     ds.append(int(input()))

# ds = [int(input()) for _ in range(n)]

# print(ds)


# Nhập trên cùng 1 hàng

'''
Split trong python chuyển đổi str -> list[str]

'''

ds = input().split() # str -> list[str] -> list[int]
ds_int = [int(item) for item in ds]
print(ds_int)


# Map, filter, reduce

def fx(item):
    return item * item

func_lambda = lambda item: item * item

print(list(map(func_lambda, ds_int)))
print(ds_int)

# Filter 

print(list(filter(lambda item: item % 2 == 0, ds_int)))

# reduce

from functools import reduce

'''
ds = [1,2,3,4,5]
x=1
y=2
x = x+y=1+2=3
y = 3
x = x+y=3+3=6
y = 4
...

x = 1+2+3+4+5 = 
giá trí khởi tạo. Ví dụ initial = 100 + 1+2+3+4+5 

'''

print(reduce(lambda x, y: x + y, ds_int, 100))
print(reduce(lambda x, y: x - y, ds_int))
print(reduce(lambda x, y: x * y, ds_int))
print(reduce(lambda x, y: x / y, ds_int))


'''
https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/
https://leetcode.com/problems/find-closest-number-to-zero/description/
https://leetcode.com/problems/check-if-matrix-is-x-matrix/description/
https://leetcode.com/problems/largest-local-values-in-a-matrix/description/
'''