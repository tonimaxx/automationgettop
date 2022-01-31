from threading import Thread
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.application import Application
chrome_options = webdriver.ChromeOptions()
from selenium.webdriver.firefox.options import Options as FirefoxOptions


# Begin Test Configuration

# BrowserStack Configuration
caps=[{
      'os_version': '11',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '96.0',
      'name': 'Parallel Test1',
      'build': 'browserstack-build-1'
      }
]

mobile_emulation = {
   "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
   "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19" }

# Note : browser now support "chrome", "firefox"
TEST_ENVIRONMENT = {
    "browser": "chrome",
    "headless": False,
    "mobile": False
}

print(f"{'Headless' if TEST_ENVIRONMENT['headless'] else 'Normal'} {TEST_ENVIRONMENT['browser']} initialization")

disable_images = False
disable_javascript = False
test_resolution = "FHD"

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

# End Initialization

def browser_init(context):
    """
    :param context: Behave context
    """

    if TEST_ENVIRONMENT["browser"] == 'safari':
        pass
    elif TEST_ENVIRONMENT["browser"] == 'edge':
        pass
    elif TEST_ENVIRONMENT["browser"] == 'firefox':
        firefox_options = FirefoxOptions()
        if TEST_ENVIRONMENT["headless"]:
            firefox_options.add_argument("--headless")
        context.driver = webdriver.Firefox(
            executable_path='geckodriver',
            options=firefox_options
        )
    else:
        # Chrome (Default)
        chrome_prefs = {
            "profile.default_content_setting_values": {
                "images": 2 if disable_images else 0,
                "javascript": 2 if disable_javascript else 0
            }
        }
        chrome_options.experimental_options["prefs"] = chrome_prefs

        # chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--kiosk")

        if TEST_ENVIRONMENT["headless"]:
            chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
            chrome_options.add_argument('headless')
            chrome_options.add_argument('window-size=0x0')

        if TEST_ENVIRONMENT["mobile"]:
            chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        context.driver = webdriver.Chrome(
            executable_path='./chromedriver',
            chrome_options=chrome_options,
        )

    # context.browser = webdriver.Safari()

    context.driver.set_window_size(browser_width, browser_height)
    context.driver.implicitly_wait(1)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    if "Verify Selecting Products to Cart" not in scenario.name:
        # print("YEHHHHHH")
        pass
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, scenario):
    print(f"scenario : {scenario}")
    # if "Verify Selecting Products to Cart" not in scenario.name:
    #
    #     pass
    # context.driver.delete_all_cookies()
    # context.driver.quit()

def after_feature(context, feature):
    print(f"feature : {feature}")