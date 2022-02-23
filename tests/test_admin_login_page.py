class TestAdminLoginPage:
    """
    Tests for admin login page
    """

    def test_check_logo(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_logo()

    def test_check_user_name_input(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_user_name_input()

    def test_check_password_input(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_password_input()

    def test_check_login_button(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_login_button()

    def test_check_footer(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.should_be_footer()
