import os
import time


# path =  r"D:\Users\Александр\OneDrive"
# for dirpath, dirnames, filenames in os.walk(path):
#     for file in filenames:
#         filepath = os.path.join(path,file)
#         filetime = os.path.getmtime(filepath)
#         formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
#         filesize = os.path.getsize(filepath)
#         parent_dir = os.path.dirname(filepath)
#         print(
#              f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


directory = '.'

for root, dirs, files in os.walk(directory): # os.walk - для обхода каталога, путь к к-му указывает переменная directory
    for file in files:
        filepath = os.path.join(root, file) # os.path.join - для формирования полного пути к файлам
        #os.path.getmtime и модуль time - для получения и отображения времени последнего изменения файла
        # os.path.getmtime() возвращает время последнего изменения файла в виде числа с плавающей точкой:
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(filepath) # os.path.getsize - для получения размера файла
parent_dir = os.path.dirname(filepath) # os.path.dirname - для получения родительской директории файла
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт', f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')









