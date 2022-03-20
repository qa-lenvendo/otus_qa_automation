from selenium.webdriver.common.by import By


class AdminProductListPageLocators:
    """
    locators from admin product list page
    """
    TITLE = (By.XPATH, ".//h1")
    ADD_PRODUCT_BUTTON = (By.XPATH, ".//a[@data-original-title='Add New']")
    ITEM_NAME = (By.XPATH, ".//table/tbody/tr/td[3]")
    ITEM_BY_NAME = (By.XPATH, ".//td[text()='{0}']/..")
    CHECKBOX_PRODUCT_BY_NAME = (By.XPATH, ".//td[text()='{0}']/..//input")
    DELETE_BUTTON = (By.XPATH, ".//button[@data-original-title='Delete']")
