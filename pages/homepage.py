"""
Abstracts web page interactions in a separate Class.
(Page Object Design Pattern)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    URL = "http://automationpractice.com/index.php"

    SEARCH_BAR = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.CLASS_NAME, "button-search")
    SEARCH_RESULTS_FRAME = (By.CLASS_NAME, "product-listing")
    SEARCH_RESULTS_NAMES = (By.CSS_SELECTOR, "div[class='right-block'] .product-name")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def search(self, text):
        # type text in search bar, click on search button,
        # wait for search results and return them
        self.driver.find_element(*self.SEARCH_BAR).send_keys(text)
        self.driver.find_element(*self.SEARCH_BUTTON).click()
        wait = WebDriverWait(self.driver, 6)
        wait.until(ec.presence_of_element_located(self.SEARCH_RESULTS_FRAME))
        search_results = self.driver.find_elements(*self.SEARCH_RESULTS_NAMES)
        return search_results
