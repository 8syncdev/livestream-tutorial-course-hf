import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Định nghĩa style màu sắc cho biểu đồ Seaborn
sns.set_theme(style='whitegrid')


tips = sns.load_dataset("tips")

sns.scatterplot(data=tips, x="total_bill", y="tip", hue="smoker", style="time", markers=["o", "s"])

# print(tips.head())

# sns.relplot(data=tips, x="total_bill", y="tip", hue="day", palette="Greys")


# kde=True vẽ thêm đường cong ước tính mật độ
# sns.histplot(data=tips, x="total_bill", kde=True)


# Box plot: tóm tắt phân bố của dữ liệu cho thấy giá trị trung vị
# sns.boxplot(data=tips, x="day", y='total_bill')

# data = pd.DataFrame(np.random.rand(10, 12))

# sns.heatmap(data=data, annot=True, fmt='.2f', cmap='viridis')


# Biểu đồ cặp (Pair Plot)

# iris = sns.load_dataset("iris")

# sns.pairplot(data=iris, hue="species")

# Diverging Palettes

# np.random.seed(0)
# data = pd.DataFrame(np.random.randn(5,5).cumsum(axis=1),
#                     columns=pd.date_range('2025-01-01', periods=5, freq='B'),
#                     index=['A', 'B', 'C', 'D', 'E'])

# correlation_matrix = data.corr()

# sns.heatmap(correlation_matrix, annot=True, cmap='vlag', center=0)

plt.savefig("ex8.png")