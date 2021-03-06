from utils.steps import step
from .base_page import BasePage
from locators.admin_product_page_locators import AdminProductPageLocators as Locators


class AdminProductPage(BasePage):
    """
    methods from admin product page
    """

    @step('Проверить открытие страницы добавления нового товара')
    def should_be_open(self):
        assert 'catalog/product/add' in self.get_current_url(), 'Page not open'

    @step('В поле ввода наименования ввести значение: "{value}"')
    def enter_value_in_product_name_field(self, value):
        field = self._find_element(*Locators.INPUT_PRODUCT_NAME)
        field.send_keys(value)

    @step('В поле ввода "Meta Tag Title" ввести значение: "{value}"')
    def enter_value_in_meta_tag_field(self, value):
        field = self._find_element(*Locators.INPUT_META_TAG_TITLE)
        field.send_keys(value)

    @step('Кликнуть по вкладке "Data"')
    def click_data_tab(self):
        tab = self._find_element_clickable(*Locators.TAB_DATA)
        tab.click()

    @step('В поле "Model" ввести значение: "{value}"')
    def enter_value_in_model_field(self, value):
        field = self._find_element(*Locators.INPUT_MODEL)
        field.send_keys(value)

    @step('Кликнуть по кнопке "Сохранить"')
    def click_save_button(self):
        button = self._find_element_clickable(*Locators.BUTTON_SAVE)
        button.click()
