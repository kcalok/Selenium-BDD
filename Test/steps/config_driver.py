from Data.config import settings
from selenium import webdriver

import pytest


@pytest.fixture(scope="module")
def driver():
    if str(settings['browser']).lower() == "firefox":
        driver = webdriver.Firefox(settings['firefox_driver'])
    elif str(settings['browser']).lower() == "chrome":
        driver = webdriver.Chrome(settings['chrome_driver'])
    else:
        driver = webdriver.Chrome(settings['chrome_driver'])
    driver .implicitly_wait(10)
    driver .maximize_window()
    print("-----------setup---------------")
    yield driver
    driver .close()
    driver .quit()
    print("Test Completed ")
