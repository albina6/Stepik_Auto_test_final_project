from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        email_input.send_keys(email)
        
        password1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD1_INPUT)
        password1.send_keys(password)
        
        password2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD2_INPUT)
        password2.send_keys(password)

        self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT).click()
        # check for success register
        self.is_element_present(*LoginPageLocators.CORRECT_REGISTER)
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'Login' is not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_LINK), \
                    "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_LINK), \
                    "Login form is not presented"