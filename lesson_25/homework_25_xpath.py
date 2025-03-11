'''
Написати 25 XPath локаторів для сайту https://qauto2.forstudy.space/
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

title_h1 = driver.find_element(By.XPATH, "//h1")
print("#1 Title: ", title_h1.text)

description = driver.find_element(By.XPATH, "//p")
print("#2 Description block: ", description.text)

youtube_link = driver.find_element(By.XPATH, "//iframe").get_attribute("src")
print("#3 Youtube link: ", youtube_link)

about_block = driver.find_elements(By.XPATH, "//div[@class='about-block']")
print("#4 Text in about block: ")
for text_line in about_block:
    print(text_line.text)

social_links = driver.find_elements(By.XPATH, "//a[@class='socials_link']")
print("#5 Social links: ")
for link_href in social_links:
    print(link_href.get_attribute("href"))

contact_link = driver.find_element(By.XPATH, "//a[@class='contacts_link display-4']")
print("#6 Contact link: ", contact_link.get_attribute("href"))

contact_email = driver.find_element(By.XPATH, "//a[@class='contacts_link h4']")
print("#7 Contact email:", contact_email.get_attribute("href"))

header_logo = driver.find_element(By.XPATH, "//a[@class='header_logo']")
if header_logo:
    print("#8 Header logo: found!")

footer_logo = driver.find_element(By.XPATH, "//a[@class='footer_logo']")
if footer_logo:
    print("#9 Footer logo: found!")

sign_up_btn = driver.find_element(By.XPATH, "//button[@class='hero-descriptor_btn btn btn-primary']")
if sign_up_btn:
    print("#10 Sign up btn: found!")
    sign_up_btn.click()

sign_up_form = driver.find_element(By.XPATH, "//div[@class='modal-content']")
if sign_up_form:
    print("#11 Sign up form: opened!")

name_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='name']")
if name_field:
    print("#12 Name input field: found!")

last_name_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='lastName']")
if last_name_field:
    print("#13 Last name input field: found!")

email_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='email']")
if email_field:
    print("#14 Email input field: found!")

password_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='password']")
if password_field:
    print("#15 Password input field: found!")

repeat_password_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@name='repeatPassword']")
if repeat_password_field:
    print("#16 Re-enter password input field: found!")

submit_sign_up_btn = driver.find_element(By.XPATH, "//div[@class='modal-footer']//button")
if submit_sign_up_btn:
    print("#17 Submit sign up btn: found!")

close_form_btn = driver.find_element(By.XPATH, "//div[@class='modal-header']//button[@class='close']")
if close_form_btn:
    print("#18 Close form btn: found!")
    close_form_btn.click()

login_btn = driver.find_element(By.XPATH, "//button[@class='btn btn-outline-white header_signin']")
if login_btn:
    print("#19 Login btn: found!")
    login_btn.click()

login_form = driver.find_element(By.XPATH, "//div[@class='modal-content']//div[@class='modal-header']//h4")
if login_form:
    print("#20 Login form title: ", login_form.text)

email_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@id='signinEmail']")
if email_field:
    print("#21 Email input field: found!")

password_field = driver.find_element(By.XPATH, "//div[@class='form-group']//input[@id='signinPassword']")
if password_field:
    print("#22 Password input field: found!")

form_btns = driver.find_elements(By.XPATH, "//div[@class='modal-content']//button")
print("#23 Form btns:")
for btn in form_btns:
    if btn.text == 'Forgot password':
        frgt_password_btn = btn
    print(btn.text)
frgt_password_btn.click()

time.sleep(2)

frgt_password_form_inputs = driver.find_elements(By.XPATH, "//div[@class='form-group']//input")
print("#24 Inputs in forgot password form:", len(frgt_password_form_inputs))

close_frgt_password_form_btn = driver.find_element(By.XPATH, "//div[@class='modal-header']//button[@aria-label='Close']")
if close_frgt_password_form_btn:
    print("#25 Close button in frgt_password_form: found!")
    close_frgt_password_form_btn.click()

driver.quit()
