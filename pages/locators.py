from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    ITEM_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    MESSAGE_SUM = (By.CSS_SELECTOR, "div.alert div p strong")
    ITEM_ADDED = (By.CSS_SELECTOR, "div.alertinner > strong")
    ITEM_NAME = (By.CSS_SELECTOR, "div h1")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')