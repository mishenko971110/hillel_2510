'''
Написати 25 XPath локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
Дані для входу на сайт -
login - guest
pass - welcome2qauto
Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
Сдавати у формі файлу з локаторами у гіті
'''
from lxml import html
import requests
from selenium import webdriver

driver = webdriver.Chrome()

domen = 'qauto2.forstudy.space'
login = 'guest'
password = 'welcome2qauto'

driver.get(f"<https://{login}:{password}@{domen}>;")

driver.quit()

# Завантаження HTML-сторінки
url = 'https://qauto2.forstudy.space/'
response = requests.get(url)
html_content = response.content


# Парсинг HTML-документу з використанням XPath
tree = html.fromstring(html_content)


#title = tree.xpath('//h1/text()')
#print("Заголовок сторінки:", title)

#description = tree.xpath('//p/text()')
#print("Описовий блок:", description)

# links = tree.xpath('//a/text()')
# for link in links:
#     print("Пункти меню:", link)

# video_link = tree.xpath('//h1/text()')
# print("Посилання на відео:", video_link)

# description = tree.xpath('//p/text()')
# print("About blocks:", description)

# title = tree.xpath('//h1/text()')
# print("Facebook link:", title)

# description = tree.xpath('//p/text()')
# print("Telegram link:", description)

# title = tree.xpath('//h1/text()')
# print("Youtube link:", title)

# description = tree.xpath('//p/text()')
# print("Instagram link:", description)

# title = tree.xpath('//h1/text()')
# print("LinkedIn link:", title)

# description = tree.xpath('//p/text()')
# print("Support email:", description)

# description = tree.xpath('//p/text()')
# print("Hillel site:", description)

