'''
Запустiть http сервер за допомогою команди python app.py
Сервер стартує за базовою адресою http://127.0.0.1:8080

1. використовуючи модуль request зробить через POST upload якогось 
зображення на сервер
2. за допомогою GET отримає посилання на цей файл
3. за допомогою DELETE зробить видалення файлу з сервера
'''

import requests
from pathlib import Path

def upload_file(url, file_path):
    with open(file_path, "rb") as image_file:
        response = requests.post(f'{url}/upload', files={"image": image_file})
    return response.json()


def get_file_link(url, file_name):
    response = requests.get(f'{url}/image/{file_name}', headers={"Content-Type": "text"})
    return response.json()


def delete_file(url, file_name):
    response = requests.delete(f'{url}/delete/{file_name}')
    return response.json()

server_url = "http://127.0.0.1:8080"
file_path = "./img_for_test/1.jpg" 

upload_file(server_url, file_path)
get_file_link(server_url, Path(file_path).name)
delete_file(server_url, Path(file_path).name)
