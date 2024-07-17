import time
import pytest
from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage


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
def test_add_product_from_product_page(browser):#, link):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.add_product()
    page.shold_is_disappeared_success_message()
    # time.sleep(3)

@pytest.mark.xfail(reason="Red mark test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Show success message after adding product"
    
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Show success message before adding product"

@pytest.mark.xfail(reason="Red mark test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_LINK), "Success message is not disappeared after adding product"



