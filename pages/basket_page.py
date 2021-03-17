from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	
	# Создайте файл basket_page.py и в нем класс BasketPage.
    # Реализуйте там необходимые проверки, в том числе отрицательную, которую мы обсуждали в предыдущих шагах.

	def some_basket_checks(self):
		self.should_be_in_basket()
		

	def should_be_in_basket(self):
		assert 'basket' in self.browser.current_url, "basket is absent in current url"

# Переходит в корзину по кнопке в шапке сайта
# Ожидаем, что в корзине нет товаров
# Ожидаем, что есть текст о том что корзина пуста
