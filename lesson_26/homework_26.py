'''
Написати на python selenium код який пройде по двох фреймах на початковiй сторiнцi, 
ввійде в кожний фрейм, введе правильний секретний текст, натисне кнопку “Перевiрити”, 
порівняє текст дiалогового вiкна для підтвердження успішності верифікації та закриє діалогове вікно

Потім ви можете запустити локальний сервер за допомогою командного рядка 
python -m http.server 8000 
виконуючи команду iї у тiй самiй директорiї де були збереженi html файли

Після цього основна веб-сторінка буде доступна за адресою http://localhost:8000/dz.html
'''
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time

# Ініціалізація драйвера
driver = webdriver.Chrome()

# Відкриття веб-сторінки
driver.get("http://localhost:8000/dz.html")

# Робота з веб-елементами і виконання дій на сторінці
frame1_field = driver.find_element(By.ID, "input1")
frame1_button = driver.find_element(By.ID, "button1")
frame1_field.send_keys("Frame1_Secret")
frame1_button.click()
alert = Alert(driver)
alert.accept()

frame2_field = driver.find_element(By.ID, "input2")

# Зачекати 2 секунди перед завершенням
time.sleep(3600)

# Закрити браузер
driver.quit()