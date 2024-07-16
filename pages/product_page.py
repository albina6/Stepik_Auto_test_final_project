import math
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    @staticmethod
    def calc_func(x):
        return math.log(abs(12*math.sin(x)))
    
    def add_product(self):
        submit = self.browser.find_element(*ProductPageLocators.SUBMIT_LINK)
        submit.click()
        alert = self.browser.switch_to.alert
        x = alert.text.split()[2]
        answer = self.calc_func(int(x))
        alert.send_keys(str(answer))
        alert.accept()
        # print(f"{int(x)} = {answer}")
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")