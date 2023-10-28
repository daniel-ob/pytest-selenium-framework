"""
Abstracts web page interactions in a separate Class.
(Page Object Design Pattern)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ShopPage:
    URL = "http://52.47.149.219/cart/shop/"

    SEARCH_BAR = (By.TAG_NAME, "input")
    SEARCH_BUTTON = (By.TAG_NAME, "button")
    RESULTS_QUERY_SPAN = (By.XPATH, "//span[contains(text(), 'Showing results')]")
    PRODUCT_TITLES = (By.CSS_SELECTOR, ".aos-init h3")

    MAX_SECONDS_WAIT = 2

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, text):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        results_query_span = self.driver.find_element(*self.RESULTS_QUERY_SPAN)
        wait = WebDriverWait(self.driver, self.MAX_SECONDS_WAIT)
        wait.until(lambda d: results_query_span.is_displayed())
        return [title.text for title in self.driver.find_elements(*self.PRODUCT_TITLES)]
