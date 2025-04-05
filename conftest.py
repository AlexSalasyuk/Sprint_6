import pytest
from selenium import webdriver
from urls import BASE_URL

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()