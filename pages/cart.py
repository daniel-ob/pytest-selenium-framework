from selenium.webdriver.common.by import By

from pages.base import BasePage


class CartPage(BasePage):
    TOTAL = (By.ID, "id_total")
    REMOVE_BUTTONS = (By.LINK_TEXT, "X")

    def __init__(self, driver):
        super().__init__(driver)
        self.url += "/cart"

    def get_total(self):
        return self.driver.find_element(*self.TOTAL).text

    def empty_cart(self):
        while self.driver.find_elements(*self.REMOVE_BUTTONS):
            self.driver.find_elements(*self.REMOVE_BUTTONS)[0].click()
