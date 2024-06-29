
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


driver = None

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. Default is chrome.")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(request, browser):
    global driver
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument('--disable-notifications')
        driver = webdriver.Edge(options=edge_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Browser {browser} is not supported.")

    driver.get("https://www.embibe.com")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver

    yield driver
    driver.quit()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)


