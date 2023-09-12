class Car:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def increase_speed(self, value:int):
        self.speed += value
        print(car.speed, "km/h")
    def decrease_speed(self, value:int):
        self.speed -= value
        print(car.speed, "km/h")
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Скорость: {self.speed}")

car = Car("Mercedes", "AMG", "2022", 100)
car.info()
car.increase_speed(10)
car.decrease_speed(5)

class Car1:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed
        
    def increase_speed(self, value:int):
        self.speed += value
        print(car1.speed, "km/h")
    def decrease_speed(self, value:int):
        self.speed -= value
        print(car1.speed, "km/h")
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Скорость: {self.speed}")

car1 = Car1("Toyota", "Camry", 2020, 60)
car1.info()
car1.increase_speed(10)
car1.decrease_speed(5)

class Motorcycle:
    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def inc_speed(self, value):
        self.speed += value
        print(motorcycle.speed, "km/h")
    def dec_speed(self, value):
        self.speed -= value
        print(motorcycle.speed, "km/h")
    def info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}, Скорость: {self.speed}")

motorcycle = Motorcycle("Dodge Tomahawk", "CBR", 2021, 40)
motorcycle.info()
motorcycle.inc_speed(10)
motorcycle.dec_speed(5)
