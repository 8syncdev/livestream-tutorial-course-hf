info_user = {
    "name": "Nguyen Van A",
    "age": 29
}
# print(info_user)

# Thêm một giá trị vào dictionary, nếu mà cố tình gán giá trị cho key không tồn tại thì sẻ tạo ra key đó và giá trị đó
# info_user['city'] = 'HCM'

copy_info_user = {
    **info_user,
    'city': 'HCM'
}

# print(info_user)
# print(copy_info_user)

copy_info_user = {
    **copy_info_user,
    "city": "HN"
}

# print(copy_info_user)


# print(copy_info_user.keys())
# print(copy_info_user.values())
# print(copy_info_user.items())

# print(copy_info_user['city'])
# print(copy_info_user.get('city'))


# Xóa phần tử trong dicionary

# del copy_info_user["city"]
# print(copy_info_user)

# copy_info_user.pop("city")
# print(copy_info_user)


# copy_info_user.clear()
# print(copy_info_user)

# print(*copy_info_user)


# for key, value in info_user.items():
#     print(key, value)


# Set giá trị mặc định

# info_user.setdefault("city", "HCM")

# print(info_user)


# Dùng hàm chức năng có sẵn là update

# info_user.update({
#     'name': 'Nguyen Van B'
# })

# print(info_user)

# Membership toán tử thành viên in

# print("name" in info_user)
# print("Nguyen Van A" in info_user.values())

# Toán tử hợp nhất |

# info_a = {
#     'a': 1
# }

# info_b = {
#     'a' : 2
# }

# new_dict = info_a | info_b

# print(new_dict, info_a, info_b)

# Cách tương tác hoạt động của str() đối với lại dict

chuoi = str(info_user)

print(chuoi)