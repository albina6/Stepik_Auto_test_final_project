import time
import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage


# link_list ='''\
# http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8
# # http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'''.split("\n")


class TestGuestAddToBasketFromProductPage():    
    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    # @pytest.mark.parametrize('link', link_list)
    @pytest.mark.xfail(reason="Red mark test")
    def test_guest_can_add_product_to_basket_with_promo_is_disappeared_success_message(self, browser):#, link):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_with_promo()
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
        page.should_is_disappeared_success_message()

    def test_guest_can_add_product_to_basket_with_promo(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_with_promo()
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
    

    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket_without_promo(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_simple() 
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()

    @pytest.mark.xfail(reason="Red mark test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_with_promo()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(page.browser, page.browser.current_url)
        login_page.should_be_login_page()    
    
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # empty cart
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_page()
        cart_page.should_be_empty_cart_summary()
    
    def test_guest_can_see_add_product_in_basket_opened_from_product_page(self, browser):
        ''' guesr can see product in basket. Without check
            name_product_in_cart == name_product_in_form_product'''
        
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_simple()
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
        page.go_to_cart_page()
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_page()
        cart_page.should_be_product_in_cart()
    
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
    
    @pytest.mark.xfail(reason="Red mark test")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_simple()
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
        page.should_is_disappeared_success_message()
    

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.com"
        password = "asdfqwe388"
        page.register_new_user(email, password)
        
    
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Red mark test, success message don't be disappeared")
    def test_user_can_add_product_to_basket_with_promo(self, browser):#, link):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.add_product_with_promo()
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
        page.should_is_disappeared_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket_without_promo(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        # with test succes message
        page.add_product_simple() 
        page.should_be_equal_name_in_cart_and_form()
        page.should_be_equal_prise_in_cart_and_form()
        
    
    
