from allure import epic, title


@epic('Страница авторизации в админ-панели')
class TestAdminLoginPage:
    """
    Tests for admin login page
    """

    @title('Проверка наличия логотипа')
    def test_check_logo(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_logo()

    @title('Проверка наличия поля ввода "Username"')
    def test_check_user_name_input(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_user_name_input()

    @title('Проверка наличия поля ввода "Password"')
    def test_check_password_input(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_password_input()

    @title('Проверка наличия кнопки "Login"')
    def test_check_login_button(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_login_button()

    @title('Проверка наличия футера')
    def test_check_footer(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_footer()
