import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    
    domen = "qauto2.forstudy.space"
    username = "guest"
    password = "welcome2qauto"
    URL = f"https://{username}:{password}@{domen}"

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(URL)
    driver.maximize_window()

    yield driver
    driver.quit()
