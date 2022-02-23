class TestRegistrationPage:
    """
    Tests for registration page
    """

    def test_check_firstname_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_firstname_input()

    def test_check_lastname_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_lastname_input()

    def test_check_email_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_email_input()

    def test_check_telephone_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_telephone_input()

    def test_check_continue_button(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_continue_button()
