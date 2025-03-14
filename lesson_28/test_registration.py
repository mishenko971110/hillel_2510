# import pytest
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from auth_page import AuthPage
# from auth_locators import AuthXpathLocators, AuthIdLocators

# @pytest.mark.parametrize("name, lastname, email, password", [
#     ("test", "test", "test@gmail.com", "Qwerty123!")
# ])


# def test_user_registration(driver, name, lastname, email, password):
#     auth_page = AuthPage(driver)
#     auth_page.open_signup_form()
    
#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(AuthIdLocators.name_input)
#     )

#     auth_page.fill_registration_form(name, lastname, email, password)
#     WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable(AuthXpathLocators.submit_btn)
#     )

#     auth_page.submit_registration()
#     actual_result = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located(AuthXpathLocators.error_msg)
#     ).text

#     actual_result = auth_page.get_error_msg()
#     expected_result = 'User already exists'
#     assert actual_result == expected_result
