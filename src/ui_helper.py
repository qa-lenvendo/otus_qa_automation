from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class UiHelper:
    _base_timeout = 10

    @staticmethod
    def is_element_present(driver, strategy, locator, timeout=_base_timeout):
        try:
            WebDriverWait(driver, timeout).until(
                expected_conditions.presence_of_element_located((strategy, locator)))
        except TimeoutException:
            return False
        return True


class Locators:

    # Main Page
    SEARCH_INPUT = (By.NAME, "search")
    BANNER_SECTION = (By.XPATH, ".//div[contains(@class, 'swiper-viewport') and contains(@class, 'slideshow')]")
    MAIN_MENU = (By.ID, "menu")
    SMALL_BASKET = (By.ID, "cart")
    LOGO = (By.ID, "logo")

    # Product Page
    ADD_CART_BUTTON = (By.ID, "button-cart")
    PRODUCT_PRICE = (By.XPATH, ".//li/h2")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    DESCRIPTION_TAB = (By.XPATH, ".//a[@data-toggle='tab' and text() = 'Description']")
    QUANTITY_INPUT = (By.ID, 'input-quantity')

    # Catalog Page
    PRODUCT_CARD = (By.XPATH, ".//div[@class='product-thumb']")
    CATALOG_MENU = (By.XPATH, ".//div[@class='list-group']")
    QUANTITY_FILTER = (By.ID, "input-limit")
    SORT_INPUT = (By.ID, 'input-sort')
    DESCRIPTION = (By.XPATH, ".//div[@class='col-sm-10']/p")

    # Admin Login Page
    USER_NAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Login')]")
    FOOTER = (By.ID, "footer")
    HEADER_LOGO = (By.ID, "header-logo")

    # Registration Page
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    CONTINUE_BUTTON = (By.XPATH, ".//input[@type='submit' and @value='Continue']")
