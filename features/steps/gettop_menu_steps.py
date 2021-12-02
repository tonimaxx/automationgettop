from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains

from gettop_helper import locatorClass

# locator = locatorClass()
# print(locator.getVal("TOP_MENU_LINKS"))
# print(locator.getVal("BROWSE_ACCESSORIES_ARROW"))

TOP_MENU_LINKS = (By.CSS_SELECTOR, ".header-nav a")
TOP_MENU_DROP_DOWN = (By.CSS_SELECTOR, ".has-dropdown")
# TOP_MENU_CURRENT_DROP_DOWN = (By.CSS_SELECTOR, "#menu-item-469 a")
TOP_MENU_CURRENT_DROP_DOWN = (By.CSS_SELECTOR, ".current-dropdown")


@when("Click top menu {menu}")
def click_top_menu(context, menu):
    context.app.header.click_top_menu(menu)

@then("The correct page is opened with expected keyword {keyword}")
def correct_page_open(context, keyword):
    context.app.base_page.wait_for_element_appear(*TOP_MENU_LINKS)
    assert context.app.header.verify_breadcrumb(keyword), f"Expect {keyword} in BreadCrumb, but not found!"

@when("Hover over top menu {menu}")
def hover_on_menu(context, menu):
    context.app.base_page.hover_link_text(menu)

@then("Menu option appear with expected keyword {keyword}")
def option_appear_with_keyword(context, keyword):
    is_keyword_found = False
    # context.app.base_page.wait_for_element_appear(*TOP_MENU_LINKS)
    context.app.base_page.wait_for_element_appear(*TOP_MENU_CURRENT_DROP_DOWN)
    all_menu = context.app.base_page.find_elements(*TOP_MENU_CURRENT_DROP_DOWN)
    for n in all_menu:
        print(n.text)
        if keyword in n.text:
            is_keyword_found = True
    assert is_keyword_found, f"Expect {keyword} in Menu option, but not found!"
