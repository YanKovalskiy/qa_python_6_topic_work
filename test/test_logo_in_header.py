import allure
from config import URL


@allure.title('Проверка нажатия на логотип Яндекс')
def test_click_logo_yandex(web_drv, header):
    with allure.step('Нажимаем на логотип Яндекс'):
        header.click_logo_yandex()
    with allure.step('Переходим в новое окно'):
        header.switch_to_new_window()
        header.wait_dzen_button_search()
    assert 'dzen.ru' in header.current_url


@allure.title('Проверка нажатия на логотип Самокат')
def test_click_logo_scooter(web_drv, header):
    with allure.step(f'Переходим на страницу {URL}/order'):
        header.open_page(f'{URL}/order')
    with allure.step('Нажимаем на логотип Самокат'):
        header.click_logo_scooter()
    assert f'{URL}/' == header.current_url
