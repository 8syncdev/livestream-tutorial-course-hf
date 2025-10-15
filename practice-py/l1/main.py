# def tong(a, b):
#     # print(a+b)
#     # return a + b
#     ...

# # tong(1,2) 
# # tong(b=1, a=2)
# c = tong(1,2)
# print(c)



# def hello():
#     # ...
#     # pass
#     '''Cách để bỏ trống'''


# def tong(a, b=1):
#     return a + b

# c = tong(1)
# print(c)

# def tong(a, c, d, *, b, e, f):
#     # Keyword only Arguments
#     return a + b

# print(tong(1,2,3, 1,2,3))


# Only Positional Agruments

'''
def my_function(arg1, arg2, ..., /):
    ...
'''


# def tong(a, b, /):
#     return a + b

# # print(tong(a=1, b=2)) # sai vì truyền theo tên
# print(tong(1, 2))


'''
positional-only: chỉ truyền giá trị theo vị trí
keyword-only: chỉ truyền giá trị theo tên
auto: truyền tự do positional hoặc keyword
'''

# def tong(a, /, b, *, c):
#     '''
#         a: là giá trị theo vị trí bắc buộc positional-only
#         b: tự do
#         c: là giá trị theo tên bắc buộc keyword-only
#     '''
#     return a + b + c

# print(tong(1, 2, c=2))


# def tong(*args):
#     t = 0
#     for item in args:
#         print(item)
#         t += item
#     return t

# print(tong(1,2,3,4))

a=10 # global

def demo():
    # local là phạm vi bên trong hàm không được phép can thiệp ra phạm vi bên ngoài là global
    # Khai báo a là pham vi global
    global a
    print(a)
    a += 1
    c = a
    b=1
    def demo2():
        nonlocal c
        c += 1
        print(c)
        d = 10
        
        def demo3():
            nonlocal b, d
            b += 1
            d += 1
            print(b, d)
            ...
        demo3()
    demo2()
demo()

