from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


class ProductListPage(BasePage):
    # Locators
    SEARCH_BAR = (By.TAG_NAME, "input")
    SEARCH_BUTTON = (By.TAG_NAME, "button")
    RESULTS_QUERY_SPAN = (By.XPATH, "//span[contains(text(), 'Showing results')]")
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".aos-init h3")

    def __init__(self, driver):
        super().__init__(driver)
        self.url += "/cart/shop"

    def search(self, text):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        results_query_span = self.driver.find_element(*self.RESULTS_QUERY_SPAN)
        wait = WebDriverWait(self.driver, self.max_seconds_wait)
        wait.until(lambda d: results_query_span.is_displayed())
        return [title.text for title in self.driver.find_elements(*self.PRODUCT_TITLES)]
