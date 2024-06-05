import allure
import test_data
from pages.reset_pass_page import ResetPassPage


class TestResetPassPage:
    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_reset_password_turn_page_success(self, driver):
        driver.get(test_data.MAIN_PAGE + test_data.LOGIN)

        reset_pass_page = ResetPassPage(driver)
        reset_pass_page.click_on_reset_password()

        assert reset_pass_page.get_text_from_header_reset_password_page() == 'Восстановление пароля'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_reset_password_input_email_success(self, driver):
        driver.get(test_data.MAIN_PAGE + test_data.LOGIN)

        reset_pass_page = ResetPassPage(driver)
        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(test_data.USER_EMAIL)
        reset_pass_page.click_on_reset_button()

        assert reset_pass_page.return_secret_key_field_text() == 'Введите код из письма'

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_hide_and_show_password_success(self, driver):
        driver.get(test_data.MAIN_PAGE + test_data.LOGIN)

        reset_pass_page = ResetPassPage(driver)
        reset_pass_page.click_on_reset_password()
        reset_pass_page.fill_email_field(test_data.USER_EMAIL)
        reset_pass_page.click_on_reset_button()
        reset_pass_page.fill_password_field(test_data.USER_PASS)

        assert reset_pass_page.return_tipe_field() == 'text'