class TestMainPage:
    """
    Tests for main page
    """

    def test_check_search_input_on_main_page(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_search_input()

    def test_check_banner_section(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_banner_section()

    def test_check_main_menu(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_main_menu()

    def test_check_small_basket(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_small_basket()

    def test_check_logo(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_logo()
