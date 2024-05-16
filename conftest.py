import pytest

from selenium import webdriver
from config import URL

from pages.header import Header
from pages.main_page import MainPage
from pages.order_page import OrderPage

def pytest_make_parametrize_id(val):
    return repr(val)


@pytest.fixture()
def web_drv():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(URL)

    yield driver

    driver.quit()


@pytest.fixture()
def header(web_drv):
    return Header(web_drv)


@pytest.fixture()
def main_page(web_drv):
    return MainPage(web_drv)


@pytest.fixture()
def order_page(web_drv):
    return OrderPage(web_drv)
