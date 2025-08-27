'''
1. Series
- Giống như các cột trong 1 bảng dữ liệu, giống array numpy
- index
'''

# Series có thể khởi tạo từ 1 list, array, dict

import pandas as pd

# data = [10, 20, 30, 40, 50]

# s = pd.Series(data)

# print(s)

# DataFrame: 

# data = {
#     'Tên': ['An', 'Bình', 'Chi', 'Dũng'],
#     'Tuổi': [22, 25, 21, 28],
#     'Thành phố': ['HN', 'TPHCM', 'Đà Nẵng', 'HN']
# }

# df = pd.DataFrame(data=data)

# df.to_csv('./export_data.csv', index=False)
# print(df)


df = pd.read_csv('./data.csv')
print(df.head())

# Xem 5 dòng cuối trong dataframe
# print(df.tail())

# Xem thông tin tổng quan về dataframe(dtype, số lượng giá trị không bị null, ...)
# df.info()


# print(df.describe())

# Lựa chọn và lọc dữ liệu


# print(type(df['SALARY']))


# Xác chỉ mục sử dụng location cho dataframe

print(df.iloc[0])




