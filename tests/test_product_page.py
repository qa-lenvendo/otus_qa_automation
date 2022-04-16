from allure import epic, title


@epic('Страница карточки товара')
class TestProductPage:
    """
    Tests for product page
    """

    @title('Проверка наличия кнопки добавления товара в корзину')
    def test_check_add_cart_button(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_add_cart_button()

    @title('Проверка наличие цены')
    def test_check_product_price(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_product_price()

    @title('Проверка наличие наименования товара')
    def test_check_product_name(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_product_name()

    @title('Проверка наличия вкладки с описанием товара')
    def test_check_description_tab(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_description_tab()

    @title('Проверка наличия поля ввода количества товара')
    def test_check_quantity_input(self, ui):
        ui.product_page.open('/macbook')
        ui.product_page.should_be_quantity_input()
