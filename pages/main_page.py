import allure

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait as WDWait
from selenium.webdriver.common.by import By


class MainPage:
    LAST_QUESTION = By.XPATH, f"//div[@id='accordion__heading-7']"

    def __init__(self, web_drv):
        self.web_drv = web_drv
        self.wait = WDWait(self.web_drv, 30)

    @allure.step('Прокрутка конца экрана')
    def scroll_to_last_question(self):
        last_question_element = self.wait.until(ec.visibility_of_element_located(self.LAST_QUESTION))
        self.web_drv.execute_script("arguments[0].scrollIntoView();", last_question_element)

    @allure.step('Нажимаем на проверяемый элемент списка')
    def click_question_by_index(self, question_index):
        question = By.XPATH, f"//div[@id='accordion__heading-{question_index}']"
        self.wait.until(ec.element_to_be_clickable(question)).click()

    @allure.step('Получаем текст ответа')
    def get_answer_text_by_question_index(self, question_index):
        self.scroll_to_last_question()
        self.click_question_by_index(question_index)
        answer = By.XPATH, f"//div[@id='accordion__panel-{question_index}']/p"
        return self.wait.until(ec.visibility_of_element_located(answer)).text
