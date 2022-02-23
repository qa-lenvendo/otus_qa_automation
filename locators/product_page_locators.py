from selenium.webdriver.common.by import By


class ProductPageLocators:
    """
    Locators for product page
    """
    ADD_CART_BUTTON = (By.ID, "button-cart")
    PRODUCT_PRICE = (By.XPATH, ".//li/h2")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    DESCRIPTION_TAB = (By.XPATH, ".//a[@data-toggle='tab' and text() = 'Description']")
    QUANTITY_INPUT = (By.ID, 'input-quantity')
