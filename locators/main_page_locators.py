from selenium.webdriver.common.by import By


class MainPageLocators:
    LAST_QUESTION = By.XPATH, "//div[@id='accordion__heading-7']"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button"
