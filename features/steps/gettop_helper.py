from selenium.webdriver.common.by import By

class locatorClass:
	def __init__(self):
		self.val = 1
		# BROWSE_self.ACCESSORIES_ARROW = (By.XPATH, "//li[@class='cat-item cat-item-74 cat-parent has-child active']//i[@class='icon-angle-down']")

	def getVal(self,thislocator):
		if thislocator == "TOP_MENU_LINKS":
			to_return = (By.CSS_SELECTOR, ".header-nav a")
		elif thislocator == "BROWSE_ACCESSORIES_ARROW":
			to_return = (By.CSS_SELECTOR, ".cat-item-74 .icon-angle-down")
		elif thislocator == "PRODUCT_CATEGORY_BROWSE":
			to_return =  (By.CSS_SELECTOR, ".product-categories a")
		return to_return