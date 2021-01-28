import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.maximize_window()
    request.cls.driver = driver  # assign driver to class using the fixture
    yield
    driver.close()
