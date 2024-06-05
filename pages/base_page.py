from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

        return self.driver.find_element(*locator)

    def wait_disappear_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)

        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.click()
        action.perform()

    def send_keys(self, locator, key):
        element = self.find_element_with_wait(locator)
        element.send_keys(key)

    def current_url(self):
        return self.driver.current_url

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def get_attribute_value(self, locator, attribute_name: str):
        element = self.find_element_with_wait(locator)
        return element.get_attribute(attribute_name)

    def element_exist(self, locator):
        try:
            self.driver.find_element_with_wait(locator)
            return True
        finally:
            return False

    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)

        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()