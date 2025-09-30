import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# --- Фикстура для управления браузером ---


# @pytest.fixture
# def driver():
#     browser = webdriver.Chrome()
#     yield browser
#     browser.quit()

# --- Тест №1: Вход с верным паролем (Happy Path) ---


def test_successful_login(driver):
    '''Проверяет правильный пароль и почту'''
    wait = WebDriverWait(driver, 10)

    login_page = LoginPage(driver)
    dashboard_page = DashboardPage(driver)
# __acting__
    login_page.open()
    login_page.login('aifstesters@gmail.com', 'Aifromspace1')
# __assert__
    dashboard_page.wait_for_url_contain('dashboard')

    dashboard_page.switch_to_assistant_iframe()
    assistant_header = dashboard_page.get_assistant_header()

    assert assistant_header.is_displayed()
    print("\nТест на успешный вход ПРОЙДЕН.")

# --- Тест №2: Вход с неверным паролем (Sad Path) ---


@pytest.mark.parametrize(
    "password, error_text",
    [
        ('WrongPass123', "Invalid email or password"),
        ('aifromspace1', "Invalid email or password")]
)
def test_failed_wrong_password(driver, password, error_text):
    '''Проверяет неправильный пароль.'''
    wait = WebDriverWait(driver, 10)

    login_page = LoginPage(driver)

    login_page.open()
    login_page.login('aifstesters@gmail.com', password)

    # Assert
    # Проверяем тот текст ошибки, который ожидаем для этого набора данных
    error_message = login_page.get_error_message(error_text)

    assert error_message.is_displayed()
    print("\nТест на провальный вход ПРОЙДЕН.")

# --- НОВЫЙ ТЕСТ №3: Проверка браузерной валидации на пустое поле ---


def test_empty_password_field_browser_validation(driver):
    '''Проверяет пустой пароль'''
    login_page = LoginPage(driver)
    login_page.open()

    # Arrange: Находим поле пароля, но ничего в него не вводим
    password_field = driver.find_element(*login_page.password_input)

    # Act: Выполняем JavaScript, чтобы проверить свойство 'validity'
    # Мы передаем элемент password_field в скрипт как arguments[0]
    is_invalid_because_empty = driver.execute_script(
        "return arguments[0].validity.valueMissing;",
        password_field
    )

    # Assert: Проверяем, что браузер вернул True
    assert is_invalid_because_empty is True
    print("\nТест на браузерную валидацию ПРОЙДЕН.")
