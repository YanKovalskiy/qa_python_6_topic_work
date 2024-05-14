from selenium.webdriver.common.by import By


class HeaderLocators:
    LOGO_YANDEX = By.XPATH, "//a[contains(@class, 'LogoYandex')]"
    LOGO_SCOOTER = By.XPATH, "//a[contains(@class, 'LogoScooter')]"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']"
