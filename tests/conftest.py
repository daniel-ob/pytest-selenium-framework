import pytest
from selenium import webdriver


@pytest.fixture()
def driver_init(request):
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    request.cls.driver = driver  # assign driver to class using the fixture
    yield
    driver.close()
