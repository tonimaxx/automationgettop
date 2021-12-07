from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_KEYWORD = "Macbook"
TARGET_URL = "https://gettop.us"

caps=[{
      'os_version': '11',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '96.0',
      'name': 'Parallel Test1',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': '11',
      'os': 'Windows',
      'browser': 'firefox',
      'browser_version': '94.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': '11',
      'os': 'Windows',
      'browser': 'edge',
      'browser_version': '96.0',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'chrome',
      'browser_version': '96.0',
      'name': 'Parallel Test1',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'edge',
      'browser_version': '96.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': '15.0',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Monterey',
      'os': 'OS X',
      'browser': 'firefox',
      'browser_version': '94.0',
      'name': 'Parallel Test1',
      'build': 'browserstack-build-1'
      }
]
#run_session on Gettop.us
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://printaninnattaka_NQLKzv:pAMz6MjxF5oe32suyU5s@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
  driver.get(TARGET_URL)
  if not "gettop.us" in driver.title:
      raise Exception("Unable to load Gettop.us page!")
  print(driver.title)
  driver.quit()

#The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session parallelly
for cap in caps:
  Thread(target=run_session, args=(cap,)).start()