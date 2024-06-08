from selenium.webdriver.common.by import By


class ProfilePageLocators:
    PROFILE_LINK = By.LINK_TEXT, 'Личный Кабинет'
    HISTORY_LINK = By.LINK_TEXT, 'История заказов'
    LOGOUT_BUTTON = By.XPATH, './/button[contains(@class, "Account_button")]'
    NAME_FIELD = By.XPATH, './/label[text()="Имя"]/parent::div/input'
    ORDER_NUMBER = By.XPATH, '(.//p[contains(@class, "text text_type_digits-default")])[1]'
    ORDER_DONE = By.XPATH, '(.//p[contains(@class, "OrderHistory_visible__19YMB")])[1]'
    LAST_ORDER = By.XPATH, '(.//div[contains(@class, "OrderHistory_textBox__3lgbs")]/p[contains(@class, "text text_type_digits-default")])[last()]'