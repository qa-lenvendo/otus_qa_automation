import pytest
from fixture.ui import UserInterface
from fixture.test_data import TestData


@pytest.fixture(scope='function')
def ui(request):
    base_url = request.config.getoption('--base_url')
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('headless')
    test_name = request.node.name
    log_level = request.config.getoption("--log_level")
    mode = request.config.getoption('--mode')
    hub = request.config.getoption('--hub')
    port = request.config.getoption('--hub_port')

    ui = UserInterface(base_url=base_url, browser_name=browser_name, headless=headless, test_name=test_name,
                       log_level=log_level, mode=mode, hub=hub, port=port)

    ui.log_level = log_level

    yield ui

    ui.close()


@pytest.fixture(scope="function")
def test_data(request):
    test_data = TestData()

    yield test_data


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='http://192.168.3.107:8081', help='stage url')
    parser.addoption('--browser_name', action='store', default='chrome', help='choose browser')
    parser.addoption('--headless', action='store', default='true', help='choose browser')
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption('--mode', action='store', default='local', help='Choose local or remote mode')
    parser.addoption('--hub', action='store', default='192.168.3.107', help='Choose hub host')
    parser.addoption('--hub_port', action='store', default='4444', help='Choose hub port')
