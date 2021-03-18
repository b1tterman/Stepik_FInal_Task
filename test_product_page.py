import pytest
import time
from .pages.product_page import PageProduct
from .pages.base_page import BasePage
from .pages.locators import BasketPageLocators
from .pages.locators import ProductPageLocators
from .pages.basket_page import BasketPage



# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# 								  ])
#
# def test_guest_can_add_product_to_basket(browser, link):
# # def test_guest_can_add_product_to_basket(browser):
# # 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# 	page = PageProduct(browser, link)
# 	page.open()
# 	page.add_goods_to_basket()
# 	page.solve_quiz_and_get_code()
# 	# time.sleep(1000)
# 	page.check_all_things_here()

# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# 	page = PageProduct(browser, link)
# 	page.open()
# 	page.add_goods_to_basket()
# 	page.solve_quiz_and_get_code()
# 	page.should_not_be_success_message()
#
# def test_guest_cant_see_success_message(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# 	page = PageProduct(browser, link)
# 	page.open()
# 	page.should_not_be_success_message()
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
# 	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
# 	page = PageProduct(browser, link)
# 	page.open()
# 	page.add_goods_to_basket()
# 	page.solve_quiz_and_get_code()
# 	page.is_disappeared(*ProductPageLocators.ITEM_ADDED)

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = PageProduct(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = PageProduct(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.some_basket_checks()
