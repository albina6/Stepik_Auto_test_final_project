import time
import pytest
from .pages.product_page import ProductPage

link_list ='''\
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8
http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'''.split("\n")


@pytest.mark.parametrize('link', link_list)
@pytest.mark.xfail(reason="Don't need to fix this")
def test_add_product_from_product_page(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_product()
    # time.sleep(3)