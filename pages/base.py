"""
Abstracts web page interactions in a separate Class.
(Page Object Design Pattern)
"""

from selenium.webdriver.common.by import By


class BasePage:
    url = "http://52.47.149.219"
    title = "Django Ecom"
    max_seconds_wait = 2

    ALERT = (By.CLASS_NAME, "alert")
    BREADCRUMB_CURRENT_PAGE = (By.CSS_SELECTOR, "strong:first-of-type")
    CART_COUNT = (By.CLASS_NAME, "count")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def get_alert_text(self):
        return self.driver.find_element(*self.ALERT).text

    def get_cart_count(self):
        return int(self.driver.find_element(*self.CART_COUNT).text)


class PageFailedToLoadException(Exception):
    pass
