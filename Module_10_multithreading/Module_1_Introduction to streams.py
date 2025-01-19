import time
import threading
from os import write


def wite_words(word_count, file_name):
    """
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
     после записи каждого на 0.1 секунду.
    """
    with open(file_name, "w", encoding='utf-8') as file:
        for f in range(word_count):
            file.write (f"Какое то слово №{f}\n")
            time.sleep(0.1)
        print(threading.current_thread()) # печатает текущий поток
    print (f"завершена запись в {file_name}")

start_time1 = time.time()
ex1 = wite_words(10, "example1.txt")
ex2 = wite_words(30, "example2.txt")
ex3 = wite_words(200, "example3.txt")
ex4 = wite_words(100, "example4.txt")
stop_time1 = time.time()
lead_time1 = stop_time1 - start_time1
print(f"Время выполнения основного потока составило: {lead_time1}")

thread5 = threading.Thread(target=wite_words,args=(10,"example5.txt"))
thread6 = threading.Thread(target=wite_words,args=(30,"example6.txt"))
thread7 = threading.Thread(target=wite_words,args=(200,"example7.txt"))
thread8 = threading.Thread(target=wite_words,args=(100,"example8.txt"))

thread5.start()
thread6.start()
thread7.start()
thread8.start()

thread5.join()
thread6.join()
thread7.join()
thread8.join()

stop_time2 = time.time()
lead_time2 = stop_time2 - stop_time1
print(f"Время выполнения дополнительных потоков составило: {lead_time2}")
