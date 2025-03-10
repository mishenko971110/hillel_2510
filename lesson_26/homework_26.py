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

def handle_frame(frame_id, secret_text, url):
    driver = webdriver.Chrome()
    driver.get(url)

    driver.switch_to.frame(driver.find_element(By.ID, "frame" + str(frame_id)))
    time.sleep(1)

    frame_field = driver.find_element(By.ID, "input" + str(frame_id))
    frame_field.send_keys(secret_text)

    time.sleep(1)
    
    frame_button = driver.find_element(By.ID, "button" + str(frame_id))
    frame_button.click()
    
    time.sleep(1)
    
    alert = Alert(driver)
    alert.accept()

    print('Done!')
    driver.quit()


url = 'http://localhost:8000/dz.html'
handle_frame(1, "Frame1_Secret", url)
handle_frame(2, "Frame2_Secret", url)
