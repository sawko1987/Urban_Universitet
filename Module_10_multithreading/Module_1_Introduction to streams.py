import time
import threading
from os import write


def wite_words(word_count, file_name):
    """
    Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл с прерыванием
     после записи каждого на 0.1 секунду.
    """
    with open(file_name, "w") as file:
        for f in range(word_count):
            file.write (f"{f}\n")
            time.sleep(0.1)
        print(threading.current_thread())
    print (f"завершена запись в {file_name}")


ex1 = wite_words(10, "example1.txt")
ex2 = wite_words(30, "example2.txt")
ex3 = wite_words(200, "example3.txt")
ex4 = wite_words(100, "example4.txt")


ex5 = wite_words(10, "example5.txt")
ex6 = wite_words(30, "example6.txt")
ex7 = wite_words(200, "example7.txt")
ex8 = wite_words(100, "example8.txt")
thread5 = threading.Thread(target=ex5)
thread6 = threading.Thread(target=ex6)
thread7 = threading.Thread(target=ex7)
thread8 = threading.Thread(target=ex8)

thread.start(ex5)
thread.start(ex6)
thread.start(ex7)
thread.start(ex8)



