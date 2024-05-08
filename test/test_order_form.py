import allure
import pytest

from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.header import Header
from data import DATA_SET


@allure.title('Проверка формы заказа самоката')
@allure.description('Позитивный сценарий проверки формы заказа самоката')
@pytest.mark.parametrize(
    'point_of_entry, data_set',
    (
            ('Main', DATA_SET[0]),
            ('Header', DATA_SET[1])
    )
)
def test_oder_form(web_drv, point_of_entry, data_set):

    if point_of_entry == 'Main':
        main_page = MainPage(web_drv)
        main_page.click_button_order()
    elif point_of_entry == 'Header':
        header = Header(web_drv)
        header.click_button_order()

    order_page = OrderPage(web_drv)
    order_page.fill_order_form(*data_set)
