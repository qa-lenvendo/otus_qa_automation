from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    _timeout = 10

    def __init__(self, ui):
        self.driver = ui.driver
        self.base_url = ui.base_url

    def _open_page(self, path=''):
        self.driver.get(self.base_url + f'/{path}')

    def _is_element_present(self, strategy, locator, timeout=_timeout):
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def _find_element_clickable(self, strategy, locator, timeout=_timeout):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((strategy, locator)),
            message=f"Element with locator: {(strategy, locator)} not available for more than {timeout} seconds")

    def _find_element(self, strategy, locator, timeout=_timeout):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")

    def _find_elements(self, strategy, locator, timeout=_timeout):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")
