import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("browser")
class TestHome:
    def test_open_url(self):
        homepage = HomePage(self.driver)
        homepage.load()
        assert self.driver.title == "My Store"

    def test_search(self):
        homepage = HomePage(self.driver)
        search_text = "Dress"
        search_results = homepage.search(search_text)
        for product in search_results:
            print(product.text)
            assert search_text in product.text
