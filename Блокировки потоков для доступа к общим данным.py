import threading


class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно средств")
        else:
            with self.lock:
                self.balance -= amount

account = BankAccount(1000)

# Поток для пополнения счёта
def deposit_thread():
    for i in range(5):
        account.deposit(100)
        print(f"Пополнение {i + 1}: {account.balance}")

# Поток для снятия денег
def withdraw_thread():
    for i in range(5):
        try:
            account.withdraw(150)
            print(f"Снятие {i + 1}: {account.balance}")
        except ValueError as e:
            print("Ошибка:", e)


dep = threading.Thread(target=deposit_thread,)
minus = threading.Thread(target=withdraw_thread,)

dep.start()
minus.start()

dep.join()
minus.join()
print('Потоки завершены')