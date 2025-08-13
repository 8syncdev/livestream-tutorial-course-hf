# name = input()

# print(name.title())
# print(name.upper())
# print(name.lower())
# print(name.capitalize())

#    01234
#    
# a = 'hello'
# print(a[0])
# print(a[-len(a)])
# print(a[-a.__len__()])


# s = 'Hello "Nam"'
# s = "Hello 'Nam'"

# s = '''
# "Hello 'Nam'"
# "Hello 'Nam'"
# "Hello 'Nam'"
# "Hello 'Nam'"
# "Hello 'Nam'"
# '''

# name = input()
# print(' '.join(name.strip().split()).title())
# print(name)

# a,b,c = input(), input(), input()
# print(a,b,c)

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

print(a+b+c)