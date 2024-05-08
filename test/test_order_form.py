import allure
import pytest
import time

from pages.order_page import OrderPage
from pages.main_page import MainPage
from data import DATA_SET


@allure.title('Проверка формы заказа самоката')
@allure.description('Позитивный сценарий проверки формы заказа самоката')
@pytest.mark.parametrize(
    'point_of_entry, client_data, rent_data',
    (
            ('Main', DATA_SET[0][0], DATA_SET[0][1]),
            ('Header', DATA_SET[1][0], DATA_SET[1][1])
    )
)
def test_(web_drv, point_of_entry, client_data, rent_data):
    mp = MainPage(web_drv)
    if point_of_entry == 'Main':
        mp.click_button_order()
    elif point_of_entry == 'Header':
        mp.click_button_order_in_header()

    op = OrderPage(web_drv)
    op.fill_section_about_client(*client_data)
    op.fill_section_about_rent(*rent_data)

    time.sleep(3)



