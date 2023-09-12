# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __str__(self):
#         return f"Книга: {self.title} - Автор: {self.author}"

# book = Book("Geeks", "Abu")
# print(str(book))

# class Animals:
#     def info_animals(self):
#         print("Я - некое животное")

# class Cat(Animals):
#     def info_cat(self):
#         print('Мяу - Мяу')

# cat = Cat()

# cat.info_animals()
# cat.info_cat()


# class Father:
#     def info(self):
#         print("Я отец")

# class Mother:
#     def info(self):
#         print("Я мама")

# class Daughter(Father, Mother):
#     def info(self):
#         print("Я дочь")

# daughter = Daughter()
# daughter.info()

class Work:
    def __init__(self, schedule, descriptions):
        self.schedule = schedule
        self.descriptions = descriptions

    def info(self):
        print(f"График: {self.schedule}")
        print(f"Работа: {self.descriptions}")

class Worker_1(Work):
    def __init__(self, schedule, descriptions, name, age, job_title):
        super().__init__(schedule, descriptions)
        self.name = name
        self.age = age
        self.job_title = job_title
    def info_worker_1(self):
        super().info()
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Должность: {self.job_title}")

class Worker_2(Work):
    def __init__(self, schedule, descriptions, name, age, job_title):
        super().__init__(schedule, descriptions)
        self.name = name
        self.age = age
        self.job_title = job_title
    def info_worker_2(self, worker_1):
        super().info()
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Должность: {self.job_title}")
        worker_1.info_worker_1()

worker_1 = Worker_1("Пн-Пт с 9:00 до 22:00", "изучайте с гарантией", "Abdulaziz", "17", "сотрудник")
worker_2 = Worker_2("Пн-Пт с 22:00 до 9:00", "изучайте c удовольствием", "Abdulloh", "19", "учитель")
worker_2.info_worker_2(worker_1)