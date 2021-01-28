from selenium import webdriver


class TestHome:
    def test_open_url(self):
        driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
        driver.get("http://automationpractice.com/index.php")
        driver.maximize_window()
        assert driver.title == "My Store"
        driver.close()
