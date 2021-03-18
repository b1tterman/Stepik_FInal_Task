import time

import pytest

from .pages.basket_page import BasketPage
from .pages.locators import ProductPageLocators
from .pages.login_page import LoginPage
from .pages.product_page import PageProduct


@pytest.mark.register_new_user
class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
		self.page = LoginPage(browser, link)
		self.page.open()
		# self.page.go_to_login_page()
		email_ = str(time.time()) + "@fakemail.org"
		password_ = str(time.time()) + "passW0rd"
		self.page.register_new_user(email_, password_)
		self.page.should_be_authorized_user()

	def test_user_cant_see_success_message(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
		page = PageProduct(browser, link)
		page.open()
		page.should_not_be_success_message()

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
		page = PageProduct(browser, link)
		page.open()
		page.add_goods_to_basket()
		page.check_all_things_here()


def test_user_cant_see_success_message(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageProduct(browser, link)
	page.open()
	page.should_not_be_success_message()


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
	page = PageProduct(browser, link)
	page.open()
	page.add_goods_to_basket()
	page.solve_quiz_and_get_code()
	page.check_all_things_here()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
	page = PageProduct(browser, link)
	page.open()
	page.add_goods_to_basket()
	page.solve_quiz_and_get_code()
	page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
	page = PageProduct(browser, link)
	page.open()
	page.add_goods_to_basket()
	# page.solve_quiz_and_get_code()
	page.is_disappeared(*ProductPageLocators.ITEM_ADDED)


def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
	page = PageProduct(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
	page = PageProduct(browser, link)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-big-u_93/"
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket_page()
	page.some_basket_checks()
