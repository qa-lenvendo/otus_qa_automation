from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """
    Locators for registration page
    """
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    CONTINUE_BUTTON = (By.XPATH, ".//input[@type='submit' and @value='Continue']")
