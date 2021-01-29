from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    url = "http://automationpractice.com/index.php"

    search_bar = (By.ID, "search_query_top")
    search_button = (By.CLASS_NAME, "button-search")
    search_results_frame = (By.CLASS_NAME, "product-listing")
    search_results_names = (By.CSS_SELECTOR, "div[class='right-block'] .product-name")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.url)

    def search(self, text):
        # type text in search bar, click on search button,
        # wait for search results and return them
        self.driver.find_element(*self.search_bar).send_keys(text)
        self.driver.find_element(*self.search_button).click()
        wait = WebDriverWait(self.driver, 6)
        wait.until(ec.presence_of_element_located(self.search_results_frame))
        search_results = self.driver.find_elements(*self.search_results_names)
        return search_results
