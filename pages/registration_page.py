from .base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators as Locators


class RegistrationPage(BasePage):
    """
    methods from registration page
    """
    _path = '/index.php?route=account/register'

    def open(self):
        self.open_page(self._path)

    def should_be_firstname_input(self):
        assert self._is_element_present(*Locators.FIRSTNAME_INPUT), 'element "Firstname Input" is not present'

    def should_be_lastname_input(self):
        assert self._is_element_present(*Locators.LASTNAME_INPUT), 'element "Lastname Input" is not present'

    def should_be_email_input(self):
        assert self._is_element_present(*Locators.EMAIL_INPUT), 'element "Email Input" is not present'

    def should_be_telephone_input(self):
        assert self._is_element_present(*Locators.TELEPHONE_INPUT), 'element "Telephone Input" is not present'

    def should_be_continue_button(self):
        assert self._is_element_present(*Locators.CONTINUE_BUTTON), 'element "Continue Button" is not present'
