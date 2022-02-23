from .base_page import BasePage
from locators.admin_login_page_locators import AdminLoginPageLocators as Locators


class AdminLoginPage(BasePage):
    """
    methods from admin login page
    """
    _path = '/admin'

    def open(self):
        self.open_page(self._path)

    def should_be_logo(self):
        assert self._is_element_present(*Locators.HEADER_LOGO), 'element "Logo" is not present'

    def should_be_user_name_input(self):
        assert self._is_element_present(*Locators.USER_NAME_INPUT), 'element "User Name Input" is not present'

    def should_be_password_input(self):
        assert self._is_element_present(*Locators.PASSWORD_INPUT), 'element "Password Input" is not present'

    def should_be_login_button(self):
        assert self._is_element_present(*Locators.LOGIN_BUTTON), 'element "Login Button" is not present'

    def should_be_footer(self):
        assert self._is_element_present(*Locators.FOOTER), 'element "Footer" is not present'
