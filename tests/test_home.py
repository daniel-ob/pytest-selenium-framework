import pytest
from pages.homepage import HomePage
from testdata.testdata import DataCollector


@pytest.mark.usefixtures("browser")
class TestHome:
    def test_open_url(self):
        homepage = HomePage(self.driver)
        homepage.load()
        assert self.driver.title == "My Store"

    # Data-driven test (CSV file)
    data = DataCollector("testdata/homepage-test_search.csv")

    @pytest.mark.parametrize("text, expected_results_number", data.get_test_data())
    def test_search(self, text, expected_results_number):
        homepage = HomePage(self.driver)
        homepage.load()

        # Make a search:
        search_text = text
        search_results = homepage.search(search_text)

        # Check results number
        results_number = len(search_results)
        print(str(results_number) + " result(s)")
        assert results_number == int(expected_results_number)

        # Check that founded items matches search text
        for product in search_results:
            print(product.text)
            assert search_text in product.text
