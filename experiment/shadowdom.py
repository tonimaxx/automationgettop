from basic_steps import *

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
import time
import config
from pyshadow.main import Shadow

# Test Credential
CC_Number = "4024007155478968"
CC_Expiration = "03/24"
CC_CVN = "123"
USER_EMAIL = "jarussoontornsing@yahoo.com"

test_results = []



@when('Search for {keyword} from Potterybarn homepage')
def pb_search(context, keyword):

    context.driver.refresh()
    enter_text(context, keyword, "Potterybarn Search Field")
    # Wait for result
    element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located(config.locator("Potterybarn Search Result Heading")),
            message=f"Expected Search Result, but not found"
        )
    e = context.driver.find_elements(*config.locator("Potterybarn Modal Minimize Button"))
    print(f"found {len(e)} elements")
    if len(e) > 0 :
        print("Click Minimize Button")
        try:
            e[0].click()
        except:
            pass

    # e.click()
    # print(f"e={e}")
    # time.sleep(30)

@when('Click on a product at column {col} row {row}')
def pb_click_product(context, row, col):
    item_to_click_index = ((int(row)-1)*4)+int(col)-1
    e = context.driver.find_elements(*config.locator("Potterybarn Product Images"))
    print(f"found {len(e)} elements")
    print(f"click on item{item_to_click_index}")
    e[item_to_click_index].click()
    # e = context.driver.find_elements(*config.locator("Latch Heading Word"))

@when('Continue to Checkout')
def pb_checkout(context):
    print("now checkout")
    context.driver.get(config.page_url("PB Shopping Cart"))
    # Wait for result
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCO CreditCard Button")),
        message=f"Expected CreditCard Radio Button, but not found"
    )
    e = context.driver.find_elements(*config.locator("PBCO Checkout Button"))
    e[0].click()
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCO Guest Checkout Button")),
        message=f"Expected Guest Checkout Button, but not found"
    )
    element.click()


@when('Place an order without Address information')
def pb_order_without_address_info(context):
    global test_results
    print("Place an order without Address information")
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCS Full Name field")),
        message=f"Expected Full Name field, but not found"
    )

    element.send_keys("")
    context.driver.find_elements(*config.locator("PBCS Address field"))[0].clear()
    context.driver.find_elements(*config.locator("PBCS Apt field"))[0].clear()
    context.driver.find_elements(*config.locator("PBCS City field"))[0].clear()
    context.driver.find_elements(*config.locator("PBCS Zip field"))[0].clear()
    context.driver.find_elements(*config.locator("PBCS Phone field"))[0].clear()
    select_state = Select(context.driver.find_elements(*config.locator("PBCS State field"))[0])
    # select_state.select_by_index(6)
    select_state.select_by_visible_text("State")
    # click_button = context.driver.find_elements(*config.locator("PBCS Continue Button"))[0].click()
    click_button = context.driver.find_elements(*config.locator("PBCS Continue Button"))
    click_button[0].click()
    print(f"Found Type {type(click_button)} Len {len(click_button)} Click Button")
    element = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located(config.locator("PBCS shipping-fullName-error")),
        message=f"Expected shipping-fullName-error, but not found"
    )
    if element:
        this_result = "✓ Place an order without Address information : Throw error as expect"
        test_results.append(this_result)
        print(this_result)
        print(test_results)


def expand_shadow_element(context, element):
    shadow_root = context.driver.execute_script("return arguments[0].shadowRoot", element)
    return shadow_root

@when('Place an order without Email')
def pb_order_without_email(context):
    print("Place an order without Email")
    context.driver.get(config.page_url("PB Checkout"))
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCS Full Name field")),
        message=f"Expected Full Name field, but not found"
    )

    element.send_keys("Jarus Soontornsing")
    context.driver.find_elements(*config.locator("PBCS Address field"))[0].send_keys("355 Reflection Cir")
    context.driver.find_elements(*config.locator("PBCS Apt field"))[0].send_keys("Apt 26")
    context.driver.find_elements(*config.locator("PBCS City field"))[0].send_keys("San Ramon")
    context.driver.find_elements(*config.locator("PBCS Zip field"))[0].send_keys("94583")
    context.driver.find_elements(*config.locator("PBCS Phone field"))[0].send_keys("9256232821")
    select_state = Select(context.driver.find_elements(*config.locator("PBCS State field"))[0])
    # select_state.select_by_index(6)
    select_state.select_by_visible_text("California")
    context.driver.find_elements(*config.locator("PBCS Continue Button"))[0].click()

    # element = WebDriverWait(context.driver, 10).until(
    #     EC.visibility_of_element_located(config.locator("PBCS Review Content Container")),
    #     message=f"Expected Review Content Container, but not found"
    # )

    time.sleep(2)
    context.driver.get(config.page_url("PB Payment"))

    # Find Place Order Button Location (Shadow DOM)
    print("Find Place Order Button Location (Shadow DOM)")

    root1 = context.driver.find_elements(By.TAG_NAME,'checkout-app')[0]
    shadow_root1 = context.driver.execute_script("return arguments[0].shadowRoot", root1)
    print(f"Root1 = {shadow_root1} type = {type(shadow_root1)}")

    print(shadow_root1.__dict__)
    print(dir(shadow_root1))


    # Fill Email Field
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCP Email Field")),
        message=f"Expected Email Field, but not found"
    )
    element.send_keys(USER_EMAIL)

    # Move from Email Field to Press Place Order Button
    N = 5  # number of times you want to press TAB
    actions = ActionChains(context.driver)
    for _ in range(N): actions = actions.send_keys(Keys.TAB)
    actions.send_keys(Keys.ENTER)
    actions.perform()

    # Fill Payment Information
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(config.locator("PBCP Credit Card Number Field")),
        message=f"Expected Email Field, but not found"
    )

    element.send_keys(CC_Number).send_keys(Keys.TAB)
    actions.send_keys(CC_Expiration).send_keys(Keys.TAB)
    actions.send_keys(CC_CVN).send_keys(Keys.TAB)
    actions.perform()




    # context.driver.find_elements(*config.locator("PBCP Email Field"))[0].send_keys("tonimaxx@gmail.com")
    #
    # shadow = Shadow(context.driver)
    # element = shadow.find_element('body')
    # print(f"shadow element : {element}")
    #
    # all_shadow = shadow.get_all_shadow_element(element,'body')
    # print(all_shadow)


    # root2 = shadow_root1.find_element('ID','payment-region')
    # shadow_root2 = context.driver.execute_script("return arguments[0].shadowRoot", root2)
    # print(f"Root2 = {shadow_root2} type = {type(shadow_root2)}")


    # shadow_root1 = expand_shadow_element(context, root1)
    # print(f"Root1 = {shadow_root1} type = {type(shadow_root1)}")
    # print(f"Root2 = {shadow_root2} type = {type(shadow_root2)}")
    # getShadowRoot = lambda host: context.driver.execute_script("return arguments[0].shadowRoot", host)
    #
    # [{"name": "css", "value": "checkout-app"}, {"name": "css", "value": "payment-region"},
    #  {"name": "css", "value": "place-order-view"}, {"name": "css", "value": "[name='placeOrder']"},
    #  {"name": "css", "value": ".primary"}]

    # host1 = context.driver.find_element(By.TAG_NAME,"checkout-app")
    # root1 = getShadowRoot(host1)
    # # NEWS_OPTION = {'By': By.ID, 'value': 'payment-region'}
    # host2 = root1.find_element(By.TAG_NAME,'payment-region')
    # # host2 = root1.find_element(By.ID, "payment-region")
    #
    #
    # root2 = getShadowRoot(host2)
    # host3 = root2.find_element(By.TAG_NAME, "place-order-view")
    # root3 = getShadowRoot(host3)

    # print(f"Root1 = {root1} /n{root2}/n{root3}")
    # print(f"Root1 = {root1} type = {type(root1)}")


    # click_button = context.driver.find_elements(*config.locator("PBCS Continue Button"))
    # for i, a_click_button in enumerate(click_button):
    #     print(f"Try Click Button #{i}")
    #     try:
    #         a_click_button.click()
    #     except:
    #         print(f"Click Button #{i} Error")


    # element = context.driver.find_elements(By.LINK_TEXT,"Continue").click()

    time.sleep(10)


@when('Place an order without Payment information')
def pb_order_without_payment_info(context):
    print("Place an order without Payment information")




@when('Add current product to cart')
def pb_add_product_to_cart(context):
    # Simulate select product subsets
    e = context.driver.find_elements(*config.locator("PB Product Subsets"))
    total_subset = len(e)
    print(e)
    print(f"Total subset = {total_subset}")
    # Expand all product subset options
    # ".product-subset dl dd#step3 a"
    for i,element in enumerate(e):

        print(f"Select an option in subset {i}")

        context.driver.execute_script("arguments[0].setAttribute('style','height: auto;')", element)
        # Simulate choosing the first option
        option_locator = f".product-subset dl dd#step{i} a"
        e = context.driver.find_elements(By.CSS_SELECTOR,option_locator)
        if len(e) > 0:
            try:
                e[0].click()
                print(f"Clicked {i}")
            except:
                pass

    # Select a color option if any
    e = context.driver.find_elements(*config.locator("PB Select Color"))
    if len(e) > 0:
        e[0].click()
        print(f"Color option : {len(e)}")

    # Select a Swatch option if any
    e = context.driver.find_elements(*config.locator("PB SELECT Swatch"))
    if len(e) > 0:
        e[0].click()
        print(f"Swatch option : {len(e)}")

    # Select Subset SKU option if any
    e = context.driver.find_elements(*config.locator("PB Select Subset SKU"))
    if len(e) > 0:
        e[0].click()
        print(f"Swatch option : {len(e)}")

    # Click Add to Cart if interactable
    e = context.driver.find_elements(*config.locator("PB Product Add to Cart Button2"))
    if len(e) > 0:
        e[0].click()
        print(f"Swatch option : {len(e)}")

    # Click Accept Terms Button
    e = context.driver.find_elements(*config.locator("PB Accept Terms Button"))
    if len(e) > 0:
        e[0].click()
        print(f"Click Accept Terms Button : {len(e)}")

    # Click Continue Shopping Button
    e = context.driver.find_elements(*config.locator("PB Continue Shopping Button"))
    if len(e) > 0:
        e[0].click()
        print(f"CLick Overlay Close Button : {len(e)}")


    # time.sleep(20)
    # e = context.driver.find_elements(*config.locator("Pottertbarn Product Add to Cart Button"))
    # e[0].click()
    # print('Clicked --> Add to cart')

#
# from selenium import webdriver
# from time import sleep
# driver = webdriver.Edge()
#
# driver.get("https://www.symbolab.com/solver/step-by-step/%5Cint%20x%5Csqrt%7B4-x%5E%7B4%7D%7Ddx")
# sleep(3)
# selects = driver.find_elements_by_xpath("//span[@class='locked-step']")
# for select in selects:
#     driver.execute_script("arguments[0].setAttribute('class', 'showStepsButton')", select)