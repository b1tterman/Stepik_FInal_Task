import pytest
import time
from .pages.product_page import PageProduct


def test_guest_can_add_product_to_basket(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	page = PageProduct(browser, link)
	page.open()
	page.add_goods_to_basket()
	page.solve_quiz_and_get_code()
	page.check_all_things_here()
