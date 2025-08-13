# t = (1,2,3,4)
#    0 1 2 3

# t[0]=10
# print(t)

# for item in t:
#     print(item)

# _set = {1,2,3}
# _list = [1,2,3]

# print(1 in _set) # O(1)
# print(1 in _list) # O(n)

# n = int(input())
# _set = set({})
# while n:
#     _set.add(int(input()))
#     n-=1

# print(_set)

# ds = input().split()
# _list=[]
# for item in ds:
#     _list.append(int(item))

# print(set(_list))


# ds = input().split()
# _list=[]
# for item in ds:
#     _list.append(int(item))

# print(tuple(_list))


# Map, filter, reduce

# ds = input().split()
# _list=[]
# for item in ds:
#     _list.append(int(item))

# map_ds = map(lambda item: item*item, _list)
# print(list(map_ds))


danh_sach_sp = [
    {
        "code": "abc0001",
        "price": 300,
        "quantity": 30,
    },
    {
        "code": "abc0002",
        "price": 500,
        "quantity": 20,
    },
    {
        "code": "abc0003",
        "price": 200,
        "quantity": 100,
    },
    {
        "code": "abc0004",
        "price": 800,
        "quantity": 10,
    },
]

def apply_price(item):
    if item['quantity'] >= 50:
        item['price'] *= 1.1
        # return item
    return item

map_apply_price = list(map(
    apply_price,
    danh_sach_sp
))

print(map_apply_price)

info = {
    'name': 'Nguyen Van A',
    'age': 20
}

# Thêm key-value, truy cập vào key không tồn tại
# info['city'] = 'TPHCM'
# info = {
#     **info,
#     'city': 'HN' # để ở cuối để ghi đè lại các key-value đã có
# }

# print(info)

key, value = input().split()
_dict = dict({})
if key not in _dict:
    _dict[key] = value

print(_dict)


