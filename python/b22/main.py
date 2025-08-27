import pandas as pd
import numpy as np

# data_missing = {
#     'A': [1, 2, np.nan, 4],
#     'B': [5, np.nan, np.nan, 8]
# }

# df = pd.DataFrame(data_missing)
# print(df)


# df_dropped = df.dropna()

# print(df_dropped)

# df_fill = df.fillna(value=0)
# print(df_fill)


# df1 = pd.DataFrame({
#     'ID': ['A01', 'A02', 'A03'],
#     'Tên': ['An', 'Bình', 'Chi']
# })

# df2 = pd.DataFrame({
#     'ID': ['A01', 'A02', 'A04'],
#     'Điểm': [8,9,7]
# })

# df_merged = pd.merge(df1, df2, on='ID', how='')

# print(df_merged)

# df = pd.read_csv('./data.csv')
# df.to_excel('./example.xlsx')

# def apply_salary_gt_5000(salary):
#     if salary > 5000:
#         return 'Lương > 5000'
#     return 'Lương <= 5000'

# df['Kết quả'] = df['SALARY'].apply(apply_salary_gt_5000)

# print(df)

# data_sales = {
#     'Ngày': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
#     'Thành phố': ['HN', 'HCM', 'DN', 'BD'],
#     'Sản phẩm': ['A', 'B', 'A', 'A'],
#     'Doanh thu': [100,50,200,50]
# }

# df = pd.DataFrame(data_sales)

# print(df.pivot(index='Thành phố', columns='Sản phẩm', values='Doanh thu',))

# excel_df = pd.read_excel('./example.xlsx')

# print(excel_df)

# import os

# os.system()