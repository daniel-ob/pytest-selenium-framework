import pytest
from pages.homepage import HomePage


@pytest.mark.usefixtures("browser")
class TestHome:
    def test_open_url(self):
        homepage = HomePage(self.driver)
        homepage.load()
        assert self.driver.title == "My Store"

    @pytest.mark.parametrize("text, expected_results_number", [("shirt", 1), ("Dress", 7)])
    def test_search(self, text, expected_results_number):
        homepage = HomePage(self.driver)
        homepage.load()

        # Make a search:
        search_text = text
        search_results = homepage.search(search_text)

        # Check results number
        results_number = len(search_results)
        print(str(results_number) + " result(s)")
        assert results_number == expected_results_number

        # Check that founded items matches search text
        for product in search_results:
            print(product.text)
            assert search_text in product.text
