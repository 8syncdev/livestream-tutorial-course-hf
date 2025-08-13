# ds = [1,2,3,4]

# print(ds[0])
# print(ds[-len(ds)])
# print(ds[-ds.__len__()])
# for item in ds:
#     print(item)

# print(ds)
# _ds = []
# values = input().split()

# for item in values:
#     _ds.append(int(item))

# print(_ds)

# Remove, pop, remove: xóa theo giá trị, pop: xóa theo vị trí

# ds=[1,2,3,4]
# ds.remove(1)
# print(ds)
# ds.pop(0)
# print(ds)

# count, index, insert

ds=[1,2,3,4,1,1]
#   0 1 2 3 4 5
# print(ds.count(1))
# print(ds.index(1))
# print(ds.index(1, 2))
# ds.insert(1, 1000)
# print(ds)

# clear, reverse, sort

# ds=[1,2,3,4]
# # ds.clear()
# # print(ds)
# # ds.reverse()
# new_ds = reversed(ds)
# print(ds)
# print(list(new_ds))


# ds = [2,3,1,5,4,7,6]

# ds.sort(reverse=True)
# print(ds)


# new_ds = sorted(ds)
# print(ds)
# print(new_ds)

# a=[]
# b=a
# b.append(1)
# print(a)

# ds=[1,2,3,4]
# new_ds = ds.copy()
# print(id(ds))
# print(id(new_ds))

# print(ds[0:2])

# new_ds = ds[:]
# print(id(ds))
# print(id(new_ds))

# a,b,c = 0,0,0

# a=[]
# b=[]

# print(id(a))
# print(id(b))

# ds = [1,2,3,4]
# new_ds = [*ds]

# print(ds)
# print(new_ds)
# print(id(ds))
# print(id(new_ds))


# a=[]
# b=a
# print(id(a))
# print(id(b))
# b.append(1)
# b.append(1)
# print(a)

# List slicing insert, start == stop
#     0 1 2
#     0 1 2 3 4 5
ds = [1,3,2,5,4,2]
# ds[1:1] = [1000, 10, 200, 300]
# print(ds)

# Xóa
# ds[:3] = []
# print(ds)

# Sắp xếp trong đoạn bất kì

# ds[1:3] = sorted(ds[1:3])

# print(ds)

ds_a = [1,2,3,4]
# ds.extend([5,6,7])
ds_b = [5,6,7]
print(ds_a)
print(ds_b)
print(ds_a+ds_b)

ds_a.extend()

