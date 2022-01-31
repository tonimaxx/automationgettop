from pages.base_page import Page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Helper(Page):

    def hellotoni(self):
        print("Hello Toni!")

    def elements_to_list(self, locator):
        e = self.driver.find_elements(*locator)
        return len(e)

    def elements_text(self, locator):
        e = self.driver.find_elements(*locator)
        return len(e)

def main():

    driver = webdriver.Chrome(
        executable_path='../chromedriver',
    )

    driver.get("http://www.python.org")
    e = driver.find_elements_by_css_selector("#mainnav .navigation.menu li.tier-1")
    print(len(e))

    x = Helper("TEST")
    x.hellotoni()


    driver.delete_all_cookies()
    driver.quit()

# main()


