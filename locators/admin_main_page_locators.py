from selenium.webdriver.common.by import By


class AdminMainPageLocators:
    """
    Locators for admin main page
    """

    USER_ICON_BY_NAME = (By.XPATH, ".//ul[contains(@class, 'navbar-right')]/li/a[contains(text(), '{0}')]")
    MAIN_MENU_CATALOG = (By.XPATH, ".//li[@id='menu-catalog']/a")
    MAIN_SUBMENU_CATALOG_BY_NAME = (By.XPATH, ".//li[@id='menu-catalog']//a[text()='{0}']")
