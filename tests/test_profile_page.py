import allure
import test_data
from pages.profile_page import ProfilePage


class TestProfilePage:
    @allure.title('переход по клику на «Личный кабинет»')
    def test_open_profile_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)
        profile_page.click_on_link_profile()

        assert profile_page.get_user_name_in_profile() == test_data.USER_NAME

    @allure.title('переход в раздел «История заказов»')
    def test_open_history_order_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)
        profile_page.click_on_link_profile()
        profile_page.click_on_history_orders()

        assert profile_page.get_status_order() == 'Выполнен'

    @allure.title('выход из аккаунта')
    def test_logout_profile_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)
        profile_page.click_on_link_profile()
        profile_page.click_on_logout_button()

        assert profile_page.get_header_login_page() == 'Вход'