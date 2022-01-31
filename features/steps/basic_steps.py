from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
import time
import config


@given('User is at {page}')
def open_page(context, page):
    context.app.base_page.open_url(config.page_url(page))


@when('Page is ready with {element} existed')
def page_ready(context, element):
    e = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator(element)),
        message=f"Expected '{element}', but not found!"
    )
    print(f"✓ Page is ready with element '{element}' founded!")

@then('Element {element} is existed')
def element_presented(context, element):
    if '|' in element:
        elements = element.split('|')
        for i in elements:
            e = WebDriverWait(context.driver, 10).until(
                    EC.presence_of_element_located(config.locator(i)),
                    message=f"Expected '{i}', but not found!"
                )
            if config.SHOWLOG: print(f"✓ Element '{i}' founded!")
            # context.app.helper.hellotoni()
    else:
        e = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(config.locator(element)),
            message=f"Expected '{element}', but not found!"
        )
        print(f"✓ Element '{element}' founded!")

@then('Click all elements in {element} and no broken link')
def click_all_no_broken(context, element):
    e = context.driver.find_elements(*config.locator(element))
    for i in range(len(e)):
        e = context.driver.find_elements(*config.locator(element))[i]
        e.click()
        context.driver.back()



@then('Element {element} contains text {text}')
def element_contains_text(context, element, text):
    e = context.driver.find_elements(*config.locator(element))[0].text
    assert text in e, f"Expected '{text}' in {e}, but not found!"
    print(f"✓ '{text}' found in {e}")
    # print(f"Element {element} text = {e}")


@then('User clicks on {element}')
def click_locator(context, element):
    e = context.driver.find_elements(*config.locator(element))[0]
    e.click()


@then('Hover mouse on {element}')
def hover_mouse(context, element):
    print(f"Hover {element} {config.locator(element)}")
    e = context.driver.find_elements(*config.locator(element))[0]
    actions = ActionChains(context.driver)
    actions.move_to_element(e)
    # actions.click(hidden_submenu)
    actions.perform()


@then('Element {element} contains {x} elements')
def element_contains_count(context, element, x):
    e = context.driver.find_elements(*config.locator(element))
    items = [n.text for n in e]
    assert int(x) == len(e), f"Expect {element} contains {x} elements but it is {len(e)} > {items}"


@then('Type {text} to {element} and Enter')
def enter_text(context, text, element):
    e = context.driver.find_elements(*config.locator(element))[0]
    e.send_keys(text)
    e.send_keys(Keys.ENTER)


@then('A page is shown, no 404 error')
def no_404(context):
    # Google for Small Business
    e = context.driver.find_element_by_css_selector(".h-c-headline.h-c-headline--one")
    print(e.text)
    thistext = e.text
    assert "Succeed" in thistext, "expect word 'Success', but not found"


@when('do something at {page}')
def do_something(context,page):
    print(config.page_url(page))

    # time.sleep(5)

    # print(*page)
    context.app.base_page.open_url(MAIN_PAGE)

    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(Amazon_homepage_logo_ID),
        message=f"Expected class home but not found"
    )

    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(Amazon_homepage_logo_ID),
        message=f"Expected class home but not found"
    )

    element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(Amazon_homepage_logo_ID),
            message=f"Expected class home but not found"
        )



    element = WebDriverWait(context.driver, 10).until(
        EC.title_is("Amazon.com. Spend less. Smile more."),
        message=f"Expected class home but not found"
    )

    a = context.driver.find_elements(*submenu_ID)
    print(f"a={len(a)}")

    textlinks = [i.text for i in a]

    # print(textlinks)

    for i in range(0, len(a)):
        a = context.driver.find_elements(*submenu_ID)

        actions = ActionChains(context.driver)
        # e = context.driver.find_elements(*User_hover_ID)[0]
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(Amazon_homepage_logo_ID),
            message=f"Expected class home but not found"
        )
        actions.click(on_element=a[i])

        # actions.move_to_element(e)

        actions.perform()


    # context.app.main_page.open_category('')
    # results = context.app.base_page.find_elements(By.CSS_SELECTOR, this_selector)


#click, click_and_hold, context_click, double_click, drag_and_drop, drag_and_drop_by_offset, key_down, key_up, move_by_offset, move_to_element, move_to_element_with_offset, perform, pause, release, reset_actions, send_keys


#https://selenium-python.readthedocs.io/waits.html
# https://www.geeksforgeeks.org/action-chains-in-selenium-python/