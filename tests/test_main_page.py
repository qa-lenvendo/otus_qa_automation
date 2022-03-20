from allure import epic, title


@epic('Главная страница')
class TestMainPage:
    """
    Tests for main page
    """

    @title('Проверка наличия поля поиска')
    def test_check_search_input_on_main_page(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_search_input()

    @title('Проверка наличия баннеров')
    def test_check_banner_section(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_banner_section()

    @title('Проверка наличия главного меню')
    def test_check_main_menu(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_main_menu()

    @title('Проверка наличия малой корзины')
    def test_check_small_basket(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_small_basket()

    @title('Проверка наличия логотипа')
    def test_check_logo(self, ui):
        ui.main_page.open()
        ui.main_page.should_be_logo()
