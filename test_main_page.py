import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.locators import LoginPageLocators
import time

@pytest.mark.login_guest
class TestLoginFromMainPage():

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

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        # page.open()
        # page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        # page.open()
        page.should_be_login_link()



def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.some_basket_checks()

