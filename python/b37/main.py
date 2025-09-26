# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self._age = age

#     def get_name(self) -> str:
#         return self.__name

#     def __info(self):
#         print(f"{self.__name}")

#     def __str__(self):
#         return f'{self.__name} {self._age}'
# p = Person(name='Nguyễn Văn A', age=20)
# print(p)
# # print(p.__name)
# # p.__info()


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f'{self.name}'
    
# class Dog(Animal):
#     def __init__(self, name, age):
#         super().__init__(name)
#         # Animal.__init__(self=self, name=name)
#         self.age = age

# dog = Dog(name='Bull',age=12)

# print(dog.name)
# print(dog.age)


class A:
    def __init__(self, a):
        self.a = a 

class B:
    def __init__(self, b):
        self.b = b 

class C(A, B):
    def __init__(self, a, b):
        A.__init__(self=self, a=a)
        B.__init__(self=self, b=b)

