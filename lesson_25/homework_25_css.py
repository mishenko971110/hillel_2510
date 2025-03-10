'''
Написати 25 CSS локаторів для сайту https://qauto2.forstudy.space/
Використовувати функцію text(), пошук за атрибутом @, та складні локатори (більш ніж з одним елементом)
'''
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")

domen = 'qauto2.forstudy.space'
username = "guest"
password = "welcome2qauto"
URL = f"https://{username}:{password}@{domen}"
driver = Chrome()
driver.get(URL)

title_h1 = driver.find_element(By.CSS_SELECTOR, ".hero-descriptor_title")
print("#1 Title: ", title_h1.text)

description = driver.find_element(By.CSS_SELECTOR, ".hero-descriptor_descr")
print("#2 Description block: ", description.text)

youtube_link = driver.find_element(By.CSS_SELECTOR, ".hero-video_frame").get_attribute("src")
print("#3 Youtube link: ", youtube_link)

about_block_titles = driver.find_elements(By.CSS_SELECTOR, ".about-block_title")
print("#4 Titles in about block: ")
for text_line in about_block_titles:
    print(text_line.text)

about_block_descriptions = driver.find_elements(By.CSS_SELECTOR, ".about-block_descr")
print("#5 Descriptions in about block: ")
for text_line in about_block_descriptions:
    print(text_line.text)

social_links = driver.find_elements(By.CSS_SELECTOR, ".socials_link")
print("#6 Social links: ")
for link_href in social_links:
    print(link_href.get_attribute("href"))

contact_link = driver.find_element(By.CSS_SELECTOR, ".contacts_link")
print("#7 Contact link: ", contact_link.get_attribute("href"))

header_logo = driver.find_element(By.CSS_SELECTOR, ".header_logo")
if header_logo:
    print("#8 Header logo: found!")
else:
    print("#8 Header logo: not found!")

footer_logo = driver.find_element(By.CSS_SELECTOR, ".footer_item")
if footer_logo:
    print("#9 Footer logo: found!")
else:
    print("#9 Footer logo: not found!")

sign_up_btn = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
if sign_up_btn:
    print("#10 Sign up btn: found!")
else:
    print("#10 Sign up btn: not found!")
sign_up_btn.click()

sign_up_form = driver.find_element(By.CSS_SELECTOR, ".modal-content")
if sign_up_form:
    print("#11 Sign up form: opened!")
else:
    print("#11 Sign up form: not opened!")

name_field = driver.find_element(By.CSS_SELECTOR, "#signupName")
if name_field:
    print("#12 Name input field: found!")
else:
    print("#12 Name input field: not found!")

last_name_field = driver.find_element(By.CSS_SELECTOR, "#signupLastName")
if last_name_field:
    print("#13 Last name input field: found!")
else:
    print("#13 Last name input field: not found!")

email_field = driver.find_element(By.CSS_SELECTOR, "#signupEmail")
if email_field:
    print("#14 Email input field: found!")
else:
    print("#14 Email input field: not found!")

password_field = driver.find_element(By.CSS_SELECTOR, "#signupPassword")
if password_field:
    print("#15 Password input field: found!")
else:
    print("#15 Password input field: not found!")

repeat_password_field = driver.find_element(By.CSS_SELECTOR, "#signupRepeatPassword")
if repeat_password_field:
    print("#16 Re-enter password input field: found!")
else:
    print("#16 Re-enter password input field: not found!")

submit_sign_up_btn = driver.find_element(By.CSS_SELECTOR, ".modal-footer .btn-primary")
if submit_sign_up_btn:
    print("#17 Submit sign up btn: found!")
else:
    print("#17 Submit sign up btn: not found!")

close_form_btn = driver.find_element(By.CSS_SELECTOR, ".modal-header .close")
if close_form_btn:
    print("#18 Close form btn: found!")
else:
    print("#18 Close form btn: not found!")
close_form_btn.click()

login_btn = driver.find_element(By.CSS_SELECTOR, ".header_signin")
if login_btn:
    print("#19 Login btn: found!")
else:
    print("#19 Login btn: not found!")
login_btn.click()

time.sleep(2)

login_form = driver.find_element(By.CSS_SELECTOR, ".modal-title")
if login_form:
    print("#20 Login form title: ", login_form.text)
else:
    print("#20 Login form title: not opened!")

email_field = driver.find_element(By.CSS_SELECTOR, "#signinEmail")
if email_field:
    print("#21 Email input field: found!")
else:
    print("#21 Email input field: not found!")

password_field = driver.find_element(By.CSS_SELECTOR, "#signinPassword")
if password_field:
    print("#22 Password input field: found!")
else:
    print("#22 Password input field: not found!")

form_link_btns = driver.find_elements(By.CSS_SELECTOR, ".btn-link")
print("#23 Form link btns:")
for btn in form_link_btns:
    if btn.text == 'Forgot password':
        frgt_password_btn = btn
    print(btn.text)
frgt_password_btn.click()

time.sleep(2)

frgt_password_form_inputs = driver.find_elements(By.CSS_SELECTOR, ".form-control")
print("#24 Inputs in forgot password form:", len(frgt_password_form_inputs))

close_frgt_password_form_btn = driver.find_element(By.CSS_SELECTOR, ".close")
if close_frgt_password_form_btn:
    print("#25 Close button in frgt_password_form: found!")
else:
    print("#25 Close button in frgt_password_form: not found!")
close_frgt_password_form_btn.click()

driver.quit()
