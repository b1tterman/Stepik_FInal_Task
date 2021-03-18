from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def some_basket_checks(self):
		self.should_be_in_basket()
		self.should_be_empty_basket_message()
		self.should_be_empty_basket()


	def should_be_in_basket(self):
		assert 'basket' in self.browser.current_url, "basket is absent in current url"

	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL), "Basket has some products"


	def should_be_empty_basket_message(self):
		assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text, "Basket not empty"

