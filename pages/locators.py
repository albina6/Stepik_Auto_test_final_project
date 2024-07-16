from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    SUBMIT_LINK = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    
    PRODUCT_NAME_IN_CART_LINK = (By.CSS_SELECTOR, ".alert-success .alertinner > strong")
    PRODUCT_PRISE_IN_CART_LINK = (By.CSS_SELECTOR, ".alert-info strong")
    
    PRODUCT_NAME_IN_FORM_LINK = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRISE_IN_FORM_LINK = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")