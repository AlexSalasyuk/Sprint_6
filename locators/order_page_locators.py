from selenium.webdriver.common.by import By

class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]//button[text()="Заказать"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]//button[text()="Заказать"]')

    # Поля формы "Для кого самокат"
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_DROPDOWN = (By.CLASS_NAME, 'select-search__option')
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    # Поля формы "Про аренду"
    DELIVERY_DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    DATE_PICKER_DAY = (By.XPATH, '//div[contains(@class, "react-datepicker__day") and not(contains(@class, "outside-month")) and text()="15"]')
    RENT_INPUT = (By.CLASS_NAME, 'Dropdown-control')
    RENT_DROPDOWN = (By.CLASS_NAME, 'Dropdown-option')
    SCOOTER_COLOR_BLACK = (By.ID, 'black')
    SCOOTER_COLOR_GRAY = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_CONFIRM_BUTTON_BOTTOM = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]//button[text()="Заказать"]')
    ORDER_YES_BUTTON = (By.XPATH, '//button[text()="Да"]')

    # Окно подтверждения заказа
    SUCCESS_MODAL = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    VIEW_STATUS_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

    # Кнопки логотипов
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')
