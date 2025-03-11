import pytest
import time
from auth_page import AuthPage
from homework_28 import driver

@pytest.mark.parametrize("name, lastname, email, password", [
    ("test", "test", "test@gmail.com", "Qwerty123!")
])


def test_user_registration(driver, name, lastname, email, password):
    auth_page = AuthPage(driver)
    auth_page.open_signup_form()
    time.sleep(1)

    auth_page.fill_registration_form(name, lastname, email, password)
    time.sleep(1)

    auth_page.submit_registration()
    time.sleep(2)

    actual_result = auth_page.get_error_msg()
    expected_result = 'User already exists'
    assert actual_result == expected_result
