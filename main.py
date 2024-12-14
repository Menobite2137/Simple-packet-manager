import requests
import asyncio
from functions import VScode, Python, OSP, Notepad, Wallpaper
import os
import sys
from variables import download_finished
from variables import download_programm
from variables import programm_list

#Выбор программы и запуск функций установки
async def download_control():
    print(programm_list)
    # Выбор номера программы
    download_programm = int(input())
    #Оператор проверяющий значение download_programm и запускающий функцию установки
    if download_programm == 1:
        VScode()
    elif download_programm == 2:
        Python()
    elif download_programm == 3:
        OSP()
    elif download_programm == 4:
        Wallpaper()
    elif download_programm == 5:
        Notepad()
    else:
        print('Программа отсутствует')

#Цикл для повтора программы
while input('Желаете продолжить?\n').lower() == 'да':
    if download_finished == False:
        asyncio.run(download_control())
    else:
        print('Выполняется загрузка')
else:
    sys.exit()