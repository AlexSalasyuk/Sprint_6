from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class FaqPage:
    def __init__(self, driver):
        self.driver = driver

    def get_question_locator(self, index):
        return (By.ID, f'accordion__heading-{index}')

    def get_answer_locator(self, index):
        return (By.ID, f'accordion__panel-{index}')

    def click_question(self, index):
        locator = self.get_question_locator(index)
        question = WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', question)
        self.driver.execute_script('arguments[0].click();', question)

    def wait_for_answer_visible(self, index):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.get_answer_locator(index)))

    def get_answer_text(self, index):
        answer_element = self.wait_for_answer_visible(index)
        return answer_element.text
