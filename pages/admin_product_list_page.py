from .base_page import BasePage
from locators.admin_product_list_page_locators import AdminProductListPageLocators as Locators


class AdminProductListPage(BasePage):
    """
    methods from admin product list page
    """

    def should_be_open(self):
        assert 'catalog/product' in self.get_current_url(), 'Page not open'

    def click_add_product_button(self):
        button = self._find_element_clickable(*Locators.ADD_PRODUCT_BUTTON)
        button.click()

    def should_be_product_name(self, product_name):
        strategy, locator = Locators.ITEM_BY_NAME
        assert self._is_element_present(strategy, locator.format(product_name)), f'Element "{product_name}" not found'
