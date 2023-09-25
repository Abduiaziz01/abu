# class People:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def info(self):
#         print(f"Имя: {self.name}, Фамилия: {self.surname}, Возраст: {self.age}")

# class Person(People):
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname, age)
        
# person = Person("Abu", "Rahimov", 18)
# person.info()

# class Builder:
#     def __init__(self, staps):
#         self.staps = staps

#     def build(self):
#         for self.staps in range(1, 10):
#             print(self.staps)

# b = Builder(0)
# b.build()

# class Math:
#     def __add__(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2
#         print("Результат сложения: ", num1 + num2)

#     def __sub__(self, num3, num4):
#         self.num3 = num3
#         self.num4 = num4
#         print("Результат вычитание: ",num3 - num4)

# a = Math()
# a.__add__(3, 4)
# a.__sub__(45, 12)

