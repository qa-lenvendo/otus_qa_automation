import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('--browser_name')
    if browser_name == 'chrome':
        options = webdriver.ChromeOptions()
        if request.config.getoption('headless') == 'true':
            options.add_argument('--headless')
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=options,
            desired_capabilities=options.to_capabilities()
        )
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        if request.config.getoption('headless') == 'true':
            options.add_argument('--headless')
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(),
            options=options,
            desired_capabilities=options.to_capabilities()
        )
    elif browser_name == 'opera':
        options = webdriver.ChromeOptions()
        if request.config.getoption('headless') == 'true':
            options.add_argument('--headless')
        driver = webdriver.Opera(
            executable_path=OperaDriverManager().install(),
            options=options,
            desired_capabilities=options.to_capabilities()
        )
    else:
        raise AssertionError(f'Unknown browser: {browser_name}')

    driver.set_window_size(1920, 1080)

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def base_url(request):
    return request.config.getoption('--base_url')


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='http://192.168.3.107:8081/', help='stage url')
    parser.addoption('--browser_name', action='store', default='chrome', help='choose browser')
    parser.addoption('--headless', action='store', default='true', help='choose browser')
