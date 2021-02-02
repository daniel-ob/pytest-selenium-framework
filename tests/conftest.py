"""
Fixtures into a separate file to share them between multiple test modules in the directory
"""
from datetime import datetime
import os

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.maximize_window()
    request.cls.driver = driver  # assign driver to class using the fixture
    yield
    # Teardown code after the yield
    driver.close()


# Add URL and Screenshot (only on test fail) to pytest-html report
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        # always add url to report
        request = item.funcargs['request']
        driver = request.cls.driver
        extra.append(pytest_html.extras.url(driver.current_url))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add screenshot on failure
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            working_directory = os.getcwd()
            image_file = working_directory+'/reports/screenshot_'+timestamp+'.png'
            driver.save_screenshot(image_file)
            extra.append(pytest_html.extras.image(image_file))
        report.extra = extra
