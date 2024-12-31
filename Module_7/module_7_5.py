import os
import time


path =  r"D:\Users\Александр\OneDrive"
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        filepath = os.path.join(path,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(
             f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')












