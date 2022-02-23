from .base_page import BasePage
from locators.main_page_locators import MainPageLocators as Locators


class MainPage(BasePage):
    """
    methods from main page
    """

    def open(self):
        self.open_page()

    def should_be_search_input(self):
        assert self._is_element_present(*Locators.SEARCH_INPUT), 'element "Search Input" is not present'

    def should_be_banner_section(self):
        assert self._is_element_present(*Locators.BANNER_SECTION), 'element "Banner Section" is not present'

    def should_be_main_menu(self):
        assert self._is_element_present(*Locators.MAIN_MENU),  'element "Main Menu" is not present'

    def should_be_small_basket(self):
        assert self._is_element_present(*Locators.SMALL_BASKET), 'element "Small Basket" is not present'

    def should_be_logo(self):
        assert self._is_element_present(*Locators.LOGO), 'element "Logo" is not present'
