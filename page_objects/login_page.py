from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from utilities.utilities import loggen, ScreeShots 

class LoginPage:
    # locators
    input_email_id = "email"
    input_pwd_id = "password"
    btn_login_id = "loginButton"

    def __init__(self, driver, logger):
        # Initialize WebDriver, WebDriverWait, Screenshots, and Logger
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 2)
        self.SS = ScreeShots(self.driver)
        self.logger = logger

    def _handle_logger(self, info):
        # Log information messages
        browser_name = self.driver.capabilities['browserName']
        self.logger.info(f"{browser_name} :: {info}")

    # Actions
    def enter_email(self, email):
        """
        Enters the provided email into the email input field
        """
        self._handle_logger("Attempting to enter email.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.input_email_id))).send_keys(email)
        self._handle_logger("Email entered.")

    def enter_password(self, password):
        """
        Enters the provided password into the password input field
        """
        self._handle_logger("Attempting to enter password.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.input_pwd_id))).send_keys(password)
        self._handle_logger("Password entered.")

    def click_login_button(self):
        """
        Clicks the login button
        """
        self._handle_logger("Attempting to click login button.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_login_id))).click()
        self._handle_logger("Login button clicked.")

    def get_user_credentials(self):
        """
        Retrieves user credentials from a JSON file
        """
        self._handle_logger("Attempting to get user credentials from file.")
        with open('test_data/new-user.json') as file:
            credentials = json.load(file)
        email = credentials['email']
        password = credentials['password']
        self._handle_logger("User credentials retrieved.")
        return email, password

    def user_login(self, email, password):
        """
        Logs in using the provided email and password
        """
        self._handle_logger("Attempting to log in with provided email and password.")
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        self._handle_logger("Login attempted with provided credentials.")


    def user_login_with_saved_credentials(self):
        """
        Logs in using credentials saved in a JSON file
        """
        self._handle_logger("Attempting to log in with saved credentials.")
        email, password = self.get_user_credentials()
        self.user_login(email, password)
        self._handle_logger("Login attempted with saved credentials.")
