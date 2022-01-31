from pages.main_page import MainPage
from pages.header import Header
from pages.base_page import Page
from pages.test_page import TestPage
from pages.helper import Helper

class Application:

    def __init__(self, driver):
            self.driver = driver
            self.main_page = MainPage(self.driver)
            self.header = Header(self.driver)
            self.base_page = Page(self.driver)
            self.test_page = TestPage(self.driver)
            self.helper = Helper(self.driver)
