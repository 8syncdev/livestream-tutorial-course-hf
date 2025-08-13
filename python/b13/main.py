# class User:
#     dem = 0
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         User.dem += 1
    

    

# User(name='Nguyen Van A', age=20)
# User(name='Nguyen Van A', age=20)
# User(name='Nguyen Van A', age=20)
# User(name='Nguyen Van A', age=20)
# print(User.dem)


# class Notification:

#     @staticmethod
#     def send_email(mail, content):
#         print(mail, content)

    
# # notice = Notification()

# Notification.send_email('example123@gmail.com', 'Hello')

# from abc import ABC, abstractmethod


# class Animal(ABC):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @abstractmethod
#     def speak(self): 
#         ...

# class Dog(Animal):
    
#     def speak(self):
#         '''hàm này tôi chưa biết làm'''

# dog = Dog(name='Bull', age=2)
# dog.speak()

# ctrl + /

from typing import Generic, TypeVar, Optional

T = TypeVar('T')

class Model(Generic[T]):

    def __init__(self, obj: T, name: Optional[str] = None):
        self.obj = obj


class User: ...
class Product: ...

model_user = Model[User]() # T=User
model_product = Model[Product]()

