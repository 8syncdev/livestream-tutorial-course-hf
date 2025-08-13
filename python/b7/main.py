info_user = {
    "name" : "Nguyen Van A",
    "age": 30
}

# Thêm key-value 

# info_user["city"] = "TPHCM"
# print(info_user)

# Copy giá trị

# Cách làm sai
# a = {}
# b = a
# b['name'] = 'Nam'
# print(a)

# dict_a = {}
# copy_dict = dict_a.copy()
# print(id(dict_a))
# print(id(copy_dict))
# copy_dict = { **dict_a }
# print(id(dict_a))
# print(id(copy_dict))


# Tham số tự do, arguments

# def tong(*args):
#     t = 0
#     for item in args:
#         t += item
#     return t

# print(tong(1,2,3,4,5,))

# Keyword arguments
# def hello(**info):
#     print(info)

# hello(name='Nguyen Van A', age=30, city='TPHCM')

info_user = {
    "name" : "Nguyen Van A",
    "age": 30
}

# print(*info_user)
# print({**info_user})


# print(info_user.keys())
# print(list(info_user.keys()))
# print(info_user.values())
# print(list(info_user.values()))
# print(info_user.items())
# print(list(info_user.items()))

# ds = input().split()
# _dict = {}
# for item in ds:
#     if item not in _dict:
#         _dict[item]=int(item)

# print(_dict)


# danh_sach_sp = [
#     {
#         "code": "abc0001",
#         "price": 300,
#         "quantity": 30,
#     },
#     {
#         "code": "abc0002",
#         "price": 500,
#         "quantity": 20,
#     },
#     {
#         "code": "abc0003",
#         "price": 200,
#         "quantity": 100,
#     },
#     {
#         "code": "abc0004",
#         "price": 800,
#         "quantity": 10,
#     },
# ]

# [1,2,3,4]
# [{}, {}, {}, {}]

# result = sorted(danh_sach_sp, key=lambda item: (
#     item['quantity'],
#     -item['price']
# ))
# print(result)


info_user = {
    "name" : "Nguyen Van A",
    "age": 30,
    "address": {
        "street": "....",
        "city": "....",
        "postcode": "..."
    }
}
# print(*info_user)
# copy_info_user = {}.fromkeys([*info_user], None)
# print(copy_info_user)

# new_dict = {}.fromkeys(['name', 'age'], None)
# print(new_dict)


