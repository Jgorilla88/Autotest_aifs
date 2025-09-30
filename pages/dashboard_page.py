from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    # --- Locators ---
    ASSISTANT_IFRAME = (
        By.CSS_SELECTOR, "iframe[src*='embed.aifromspace.com']")
    ASSISTANT_HEADER = (
        By.XPATH, "//*[normalize-space()='QA Testing Assistant']")

    # --- Actions ---
    def __init__(self, driver):
        self.driver = driver
        # Создаем объект ожидания прямо здесь для удобства
        self.wait = WebDriverWait(self.driver, 10)

    def switch_to_assistant_iframe(self):
        """Ожидает iframe и переключается на него."""
        self.wait.until(
            EC.frame_to_be_available_and_switch_to_it(self.ASSISTANT_IFRAME)
        )

    def get_assistant_header(self):
        """Ожидает и возвращает элемент заголовка ассистента."""
        return self.wait.until(
            EC.visibility_of_element_located(self.ASSISTANT_HEADER)
        )

    def wait_for_url_contain(self, text):
        '''Проверяет содержит ли адрес текст'''
        return self.wait.until(
            EC.url_contains(text)
        )
