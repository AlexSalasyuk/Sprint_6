import pytest
from pages.order_page import OrderPage
from data.order_test_data import ORDER_DATA_SET
from urls import *
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.parametrize('data', ORDER_DATA_SET)
def test_order_flow(driver, data):
    page = OrderPage(driver)
    page.click_order_button(position=data['button_position'])
    page.fill_customer_info(
        first_name=data['first_name'],
        last_name=data['last_name'],
        address=data['address'],
        metro_station=data['metro_station'],
        phone=data['phone']
    )
    page.fill_rent_info(
        delivery_day=data['delivery_day'],
        rent_duration=data['rent_duration'],
        color=data['color'],
        comment=data['comment']
    )
    assert page.is_order_successful()

    page.click_view_status_button()
    page.click_scooter_logo()
    WebDriverWait(driver, 5).until(lambda d: d.current_url == BASE_URL)
    assert driver.current_url == BASE_URL

    page.click_yandex_logo()
    page.switch_to_new_tab()
    WebDriverWait(driver, 10).until(lambda d: d.current_url.startswith(YANDEX_URL))
    assert driver.current_url.startswith(YANDEX_URL)
