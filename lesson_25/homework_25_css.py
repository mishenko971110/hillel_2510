'''
Написати 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
Дані для входу на сайт -
login - guest
pass - welcome2qauto
Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
Сдавати у формі файлу з локаторами у гіті
'''
from bs4 import BeautifulSoup
import requests

# Завантаження HTML-сторінки
url = 'https://qauto2.forstudy.space/'
response = requests.get(url)
html_content = response.content

# Аналіз HTML-документу з використанням BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Вилучення тексту з тегу <title> за допомогою CSS-локатора
title = soup.select_one('title').text
print("Заголовок сторінки:", title)

# Вилучення тексту з усіх тегів <a> за допомогою CSS-локатора
links = soup.select('a')
for link in links:
    print("Посилання:", link.get('href'))