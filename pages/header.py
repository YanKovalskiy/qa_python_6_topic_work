import allure

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'LogoYandex')]"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'LogoScooter')]"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"

    DZEN_SEARCH_BUTTON = By.XPATH, "//button[@class ='dzen-search-arrow-common__button']"

    def __init__(self, web_drv):
        super().__init__(web_drv)

    def click_button_order(self):
        with allure.step("Нажимаем кнопку 'Заказать' в шапке сайта"):
            self.click_by_element(self.BUTTON_ORDER)

    def click_logo_yandex(self):
        self.click_by_element(self.LOGO_YANDEX)

    def click_logo_scooter(self):
        self.click_by_element(self.LOGO_SCOOTER)

    def wait_dzen_button_search(self):
        self.wait_visible_element(self.DZEN_SEARCH_BUTTON, timeout=30)
