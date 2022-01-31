from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
import time
import config

@then('Click all LatchOS sub menus and no broken link')
def click_all_no_broken(context):
    element_latchos = "Latch Top Menu LatchOS"
    ea = context.driver.find_elements(*config.locator(element_latchos))[0]
    ea.click()
    element_submenu = "Latch Top Menu"
    e = context.driver.find_elements(*config.locator(element_submenu))
    print(f"Found {len(e)} menus")
    ea.click()
    # exit()

    # e = context.driver.find_elements(*config.locator(element))
    for i in range(len(e)):
        element_latchos = "Latch Top Menu LatchOS"
        e1 = context.driver.find_elements(*config.locator(element_latchos))[0]
        e1.click()
        element_submenu = "Latch Top Menu"
        e2 = context.driver.find_elements(*config.locator(element_submenu))[i]
        print(f"Click menu > {e2.text}")
        e2.click()

        context.driver.back()

@then('Click LatchOS sub menu {submenu} and navigate correctly')
def click_latchos_submenu(context,submenu):
    element_latchos = "Latch Top Menu LatchOS"
    ea = context.driver.find_elements(*config.locator(element_latchos))[0]
    ea.click()
    element_submenu = "Latch Top Menu"
    # e = context.driver.find_elements(*config.locator(element_submenu))
    esub = context.driver.find_element_by_link_text(submenu)
    esub.click()
    element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".heading-42")),
            message=f"Expected class home but not found"
        )
    print(f"✓ Header : {element.text}")
    assert submenu.split(" ")[0] in element.text, f"Expect {submenu} in the header, but not!"