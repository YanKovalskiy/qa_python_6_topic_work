import allure

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators
from locators.external_locators import YandexPageLocators


class Header(BasePage):

    def click_button_order(self):
        with allure.step("Нажимаем кнопку 'Заказать' в шапке сайта"):
            self.click_by_element(HeaderLocators.BUTTON_ORDER)

    def click_logo_yandex(self):
        self.click_by_element(HeaderLocators.LOGO_YANDEX)

    def click_logo_scooter(self):
        self.click_by_element(HeaderLocators.LOGO_SCOOTER)

    def wait_dzen_button_search(self):
        self.wait_visible_element(YandexPageLocators.DZEN_SEARCH_BUTTON, timeout=30)
