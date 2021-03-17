from .base_page import BasePage
import time
from selenium.webdriver.common.by import By

from .locators import ProductPageLocators

class PageProduct(BasePage):

	def check_all_things_here(self):
		self.check_item_price_in_basket()
		self.check_item_name_in_basket()

	def add_goods_to_basket(self):
		button = self.browser.find_element(*ProductPageLocators.ADD_CART_BUTTON)
		button.click()


	def check_item_name_in_basket(self):
		time.sleep(1)
		name_in_basket = self.browser.find_element(*ProductPageLocators.ITEM_ADDED).text
		item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
		assert name_in_basket == item_name, f"{item_name} is not {name_in_basket}"

	def check_item_price_in_basket(self):
		basket_price = self.browser.find_element(*ProductPageLocators.MESSAGE_SUM).text
		product_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
		assert product_price == basket_price, f"{product_price} not equal {basket_price}"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.ITEM_ADDED), \
			"Success message is presented, but should not be"

