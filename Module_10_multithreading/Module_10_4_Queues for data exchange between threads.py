import time
import threading
import queue
from queue import Queue
from random import random
from threading import Thread


class Table:
    """
    Объекты этого класса должны создаваться следующим способом - Table(1)
    Обладать атрибутами number - номер стола и guest - гость, который сидит за этим столом (по умолчанию None)
    """
    def __init__(self,number:int,guest= None):#None означает, что стол свободен
        self.number = number
        self.guest = guest


class Guest(Thread):
    """
    Должен наследоваться от класса Thread (быть потоком).
    Объекты этого класса должны создаваться следующим способом - Guest('Vasya').
    Обладать атрибутом name - имя гостя.
    """
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name


    def run(self):
        """
        происходит ожидание случайным образом от 3 до 10 секунд.
        """
        return time.sleep(random.random(3, 10))

class Cafe():
    """
    Обладать атрибутами queue - очередь (объект класса Queue) и tables - столы в этом кафе (любая коллекция).
    Обладать методами guest_arrival (прибытие гостей) и discuss_guests (обслужить гостей).
    """
    def __init__(self, queue: Queue, *tables):
        self.tables = tables
        self.queue = Queue


    def guest_arrival(self,*guests:Table):
        """
        Метод guest_arrival Должен принимать неограниченное кол-во гостей (объектов класса Guest).
        Далее, если есть свободный стол, то садить гостя за стол (назначать столу guest), запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер
        <номер стола>".
        Если же свободных столов для посадки не осталось, то помещать гостя в очередь queue и выводить сообщение "<имя гостя> в очереди".
        """

        for guest in guests:
            for table in self.tables:
                if guest is None:
                    guest = table










    def discuss_guests(guest_arrival):
        """
        Этот метод имитирует процесс обслуживания гостей.
        Обслуживание должно происходить пока очередь не пустая (метод empty) или хотя бы один стол занят.
        Если за столом есть гость(поток) и гость(поток) закончил приём пищи(поток завершил работу - метод is_alive), то вывести строки "<имя гостя за текущим столом> покушал(-а)
         и ушёл(ушла)" и "Стол номер <номер стола> свободен". Так же текущий стол освобождается (table.guest = None).
        Если очередь ещё не пуста (метод empty) и стол один из столов освободился (None), то текущему столу присваивается гость взятый из очереди (queue.get()). Далее выводится
         строка "<имя гостя из очереди> вышел(-ла) из очереди и сел(-а) за стол номер <номер стола>"
        Далее запустить поток этого гостя (start)
        Таким образом мы получаем 3 класса на основе которых имитируется работа кафе:
        """
        pass

thread = threading.Thread(target=guest_arrival)
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


