from allure import epic, title
from datetime import datetime
from random import choice


@epic('Страница карточки товара')
class TestAdminProductPage:
    """
    Tests for admin product page
    """

    @title('Добавление новой карточки товара')
    def test_add_new_product(self, ui):
        product_name = f'Product_{str(datetime.now().__format__("%Y%m%d%H%M%S"))}'
        meta_tag = f'MetaTag_{str(datetime.now().__format__("%Y%m%d%H%M%S"))}'
        product_model = f'Model_{str(datetime.now().__format__("%Y%m%d%H%M%S"))}'

        ui.admin_login_page.open()
        ui.admin_login_page.login_user(user_name='user', user_password='bitnami')
        ui.admin_main_page.should_be_login_user('John Doe')

        ui.admin_main_page.click_catalog_menu()
        ui.admin_main_page.click_catalog_submenu('Products')

        ui.admin_product_list_page.should_be_open()
        ui.admin_product_list_page.click_add_product_button()

        ui.admin_product_page.should_be_open()
        ui.admin_product_page.enter_value_in_product_name_field(value=product_name)
        ui.admin_product_page.enter_value_in_meta_tag_field(value=meta_tag)
        ui.admin_product_page.click_data_tab()
        ui.admin_product_page.enter_value_in_model_field(value=product_model)
        ui.admin_product_page.click_save_button()

        ui.admin_product_list_page.should_be_open()
        ui.admin_product_list_page.should_be_product_name(product_name=product_name)

    @title('Удаление товара из каталога')
    def test_delete_product(self, ui):
        ui.admin_login_page.open()
        ui.admin_login_page.login_user(user_name='user', user_password='bitnami')
        ui.admin_main_page.should_be_login_user('John Doe')

        ui.admin_main_page.click_catalog_menu()
        ui.admin_main_page.click_catalog_submenu('Products')

        ui.admin_product_list_page.should_be_open()
        product = choice(ui.admin_product_list_page.get_product_name_list())
        ui.admin_product_list_page.select_product(product_name=product)
        ui.admin_product_list_page.click_delete_button()
        ui.admin_product_list_page.should_not_be_product_name(product_name=product)
