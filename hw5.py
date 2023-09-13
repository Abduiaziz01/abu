class Animal:
    def get_name(self, name):
        self._name = name
    def get_age(self, age):
        self._age = age

class Dog(Animal):
    def get_name(self, name):
        super().get_name(name)
    def get_age(self, age, breed):
        super().get_age(age)
        self._breed = breed
        print(f"Собака: {self._name}, Возраст: {self._age}, Порода: {self._breed}")
    def bark(self):
        print("Гав-гав")

class Cat(Animal):
    def get_name(self, name):
        super().get_name(name)
    def get_age(self, age, color):
        super().get_age(age)
        self._color = color
        print(f"Собака: {self._name}, Возраст: {self._age}, Цвет: {self._color}")
    def meow(self):
        print("Мяу-мяу")

dog = Dog()
dog.get_name("Рекс")
dog.get_age(2, "Дог")
dog.bark()
cat = Cat()
cat.get_name("Киса")
cat.get_age(1, "черно-белый")
cat.meow()