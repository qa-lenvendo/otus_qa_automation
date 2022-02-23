from selenium.webdriver.common.by import By


class AdminLoginPageLocators:
    """
    Locators for admin login page
    """
    USER_NAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.ID, "input-password")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Login')]")
    FOOTER = (By.ID, "footer")
    HEADER_LOGO = (By.ID, "header-logo")
