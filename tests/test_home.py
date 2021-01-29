import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver_init")
class TestHome:
    def test_open_url(self):
        self.driver.get("http://automationpractice.com/index.php")
        assert self.driver.title == "My Store"

    def test_search(self):
        wait = WebDriverWait(self.driver, 6)
        search_text = "Dress"
        self.driver.find_element(By.ID, "search_query_top").send_keys(search_text)
        self.driver.find_element(By.CLASS_NAME, "button-search").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-listing")))
        search_results = self.driver.find_elements(By.CSS_SELECTOR, "div[class='right-block'] .product-name")
        for product in search_results:
            print(product.text)
            assert search_text in product.text
