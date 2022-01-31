import json
import os
from selenium.webdriver.common.by import By

SHOWLOG = True

PAGE_URLS = {
    "Amazon Homepage": "https://amazon.com",
    "Google Homepage": "https://google.com",
    "Gmail Homepage": "https://mail.google.com",
    "Gettop Homepage": "https://gettop.us",
    "Python.org": "https://python.org",
    "Latch.com": "https://latch.com",
    "Potterybarn.com": "https://www.potterybarn.com",
    "PB Checkout": "https://www.potterybarn.com/checkout/app/shipping.html",
    "PB Shopping Cart": "https://www.potterybarn.com/shoppingcart/",
    "PB Payment":"https://www.potterybarn.com/checkout/app/payment.html"

}

LOCATORS = {
    "Gettop Homepage Logo": (By.XPATH, "//img[@src='https://gettop.us/wp-content/uploads/2020/06/black.png']"),
    "Gettop Footer Copyright": (By.XPATH, "//div[@class='copyright-footer']"),
    "Cart Logo": (By.XPATH, "//span[2]/strong[.='0']"),
    "Latest Product": (By.CSS_SELECTOR, "#content > div:nth-of-type(2) .section-title-main"),
    "Top Menu Mac": (By.XPATH, "//li[@class='menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-468 has-dropdown']/a[.='Mac']"),
    "Top Menu Mac2": (By.ID, "menu-item-468"),
    "Top Menu Mac3": (By.XPATH, "//li[@class='menu-item menu-item-type-custom menu-item-object-custom current-menu-item menu-item-has-children menu-item-468 active has-dropdown']/a[.='Mac']"),
    "Bread Crumb": (By.XPATH, "//nav[@class='woocommerce-breadcrumb breadcrumbs uppercase']"),
    "Left Menu": (By.CSS_SELECTOR, "ul.product-categories li a"),
    "Search Icon": (By.CSS_SELECTOR, "[aria-label='Search'] > .icon-search"),
    "Search Field": (By.ID, "woocommerce-product-search-field-0"),
    "Python Homepage Logo": (By.XPATH, "//img[@alt='python™']"),
    "Python Homepage Main Navigator": (By.CSS_SELECTOR, "#mainnav .navigation.menu li.tier-1"),
    "Python Homepage Top Menu": (By.CSS_SELECTOR, "#top .menu li"),
    "Python Homepage Slide Menu Buttons": (By.CSS_SELECTOR, ".flex-control-nav li"),
    "Latch Top Menu LatchOS": (By.CLASS_NAME,"w-icon-dropdown-toggle"),
    "Latch Top Menu": (By.CSS_SELECTOR, "#w-dropdown-list-0 a"),
    "Latch Heading Word": (By.CSS_SELECTOR, ".heading-42"),
    "Potterybarn Main Icon": (By.CLASS_NAME,"icon-cart"),
    "Potterybarn Search Field": (By.ID,"search-field"),
    "Potterybarn Search Result Heading": (By.CSS_SELECTOR,".search-results-heading-term"),
    "Potterybarn Modal Minimize Button": (By.CLASS_NAME,"stickyOverlayMinimizeButton"),
    "Potterybarn Product Images": (By.CSS_SELECTOR,".shopgrid_image a"),
    "PB Continue Shopping Button": (By.XPATH,"//div[@id='btn-view-cart']/a[.='Continue Shopping']"),
    "PB Overlay Close Button": (By.ID,"overlayCloseButton"),
    "PB Checkout Button": (By.ID,"anchor-btn-checkout"),
    "PB Accept Terms Button": (By.XPATH,"//button[@class='btn btn-primary js-accept-shipping-button']"),
    "PB Product Add to Cart Button": (By.XPATH,"//button[.='Add to Cart']"),
    "PB Product Add to Cart Button2": (By.CSS_SELECTOR,"button[aria-label='Add to Cart'"),
    "PB Product Add to Cart Button from Text": (By.LINK_TEXT," Add to Cart "),
    "PB Select Color" : (By.CSS_SELECTOR,".pip-summary ul.visual-attributes li a"),
    "PB SELECT Swatch" : (By.CSS_SELECTOR,".swatch-group-container ul li"),
    "PB Product Subsets" : (By.CSS_SELECTOR,".product-subset dl dd"),
    "PB Product Subsets Link" : (By.CSS_SELECTOR,".product-subset dl dd a.attribute"),
    "PB Configurations Panel" : (By.CSS_SELECTOR,"[href='step0']"),
    "PB Configurations" : (By.CSS_SELECTOR,".attribute-selector.attributeValue a"),
    "PB Select Fabric and Color Panel": (By.CSS_SELECTOR,"[href='step1']"),
    "PB Select Fabric and Color":(By.CSS_SELECTOR,".thumb-swatches.thumbSwatches li"),
    "PB Select Subset SKU":(By.CSS_SELECTOR,".subset-attributes ul.visual-attributes li a"),
    "PB Input Quantity":(By.CSS_SELECTOR,"input.qty"),
    "PBCO CreditCard Button":(By.CSS_SELECTOR,".radio-button #creditCard"),
    "PBCO Checkout Button":(By.CSS_SELECTOR,"button[data-test-id='topCheckout'"),
    "PBCO Guest Checkout Button":(By.XPATH,"//button[contains(.,'Guest Checkout')]"),
    "PBCS Full Name field":(By.XPATH,"//address-form-feature[@id='shipping']//input[@id='fullName']"),
    "PBCS Address field":(By.XPATH,"//address-form-feature[@id='shipping']//address-suggestion-feature[1]//input[@class='DEFAULT']"),
    "PBCS Apt field":(By.XPATH,"//address-form-feature[@id='shipping']//checkout-text-ui[2]//input[@class='DEFAULT']"),
    "PBCS City field":(By.XPATH,"//address-form-feature[@id='shipping']//input[@id='city']"),
    "PBCS State field":(By.XPATH,"//address-form-feature[@id='shipping']//select[@name='stateProvince']"),
    "PBCS Zip field":(By.XPATH,"//address-form-feature[@id='shipping']//input[@id='postalCode']"),
    "PBCS Phone field":(By.XPATH,"//address-form-feature[@id='shipping']//input[@id='phone']"),
    "PBCS Continue Button":(By.CSS_SELECTOR,"button-ui[label='Continue']"),
    "PBCS Review Content Container":(By.CSS_SELECTOR,"review-content"),
    "PBCS shipping-fullName-error":(By.CSS_SELECTOR,"#shipping-fullName-error"),
    "PBCP Email Field":(By.CSS_SELECTOR,"input[name='email'"),
    "PBCP Credit Card Number Field":(By.CSS_SELECTOR,"#creditCardNumber"),
    "PBCP Invalid Email":(By.CSS_SELECTOR,".email-form-feature-wrapper checkout-text-ui[validation-state='INVALID']"),
    "PBCC Number":(By.ID,"creditCardNumber"),
    "PBCC Expiration":(By.ID,"expiration"),
    "PBCC CVN":(By.ID,"cvn"),
    "PBCC Invalid Credit Card":(By.CSS_SELECTOR,".credit-card-field-container checkout-text-ui[validation-state='INVALID']")


}

PLACE_ORDER_BUTTON_SHADOW = '[{"name":"css","value":"checkout-app"},{"name":"css","value":"payment-region"},{"name":"css","value":"place-order-view"},{"name":"css","value":"[name=\'placeOrder\']"},{"name":"css","value":".primary"}]'

def locator(thislocator):
    return LOCATORS[thislocator]

def page_url(page):
    return PAGE_URLS[page]

def file_init():
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, 'test.txt')

    print(filepath)

    a = "Hello"

    LOCATORS = {
        "I am feeling button": "css||div:nth-of-type(8)"
    }

    f = open("/Users/tonimaxx/careerist/automationgettop/features/steps/config.json")
    data = json.load(f)

# print(locator("Amazon Homepage"))
