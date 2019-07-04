from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from Data.config import settings
from urllib.parse import urljoin

class BaseClass:

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = BaseClass()
        return cls.instance

    def __init__(self):
        self.driver = None

    def set_driver(self, driver):
        self.driver = driver

    def get_driver(self):
        return self.driver

    def goto_page(self, page):
        self.driver.get(urljoin(settings['url'], page.lower()))

    def switch_to_frame_by_name(self, frame_name):
        try:

           # WebDriverWait(self.driver,settings['wait_time']).until(cond.presence_of_element_located(By.NAME,frame_name))
            return self.driver.switch_to.frame(self.driver.find_element_by_name(frame_name))
        except:
            print("{} , : Frame is not found on the screen".format(frame_name))


    def switch_to_frame_by_id(self, frame_id):
        try:

            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.ID, frame_id))
            return self.driver.switch_to.frame(self.driver.find_element_by_name(frame_id))
        except:
            print("{} , : Frame is not found on the screen".format(frame_id))

    def switch_to_default(self):
        print("Switched to default frame")
        return self.driver.switch_to.default_content()


    def find_element_by_id(self, element_id):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.ID,element_id))
            return self.driver.find_element_by_css_selector(element_id)
        except:

            print("{} , : Element is not present on the screen".format(element_id))

    def find_element_by_name(self, element_name):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.NAME,element_name))
            self.driver.find_element_by_name(element_name)
        except:
            print("{} , : Element is not present on the screen".format(element_name))

    def find_element_by_xpath(self, element_xpath):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.XPATH,element_xpath))
            return self.driver.find_element_by_xpath(element_xpath)
        except:
            print("{} , : Element is not present on the screen".format(element_xpath))

    def find_element_by_css_selector(self,element_css):
        try:
            #WebDriverWait(driver, settings['wait_time']).until(cond.element_to_be_selected(By.CSSSELECTOR, element_css))
            return self.driver.find_element_by_css_selector(element_css)
        except:
            print("{} , : Element is not present on the screen".format(element_css))

    def find_element_by_tag_name(self, tag_name):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.TAG_NAME, tag_name))
            return self.driver.find_element_by_tag_name(tag_name)
        except:
            print("{} , : Element is not present on the screen".format(tag_name))

    def find_element_by_class_name(self, class_name):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.CLASS_NAME, class_name))
            return self.driver.find_element_by_class_name(class_name)
        except:
            print("{} , : Element is not present on the screen".format(class_name))

    def find_element_by_link_text(self, link_text):
        try:
            #WebDriverWait(self.driver, settings['wait_time']).until(cond.presence_of_element_located(By.LINK_TEXT, link_text))
            return self.driver.find_element_by_link_text(link_text)
        except:
            print("{} , : Element is not present on the screen".format(link_text))

    def find_element_by_partial_link_text(self, partiallink_text):
        try:
            #WebDriverWait(self.driver,settings['wait_time']).until(cond.presence_of_element_located(By.PARTIAL_LINK_TEXT,partiallink_text))
            return self.driver.find_element_by_partial_link_text(partiallink_text)
        except:
            print("{} , : Element is not present on the screen".format(partiallink_text))

    def verify_page_name_exists(self, pagename):
        assert pagename in self.find_element_by_tag_name(self.driver, pagename).text, "PageName {} not found on the page".format(pagename)

base = BaseClass.get_instance()



















