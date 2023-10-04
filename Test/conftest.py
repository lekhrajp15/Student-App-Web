import pytest
from selenium import webdriver
import time

from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.service import Service



def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="Specify the browser name")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser_name")

@pytest.fixture
def setup(request, browser):
    global driver
    if browser == "chrome":
        obj = Service('/Users/lekhraj/PycharmProjects/EmbibeFramework/browsers driver/chromedriver')
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        driver = webdriver.Chrome(service=obj, options=chrome_options)
    elif browser == "edge":
        obj = Service('/Users/lekhraj/PycharmProjects/EmbibeFramework/browsers driver/msedgedriver')
        edge_options = EdgeOptions()
        edge_options.add_argument('--disable-notifications')
        driver = webdriver.Edge(service=obj, options=edge_options)

    driver.get("https://www.embibe.com")
    driver.maximize_window()
    driver.implicitly_wait(20)

    request.cls.driver = driver
    yield driver
    driver.quit()



# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item):
#     """
#         Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
#         :param item:
#         """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             file_name = report.nodeid.replace("::", "_") + ".png"
#             _capture_screenshot(file_name)
#             if file_name:
#                 html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
#
# def _capture_screenshot(name):
#         driver.get_screenshot_as_file(name)

