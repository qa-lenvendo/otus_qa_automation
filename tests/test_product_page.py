class TestProductPage:
    """
    Tests for product page
    """

    def test_check_add_cart_button(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_add_cart_button()

    def test_check_product_price(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_product_price()

    def test_check_product_name(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_product_name()

    def test_check_description_tab(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_description_tab()

    def test_check_quantity_input(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_quantity_input()
