from pytest_bdd import (
    given,
    scenario,
    when,
    then,
)
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


def test_base(driver):
    from Framework.Base import base
    base.set_driver(driver)
    print("-----------test base called first  ---------------")


@pytest.fixture(scope="module")
def login():
    from Pages.Login import login
    print("----------- login fixture called ---------------")
    yield login

@scenario('testlink.feature','Login to testlink')
def test_login():
    pass

@given('I load the website')
def open_application(login):
    login.load_application()

@given('I enter userid')
def enter_userid(login):
    login.Enter_userid_text()

@given('I enter Password')
def enter_Password(login):
    login.Enter_password_text()

@given('I Click Login button')
def home_page(login):
    # home page is displayed hence returned
    home = login.ClickSubmit()
    return home


@then('I am able to login to testlink application')
def user_is_logged(home_page):
        assert "Alok.Chauhan" in home_page.verify_title(), "UserName {} not found on the page".format("Alok.Chauhan")
        print(home_page.verify_title())


















