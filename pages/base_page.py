from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import logging


class BasePage:
    _timeout = 10

    def __init__(self, ui):
        self.test_name = ui.test_name
        self.log_level = ui.log_level
        self.driver = ui.driver
        self.base_url = ui.base_url
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.handlers.clear()
        self.logger.addHandler(logging.FileHandler(f"logs/{self.test_name}.log"))
        self.logger.setLevel(level=self.log_level)

    def _open_page(self, path=''):
        self.logger.info("Opening url: {}".format(self.base_url + f'{path}'))
        self.driver.get(self.base_url + f'/{path}')

    def _is_element_present(self, strategy, locator, timeout=_timeout):
        self.logger.info("Check if element {} is present".format(locator))
        try:
            WebDriverWait(self.driver, timeout).until(
                expected_conditions.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def _is_not_element_present(self, strategy, locator, timeout=_timeout):
        self.logger.info("Check if element {} is not present".format(locator))
        try:
            WebDriverWait(self.driver, timeout).until_not(
                expected_conditions.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True

    def _find_element_clickable(self, strategy, locator, timeout=_timeout):
        self.logger.info("Find element clickable with locator: {}".format(locator))
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable((strategy, locator)),
            message=f"Element with locator: {(strategy, locator)} not available for more than {timeout} seconds")

    def _find_element(self, strategy, locator, timeout=_timeout):
        self.logger.info("Find element with locator: {}".format(locator))
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_element_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")

    def _find_elements(self, strategy, locator, timeout=_timeout):
        self.logger.info("Find elements with locator: {}".format(locator))
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.presence_of_all_elements_located((strategy, locator)),
            message=f"Не найден элемент с локатором: {(strategy, locator)}")

    def get_current_url(self):
        self.logger.info("Get current URL")
        return self.driver.current_url

    def _alert_accept(self):
        self.logger.info("Switch alert")
        alert = self.driver.switch_to.alert
        self.logger.info("Accept alert")
        alert.accept()
