from .base_page import BasePage
import time
from selenium.webdriver.common.by import By

from .locators import ProductPageLocators

class PageProduct(BasePage):

	def check_all_things_here(self):
		self.check_item_added_to_basket()
		self.check_item_price_in_basket()
		self.check_item_name_in_basket()

	def add_goods_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
		button.click()

	def check_item_added_to_basket(self):
		time.sleep(3)
		added = self.browser.find_element(*ProductPageLocators.ITEM_ADDED).text
		assert 'has been added to your basket' in added, "Item doesnt added to cart"

	def check_item_name_in_basket(self):
		time.sleep(3)
		name_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_ADDED).text
		item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
		assert item_name in name_in_basket, 'Item name doesnt added to cart'

	def check_item_price_in_basket(self):
		summ = self.browser.find_element(*ProductPageLocators.MESSAGE_SUM).text.split(" ")[0]
		# summ1 = self.browser.find_element(*ProductPageLocators.BASKET_SUM)
		# print(summ1)
		price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text.split(" ")[0]
		assert summ == price, "Summary doesnt match"