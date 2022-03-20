from .base_page import BasePage
from locators.product_page_locators import ProductPageLocators as Locators


class ProductPage(BasePage):
    """
    methods from product page
    """

    def open(self, path):
        self._open_page(path)

    def should_be_add_cart_button(self):
        assert self._is_element_present(*Locators.ADD_CART_BUTTON), 'element "Cart Button" is not present'

    def should_be_product_price(self):
        assert self._is_element_present(*Locators.PRODUCT_PRICE), 'element "Product Price" is not present'

    def should_be_quantity_input(self):
        assert self._is_element_present(*Locators.QUANTITY_INPUT), 'element "Quantity Input" is not present'

    def should_be_product_name(self):
        assert self._is_element_present(*Locators.PRODUCT_NAME), 'element "Product Name" is not present'

    def should_be_description_tab(self):
        assert self._is_element_present(*Locators.DESCRIPTION_TAB), 'element "Description Tab" is not present'
