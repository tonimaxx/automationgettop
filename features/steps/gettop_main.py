from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains


try_negative_test = False

TOP_MENU_LINKS = (By.CSS_SELECTOR, ".header-nav a")
# BROWSE_ACCESSORIES_ARROW = (By.XPATH, "//li[@class='cat-item cat-item-74 cat-parent has-child active']//i[@class='icon-angle-down']")
BROWSE_ACCESSORIES_ARROW = (By.CSS_SELECTOR, ".cat-item-74 .icon-angle-down")
PRODUCT_CATEGORY_BROWSE = (By.CSS_SELECTOR, ".product-categories a")


@given('Open Home Page')
def open_home_page(context):
    context.app.main_page.open_category('')


@given('Open Category {this_category}')
def open_category(context, this_category):
    context.app.main_page.open_category(this_category)


@given('Open Page {this_page}')
def open_page(context, this_page):
    context.app.main_page.open_page(this_page)


@then('Home Page is shown')
def home_page_shown(context):
    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'home')),
        message=f"Expected class home but not found"
    )


@then('Expected all products url are not #')
def verify_all_products(context):

    top_menu_categories, top_menu_products, top_menu_incompletes = context.app.header.get_top_menu_categories()

    print("Product Categories")
    for a in top_menu_categories:
        print(f"{a} > {top_menu_categories[a]}")
    print("Products")
    for a in top_menu_products:
        print(f"{a} > {top_menu_products[a]}")
    print("Products incomplete")
    for a in top_menu_incompletes:
        print(f"{a}")

    assert len(top_menu_incompletes) == 0, f"Expected all product contain valid link, but the following product(s) does not > {top_menu_incompletes}"


@then('All categories are displayed correctly')
def verify_all_categories(context):

    results = {}
    error_results = []

    element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'header-nav')),
        message=f"Expected class header-nav for top menu, but not found"
    )
    top_menu_categories, top_menu_products, top_menu_incompletes = context.app.header.get_top_menu_categories()
    for a in top_menu_categories:
        context.app.header.click_top_menu(a.upper())
        results[a.upper()] = context.app.header.verify_breadcrumb(a.upper())

    # Negative Test
    if try_negative_test:
        test_categories = ["TELEVISION", "CAR", "BOAT"]
        for a in test_categories:
            results[a] = context.app.header.verify_breadcrumb(a)

    # Collecting results
    for x, y in results.items():
        if not y:
            error_results.append(x)
        # print(f"{x} : Is matched with Breadcrumb > {y}")

    if len(error_results) > 0 :
        print(f"{len(error_results)} Error Results > {error_results}")

    assert len(error_results) == 0, f"Expected all categories are displayed correctly, but the {len(error_results)} followings do not match > {error_results}"

@then("Click top menu {this_menu}")
def click_top_menu(context, this_menu):
    context.app.header.click_top_menu(this_menu.upper())


@then("All browse menu items are displayed correctly")
def all_browse_menu_correct(context):

    results = {}
    error_results = []
    browse_menu = []
    START_POINT_MENU = "MAC"

    context.app.header.click_top_menu(START_POINT_MENU)
    elements = context.driver.find_elements(*PRODUCT_CATEGORY_BROWSE)

    # n = 0
    for a in context.driver.find_elements(*PRODUCT_CATEGORY_BROWSE):
        thisurl = a.get_attribute('href')
        thistext = a.get_attribute('text').strip()
        # print(f"{thistext} > {thisurl}")
        browse_menu.append(thistext)

    print(f"Total links to test = {len(elements)}")

    for n in range(0, len(elements)):
        # print(f"Testing Click > {browse_menu[n]}")
        elements = context.driver.find_elements(*PRODUCT_CATEGORY_BROWSE)
        context.app.header.click_accessories_arrow()
        action = ActionChains(context.driver)
        action.click(on_element=elements[n])
        action.perform()
        element = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.woocommerce-breadcrumb')),
            message=f"Expected class breadcrumb, but not found"
        )
        results[browse_menu[n]] = context.app.header.verify_breadcrumb(browse_menu[n])
        # print(f"Result > {results[browse_menu[n]]}")
        context.driver.back()

    # Collecting results
    for x, y in results.items():
        if not y:
            error_results.append(x)
        # print(f"{x} : Is matched with Breadcrumb > {y}")

    if len(error_results) > 0 :
        print(f"{len(error_results)} Error Results > {error_results}")

    assert len(error_results) == 0, f"Expected all browse menu items are displayed correctly, but the {len(error_results)} followings do not match > {error_results}"