from Framework.Base import base
from selenium import webdriver
from Data.config import settings

class HomePage:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
        return cls.instance


    def __init__(self):
        self.driver = base.get_driver()
        self.frame_name = 'titlebar'
        self.menu_title = "div[class = 'menu_title'] span[class = 'bold']"
        self.logout_img = "img[title = 'Logout']"
        self.d = webdriver.Chrome(settings['chrome_driver'])



    def verify_title(self):
        base.switch_to_default()
        base.switch_to_frame_by_name(self.frame_name)
        text = base.find_element_by_css_selector(self.menu_title).text.split()
        return text[0]

    def verify_Logout_Img_IsDisplayed(self):
        base.switch_to_default()
        base.switch_to_frame_by_name(self.frame_name)
        flag = base.find_element_by_css_selector(self.logout_img).is_displayed()
        return flag

    def logout_Application(self):
        base.switch_to_default()
        base.switch_to_frame_by_name(self.frame_name)
        #self.driver.switch_to.frame(self.driver.find_element_by_name(self.frame_name))
        base.find_element_by_css_selector(self.logout_img).click()

home = HomePage.get_instance()



