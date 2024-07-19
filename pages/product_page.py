import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    @staticmethod
    def calc_func(x):
        return math.log(abs(12*math.sin(x)))

    def add_product_simple(self):
        submit = self.browser.find_element(*ProductPageLocators.SUBMIT_LINK)
        submit.click()
    
    def add_product_with_promo(self):
        submit = self.browser.find_element(*ProductPageLocators.SUBMIT_LINK)
        submit.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = self.calc_func(int(x))
        alert.send_keys(str(answer))
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    
    def should_be_equal_name_in_cart_and_form(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART_LINK).text == \
                    self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_FORM_LINK).text, \
                    "Name product in card not equal name in main form product"

    def should_be_equal_prise_in_cart_and_form(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE_IN_CART_LINK).text == \
                    self.browser.find_element(*ProductPageLocators.PRODUCT_PRISE_IN_FORM_LINK).text, \
                    "Name product in card not equal name in main form product"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_LINK), \
           "Success message is presented, but should not be"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_LINK), \
           "Success message is presented, but should is disappeared"
    
        