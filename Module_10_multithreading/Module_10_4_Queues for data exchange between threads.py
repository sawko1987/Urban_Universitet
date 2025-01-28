import time
import threading
import queue
from queue import Queue
from random import random, randint
from threading import Thread


class Table:
    def __init__(self,number:int,guest= None):#None означает, что стол свободен
        self.number = number
        self.guest = guest

class Guest(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):       #запускается .start()
        time.sleep(randint(3, 10)) #происходит ожидание случайным образом от 3 до 10 секунд.

class Cafe:
    def __init__(self,*tables):
        self.tables = tables
        self.queue = Queue()

    def guest_arrival(self,*guests:Table):
        """
        Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер
        <номер стола>".
        Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
        """
        for guest in guests: # для всех гостей
            for table in self.tables: # проверяем все столы
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}.")
                    break
            else:
                    self.queue.put(guest)
                    print(f"{guest} в очереди")


    def discuss_guests(self):
        while not self.queue.empty()or any([table.guest for table in self.tables]):
            #пока очередь не пустаg пока за столом есть гости
                for table in self.tables:
                    if table.guest is not None and not table.guest.is_alive():
                        #если есть хотя бы один пустой стол и если есть поток
                        print(f"{table.guest.name} покушал(-а)) и ушёл(ушла)")
                        print(f"{table.number} сбободен")
                        table.guest =None # текущий стол освобождается
                    if not self.queue.empty() and table.guest is None:
                        table.guest = self.queue.get()  # Берём гостя из очереди
                        print(f"{table.guest.name} вышел из очереди и сел за стол {table.number}")
                        table.guest.start()

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей

guests_names = [
                'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей

cafe.guest_arrival(*guests)
# Обслуживание гостей

cafe.discuss_guests()


