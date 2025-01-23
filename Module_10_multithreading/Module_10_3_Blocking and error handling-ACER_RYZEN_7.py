import time
import threading
import random
lock = threading.Lock()

class Bank(threading.Thread):


    def __init__(self):
        self.
        self.balance = 0
        self.lock = lock.locked()


    def deposit(self):
        """ Будет совершать 100 транзакций пополнения средств.
        Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
        После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
        Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
        """
        generate_number = random.randint(50, 500)
        count = 0
        while count < 100 and self.balance >= 500 and lock.locked():
            lock.release()
            self.balance += generate_number
            count += 1
            print(f"Пополнение {generate_number}. Баланс после пополнения {self.balance} ")
            time.sleep(0.001)

    def take(self):
        """
        Будет совершать 100 транзакций снятия.Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
        В начале должно выводится сообщение "Запрос на <случайное число>".
        Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на
        соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
        Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток
        методом acquiere.
        """
        generate_take = random.randint(50, 500)
        count_take = 0
        while count_take < 100:
            print(f"Запрос на {generate_take}")
            if generate_take <= self.balance:
                self.balance -= generate_take
                print(f"Снять: {generate_take}. Баланс после снятия: {self.balance}")
                count_take += 1
            else:
                print("Недостаточно средств")
                self.lock = lock.acquire()




bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))



th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')