from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base import BasePage, PageFailedToLoadException


class ProductDetailPage(BasePage):
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".col-md-6 h2")
    QUANTITY_INPUT = (By.ID, "id_quantity")
    COLOUR_SELECT = (By.ID, "id_colour")
    SIZE_SELECT = (By.ID, "id_size")
    ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver, slug):
        super().__init__(driver)
        self.url += f"/cart/shop/{slug}"
        self.slug = slug

    def load(self):
        super().load()
        super().load()  # workaround for issue with page loading on Chrome

        try:
            self.driver.find_element(*self.PRODUCT_TITLE)
        except NoSuchElementException:
            raise PageFailedToLoadException(
                f"Failed to load product detail page for slug {self.slug}"
            )

    def set_quantity(self, quantity):
        quantity_input = self.driver.find_element(*self.QUANTITY_INPUT)
        quantity_input.send_keys(quantity)

    def set_colour(self, index):
        colour_select = Select(self.driver.find_element(*self.COLOUR_SELECT))
        colour_select.select_by_index(index)

    def set_size(self, index):
        size_select = Select(self.driver.find_element(*self.SIZE_SELECT))
        size_select.select_by_index(index)

    def add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
