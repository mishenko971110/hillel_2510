from selenium.webdriver.common.by import By

class AuthXpathLocators:
    sign_up_btn = (By.XPATH, "//button[text()='Sign up']")
    submit_btn = (By.XPATH, "//button[text()='Register']")
    error_msg = (By.XPATH, "//p[@class='alert alert-danger']")

class AuthIdLocators:
    name_input = (By.ID, "signupName")
    last_name_input = (By.ID, "signupLastName")
    email_input = (By.ID, "signupEmail")
    password_input = (By.ID, "signupPassword")
    repeat_password_input = (By.ID, "signupRepeatPassword")
