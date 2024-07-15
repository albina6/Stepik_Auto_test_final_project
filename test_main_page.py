# test_items.py

import time
import selenium
from selenium.webdriver.common.by import By


class TestProduct():
    
    # def test_button_submit(self, browser):
    #     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    #     browser.get(link)
    #     time.sleep(5)
    #     # time.sleep(30)
    #     # submit = browser.find_element(By.CSS_SELECTOR, ".product_page button[type='submit']")
    #     try:
    #         browser.find_element(By.CSS_SELECTOR, ".product_page button[type='submit']")
    #     except selenium.common.exceptions.NoSuchElementException:
    #         raise AssertionError('Button not found')

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        browser.get(link)
        login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
        time.sleep(5)