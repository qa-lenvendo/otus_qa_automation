from selenium.webdriver.common.by import By


class MainPageLocators:
    """
    Locators for main page
    """
    SEARCH_INPUT = (By.NAME, "search")
    BANNER_SECTION = (By.XPATH, ".//div[contains(@class, 'swiper-viewport') and contains(@class, 'slideshow')]")
    MAIN_MENU = (By.ID, "menu")
    SMALL_BASKET = (By.ID, "cart")
    LOGO = (By.ID, "logo")
