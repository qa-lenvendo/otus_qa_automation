from src.ui_helper import UiHelper, Locators


class TestCheckExistMainPage:
    """
    Checking the presence of elements on main pages
    """

    def test_check_search_input_on_main_page(self, browser, base_url):
        browser.get(base_url)
        assert UiHelper.is_element_present(browser, *Locators.SEARCH_INPUT), 'element "Search Input" is not present'

    def test_check_banner_section(self, browser, base_url):
        browser.get(base_url)
        assert UiHelper.is_element_present(browser, *Locators.BANNER_SECTION), 'element "Search Input" is not present'

    def test_check_main_menu(self, browser, base_url):
        browser.get(base_url)
        assert UiHelper.is_element_present(browser, *Locators.MAIN_MENU), 'element "Search Input" is not present'

    def test_check_small_basket(self, browser, base_url):
        browser.get(base_url)
        assert UiHelper.is_element_present(browser, *Locators.SMALL_BASKET), 'element "Search Input" is not present'

    def test_check_logo(self, browser, base_url):
        browser.get(base_url)
        assert UiHelper.is_element_present(browser, *Locators.LOGO), 'element "Search Input" is not present'


class TestCheckExistProductPage:
    """
    Checking the presence of elements on product pages
    """
    _path = '/macbook'

    def test_check_add_cart_button(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.ADD_CART_BUTTON), 'element "Search Input" is not present'

    def test_check_product_price(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.PRODUCT_PRICE), 'element "Search Input" is not present'

    def test_check_product_name(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.PRODUCT_NAME), 'element "Search Input" is not present'

    def test_check_description_tab(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.DESCRIPTION_TAB), 'element "Search Input" is not present'

    def test_check_quantity_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.QUANTITY_INPUT), 'element "Search Input" is not present'


class TestCheckExistCatalogPage:
    """
    Checking the presence of elements on catalog pages
    """
    _path = '/desktops'

    def test_check_product_card(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.PRODUCT_CARD), 'element "Search Input" is not present'

    def test_check_catalog_menu(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.CATALOG_MENU), 'element "Search Input" is not present'

    def test_check_description_page(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.DESCRIPTION), 'element "Search Input" is not present'

    def test_check_quantity_filter(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.QUANTITY_FILTER), 'element "Search Input" is not present'

    def test_check_sort_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.SORT_INPUT), 'element "Search Input" is not present'


class TestCheckExistAdminLoginPage:
    """
    Checking the presence of elements on admin login pages
    """
    _path = "/admin"

    def test_check_logo(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.HEADER_LOGO), 'element "Search Input" is not present'

    def test_check_user_name_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.USER_NAME_INPUT), 'element "Search Input" is not present'

    def test_check_password_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.PASSWORD_INPUT), 'element "Search Input" is not present'

    def test_check_login_button(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.LOGIN_BUTTON), 'element "Search Input" is not present'

    def test_check_footer(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.FOOTER), 'element "Search Input" is not present'


class TestCheckExistRegistrationUserPage:
    """
    Checking the presence of elements on registration pages
    """
    _path = "/index.php?route=account/register"

    def test_check_firstname_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.FIRSTNAME_INPUT), 'element "Search Input" is not present'

    def test_check_lastname_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.LASTNAME_INPUT), 'element "Search Input" is not present'

    def test_check_email_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.EMAIL_INPUT), 'element "Search Input" is not present'

    def test_check_telephone_input(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.TELEPHONE_INPUT), 'element "Search Input" is not present'

    def test_check_continue_button(self, browser, base_url):
        browser.get(base_url + self._path)
        assert UiHelper.is_element_present(browser, *Locators.CONTINUE_BUTTON), 'element "Search Input" is not present'
