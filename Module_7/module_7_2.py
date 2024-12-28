from pprint import pprint
import io

# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи, strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>), а значением - записываемая строка.
# Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:  {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# # Где:
# 1, 2 - номера записанных строк.
#  0, 16 - номера байт, на которых началась запись строк.

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(f"{file_name}", 'w', encoding='utf-8') # открываем файл в режиме записи
    my_string = ""
    lines = 0
    for element in strings:
        lines += 1
        bytes = file.tell()
        file.write(f"{element}\n")
        strings_positions[lines,bytes]=element # добавляем в словарь {ключ(), значение)
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print (elem)
