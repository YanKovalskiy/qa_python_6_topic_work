import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def click_question_by_index(self, question_index):
        with allure.step('Нажимаем на проверяемый элемент списка'):
            question = By.XPATH, f"//div[@id='accordion__heading-{question_index}']"
            self.click_by_element(question)

    def get_answer_text_by_question_index(self, question_index):
        with allure.step('Прокручиваем страницу до последнего вопроса'):
            self.scroll_to_element(MainPageLocators.LAST_QUESTION)

        self.click_question_by_index(question_index)

        with allure.step('Получаем текст ответа'):
            answer = By.XPATH, f"//div[@id='accordion__panel-{question_index}']/p"
            return self.get_element_text(answer)

    def click_button_order(self):
        with allure.step("Прокручиваем страницу до кнопки 'Заказать' на главной странице"):
            self.scroll_to_element(MainPageLocators.BUTTON_ORDER)
        with allure.step("Нажимаем на кнопку"):
            self.click_by_element(MainPageLocators.BUTTON_ORDER)
