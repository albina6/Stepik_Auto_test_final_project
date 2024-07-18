from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CARET_LINK = (By.CSS_SELECTOR, ".btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class CartPageLocators():
    # CART_SUMMARY_LINK = (By.CSS_SELECTOR,".basket_summary")
    PRODUCT_IN_CART_LINK = (By.CSS_SELECTOR,".basket-items > .row")
    TEXT_ABOUT_EMPTY_CART_LINK = (By.CSS_SELECTOR, "#content_inner > p")

class MainPageLocators():
    pass
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_LINK = (By.CSS_SELECTOR, "#register_form")
    
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTER_PASSWORD1_INPUT = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REGISTER_PASSWORD2_INPUT = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")

    CORRECT_REGISTER = (By.CSS_SELECTOR, ".icon-ok-sign")

class ProductPageLocators():
    SUBMIT_LINK = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    
    PRODUCT_NAME_IN_CART_LINK = (By.CSS_SELECTOR, ".alert-success .alertinner > strong")
    PRODUCT_PRISE_IN_CART_LINK = (By.CSS_SELECTOR, ".alert-info strong")
    
    PRODUCT_NAME_IN_FORM_LINK = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRISE_IN_FORM_LINK = (By.CSS_SELECTOR, ".product_main .price_color")

    SUCCESS_MESSAGE_LINK = (By.CSS_SELECTOR, ".alert-success")