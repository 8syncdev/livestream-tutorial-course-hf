# class User:
#     def __init__(self, name):
#         self.name = name
#         self.__is_admin = True # phạm vi private
#         self._is_protected = True

#     def __get_info(self): # __ trước tên của 1 chức năng
#         return self.name                


# user = User(name='Nguyen Van A')
# print(user.__get_info())
# # print(user.__is_admin)
# print(user._is_protected)


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def sound(self):
#         ...

# class Dog(Animal):

#     def __init__(self, name, age):
#         super().__init__(name, age)
#         # Animal.__init__(self, name, age)
    
#     def sound(self):
#         print('Gau')

# class Cat(Animal):

#     def sound(self):
#         print('Meo')


# dog = Dog(name='Bull', age=1)
# cat = Cat(name='Katy', age=2)

# dog.sound()
# cat.sound()


# a: 'INT'


class INT:
    def __init__(self, value):
        self.value = value 

    def __add__(self, other: 'INT'):
        return INT(self.value + other.value)
    

a = INT(1)
b = INT(2)

c = a + b
print(c.value)

