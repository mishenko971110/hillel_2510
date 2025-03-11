'''
Створіть необхідні класи та функції, щоб за допомогою Selenium на сайті
ввести номер накладної (передається з тесту) та отримує статус посилки в теркінгу.
Тест повинен перівіряти, що отриманий статус відповідає очікуваному.
'''
from selenium import webdriver
from track_locators import TrackingCssLocators, TrackingXpathLocators
import time


def check_post_status(post_URL, post_id):
    driver = webdriver.Chrome()
    driver.get(post_URL)

    time.sleep(1)

    track_post_field = driver.find_element(*TrackingCssLocators.track_post_field)
    track_post_field.send_keys(post_id)

    search_button = driver.find_element(*TrackingCssLocators.search_button)
    search_button.click()

    time.sleep(3)

    try:
        error_check = driver.find_element(*TrackingXpathLocators.error_msg)
        if error_check:
            print('Посилки з таким номером не знайдено!')
            driver.quit()
            return 'Ми не знайшли посилку за таким номером.'
    except:
        frame_btn = driver.find_element(*TrackingXpathLocators.frame_btn)
        frame_btn.click()

        time.sleep(2)

        status_text = driver.find_element(*TrackingXpathLocators.status_text).text
        print('Статус посилки: ', status_text)
        driver.quit()
        return status_text
