# def hello():
#     return 'Hello'

# a=hello 

# a()

ds = [1,2,3,4]

def power(item):
    return item ** 2

print(list(map(power, ds)))
print(list(map(lambda item: item ** 2, ds)))

# def check_even(item):
#     return item % 2 == 0

# print(list(filter(check_even, ds)))



# from functools import reduce

# ds=[1,2,3,4]
'''
x=1
y=2
x=x+y=1+2=3
y=3
x=x+y=3+3=6
y=4
x=x+y=6+4=10
y dừng => x=10
'''
# print(reduce(lambda x,y: x+y, ds))


# print(__file__)

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

FILE = BASE_DIR / 'note.txt'

# print(FILE)
with open(FILE, 'w', encoding='utf-8') as file:
    file.write('1')




