'''
Створіть необхідні класи та функції, щоб за допомогою Selenium на сайті
ввести номер накладної (передається з тесту) та отримує статус посилки в теркінгу.
Тест повинен перівіряти, що отриманий статус відповідає очікуваному.
'''
# from selenium import webdriver
# from tracking_page import TrackingPage

# def check_post_status(post_URL, post_id):
#     driver = webdriver.Chrome()
#     tracking_page = TrackingPage(driver)

#     try:
#         tracking_page.open_url(post_URL)
#         tracking_page.track_package(post_id)
#         return tracking_page.get_tracking_status()
#     finally:
#         driver.quit()
