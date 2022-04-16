from allure import epic, title


@epic('Страница регистрации пользователя')
class TestRegistrationPage:
    """
    Tests for registration page
    """

    @title('Проверка наличия поля ввода имени')
    def test_check_firstname_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_firstname_input()

    @title('Проверка наличия поля ввода фамилии')
    def test_check_lastname_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_lastname_input()

    @title('Проверка наличия поля ввода email')
    def test_check_email_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_email_input()

    @title('Проверка наличия поля ввода номера телефона')
    def test_check_telephone_input(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_telephone_input()

    @title('Проверка наличия кнопки "Continue"')
    def test_check_continue_button(self, ui):
        ui.registration_page.open()
        ui.registration_page.should_be_continue_button()

    @title('Регистрация нового пользователя')
    def test_registration_new_user(self, ui, test_data):
        ui.registration_page.open()

        ui.registration_page.enter_value_in_first_name_field(value=test_data.firstname)
        ui.registration_page.enter_value_in_lastname_field(value=test_data.lastname)
        ui.registration_page.enter_value_in_email_field(value=test_data.email)
        ui.registration_page.enter_value_in_telephone_field(value=test_data.phone)
        ui.registration_page.enter_value_in_password_field(value=test_data.password)
        ui.registration_page.enter_value_in_confirm_password_field(value=test_data.password)
        ui.registration_page.click_privacy_policy_checkbox()
        ui.registration_page.click_continue_button()

        ui.registration_page.should_be_open_account_success()
