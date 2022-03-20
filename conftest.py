import pytest
from fixture.ui import UserInterface
from fixture.test_data import TestData


@pytest.fixture(scope='function')
def ui(request):
    base_url = request.config.getoption('--base_url')
    browser_name = request.config.getoption('--browser_name')
    headless = request.config.getoption('headless')

    ui = UserInterface(base_url=base_url, browser_name=browser_name, headless=headless)

    yield ui

    ui.close()


@pytest.fixture(scope="function")
def test_data(request):
    test_data = TestData()

    yield test_data


def pytest_addoption(parser):
    parser.addoption('--base_url', action='store', default='http://192.168.3.107:8081/', help='stage url')
    parser.addoption('--browser_name', action='store', default='chrome', help='choose browser')
    parser.addoption('--headless', action='store', default='true', help='choose browser')
