from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def click_order_button(self, position='top'):
        if position == 'top':
            locator = OrderPageLocators.ORDER_BUTTON_TOP
        else:
            locator = OrderPageLocators.ORDER_BUTTON_BOTTOM

        button = WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView();', button)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator)).click()

    def fill_customer_info(self, first_name, last_name, address, metro_station, phone):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        metro_input = self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT)
        metro_input.send_keys(metro_station)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(OrderPageLocators.METRO_STATION_DROPDOWN)).click()
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_rent_info(self, delivery_day, rent_duration, color, comment):
        self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_INPUT).click()
        day_locator = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and text()="{delivery_day}"]')
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(day_locator)).click()
        self.driver.find_element(*OrderPageLocators.RENT_INPUT).click()
        rent_options = self.driver.find_elements(*OrderPageLocators.RENT_DROPDOWN)
        if rent_duration < len(rent_options):
            rent_options[rent_duration].click()
        else:
            rent_options[0].click()

        if color == 'black':
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_BLACK).click()
        elif color == 'grey':
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GRAY).click()

        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        self.driver.find_element(*OrderPageLocators.ORDER_CONFIRM_BUTTON_BOTTOM).click()
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(OrderPageLocators.ORDER_YES_BUTTON)).click()

    def is_order_successful(self):
        return WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderPageLocators.SUCCESS_MODAL))

    def click_view_status_button(self):
        self.driver.find_element(*OrderPageLocators.VIEW_STATUS_BUTTON).click()

    def click_scooter_logo(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*OrderPageLocators.YANDEX_LOGO).click()

    def switch_to_new_tab(self):
        WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)

    def get_current_url(self):
        return self.driver.current_url
