from .base_page import BasePage
from locators.catalog_page_locators import CatalogPageLocators as Locators


class CatalogPage(BasePage):
    """
    methods from catalog page
    """

    def open(self, path):
        self._open_page(path)

    def should_be_product_card(self):
        assert self._is_element_present(*Locators.PRODUCT_CARD), 'element "Product Card" is not present'

    def should_be_catalog_menu(self):
        assert self._is_element_present(*Locators.CATALOG_MENU), 'element "Catalog Menu" is not present'

    def should_be_description_page(self):
        assert self._is_element_present(*Locators.DESCRIPTION), 'element "Description Page" is not present'

    def should_be_quantity_filter(self):
        assert self._is_element_present(*Locators.QUANTITY_FILTER), 'element "Quantity filter" is not present'

    def should_be_sort_input(self):
        assert self._is_element_present(*Locators.SORT_INPUT), 'element "Sort Input" is not present'
