from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ABOUT_MENU = (By.XPATH,"//ul[@class='navigation menu']//a[@href='/about/']")
ABOUT_HEADER = (By.XPATH,"//h1[@class='call-to-action']")
SEARCH_BAR = (By.XPATH,"//input[@id='id-search-field']")
MAIN_TOP_MENUS = (By.XPATH,"//nav[@id='mainnav']//ul[@class='navigation menu']//li[contains(@class,'tier-1')]")

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.python.org")
print(driver.title)

e = driver.find_elements(*ABOUT_MENU)[0]
e.click()
element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(ABOUT_HEADER),
        message=f"Expected class home but not found"
    )
print(element.text)

# e = driver.find_element_by_link_text("Downloads")
e = driver.find_element(By.LINK_TEXT, 'Downloads')
e.click()


e = driver.find_element(*SEARCH_BAR)
e.clear()
e.send_keys("download python mac")
e.send_keys(Keys.ENTER)

sleep(5)

actions = ActionChains(driver)
e = driver.find_elements(*MAIN_TOP_MENUS)
for i in e:
    actions.move_to_element(i)
    sleep(2)
    actions.perform()






# actions.click(hidden_submenu)


driver.close()

# // Action Chain



# //nav[@id='mainnav']//ul[@class='navigation menu']//li[contains(@class,'tier-1')]
# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)
# driver.maximize_window()
# driver.get('https://www.google.com')

# ser = Service("chromedriver'")
# op = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=ser, options=op)
# driver.get("https://www.python.org")
# print(driver.title)

