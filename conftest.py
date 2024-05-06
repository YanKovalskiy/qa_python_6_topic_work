import pytest
import allure

from selenium import webdriver
from config import URL


def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture()
def web_drv():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()
