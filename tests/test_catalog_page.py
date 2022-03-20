class TestCatalogPage:
    """
    Tests for catalog page
    """

    def test_check_product_card(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_product_card()

    def test_check_catalog_menu(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_catalog_menu()

    def test_check_description_page(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_description_page()

    def test_check_quantity_filter(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_quantity_filter()

    def test_check_sort_input(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_sort_input()
