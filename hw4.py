#Задача 1
# class Sharp:
#     def draw(self):
#         print("Рисуем фигуру")

# class Circle(Sharp):
#     def draw(self):
#         print("Рисуем круг")        

# class Rectangle(Sharp):
#     def draw(self):
#         print("Рисуем прямоугольник")

# sharp = Sharp()
# sharp.draw()
# circle = Circle()
# circle.draw()
# rectangle = Rectangle()
# rectangle.draw()

#Задача 2
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, value):
        self.value += value

    def get_value(self):
        return self.value

counter = Counter()
print(counter.get_value())
counter.increment(5)
print(counter.get_value())
