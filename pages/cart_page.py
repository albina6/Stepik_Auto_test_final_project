from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):  
    def should_be_empty_cart_summary(self):
        assert self.is_not_element_present(*CartPageLocators.PRODUCT_IN_CART_LINK), "Cart is not Empty"

    def should_be_text_about_empty_cart(self):
        assert self.is_element_present(*CartPageLocators.TEXT_ABOUT_EMPTY_CART_LINK), "Cart have not text about empty cart"

    def shold_be_empty_cart(self):
        self.should_be_empty_cart_summary()
        self.should_be_text_about_empty_cart()

    def should_be_product_in_cart(self):
        assert self.is_element_present(*CartPageLocators.PRODUCT_IN_CART_LINK), "Add product but cart is empty"
        
    
