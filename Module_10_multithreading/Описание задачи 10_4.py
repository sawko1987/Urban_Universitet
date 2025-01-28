import queue  # Импорт модуля queue для работы с очередями
import threading  # Импорт модуля threading для работы с потоками
from queue import Queue  # Импортируем потокобезопасную очередь
from time import sleep  # Импортируем функцию sleep для приостановки потока
from random import randint  # Импортируем randint для генерации случайного времени

# Класс Table представляет стол в кафе
class Table:
    def __init__(self, number):  # Конструктор принимает номер стола
        self.number = number  # Номер стола
        self.guest = None  # Гость за столом (по умолчанию стол свободен)

# Класс Guest представляет гостя, который является потоком
class Guest(threading.Thread):
    def __init__(self, name):  # Конструктор принимает имя гостя
        super().__init__()  # Инициализация базового класса Thread
        self.name = name  # Имя гостя

    def run(self):  # Метод запускается при вызове guest.start()
        sleep(randint(3, 10))  # Поток "засыпает" на случайное время от 3 до 10 секунд

# Класс Cafe представляет кафе
class Cafe:
    def __init__(self, *tables):  # Конструктор принимает список столов
        self.queue = Queue()  # Очередь для ожидающих гостей
        self.tables = tables  # Список столов в кафе

    # Метод для обработки прихода гостей
    def guest_arrival(self, *guests):
        for guest in guests:  # Для каждого гостя
            for table in self.tables:  # Проверяем все столы
                if table.guest is None:  # Если стол свободен
                    guest.start()  # Запускаем поток гостя
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    table.guest = guest  # Назначаем гостя этому столу
                    break  # Прекращаем проверку столов для текущего гостя
            else:  # Если все столы заняты
                print(f'{guest.name} в очереди')  # Выводим сообщение, что гость в очереди
                self.queue.put(guest)  # Добавляем гостя в очередь

    # Метод для обработки ухода гостей и назначения новых из очереди
    def discuss_guests(self):
        while not self.queue.empty() or any([table.guest for table in self.tables]):
            # Пока очередь не пуста или за столами есть гости
            for table in self.tables:  # Проверяем все столы
                if table.guest is not None and not table.guest.is_alive():
                    # Если гость за столом завершил поток
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None  # Освобождаем стол
                if not self.queue.empty() and table.guest is None:
                    # Если очередь не пуста и стол свободен
                    table.guest = self.queue.get()  # Берём гостя из очереди
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()  # Запускаем поток для нового гостя

# Создание списка столов
tables = [Table(number) for number in range(1, 6)]  # 5 столов с номерами от 1 до 5

# Список имён гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание объектов гостей
guests = [Guest(name) for name in guests_names]  # Каждый гость является отдельным потоком

# Создаём объект кафе с переданными столами
cafe = Cafe(*tables)

# Запускаем процесс прихода гостей
cafe.guest_arrival(*guests)

# Обрабатываем очередь и уход гостей
cafe.discuss_guests()