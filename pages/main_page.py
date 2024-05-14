import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    LAST_QUESTION = By.XPATH, "//div[@id='accordion__heading-7']"
    BUTTON_ORDER = By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button"

    def __init__(self, web_drv):
        super().__init__(web_drv)

    def click_question_by_index(self, question_index):
        with allure.step('Нажимаем на проверяемый элемент списка'):
            question = By.XPATH, f"//div[@id='accordion__heading-{question_index}']"
            self.click_by_element(question)

    def get_answer_text_by_question_index(self, question_index):
        with allure.step('Прокручиваем страницу до последнего вопроса'):
            self.scroll_to_element(self.LAST_QUESTION)

        self.click_question_by_index(question_index)

        with allure.step('Получаем текст ответа'):
            answer = By.XPATH, f"//div[@id='accordion__panel-{question_index}']/p"
            return self.get_element_text(answer)

    def click_button_order(self):
        with allure.step("Прокручиваем страницу до кнопки 'Заказать' на главной странице"):
            self.scroll_to_element(self.BUTTON_ORDER)
        with allure.step("Нажимаем на кнопку"):
            self.click_by_element(self.BUTTON_ORDER)
