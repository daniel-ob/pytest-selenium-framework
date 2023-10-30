import pytest

from pages.cart import CartPage
from pages.login import LoginPage
from pages.product_detail import ProductDetailPage
from pages.product_list import ProductListPage
from testdata.testdata import DataCollector


@pytest.mark.usefixtures("browser")
class TestShop:
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.load()

        home_page = login_page.login(
            email="test_user@ecommerce.com",
            password="Q9aDJ~Snd]wx9WL",
        )

        assert "test_user" in home_page.get_alert_text()

    # Data-driven test (CSV file)
    data_test_search = DataCollector("testdata/test_search.csv")

    @pytest.mark.parametrize(
        "text, expected_results_number", data_test_search.get_test_data()
    )
    def test_search(self, text, expected_results_number):
        product_list_page = ProductListPage(self.driver)
        product_list_page.load()

        results = product_list_page.search(text)

        assert len(results) == int(expected_results_number)
        # all results must match search text
        for product_title in results:
            assert text.lower() in product_title.lower()

    data_test_search = DataCollector("testdata/test_add_to_cart.csv")

    @pytest.mark.parametrize(
        "slug_quantities, expected_cart_total",
        [
            ([("cotton-t-shirt", 1), ("long-sleeves-shirt", 2)], "$42.00"),
            ([("short-sleeves-dress", 3), ("ai-generated-dress", 1)], "$220.00"),
        ],
    )
    def test_add_to_cart(self, slug_quantities, expected_cart_total):
        cart_page = CartPage(self.driver)
        cart_page.load()
        cart_page.empty_cart()

        # Add all products to cart
        for slug, quantity in slug_quantities:
            product_detail_page = ProductDetailPage(self.driver, slug)
            product_detail_page.load()

            product_detail_page.set_quantity(quantity)
            product_detail_page.set_colour(1)
            product_detail_page.set_size(1)
            product_detail_page.add_to_cart()

        assert cart_page.get_cart_count() == len(slug_quantities)
        assert cart_page.get_total() == expected_cart_total
