from selenium.webdriver.common.by import By


class CalendarLocators:
    BUTTON_NEXT_MONTH = By.XPATH, "//button[contains(@class, 'next')]"
    MONTH_GRID = By.XPATH, "//div[@class='react-datepicker__month']"
