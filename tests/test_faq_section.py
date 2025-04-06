import pytest
from pages.faq_page import FaqPage
import allure

@allure.title('Проверить открытие ответа на вопрос №{index}')
@pytest.mark.parametrize('index', list(range(8)))
def test_faq_question_has_visible_answer(driver, index):
    page = FaqPage(driver)
    page.click_question(index)
    text = page.get_answer_text(index)
    assert text.strip() != ''
