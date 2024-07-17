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


# @pytest.mark.parametrize('link', link_list)
@pytest.mark.xfail(reason="Red mark test")
def test_add_product_from_product_page_with_promo(browser):#, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_with_promo()
    page.shold_is_disappeared_success_message()


def test_add_product_from_product_page_without_promo(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product_simple()    


@pytest.mark.xfail(reason="Red mark test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_with_promo()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Show success message after adding product"

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(page.browser, page.browser.current_url)
    login_page.should_be_login_page()
    # time.sleep(3)

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Show success message before adding product"

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    # empty cart
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_empty_cart_summary()

def test_guest_can_see_add_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_simple()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_product_in_cart()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.xfail(reason="Red mark test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_simple()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Success message is not disappeared after adding product"



