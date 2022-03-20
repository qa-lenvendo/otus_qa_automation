from allure import step
from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):
    """
    methods from main page
    """

    @step('Открыть главную страницу')
    def open(self):
        self._open_page()

    @step('Проверить наличие поля ввода поискового запроса')
    def should_be_search_input(self):
        assert self._is_element_present(*Locators.SEARCH_INPUT), 'element "Search Input" is not present'

    @step('Проверить наличие баннера')
    def should_be_banner_section(self):
        assert self._is_element_present(*Locators.BANNER_SECTION), 'element "Banner Section" is not present'

    @step('Проверить наличие главного меню')
    def should_be_main_menu(self):
        assert self._is_element_present(*Locators.MAIN_MENU),  'element "Main Menu" is not present'

    @step('Проверить наличие малой корзины')
    def should_be_small_basket(self):
        assert self._is_element_present(*Locators.SMALL_BASKET), 'element "Small Basket" is not present'

    @step('Проверить наличия логотипа')
    def should_be_logo(self):
        assert self._is_element_present(*Locators.LOGO), 'element "Logo" is not present'
