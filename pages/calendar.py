from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Calendar(BasePage):
    BUTTON_NEXT_MONTH = By.XPATH, "//button[contains(@class, 'next')]"
    MONTH_GRID = By.XPATH, "//div[@class='react-datepicker__month']"

    MONTHS = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря'
    }

    def __init__(self, web_drv):
        super().__init__(web_drv)

    def set_month(self, date):
        month = f'0{date.month}' if date.month < 10 else str(date.month)
        year = str(date.year)

        while True:
            str_month_year = self.get_attribute_element(self.MONTH_GRID, attribute='aria-label')
            current_month = str_month_year[-2:14]
            current_year = str_month_year[-7:11]
            if current_month == month and current_year == year:
                break
            else:
                self.click_by_element(self.BUTTON_NEXT_MONTH)

    def select_date(self, date):
        self.set_month(date)
        day_locator = By.XPATH, f"//div[contains(@aria-label,' {date.day}-е {self.MONTHS[date.month]} {date.year}')]"
        self.click_by_element(day_locator)
