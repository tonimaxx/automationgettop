from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains

TOP_MENU_LINKS = (By.CSS_SELECTOR, ".header-nav a")
# BROWSE_ACCESSORIES_ARROW = (By.XPATH, "//li[@class='cat-item cat-item-74 cat-parent has-child active']//i[@class='icon-angle-down']")
BROWSE_ACCESSORIES_ARROW = (By.CSS_SELECTOR, ".cat-item-74 .icon-angle-down")
PRODUCT_CATEGORY_BROWSE = (By.CSS_SELECTOR, ".product-categories a")


