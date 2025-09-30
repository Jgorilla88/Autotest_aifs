from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:
    # -- All lockators --
    email_input = (By.ID, 'email')
    password_input = (By.ID, 'password')
    login_button = (By.CSS_SELECTOR, 'button[type="submit"]')
    error_message = (By.XPATH, '//*[contains(., "Invalid email or password")]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Open page

    def open(self):
        self.driver.get('https://app.aifromspace.com/')

    def enter_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def get_error_message(self, error_text):
        return self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f'//*[contains(., "{error_text}")]')
            ))
        pass
