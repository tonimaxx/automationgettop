from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:


    TEST_URL = 'https://gmail.com'

    ROOT_URL = 'https://gettop.us/'
    PRODUCT_CATEGORY_URL = (f"{ROOT_URL}product-category/")
    CATEGORIES = {'macbook', 'iphone', 'ipad', 'accessories'}

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.base_url = self.ROOT_URL

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def hover_link_text(self, link_text):
        element = self.driver.find_element_by_link_text(link_text)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_url(self, end_url=''):
        self.driver.get(f'{end_url}')

    def click_link_text(self, link_text):
        element = self.driver.find_element_by_link_text(link_text)
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()

    def open_page(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def open_category_page(self, end_url=''):
        self.driver.get(f'{self.base_url}{end_url}')

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'

    def verify_title_contains(self, expected_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.title_contains(expected_text), message=f'{expected_text} not in title'
        )

    def go_back(self):
        self.driver.back()

    def log(self, log):
        print(f"log>{log}")
