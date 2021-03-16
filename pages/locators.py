from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_PRICE = (By.XPATH, '// *[ @ id = "content_inner"] / article / div[1] / div[2] / p[1]')
    BASKET_SUM = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/text()')
    ITEM_ADDED = (By.XPATH, '//*[@id="messages"]/div[1]/div/text()')
    ITEM_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')