import allure

from selenium.webdriver.common.by import By
from locators.locators import OrderPageLocators as OrdPL
from pages.base_page import BasePage
from pages.header import Header


class OrderPage(BasePage):
    def __init__(self, web_drv):
        super().__init__(web_drv)

    def fill_field_name(self, name):
        with allure.step("Заполняем поле 'Имя'"):
            self.fill_field(OrdPL.INPUT_FIELD_NAME, name)

    def fill_field_last_name(self, last_name):
        with allure.step("Заполняем поле 'Фамилия'"):
            self.fill_field(OrdPL.INPUT_FIELD_LASTNAME, last_name)

    def fill_field_address(self, address):
        with allure.step("Заполняем поле 'Адрес'"):
            self.fill_field(OrdPL.INPUT_FIELD_ADDRESS, address)

    def select_metro_station(self, name_metro_station):
        with allure.step("Выбираем станцию метро в поле выбора 'Станция метро'"):
            self.fill_field(OrdPL.SELECT_FIELD_METRO, name_metro_station)
            item_list_locator = By.XPATH, f"//*[text()='{name_metro_station}']"
            self.click_by_element(item_list_locator)

    def fill_field_phone(self, phone):
        with allure.step("Заполняем поле 'Телефон'"):
            self.fill_field(OrdPL.INPUT_FIELD_PHONE, phone)

    def click_button_next(self):
        with allure.step("Нажимаем кнопку 'Далее'"):
            self.click_by_element(OrdPL.BUTTON_NEXT)

    def fill_section_about_client(self, name, last_name, address, name_metro_station, phone):
        with allure.step("Заполняем форму заказа, раздел о клиенте"):
            self.fill_field_name(name)
            self.fill_field_last_name(last_name)
            self.fill_field_address(address)
            self.select_metro_station(name_metro_station)
            self.fill_field_phone(phone)
            self.click_button_next()

    def select_date_scooter_delivery(self, rental_date):
        with allure.step("Выбираем дату доставки самоката"):
            pass

    def select_rental_period(self, period):
        with allure.step("Выбираем период аренды"):
            self.click_by_element(OrdPL.SELECT_FIELD_RENTAL_PERIOD)
            item_list_locator = By.XPATH, f"//*[text()='{period}']"
            self.click_by_element(item_list_locator)

    def select_color_scooter(self, scooter_color):
        with allure.step("Выбираем цвет самоката"):
            if scooter_color[0]:
                self.click_by_element(OrdPL.CHECKBOX_ITEM_BLACK)
            if scooter_color[1]:
                self.click_by_element(OrdPL.CHECKBOX_ITEM_GRAY)

    def fill_field_comment(self, comment):
        with allure.step("Заполняем поле 'Комментарий'"):
            self.fill_field(OrdPL.INPUT_FIELD_COMMENT, comment)

    def fill_section_about_rent(self, rental_date, period, scooter_color, comment):
        with allure.step("Заполняем форму заказа, раздел об аренде"):
            self.select_date_scooter_delivery(rental_date)
            self.select_rental_period(period)
            self.select_color_scooter(scooter_color)
            self.fill_field_comment(comment)
            header = Header(self.web_drv)
            header.click_button_order()

    def fill_order_form(self, name, last_name, address, name_metro_station, phone,
                        rental_date, period, scooter_color, comment):
        self.fill_section_about_client(name, last_name, address, name_metro_station, phone)
        self.fill_section_about_rent(rental_date, period, scooter_color, comment)
