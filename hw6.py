import sqlite3

conn = sqlite3.connect('cars.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS users (
               number INTEGER(10),
               brand VARCHAR(255),
               model VARCHAR(255),
               year INTEGER,
               discribe VARCHAR(255),
               status_work TEXT
               )""")

class Cars:
    def __init__(self):
        self.number = None
        self.brand = None
        self.model = None
        self.year = None
        self.discribe = None
        self.status_work = None

    def register(self, number, brand, model, year, discribe):
        self.number = number
        self.brand = brand
        self.model = model
        self.year = year
        self.discribe = discribe
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO users(number, brand, model, year, discribe, status_work) 
                       VALUES ('{self.number}', '{self.brand}', '{self.model}', '{self.year}', '{self.discribe}', 'на обслуживании')""")
        conn.commit()
        print(f"Уважаемый клиент. Вы успешно добавили свою машину на обслуживание.")

    def update(self, new_number, new_brand, new_model, new_year, new_discribe, new_status_work):
        cursor = conn.cursor()
        cursor.execute(f"UPDATE users SET brand = '{new_brand}', model = '{new_model}', year = '{new_year}', discribe = '{new_discribe}', status_work = '{new_status_work}' WHERE number = '{new_number}'")
        conn.commit()
        self.number = new_number
        self.brand = new_brand
        self.model = new_model
        self.year = new_year
        self.discribe = new_discribe
        self.status_work = new_status_work
        print(f"Уважаемый клиент. Вы успешно обновили информацию о своей машине.")

    def info(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE status_work = 'на обслуживании'")
        cars = cursor.fetchall()
        if cars:
            for car in cars:
                print(f"Номер: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год: {car[3]}, Описание: {car[4]}")
        else:
            print("Нет автомобилей на обслуживании.")

    def finished_info(self):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE status_work = 'готов к выдаче'")
        cars = cursor.fetchall()
        if cars:
            for car in cars:
                print(f"Номер: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год: {car[3]}, Описание: {car[4]}")
        else:
            print("Нет готовых автомобилей.")

    def main(self):
        while True:
            command = input("1 - добавление новых автомобилей, 2 - обновление информации, 3 - просмотр списка всех автомобилей, 4 - автомобили готовые к выдаче: ")
            if command == "1":
                number = input("Введите номер машины: ")
                brand = input("Введите брэнд автомобиля: ")
                model = input("Введите модель автомобиля: ")
                year = input("Введите год выпуска автомобиля: ")
                discribe = input("Введите описание работ: ")
                self.register(number, brand, model, year, discribe)
            elif command == "2":
                number1 = input("Введите номер машины которую хотите обновить: ")
                brand = input("Введите брэнд автомобиля: ")
                model = input("Введите модель автомобиля: ")
                year = input("Введите год выпуска автомобиля: ")
                discribe = input("Введите описание работ: ")
                status_work = input("Машина на обслуживании или готов к выдаче: ").lower()
                self.update(number1, brand, model, year, discribe, status_work)
            elif command == "3":
                self.info()
            elif command == "4":
                self.finished_info()



cars = Cars()
cars.main()