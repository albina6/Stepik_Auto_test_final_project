# test_items.py

import time
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage

from .pages.locators import MainPageLocators


@pytest.mark.login_guest
class TestLoginFormMainPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()    

    def test_guest_can_go_to_login_page(self, browser):
        self.page.should_be_login_link()
        self.page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        time.sleep(3)
    
    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        self.page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_empty_cart_summary()

    
