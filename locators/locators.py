from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'LogoYandex')]"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'LogoScooter')]"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"


class MainPageLocators:
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button"


class OrderPageLocators:
    INPUT_FIELD_NAME = By.XPATH, "//input[contains(@placeholder, 'Имя')]"
    INPUT_FIELD_LASTNAME = By.XPATH, "//input[contains(@placeholder, 'Фамилия')]"
    INPUT_FIELD_ADDRESS = By.XPATH, "//input[contains(@placeholder,'Адрес')]"
    INPUT_FIELD_METRO = By.XPATH, "//input[contains(@class,'select-search')]"
    INPUT_FIELD_PHONE = By.XPATH, "//input[contains(@placeholder,'Телефон')]"
    BUTTON_NEXT = By.XPATH, "//button[text()='Далее']"

    SELECT_FIELD_DATE = By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]"
    SELECT_FIELD_RENTAL_PERIOD = By.XPATH, "//div[@class='Dropdown-control']"
    CHECKBOX_ITEM_BLACK = By.ID, 'black'
    CHECKBOX_ITEM_GRAY = By.ID, 'grey'
    INPUT_FIELD_COMMENT = By.XPATH, "//input[contains(@placeholder,'Комментарий')]"

    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"
    BUTTON_YES = By.XPATH, "//button[text()='Да']"

    TEXT_HEADER_ORDER_PLACED = By.XPATH, "//*[contains(@class, 'Order_ModalHeader')]"
