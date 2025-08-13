from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# print(BASE_DIR)

# Đường dẫn file tới note.txt
NOTE_PATH = BASE_DIR / 'data' / 'note.txt'

# Đường dẫn vào file data.json
JSON_PATH = BASE_DIR / 'data' / 'data.json'

# with open(NOTE_PATH, 'r', encoding='utf-8') as file:
#     # content = file.read()
#     # # 'Hello\nHello\nHello...'
#     # print(content)

#     lines = file.readlines() 
#     '''
#     [
#         'Hello',
#         'Hello',
#         'Hello',
#         'Hello',
#     ]
#     '''
#     print(lines)

#     for line in lines:
#         print(line.replace('\n',''))


import json
from typing import *

CarType = Literal['turn on', 'turn off']

def car(val: CarType):
    return val

# print(car('turn on'))

DataKeyJsonType = Literal['name', 'age']
DataValueJsonType = Union[str, int]

DataJsonType = Dict[
    DataKeyJsonType, # Định nghĩa Key
    DataValueJsonType
]

# with open(JSON_PATH, 'r', encoding='utf-8') as file:
#     data: DataJsonType = json.load(file)
#     print(data.get('name'))
#     # print(type(data))

# data_json_string = '''
# {
#     "name": "Nguyễn Văn A",
#     "age": 20
# }
# '''

# data: DataJsonType = json.loads(data_json_string)

# print(data.get('name'))

# with open(JSON_PATH, 'w', encoding='utf-8') as file:
#     json.dump({
#         'name': 'Nguyễn Văn B',
#         'age': 20
#     }, file, ensure_ascii=False, indent=4)

try:
    a = 1/0
    print(a)
except Exception as error:
    print(error)


