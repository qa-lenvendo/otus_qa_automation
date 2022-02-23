from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    """
    Locators for registration page
    """
    SUCCESS_TITLE = (By.XPATH, ".//h1[text()='Your Account Has Been Created!']")
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    TELEPHONE_INPUT = (By.ID, "input-telephone")
    PASSWORD_INPUT = (By.ID, 'input-password')
    CONFIRM_PASSWORD_INPUT = (By.ID, 'input-confirm')
    CONTINUE_BUTTON = (By.XPATH, ".//input[@type='submit' and @value='Continue']")
    CHECKBOX_PRIVACY_POLICY = (By.NAME, 'agree')
