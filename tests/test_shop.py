import pytest

from pages.shoppage import ShopPage
from testdata.testdata import DataCollector


@pytest.mark.usefixtures("browser")
class TestShop:
    def test_open_url(self):
        homepage = ShopPage(self.driver)
        homepage.load()
        assert self.driver.title == "Django Ecom"

    # Data-driven test (CSV file)
    data = DataCollector("testdata/shoppage-test_search.csv")

    @pytest.mark.parametrize("text, expected_results_number", data.get_test_data())
    def test_search(self, text, expected_results_number):
        homepage = ShopPage(self.driver)
        homepage.load()

        results = homepage.search(text)
        assert len(results) == int(expected_results_number)

        for product_title in results:
            assert text.lower() in product_title.lower()
