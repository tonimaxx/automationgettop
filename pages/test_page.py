from selenium.webdriver.common.by import By
from pages.base_page import Page

class TestPage(Page):

    TOP_MENU_LINKS = (By.CSS_SELECTOR, ".header-nav a")

    def open_main_page(self):
        self.open_page('')

    def open_category(self, end_url=''):
        self.open_category_page(end_url)

    def open_page(self, end_url=''):
        self.open_page(end_url)


