from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application
chrome_options = webdriver.ChromeOptions()

# Begin Test Configuration
disable_images = True
disable_javascript = False
test_resolution = "QHD"
# End Configuration
# Do not change below this line

#Initialization ----------------

screen_resolution = {
    "SD": "640x480",
    "HD": "1280x720",
    "FHD": "1920x1080",
    "QHD": "2560x1440",
    "UHD": "3840x2160",
    "4K": "4096x2160",
    "iphone13": "390x844",
    "iphone13mini": "375x812",
    "iphone13promax": "428x926"
}

browser_resolution = screen_resolution[test_resolution]
browser_width = browser_resolution.split("x")[0]
browser_height = browser_resolution.split("x")[1]

chrome_prefs = {
    "profile.default_content_setting_values": {
        "images": 2 if disable_images else 0,
        "javascript": 2 if disable_javascript else 0
    }
}
chrome_options.experimental_options["prefs"] = chrome_prefs

# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--kiosk")

# End Initialization

def browser_init(context):
    """
    :param context: Behave context
    """
    context.driver = webdriver.Chrome(
        executable_path='./chromedriver',
        chrome_options=chrome_options,
    )

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.set_window_size(browser_width, browser_height)
    context.driver.implicitly_wait(4)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()