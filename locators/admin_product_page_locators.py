from selenium.webdriver.common.by import By


class AdminProductPageLocators:
    """
    Locators for admin product page
    """
    INPUT_PRODUCT_NAME = (By.ID, 'input-name1')
    INPUT_META_TAG_TITLE = (By.ID, 'input-meta-title1')
    TAB_DATA = (By.XPATH, ".//a[@data-toggle='tab' and text() = 'Data']")
    INPUT_MODEL = (By.ID, "input-model")
    BUTTON_SAVE = (By.XPATH, ".//button[@data-original-title='Save']")
