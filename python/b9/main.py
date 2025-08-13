# def tong(a, b):
#     return a + b

# print(tong(1,2))
# print(tong(a=1,b=2))

# def tong(a=0, b=0):
#     return a + b

# print(tong(b=1))


# def tong(a, b):
#     return a + b

# print()

# a, b = input().split()
# a, b = int(a), int(b)

# def tong(a, *, b):
#     return a + b

# print(tong(a, b=b))


# dem = 1 # Global

# def ham1():
#     # Phạm vi local
#     # dem += 1
#     global dem
#     dem += 1
#     print(dem+100)
#     dem2 = 0
#     def ham2():
#         # Phạm vi nonlocal
#         nonlocal dem2
#         dem2+=1
#         print(dem2)
#         dem3=0
#         def ham3():
#             nonlocal dem3
#             dem3+=1
#             print(dem3)
#         ham3()
#     ham2()
# ham1()

# import sys

# print(sys.int_info.default_max_str_digits)


if __name__ == '__main__':
    print((lambda a, b: a+b)(1, 2))