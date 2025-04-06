from locators.order_page_locators import *
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step('Кликнуть по кнопке "Заказать" в {position}')
    def click_order_button(self, position='top'):
        if position == 'top':
            locator = OrderPageLocators.ORDER_BUTTON_TOP
        else:
            locator = OrderPageLocators.ORDER_BUTTON_BOTTOM
        button = self.find(locator)
        self.scroll_to(locator)
        self.click(locator)

    @allure.step('Заполнить информацию о заказчике: {first_name} {last_name}')
    def fill_customer_info(self, first_name, last_name, address, metro_station, phone):
        self.enter_text(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        self.enter_text(OrderPageLocators.LAST_NAME_INPUT, last_name)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.enter_text(OrderPageLocators.METRO_STATION_INPUT, metro_station)
        self.click(OrderPageLocators.METRO_STATION_DROPDOWN)
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить информацию об аренде: {delivery_day}, срок: {rent_duration}, цвет: {color}')
    def fill_rent_info(self, delivery_day, rent_duration, color, comment):
        self.click(OrderPageLocators.DELIVERY_DATE_INPUT)
        day_locator = (By.XPATH, f'//div[contains(@class, "react-datepicker__day") and text()="{delivery_day}"]')
        self.click(day_locator)
        self.click(OrderPageLocators.RENT_INPUT)
        rent_options = self.driver.find_elements(*OrderPageLocators.RENT_DROPDOWN)
        if rent_duration < len(rent_options):
            rent_options[rent_duration].click()
        else:
            rent_options[0].click()

        if color == 'black':
            self.click(OrderPageLocators.SCOOTER_COLOR_BLACK)
        elif color == 'grey':
            self.click(OrderPageLocators.SCOOTER_COLOR_GRAY)

        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)
        self.click(OrderPageLocators.ORDER_CONFIRM_BUTTON_BOTTOM)
        self.click(OrderPageLocators.ORDER_YES_BUTTON)

    @allure.step('Проверить, что заказ успешно оформлен')
    def is_order_successful(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)

    @allure.step('Кликнуть по кнопке "Статус заказа"')
    def click_view_status_button(self):
        self.click(OrderPageLocators.VIEW_STATUS_BUTTON)

    @allure.step('Кликнуть по логотипу Самоката')
    def click_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step('Кликнуть по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(OrderPageLocators.YANDEX_LOGO)

