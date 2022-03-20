from allure import epic, title


@epic('Страница листинга каталога')
class TestCatalogPage:
    """
    Tests for catalog page
    """

    @title('Проверка наличия товаров')
    def test_check_product_card(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_product_card()

    @title('Проверка наличия меню категорий в каталоге')
    def test_check_catalog_menu(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_catalog_menu()

    @title('Проверка наличия описания категории')
    def test_check_description_page(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_description_page()

    @title('Проверка наличия фильтра по количеству товаров')
    def test_check_quantity_filter(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_quantity_filter()

    @title('Проверка наличия элемента сортировки')
    def test_check_sort_input(self, ui):
        ui.catalog_page.open('/desktops')
        ui.catalog_page.should_be_sort_input()
