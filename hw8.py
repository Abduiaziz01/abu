# import sqlite3
# import random

# conn = sqlite3.connect('bank1.db')
# cursor = conn.cursor()

# cursor.execute("""
#                CREATE TABLE IF NOT EXISTS users (
#                first_name TEXT,
#                last_name TEXT,
#                age INTEGER,
#                address TEXT,
#                number_balance INTEGER,
#                balance INTEGER
#                )""")

# class Users:
#     def __init__(self):
#         self.first_name = None
#         self.last_name = None
#         self.age = None
#         self.balance = 0
#         self.number_balance = None
#         self.address = None

#     def register(self, first_name, last_name, age, number_balance, address):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.number_balance = number_balance
#         self.address = address
#         cursor = conn.cursor()
#         cursor.execute(f"""INSERT INTO users(first_name, last_name, age, number_balance, address, balance) 
#                        VALUES ('{self.first_name}', '{self.last_name}', '{self.age}', '{self.number_balance}', '{self.address}', 0)""")
#         conn.commit()
#         print(f"Уважаемый клиент. Вы успешно создали свою учетную запись в нашем банке")


#     def deposit(self, amount, new_number_balance):
#         cursor = conn.cursor()
#         cursor.execute(f"UPDATE users SET balance = balance + {amount} WHERE number_balance = '{new_number_balance}'")
#         conn.commit()
#         self.balance += amount
#         print(f"Вы успешно пополнили баланс на сумму: {amount}.")

#     def curn(self, amount,old_number_balance, new_number_balance):
#         cursor = conn.cursor()
#         cursor.execute(f"UPDATE users SET balance = balance - {amount} WHERE number_balance = '{old_number_balance}'")
#         self.balance -= amount
#         cursor = conn.cursor()
#         cursor.execute(f"UPDATE users SET balance = balance + {amount} WHERE number_balance = '{new_number_balance}'")
#         conn.commit()
#         self.balance += amount
#         print(f"Вы успешно перевели средства на сумму: {amount}.")

#     def money(self, amount, new_number_balance):
#         cursor = conn.cursor()
#         cursor.execute(f"UPDATE users SET balance = balance - {amount} WHERE number_balance = '{new_number_balance}'")
#         conn.commit()
#         self.balance -= amount
#         print(f"Вы успешно вывили сумму: {amount}.")

    

#     def main(self):
#         while True:
#             command = input("1 - регистрация, 2 - пополнение баланса, 3 - перевод средств, 4 - вывод баланса: ")
#             if command == "1":
#                 first_name = input("Введите свое имя: ")
#                 last_name = input("Введите свою фамилию: ")
#                 age = input("Введите свой возраст: ")
#                 number_balance = random.randint(10000, 99999)
#                 print(f"Ваш номер баланса {number_balance}")
#                 address = input("Введите свой адрес: ")
#                 self.register(first_name, last_name, age, number_balance, address)
#             elif command == "2":
#                 new_number_balance = input("Введите номер счета: ")
#                 amount = int(input("Введите сумму: "))
#                 self.deposit(amount, new_number_balance)
#             elif command == "3":
#                 old_number_balance = input("Введите номер счета откуда вы хотите перевести деньги: ")
#                 amount = int(input("Введите сумму: "))
#                 new_number_balance = input("Введите номер счета куда вы хотите перевести деньги: ")
#                 self.curn(amount, old_number_balance, new_number_balance)
#             elif command == "4":
#                 new_number_balance = input("Введите номер счета: ")
#                 amount = int(input("Введите сумму: "))
#                 self.money(amount, new_number_balance)



# users = Users()
# users.main()