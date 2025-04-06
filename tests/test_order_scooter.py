import pytest
from pages.order_page import OrderPage
from data.order_test_data import ORDER_DATA_SET
from urls import *
import allure

@allure.title('Проверить оформление заказа с данными из набора и переход по логотипам')
@pytest.mark.parametrize('data', ORDER_DATA_SET)
def test_order_flow(driver, data):
    page = OrderPage(driver)

    with allure.step('Нажать кнопку "Заказать"'):
        page.click_order_button(position=data['button_position'])

    with allure.step('Заполнить данные пользователя'):
        page.fill_customer_info(
            first_name=data['first_name'],
            last_name=data['last_name'],
            address=data['address'],
            metro_station=data['metro_station'],
            phone=data['phone'])

    with allure.step('Заполнить данные аренды и подтвердить заказ'):
        page.fill_rent_info(
            delivery_day=data['delivery_day'],
            rent_duration=data['rent_duration'],
            color=data['color'],
            comment=data['comment'])
        assert page.is_order_successful()

    with allure.step('Перейти по кнопке "Статус заказа" и логотипу Самоката'):
        page.click_view_status_button()
        page.click_scooter_logo()
        assert page.is_current_url(BASE_URL)

    with allure.step('Перейти по логотипу Яндекса в новую вкладку'):
        page.click_yandex_logo()
        page.switch_to_new_tab()
        page.wait_until_url_starts_with(YANDEX_URL)
        assert page.is_current_url_startswith(YANDEX_URL)

