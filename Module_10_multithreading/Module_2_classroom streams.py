import threading
import time

class Knight(threading.Thread):
    def __init__(self, name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        print()

    def run(self):
        print(f'{self.name}, на нас напали!')
        power = 100
        day = 0
        while power > 0:
            power = power - self.power
            time.sleep(1)
            print(f'{self.name}сражается {day}..., осталось {power} воинов.')
            day +=1
        print(f'{self.name} одержал победу спустя {day} дней(дня)!"')



# Создание класса

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потока
first_knight.start()
second_knight.start()
# Остановка потока
first_knight.join()
second_knight.join()

print('Все битвы закончились')



