import allure
import pytest

from data import ORDER_DATA_SET


@allure.title('Проверка формы заказа самоката')
@allure.description('Позитивный сценарий проверки формы заказа самоката')
@pytest.mark.parametrize(
    'point_of_entry, data_set',
    (
            ('Main', ORDER_DATA_SET[0]),
            ('Header', ORDER_DATA_SET[1])
    )
)
def test_oder_form(web_drv, header, main_page, order_page, point_of_entry, data_set):

    if point_of_entry == 'Main':
        main_page.click_button_order()
    elif point_of_entry == 'Header':
        header.click_button_order()

    order_page.fill_order_form(*data_set)
    order_page.click_button_yes_in_confirmation_window()
    assert 'Заказ оформлен' in order_page.get_header_text_in_success_window()
