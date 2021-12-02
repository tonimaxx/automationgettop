from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class Header(Page):

    TOP_MENU_LINKS = (By.CSS_SELECTOR, ".header-nav a")
    BREADCRUMB = (By.CLASS_NAME, "woocommerce-breadcrumb")
    PRODUCT_CATEGORY_BROWSE = (By.CSS_SELECTOR, ".product-categories a")
    # BROWSE_ACCESSORIES_ARROW = (By.XPATH, "//li[@class='cat-item cat-item-74 cat-parent has-child active']//i[@class='icon-angle-down']")
    BROWSE_ACCESSORIES_ARROW = (By.CSS_SELECTOR, ".cat-item-74 .icon-angle-down")


    def verify_breadcrumb(self, check_text):
        breadcrumb = self.driver.find_element(*self.BREADCRUMB).text.upper()
        is_matched = True if (check_text.upper() in breadcrumb) else False
        test_result = "Matched | ✓ Pass" if is_matched else "Not Matched | ✕ Fail"
        print(f"Check '{check_text}', Breadcrumb = {breadcrumb} > {test_result}")
        return is_matched


    def click_top_menu(self, link_text):
        element = self.driver.find_element_by_link_text(link_text)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()


    def click_accessories_arrow(self):
        # element = self.driver.find_elements(*self.BROWSE_ACCESSORIES_ARROW)
        self.click(*self.BROWSE_ACCESSORIES_ARROW)


    def click_browse_menu(self, link_no):
        # element = self.driver.find_element_by_link_text(link_text)
        # elements = self.driver.find_elements(*self.PRODUCT_CATEGORY_BROWSE)
        elements = self.driver.find_elements(*self.PRODUCT_CATEGORY_BROWSE)
        action = ActionChains(self.driver)
        action.click(on_element=elements[link_no])
        action.perform()


    def get_top_menu_categories(self):
        product_links = {}
        product_incomplete = []
        product_categories = {}

        for a in self.driver.find_elements(*self.TOP_MENU_LINKS):
            thisurl = a.get_attribute('href')
            thistext = a.get_attribute('text').strip()
            if "/product/" in thisurl and len(thistext) > 0:
                product_links[thistext] = thisurl
            elif "/product-category/" in thisurl and len(thistext) > 0:
                product_categories[thistext] = thisurl
            elif "#" in thisurl and len(thistext) > 0:
                product_incomplete.append(thistext)

        return product_categories, product_links, product_incomplete

    def get_browse_menu_categories(self):

        product_links = {}
        product_incomplete = []
        product_categories = {}

        for a in self.driver.find_elements(*self.PRODUCT_CATEGORY_BROWSE):
            thisurl = a.get_attribute('href')
            thistext = a.get_attribute('text').strip()

            print(f"{thistext} > {thisurl}")

        #     if "/product/" in thisurl and len(thistext) > 0:
        #         product_links[thistext] = thisurl
        #     elif "/product-category/" in thisurl and len(thistext) > 0:
        #         product_categories[thistext] = thisurl
        #     elif "#" in thisurl and len(thistext) > 0:
        #         product_incomplete.append(thistext)
        #
        # return product_categories, product_links, product_incomplete
