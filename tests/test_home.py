import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("browser")
class TestHome:
    def test_open_url(self):
        homepage = HomePage(self.driver)
        homepage.load()
        assert self.driver.title == "My Store"

    @pytest.mark.parametrize("text", ["shirt", "Dress"])
    def test_search(self, text):
        # Make a search and check that founded items matches that search
        homepage = HomePage(self.driver)
        homepage.load()
        search_text = text
        search_results = homepage.search(search_text)
        for product in search_results:
            print(product.text)
            assert search_text in product.text
