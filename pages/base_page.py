from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.step('Кликнуть по элементу')
    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    @allure.step('Ввести текст: {text}')
    def enter_text(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.send_keys(text)

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator)).text

    @allure.step('Проверить видимость элемента')
    def is_visible(self, locator):
        return self.wait.until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Найти элемент')
    def find(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Скроллить к элементу')
    def scroll_to(self, locator):
        element = self.wait.until(expected_conditions.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    @allure.step('Переключить на новую вкладку')
    def switch_to_new_tab(self):
        self.wait.until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Получить текущий URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Проверить, что текущий URL равен {url}')
    def is_current_url(self, url):
        return self.driver.current_url == url

    @allure.step('Проверить, что текущий URL начинается с {prefix}')
    def is_current_url_startswith(self, prefix):
        return self.driver.current_url.startswith(prefix)

    @allure.step('Ждать, что текущий URL начинается с {prefix}')
    def wait_until_url_starts_with(self, prefix, timeout=10):
        self.wait.until(lambda driver: driver.current_url.startswith(prefix))
