import allure
import test_data
from pages.orders_feed_page import OrdersFeedPage
from pages.profile_page import ProfilePage


class TestOrdersFeedPage:
    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_details_order_window_success(self, driver):
        driver.get(test_data.MAIN_PAGE + test_data.ORDER_FEED)

        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.click_on_first_order()

        assert orders_feed_page.order_window_open() is True

    @allure.title('закрытие окна заказа')
    def test_close_details_order_window_success(self, driver):
        driver.get(test_data.MAIN_PAGE + test_data.ORDER_FEED)

        orders_feed_page = OrdersFeedPage(driver)
        orders_feed_page.click_on_first_order()
        orders_feed_page.close_details_order_window()

        assert orders_feed_page.order_window_open() is False

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_check_order_user_in_orders_feed_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)

        orders_feed = OrdersFeedPage(driver)
        orders_feed.create_order()
        orders_feed.wait_order_placed()
        orders_feed.close_details_order_window()
        order_number = orders_feed.get_lust_number_order()
        orders_feed.go_to_orders_feed()
        orders_feed.click_on_first_order()

        assert orders_feed.get_order_number_in_orders_feed() == order_number

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_check_all_order_counter_increased(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)

        orders_feed = OrdersFeedPage(driver)
        orders_feed.click_on_orders_feed()
        before_orders = orders_feed.get_all_orders_counter()

        orders_feed.click_on_builder()
        orders_feed.create_order()
        orders_feed.wait_order_placed()
        orders_feed.close_details_order_window()

        orders_feed.click_on_orders_feed()
        after_orders = orders_feed.get_all_orders_counter()

        assert int(before_orders) < int(after_orders)

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_check_today_order_counter_increased(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)

        orders_feed = OrdersFeedPage(driver)
        orders_feed.click_on_orders_feed()
        before_orders = orders_feed.get_today_orders_counter()

        orders_feed.click_on_builder()
        orders_feed.create_order()
        orders_feed.wait_order_placed()
        orders_feed.close_details_order_window()

        orders_feed.click_on_orders_feed()
        after_orders = orders_feed.get_today_orders_counter()

        assert int(before_orders) < int(after_orders)

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_check_new_order_in_work_success(self, driver):
        driver.get(test_data.MAIN_PAGE)

        profile_page = ProfilePage(driver)
        profile_page.click_on_link_profile()
        profile_page.enter_profile(email=test_data.USER_EMAIL, password=test_data.USER_PASS)

        orders_feed = OrdersFeedPage(driver)
        orders_feed.create_order()
        orders_feed.wait_order_placed()
        order_number = orders_feed.get_new_order_number()
        orders_feed.close_details_order_window()
        orders_feed.click_on_orders_feed()

        assert order_number in orders_feed.get_orders_in_work()