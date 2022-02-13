from src.ui_helper import UiHelper, Locators


class TestCheckExistMainPage:
    """
    Checking the presence of elements on main pages
    """

    def test_check_search_input_on_main_page(self, browser, base_url):
        browser.get(base_url)
        strategy, locator = Locators.SEARCH_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_banner_section(self, browser, base_url):
        browser.get(base_url)
        strategy, locator = Locators.BANNER_SECTION

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_main_menu(self, browser, base_url):
        browser.get(base_url)
        strategy, locator = Locators.MAIN_MENU

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_small_basket(self, browser, base_url):
        browser.get(base_url)
        strategy, locator = Locators.SMALL_BASKET

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_logo(self, browser, base_url):
        browser.get(base_url)
        strategy, locator = Locators.LOGO

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'


class TestCheckExistProductPage:
    """
    Checking the presence of elements on product pages
    """
    _path = '/macbook'

    def test_check_add_cart_button(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.ADD_CART_BUTTON

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_product_price(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.PRODUCT_PRICE

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_product_name(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.PRODUCT_NAME

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_description_tab(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.DESCRIPTION_TAB

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_quantity_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.QUANTITY_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'


class TestCheckExistCatalogPage:
    """
    Checking the presence of elements on catalog pages
    """
    _path = '/desktops'

    def test_check_product_card(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.PRODUCT_CARD

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_catalog_menu(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.CATALOG_MENU

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_description_page(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.DESCRIPTION

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_quantity_filter(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.QUANTITY_FILTER

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_sort_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.SORT_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'


class TestCheckExistAdminLoginPage:
    """
    Checking the presence of elements on admin login pages
    """
    _path = "/admin"

    def test_check_logo(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.HEADER_LOGO

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_user_name_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.USER_NAME_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_password_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.PASSWORD_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_login_button(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.LOGIN_BUTTON

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_footer(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.FOOTER

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'


class TestCheckExistRegistrationUserPage:
    """
    Checking the presence of elements on registration pages
    """
    _path = "/index.php?route=account/register"

    def test_check_firstname_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.FIRSTNAME_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_lastname_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.LASTNAME_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_email_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.EMAIL_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_telephone_input(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.TELEPHONE_INPUT

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'

    def test_check_continue_button(self, browser, base_url):
        browser.get(base_url + self._path)
        strategy, locator = Locators.CONTINUE_BUTTON

        assert UiHelper.is_element_present(browser, strategy, locator), 'element "Search Input" is not present'
