from auth_locators import AuthXpathLocators, AuthIdLocators
from homework_28 import driver

class AuthPage:
    def __init__(self, driver):
        self.driver = driver

    def open_signup_form(self):
        self.driver.find_element(*AuthXpathLocators.sign_up_btn).click()

    def fill_registration_form(self, name, lastname, email, password):
        self.driver.find_element(*AuthIdLocators.name_input).send_keys(name)
        self.driver.find_element(*AuthIdLocators.last_name_input).send_keys(lastname)
        self.driver.find_element(*AuthIdLocators.email_input).send_keys(email)
        self.driver.find_element(*AuthIdLocators.password_input).send_keys(password)
        self.driver.find_element(*AuthIdLocators.repeat_password_input).send_keys(password)

    def submit_registration(self):
        self.driver.find_element(*AuthXpathLocators.submit_btn).click()

    def get_error_msg(self):
        return self.driver.find_element(*AuthXpathLocators.error_msg).text
