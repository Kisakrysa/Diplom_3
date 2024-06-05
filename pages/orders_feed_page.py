import allure
from locators.main_page_locators import MainPageLocators
from locators.orders_feed_locators import OrdersFeedLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class OrdersFeedPage(BasePage):
    @allure.step('клик по "Ленте заказов"')
    def click_on_orders_feed(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('переход в "Ленту заказов" из "Личного кабинета"')
    def go_to_orders_feed(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_LINK)

    @allure.step('клик по "Конструктору"')
    def click_on_builder(self):
        self.click_on_element(MainPageLocators.BUILDER_LINK)

    @allure.step('клик на первый заказ')
    def click_on_first_order(self):
        self.click_on_element(OrdersFeedLocators.FIRST_ORDER)

    @allure.step('открытие окна заказа')
    def order_window_open(self):
        element = self.get_attribute_value(OrdersFeedLocators.ORDER_WINDOW, 'class')
        if 'opened' in element:
            return True
        else:
            return False

    @allure.step('зарытие окна заказа')
    def close_details_order_window(self):
        self.click_on_element(OrdersFeedLocators.CLOSE_WINDOW_ORDER_BUTTON)

    @allure.step('вывод номер последнего заказа')
    def get_lust_number_order(self):
        self.click_on_element(ProfilePageLocators.PROFILE_LINK)
        self.click_on_element(ProfilePageLocators.HISTORY_LINK)
        return self.get_text_from_element(ProfilePageLocators.LAST_ORDER)

    @allure.step('вывод номера нового заказа')
    def get_new_order_number(self):
        return self.get_text_from_element(MainPageLocators.ORDER_NUMBER)

    @allure.step('вывод номера заказа в "Лента заказов"')
    def get_order_number_in_orders_feed(self):
        return self.get_text_from_element(OrdersFeedLocators.ORDER_NUMBER_IN_WINDOW)

    @allure.step('создать заказ')
    def create_order(self):
        self.find_element_with_wait(MainPageLocators.BUILDER_HEADER)
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.DROP_BASKET_AREA)
        self.click_on_element(MainPageLocators.ORDER_BUTTON)

    @allure.step('вывод значения счетчика заказов ЗА ВСЕ ВРЕМЯ')
    def get_all_orders_counter(self):
        self.find_element_with_wait(OrdersFeedLocators.ALL_ORDERS_COUNTER)
        return self.get_text_from_element(OrdersFeedLocators.ALL_ORDERS_COUNTER)

    @allure.step('вывод значения счетчика заказов ЗА СЕГОДНЯ')
    def get_today_orders_counter(self):
        self.find_element_with_wait(OrdersFeedLocators.TODAY_ORDERS_COUNTER)
        return self.get_text_from_element(OrdersFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step('вывод списка заказов "В работе"')
    def get_orders_in_work(self):
        self.find_element_with_wait(OrdersFeedLocators.EMPTY_ORDERS_IN_WORK)
        self.wait_disappear_element(OrdersFeedLocators.EMPTY_ORDERS_IN_WORK)
        return self.get_text_from_element(OrdersFeedLocators.ORDERS_IN_WORK)

    @allure.step('ожидание номера заказа')
    def wait_order_placed(self):
        self.find_element_with_wait(OrdersFeedLocators.ORDER_WINDOW_OPENED)
        self.wait_disappear_element(OrdersFeedLocators.ORDER_WINDOW_OPENED)