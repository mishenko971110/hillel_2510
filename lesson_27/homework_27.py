'''
Створіть необхідні класи та функції, щоб за допомогою Selenium на сайті
ввести номер накладної (передається з тесту) та отримує статус посилки в теркінгу.
Тест повинен перівіряти, що отриманий статус відповідає очікуваному.
'''
from selenium import webdriver
from track_locators import TrackingCssLocators, TrackingXpathLocators

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework_27 import TrackingCssLocators, TrackingXpathLocators

def check_post_status(post_URL, post_id):
    driver = webdriver.Chrome()
    driver.get(post_URL)

    wait = WebDriverWait(driver, 3)

    track_post_field = wait.until(EC.presence_of_element_located(TrackingCssLocators.track_post_field))
    track_post_field.send_keys(post_id)

    search_button = wait.until(EC.element_to_be_clickable(TrackingCssLocators.search_button))
    search_button.click()

    try:
        error_check = wait.until(EC.presence_of_element_located(TrackingXpathLocators.error_msg))
        return 'Ми не знайшли посилку за таким номером.'
    except:
        frame_btn = wait.until(EC.element_to_be_clickable(TrackingXpathLocators.frame_btn))
        frame_btn.click()
        status_text = wait.until(EC.presence_of_element_located(TrackingXpathLocators.status_text)).text
        return status_text
    finally:
        driver.quit()
