from utils.steps import step
from .base_page import BasePage
from locators.admin_product_list_page_locators import AdminProductListPageLocators as Locators


class AdminProductListPage(BasePage):
    """
    methods from admin product list page
    """

    @step('Проверить открытие страницы со списком товаров')
    def should_be_open(self):
        assert 'catalog/product' in self.get_current_url(), 'Page not open'

    @step('Кликнуть по кнопке добавления нового товара')
    def click_add_product_button(self):
        button = self._find_element_clickable(*Locators.ADD_PRODUCT_BUTTON)
        button.click()

    @step('Проверить наличия в списке товара с именем: {product_name}')
    def should_be_product_name(self, product_name):
        strategy, locator = Locators.ITEM_BY_NAME
        assert self._is_element_present(strategy, locator.format(product_name)), f'Element "{product_name}" not found'

    @step('Проверить отсутствие в списке товара с именем: {product_name}')
    def should_not_be_product_name(self, product_name):
        strategy, locator = Locators.ITEM_BY_NAME
        assert self._is_not_element_present(strategy, locator.format(product_name)), f'Element "{product_name}" found'

    def get_product_name_list(self):
        products = self._find_elements(*Locators.ITEM_NAME)
        return [x.text for x in products]

    @step('Выбрать товар с именем: {product_name}')
    def select_product(self, product_name):
        strategy, locator = Locators.CHECKBOX_PRODUCT_BY_NAME
        checkbox = self._find_element(strategy, locator.format(product_name))
        checkbox.click()

    @step('Кликнуть по кнопке удаления')
    def click_delete_button(self):
        button = self._find_element_clickable(*Locators.DELETE_BUTTON)
        button.click()
        self._alert_accept()
