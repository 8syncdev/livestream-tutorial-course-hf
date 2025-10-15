def tong(a: int, b: int) -> int:
    '''
    ## Đây là hàm tổng

    Args:
        - a: là giá trị đầu tiên
        - b: là giá trị thứ hai

    Returns:
        Tổng của a và b

    [Google](https:///www.google.com)
    '''
    return a + b

# print(tong(1, 2))


# def func(para1: int, para2: str = "default", *args: float):
#     '''Hàm ví dụ để minh họa annotations'''

# print(func.__annotations__)

from typing import Optional, Literal

# def tong(a: Optional[int] = 0, b: Optional[int] = 0):
#     return a + b

# print(tong(1,2))

# OptionsType = Literal['run', 'stop']

# def car(option: OptionsType):
#     return option


# print(car('stop'))


# from typing import Callable


# MyFunc = Callable[
#     [int, int], # a là int, b là int
#     int
# ]

# def tong(a, b):
#     return a + b

# def call_tong(fn: MyFunc, a, b):
#     return fn(a, b)

# print(call_tong(tong, 1, 1))



# from src.main import MODULE_A, MODULE_B

# print(MODULE_B, MODULE_A)

'''
1. Hàm làm việc với dữ liệu
Non - Primitive Type: type, len, str, int, float, bool
Primittive: func, dict, list, set, class

2. Hàm làm việc với chuỗi:
format, ord, chr, ascii

3. Hàm chức năng làm việc với số:
abs, round, sum, max, min

4. Làm việc với đối tượng
hasattr(obj, tên_attr), getattr(), setattr()

5. Làm việc với file
open(), close()

6. Làm việc với Iterator
iter(), next(), enumerate()
'''


# so = 10
# chuoi = "python"
# danh_sach = [1,2,3]

# print(type(so))
# print(type(chuoi))
# print(type(danh_sach))

# print(len(chuoi))
# print(len(danh_sach))


# so_thuc = "2.5"

# print(int(float(so_thuc)))


# ORD và CHR
# ky_tu = 'A'

# ma_unicode = ord(ky_tu)

# print(ma_unicode)

# print(chr(97))


chuoi = "python"

print(dir(chuoi))