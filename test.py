import os
import time

directory = 'C:\\'


def process_file(filepath):
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(
        f'Обнаружен файл: {os.path.basename(filepath)}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)
        process_file(filepath)