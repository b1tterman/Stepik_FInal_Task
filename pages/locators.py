from selenium.webdriver.common.by import By
import time


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_REGISTER_MAIL = (By.CSS_SELECTOR, "#id_registration-email")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    INPUT_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    MESSAGE_SUM = (By.CSS_SELECTOR, "div.alert div p strong")
    ITEM_ADDED = (By.CSS_SELECTOR, "div.alertinner > strong")
    ITEM_NAME = (By.CSS_SELECTOR, "div h1")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (
    By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_TOTAL = (By.CSS_SELECTOR, "table.table > th.total")