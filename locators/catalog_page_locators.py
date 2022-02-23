from selenium.webdriver.common.by import By


class CatalogPageLocators:
    """
    Locators for catalog page
    """
    PRODUCT_CARD = (By.XPATH, ".//div[@class='product-thumb']")
    CATALOG_MENU = (By.XPATH, ".//div[@class='list-group']")
    QUANTITY_FILTER = (By.ID, "input-limit")
    SORT_INPUT = (By.ID, 'input-sort')
    DESCRIPTION = (By.XPATH, ".//div[@class='col-sm-10']/p")
