import numpy as np

# arr_1d = np.array([10, 20, 30, 40, 50], dtype=np.int8)

# # print(arr_1d.shape)
# # print(arr_1d.ndim)
# # print(arr_1d.size)
# # print(arr_1d.dtype)

# # print(arr_1d[1])


# # Đối với vector 2D, arr[hàng, cột]

arr_2d = np.array([
#    0 1 2
    [1,2,3], # 0
    [4,5,6], # 1
    [7,8,9]  # 2
])

# # list_2d = [
# # #    0 1 2
# #     [1,2,3], # 0
# #     [4,5,6], # 1
# #     [7,8,9]  # 2
# # ]

# # print(list_2d[1][2])

# # print(arr_2d[1, 2])

# # start: stop: step
# '''
# start: mặc định là 0
# stop: mặc định là kết thúc n-1
# step: mặc định là 1
# '''

# arr_1d = np.arange(10)

# print(arr_1d)

# print(arr_1d[2:5])

# print(arr_1d[:4])

# print(arr_1d[5:])



'''
Cú pháp: arr[hang->slicing(start:stop), cot->slicing(start:stop)]
'''

# print(arr_2d[:2,:2])


# print(arr_2d[0, :])
# print(arr_2d[:, 0])

# arr = np.arange(5)

# slice_arr = arr[1:3].copy()

# slice_arr[0] = 99

# print(slice_arr)
# print(arr)


# list_a = [1,2,3,4,5]
# list_b = list_a[1:3]
# list_b[0] = 99
# print(id(list_a))
# print(id(list_b))


# bool_arr = arr_2d > 2

# print(bool_arr)

# print(arr_2d[bool_arr])
# print(arr_2d[arr_2d > 2])
# print(arr_2d[arr_2d % 2 == 1])