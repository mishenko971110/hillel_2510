'''
Написати тест, який перевіяє процес реєстрації користувача в системі https://qauto2.forstudy.space/
Використовувати PageObject-и тільки для пошуку елементів.
PageObject-и повинні логічно співвідностись з частинами програми.
Для взаємодії з елементами використовувати фікстури.
Тести можуть використовувати ТІЛЬКИ фікстури.
Для доступу через селеніум можна використати наступну конструкцію - driver.get("<https://UserName:Password@qauto2.forstudy.space>;");
'''
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    
    domen = "qauto2.forstudy.space"
    username = "guest"
    password = "welcome2qauto"

    URL = f"https://{username}:{password}@{domen}"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    driver.maximize_window()

    yield driver
    driver.quit()
