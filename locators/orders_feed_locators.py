from selenium.webdriver.common.by import By


class OrdersFeedLocators:
    ORDER_FEED_HEADER = By.XPATH, './/h1[text()="Лента заказов"]'
    FIRST_ORDER = By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]'
    ORDER_WINDOW = By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section'
    CLOSE_WINDOW_ORDER_BUTTON = By.XPATH, '(.//button[contains(@class, "Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK")])[last()]'
    ORDER_NUMBER_IN_WINDOW = By.XPATH, './/p[contains(@class, "text text_type_digits-default mb-10 mt-5")]'
    ALL_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[1]'
    TODAY_ORDERS_COUNTER = By.XPATH, '(.//p[contains(@class, "OrderFeed_number__2MbrQ")])[last()]'
    EMPTY_ORDERS_IN_WORK = By.XPATH, './/li[text()="Все текущие заказы готовы!"]'
    ORDERS_IN_WORK = By.XPATH, '(.//ul[contains(@class, "OrderFeed_orderListReady")]/li)[1]'
    ORDER_WINDOW_OPENED = By.XPATH, './/div[contains(@class, "Modal_modal_opened__3ISw4")]'
    ORDER_WINDOW_CLOSE = By.XPATH, './/section[contains(@class, "Modal_modal__P3_V5")]'