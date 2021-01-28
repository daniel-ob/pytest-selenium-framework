import pytest


@pytest.mark.usefixtures("driver_init")
class TestHome:
    def test_open_url(self):
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.maximize_window()
        assert self.driver.title == "My Store"
