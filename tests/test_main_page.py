import allure
import test_data
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestMainPage:
    @allure.title('переход по клику на «Конструктор»')
    def test_open_builder_page_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()
        main_page.click_on_builder_link()

        assert main_page.get_header_builder() == 'Соберите бургер'

    @allure.title('переход по клику на «Лента заказов»')
    def test_open_order_feed_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_on_order_feed_link()

        assert main_page.get_header_order_feed() == 'Лента заказов'

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_open_details_ingredient_window(self, driver):
        driver.get(test_data.MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_on_first_ingredient()

        assert main_page.get_header_ingredient_window() == 'Детали ингредиента'

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_close_ingredient_details_window_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_on_first_ingredient()
        main_page.close_ingredient_details_window()

        assert main_page.find_ingredient_details_window() is False

    @allure.title('при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается')
    def test_drag_and_drop_top_bun_counter_not_zero(self, driver):
        driver.get(test_data.MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.drag_bun_and_drop_in_order()

        assert main_page.get_bun_counter() == '2'

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_place_order_authorization_user_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)

        main_page = MainPage(driver)
        main_page.drag_bun_and_drop_in_order()
        main_page.click_on_order_button()

        assert main_page.get_order_number() != 0