from selenium.webdriver.common.by import By

from pages.base import BasePage, PageFailedToLoadException
from pages.home import HomePage


class LoginPage(BasePage):
    TITLE = (By.TAG_NAME, "h2")
    EMAIL = (By.ID, "id_login")
    PASSWORD = (By.ID, "id_password")
    SIGNIN_BUTTON = (By.CLASS_NAME, "btn-primary")

    def __init__(self, driver):
        super().__init__(driver)
        self.url += "/accounts/login"

    def load(self):
        super().load()

        page_title = self.driver.find_element(*self.TITLE)
        if page_title.text != "Sign in":
            raise PageFailedToLoadException

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
        return HomePage(self.driver)
