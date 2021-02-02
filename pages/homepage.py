"""
Abstracts web page interactions in a separate Class.
(Page Object Design Pattern)
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains


class HomePage:
    URL = "http://automationpractice.com/index.php"

    SEARCH_BAR = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.CLASS_NAME, "button-search")
    SEARCH_RESULTS_FRAME = (By.CLASS_NAME, "product-listing")
    SEARCH_RESULTS_NAMES = (By.CSS_SELECTOR, "div[class='right-block'] .product-name")
    PRODUCTS = (By.XPATH, "//a[@class='product-name']")
    PRODUCT_ADD_BUTTON = (By.XPATH, "parent::h5/parent::div/div/a[@title='Add to cart']/span")  # starting from PRODUCTS
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "span[title='Continue shopping']")

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

    def add_to_cart(self, item):
        # hover mouse over selected item, click on "add to cart" button, then close "cart layer"
        products = self.driver.find_elements(*self.PRODUCTS)
        for product in products:
            if product.text == item:
                action = ActionChains(self.driver)
                action.move_to_element(product)
                add_to_cart_button = product.find_element(*self.PRODUCT_ADD_BUTTON)
                action.move_to_element(add_to_cart_button).click().perform()
                break
        # wait for cart layer to be displayed
        self.driver.implicitly_wait(5)
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
