# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def info(self):
#         print(f"Привет, меня зовут - {self.name} и мне {self.age} лет")

# person = Person("Abu", 18)
# person.info()

# class Toys:
#     def play(self):
#         pass

# class Car(Toys):
#     def play(self):
#         return "Машина едет"
    
# class Doll(Toys):
#     def play(self):
#         return "Я кукла!!!"
    
# class Ball(Toys):
#     def play(self):
#         return "Я прыгаю"
    
# def play_toys(toy):
#     return toy.play()

# car = Car()
# doll = Doll()
# ball = Ball()
# print(play_toys(ball))

# class Animals:
#     def speak(self):
#         pass

# class Cow(Animals):
#     def speak(self):
#         return "Я корова, Мууууу мууу муу"
    
# class Cat(Animals):
#     def speak(self):
#         return "Я кошка, мяу мяу мяу"
    
# class Dog(Animals):
#     def speak(self):
#         return "Я собака, гав гав гав"

# def animal_sound(sound):
#     return sound.speak()

# cow = Cow()
# cat = Cat()
# dog = Dog()
# print(animal_sound(cow))
# print(animal_sound(cat))
# print(animal_sound(dog))

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

person = Person("Geeks", 2)
print(f"Имя: {person.get_name()}")
print(f"Возраст: {person.get_age()}")

person.set_name("Жакшылык")
person.set_age(14)

print(f"Имя: {person.get_name()}")
print(f"Возраст: {person.get_age()}")