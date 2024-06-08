from selenium.webdriver.common.by import By


class ResetPassPageLocators:
    RESET_BUTTON = By.XPATH, './/button[contains(@class, "button_button_size_medium")]'
    RESET_PASS_LINK = By.LINK_TEXT, 'Восстановить пароль'
    RESET_PASS_HEADER = By.XPATH, './/h2[text()="Восстановление пароля"]'
    SECRET_KEY_FIELD = By.XPATH, './/label[text()="Введите код из письма"]'
    SHOW_PASS_BUTTON = By.XPATH, './/div[contains(@class,"icon-action")]'