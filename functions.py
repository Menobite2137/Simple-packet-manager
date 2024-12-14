import requests
import asyncio
import os
import time

#Переменная показывающая загрузился ли файл
download_finished = False

#Функции установки программ и проверки на их наличие в исполняемой папке
def OSP():
    if os.path.isfile('OSP6.0.exe'):
        print('Файл установлен')
    else:
        print('Начинаю установку')
        url = "https://lapkabot.ru/Software/open_server_panel_6_0_0_setup.exe"
        local_file_name = "OSP6.0.exe"

        response = requests.get(url)
        with open(local_file_name, "wb") as f:
            f.write(response.content)
            if os.path.isfile('OSp6.0.exe'):
                download_finished = True
                print('Загрузка завершена')

def VScode():
    if os.path.isfile('VScode.exe'):
        print('Файл установлен')
    else:
        print('Начинаю установку')
        url = "https://lapkabot.ru/Software/VSCodeUserSetup-x64-1.95.3.exe"
        local_file_name = "VScode.exe"

        response = requests.get(url)
        with open(local_file_name, "wb") as f:
            f.write(response.content)
        if os.path.isfile('VScode.exe'):
            download_finished = True
            print('Загрузка завершена')

def Python():
    if os.path.isfile('Python 3.13.1.exe'):
        print('Файл установлен')
    else:
        print('Начинаю установку')
        url = "https://lapkabot.ru/Software/python-3.13.1-amd64.exe"
        local_file_name = "Python 3.13.1.exe"

        response = requests.get(url)
        with open(local_file_name, "wb")as f:
            f.write(response.content)
            if os.path.isfile('Python 3.13.1.exe'):
                download_finished = True
                print('Загрузка завершена')

def Wallpaper():
    if os.path.isfile('wallpaper.jpg'):
        print('Файл установлен')
    else:
        print('Начинаю установку')
        url = "https://lapkabot.ru/Software/wpapers_ru_%D0%9D%D0%B5%D0%BE%D0%BD%D0%BE%D0%B2%D0%B0%D1%8F-%D0%BA%D0%BE%D1%88%D0%BA%D0%B0.jpg"
        local_file_name = "wallpaper.jpg"

        response = requests.get(url)
        with open(local_file_name, "wb")as f:
            f.write(response.content)
            if os.path.isfile('wallpaper.jpg'):
                download_finished = True
                print('Загрузка завершена')

def Notepad():
    if os.path.isfile('notepad++.exe'):
        print('Файл установлен')
    else:
        print('Начинаю установку')
        url = "https://lapkabot.ru/Software/npp.8.7.4.Installer.x64.exe"
        local_file_name = "notepad++.exe"

        response = requests.get(url)
        with open(local_file_name, "wb")as f:
            f.write(response.content)
            if os.path.isfile('notepad++.exe"'):
                download_finished = True
                print('Загрузка завершена')


