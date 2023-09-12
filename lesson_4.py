import sqlite3

conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS accounts (
               name VARCHAR(255),
               age INTEGER,
               balance INTEGER,
               wallet_id VARCHER(12)
               )""")

class Bank:
    def __init__(self):
        self.name = None
        self.balance = 0
        self.age = None
        self.wallet_id = None

    def register(self, name, age):
        self.name = name
        self.age = age
        cursor = conn.cursor()
        cursor.execute(f"""INSERT INTO accounts(name, age, balance, wallet_id) 
                       VALUES ('{self.name}', '{self.age}', 0, "vcgdvgh12478")""")
        conn.commit()
        print(f"Уважаемый {self.name}. Вы успешно создали счет в нашем Банке Nurbobo")

    def info(self):
        print(f"Ваша информация: Имя: {self.name}, Возраст: {self.age}, Баланс: {self.balance}")

    def deposit(self, amount):
        cursor = conn.cursor()
        cursor.execute(f"UPDATE accounts SET balance = balance + {amount}")
        conn.commit()
        self.balance += amount
        print(f"Вы успешно пополнили баланс на сумму: {amount}. Ваш счет: {self.balance}")

    def money(self, amount):
        cursor = conn.cursor()
        cursor.execute(f"UPDATE accounts SET balance = balance - {amount}")
        conn.commit()
        self.balance -= amount
        print(f"Вы успешно вывили сумму: {amount}. Ваш счет: {self.balance}")

    def log_out(self):
        cursor = conn.cursor()
        cursor.execute(f"DELETE FROM accounts WHERE name = '{self.name}'")
        conn.commit()
        print(f"Вы успешно вышли из аккунта.")


    def main(self):
        while True:
            command = input("1 - регистрация, 2 - информация, 3 - пополнение баланса, 4 - вывод баланса, 5 - выход из аккаунта: ")
            if command == "1":
                name = input("Введите имя: ")
                age = int(input("Введите возраст: "))
                self.register(name, age)
            elif command == "2":
                self.info()
            elif command == "3":
                amount = int(input("Введите сумму: "))
                self.deposit(amount)
            elif command == "4":
                amount = int(input("Введите сумму: "))
                self.money(amount)
            elif command == "5":
                self.log_out()


bank = Bank()
bank.main()
