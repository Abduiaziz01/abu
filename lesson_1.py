# class Animal:
#     name = "Корова"
    
#     def make_sound(self, sound):
#         print(f"{self.name} издает звук {sound}")

# animal = Animal()
# animal.make_sound("муууу")


# class Calculator:
#     def add(self, num1, num2):
#         print(f"Результат: {num1 + num2}")

#     def sub(self, num1, num2):
#         print(f"Результат: {num1 - num2}")

#     def mult(self, num1, num2):
#         print(f"Результат: {num1 * num2}")

#     def div(self, num1, num2):
#         print(f"Результат: {num1 / num2}")

# calculator = Calculator()

# calculator.add(5, 6)
# calculator.sub(89, 12)
# calculator.mult(5, 6)
# calculator.div(56, 7)

# class Doll:
#     def __init__(self, color, size):
#         self.color = color
#         self.size = size

#     def info(self):
#         print(f"Кукла имеет цвет {self.color} и размер {self.size}.")

# doll = Doll("Черный", "Medium")
# doll.info()

#1)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def info(self):
        print(f"Книга: '{self.title}', автор - {self.author}.")

book = Book("Приключения Гарри Потера", "Джоан Роулинг")
book.info()