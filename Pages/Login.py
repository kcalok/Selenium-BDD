from Framework.Base import base
from Pages.HomePage import home
from Data.config import settings
from selenium import webdriver

class Login:

    instance = None


    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Login()
        return cls.instance

    def __init__(self):

        self.driver = base.get_driver()
        self.username_test_id = "#tl_login"
        self.password_text_id = "#tl_password"
        self.login_Button = "input[type = 'submit']"
        self.username = "Alok.Chauhan"
        self.password = "Passcode@321"



    def load_application(self):
        self.driver.get(settings['url'])


    def Enter_userid_text(self):
        userid = base.find_element_by_css_selector(self.username_test_id)
        userid.clear()
        userid.send_keys(self.username)

    def Enter_password_text(self):
        pwd = base.find_element_by_css_selector(self.password_text_id)
        pwd.clear()
        pwd.send_keys(self.password)

    def ClickSubmit(self):
        btn = base.find_element_by_css_selector(self.login_Button)
        btn.click()
        return home

login = Login.get_instance()












