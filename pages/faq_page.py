from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure

class FaqPage(BasePage):
    @allure.step('Получить локатор вопроса №{index}')
    def get_question_locator(self, index):
        return (By.ID, f'accordion__heading-{index}')

    @allure.step('Получить локатор ответа на вопрос №{index}')
    def get_answer_locator(self, index):
        return (By.ID, f'accordion__panel-{index}')

    @allure.step('Скроллить и кликнуть по вопросу №{index}')
    def click_question(self, index):
        locator = self.get_question_locator(index)
        self.scroll_to(locator)
        element = self.find(locator)
        self.driver.execute_script('arguments[0].click();', element)

    @allure.step('Ждать появления ответа на вопрос №{index}')
    def wait_for_answer_visible(self, index):
        return self.is_visible(self.get_answer_locator(index))

    @allure.step('Получить текст ответа на вопрос №{index}')
    def get_answer_text(self, index):
        locator = self.get_answer_locator(index)
        return self.get_text(locator)
