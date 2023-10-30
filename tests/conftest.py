"""
Fixtures into a separate file to share them between multiple test modules in the directory
"""
import pytest
import pytest_html
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    if request.param == "firefox":
        driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver
    yield
    # Teardown after the test
    driver.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add URL and screenshot (only on Fail) to html report"""
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        request = item.funcargs["request"]
        driver = request.cls.driver
        extras.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            screenshot = driver.get_screenshot_as_base64()
            extras.append(pytest_html.extras.image(screenshot, ""))
        report.extras = extras
