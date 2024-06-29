import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type of browser. Default is chrome.")

@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def setup(request, browser):
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

