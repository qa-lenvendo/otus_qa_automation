from utils.steps import step
from .base_page import BasePage
from locators.admin_login_page_locators import AdminLoginPageLocators as Locators


class AdminLoginPage(BasePage):
    """
    methods from admin login page
    """
    _path = '/admin'

    @step('Открыть страницу авторизации в админ-панели')
    def open(self):
        self._open_page(self._path)

    @step('Проверить наличие логотипа')
    def should_be_logo(self):
        assert self._is_element_present(*Locators.HEADER_LOGO), 'element "Logo" is not present'

    @step('Проверить наличие поля ввода: "Username"')
    def should_be_user_name_input(self):
        assert self._is_element_present(*Locators.USER_NAME_INPUT), 'element "User Name Input" is not present'

    @step('Проверить наличие поля ввода: "Password"')
    def should_be_password_input(self):
        assert self._is_element_present(*Locators.PASSWORD_INPUT), 'element "Password Input" is not present'

    @step('Проверить наличие кнопки входа')
    def should_be_login_button(self):
        assert self._is_element_present(*Locators.LOGIN_BUTTON), 'element "Login Button" is not present'

    @step('Проверить наличие футера')
    def should_be_footer(self):
        assert self._is_element_present(*Locators.FOOTER), 'element "Footer" is not present'

    @step('Авторизоваться в админ панели')
    def login_user(self, user_name, user_password):
        with step(f'В поле ввода "Username" ввести значение: {user_name}'):
            login_input = self._find_element(*Locators.USER_NAME_INPUT)
            login_input.send_keys(user_name)
        with step(f'В поле ввода "Password" ввести значение: {user_password}'):
            password_input = self._find_element(*Locators.PASSWORD_INPUT)
            password_input.send_keys(user_password)
        with step('Нажать на кнопку: "Login"'):
            login_button = self._find_element_clickable(*Locators.LOGIN_BUTTON)
            login_button.click()
