from .base_page import BasePage
from locators.registration_page_locators import RegistrationPageLocators as Locators


class RegistrationPage(BasePage):
    """
    methods from registration page
    """
    _path = '/index.php?route=account/register'

    def open(self):
        self._open_page(self._path)

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

    def enter_value_in_first_name_field(self, value):
        field = self._find_element(*Locators.FIRSTNAME_INPUT)
        field.send_keys(value)

    def enter_value_in_lastname_field(self, value):
        field = self._find_element(*Locators.LASTNAME_INPUT)
        field.send_keys(value)

    def enter_value_in_email_field(self, value):
        field = self._find_element(*Locators.EMAIL_INPUT)
        field.send_keys(value)

    def enter_value_in_telephone_field(self, value):
        field = self._find_element(*Locators.TELEPHONE_INPUT)
        field.send_keys(value)

    def enter_value_in_password_field(self, value):
        field = self._find_element(*Locators.PASSWORD_INPUT)
        field.send_keys(value)

    def enter_value_in_confirm_password_field(self, value):
        field = self._find_element(*Locators.CONFIRM_PASSWORD_INPUT)
        field.send_keys(value)

    def click_privacy_policy_checkbox(self):
        checkbox = self._find_element(*Locators.CHECKBOX_PRIVACY_POLICY)
        checkbox.click()

    def click_continue_button(self):
        button = self._find_element_clickable(*Locators.CONTINUE_BUTTON)
        button.click()

    def should_be_open_account_success(self):
        assert self._is_element_present(*Locators.SUCCESS_TITLE), 'User not registration'
