from utils.steps import step
from .base_page import BasePage
from locators.admin_main_page_locators import AdminMainPageLocators as Locators


class AdminMainPage(BasePage):
    """
    methods for admin main page
    """

    @step('Проверить авторизацию пользователя: "{user_name}"')
    def should_be_login_user(self, user_name):
        strategy, locator = Locators.USER_ICON_BY_NAME
        assert self._is_element_present(strategy, locator.format(user_name)), f'User: "{user_name}" not login'

    @step('Кликнуть по кнопке "Catalog" в меню админ-панели')
    def click_catalog_menu(self):
        catalog_menu_button = self._find_element_clickable(*Locators.MAIN_MENU_CATALOG)
        catalog_menu_button.click()

    @step('Кликнуть по кнопке: "{item_name}" в меню "Catalog"')
    def click_catalog_submenu(self, item_name):
        strategy, locator = Locators.MAIN_SUBMENU_CATALOG_BY_NAME
        catalog_submenu_button = self._find_element_clickable(strategy, locator.format(item_name))
        catalog_submenu_button.click()
