import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x = [1, 2, 3, 4, 5]
# y = [2,3,5,7,11]
# plt.plot(x, y)

# plt.title('Biểu đồ đơn giản')
# plt.xlabel('Trục X')
# plt.ylabel('Trục Y')

# plt.savefig('example.png')


# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)

# # Vẽ hai đường trên cùng một biểu đồ
# plt.plot(x, y1, color='blue', linestyle='--', linewidth=2, marker='o', markersize=4, label='Sin(x)')
# plt.plot(x, y2, color='#FF0000', linestyle=':', linewidth=2, marker='x', markersize=4, label='Cos(x)')


# plt.title('Biểu đồ đơn giản')
# plt.xlabel('Trục X')
# plt.ylabel('Trục Y')

# plt.grid(True)

# plt.legend()

# plt.xlim(0, 10)
# plt.ylim(-1.5, 1.5)

# plt.savefig('ex2.png',dpi=300)

fig, ax = plt.subplots(figsize=(8, 6)) # rộng x cao

x = np.linspace(0, 10, 100)
y = np.sin(x)

ax.plot(x, y, label='Sin(x)')

ax.set_title('Hình con')
ax.set_xlabel('Trục X')
ax.set_ylabel('Trục Y')
ax.grid(True)
ax.legend()

plt.savefig('ex3.png')

