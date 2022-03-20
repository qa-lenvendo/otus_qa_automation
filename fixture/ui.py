from selenium import webdriver
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.catalog_page import CatalogPage
from pages.admin_main_page import AdminMainPage
from pages.admin_login_page import AdminLoginPage
from pages.registration_page import RegistrationPage
from pages.admin_product_page import AdminProductPage
from webdriver_manager.opera import OperaDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.admin_product_list_page import AdminProductListPage


class UserInterface:
    def __init__(self, base_url, browser_name, headless):

        self._window_width = 1920
        self._window_height = 1080

        if browser_name == 'chrome':
            options = webdriver.ChromeOptions()
            if headless == 'true':
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(
                executable_path=ChromeDriverManager().install(),
                options=options,
                desired_capabilities=options.to_capabilities()
            )
        elif browser_name == 'firefox':
            options = webdriver.FirefoxOptions()
            if headless == 'true':
                options.add_argument('--headless')
            self.driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options,
                desired_capabilities=options.to_capabilities()
            )
        elif browser_name == 'opera':
            options = webdriver.ChromeOptions()
            if headless == 'true':
                options.add_argument('--headless')
            self.driver = webdriver.Opera(
                executable_path=OperaDriverManager().install(),
                options=options,
                desired_capabilities=options.to_capabilities()
            )
        else:
            raise AssertionError(f'Unknown browser: {browser_name}')
        self.driver.set_window_size(self._window_width, self._window_height)

        self.base_url = base_url
        self.main_page = MainPage(self)
        self.catalog_page = CatalogPage(self)
        self.product_page = ProductPage(self)
        self.admin_main_page = AdminMainPage(self)
        self.admin_login_page = AdminLoginPage(self)
        self.registration_page = RegistrationPage(self)
        self.admin_product_page = AdminProductPage(self)
        self.admin_product_list_page = AdminProductListPage(self)

    def close(self):
        self.driver.quit()
