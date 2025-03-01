'''
1. За певними параметрами отримати данi у виглядi JSON про фото зробленi ровером 'Curiosity' на Марсi. 
2. Серед цих даних є посилання на фото, якi потрiбно розпарсити.
3. За допомогою додаткових запитiв скачати i зберiгти цi фото як локальнi файли mars_photo1.jpg. 
Завдання потрiбно зробити використовуючи модуль requests.
'''
import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}


def get_photos_list(url, params):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        photos_list = [photo['img_src'] for photo in data['photos']]
        return photos_list
    else:
        print('Помилка запиту:', response.status_code)


def download_photos(photos_list):
    n = 1
    for file_url in photos_list:
        filename = f'mars_photo{n}.jpg'
        n += 1

        response = requests.get(file_url)
        if response.status_code == 200:
            with open(filename, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"Файл збережено як {filename}")
        else:
            print(f"Помилка: {response.status_code}")


photos_list = get_photos_list(url, params)
download_photos(photos_list)
