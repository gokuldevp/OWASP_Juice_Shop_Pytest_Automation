from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.utilities import ScreeShots

class HomePage:
    # Locators
    btn_welcome_popup_dismiss_xpath = "//button[@aria-label='Close Welcome Banner']"
    btn_cookie_popup_dismiss_xpath = "//a[@aria-label='dismiss cookie message']"
    btn_account_id = "navbarAccount"
    home_login_button_id = "navbarLoginButton"
    btn_orders_payment_xpath = "//button[@aria-label='Show Orders and Payment Menu']"
    btn_my_payment_option_xpath = "//button[@aria-label='Go to saved payment methods page']"

    # urls
    payment_page_url = "http://localhost:3000/#/saved-payment-methods"

    def __init__(self, driver, logger):
        # Initialize WebDriver, WebDriverWait, Screenshots, and Logger
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 2)
        self.SS = ScreeShots(self.driver)
        self.logger = logger

    # Actions
    def _handle_logger(self, info):
        # Log information messages
        browser_name = self.driver.capabilities['browserName']
        self.logger.info(f"{browser_name} :: {info}")

    def dismiss_welcome_message(self):
        """
        Dismisses the welcome message popup 
        """
        self._handle_logger("Attempting to dismiss welcome message.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_welcome_popup_dismiss_xpath))).click()
        self._handle_logger("Welcome message dismissed.")

    def dismiss_cookie_message(self):
        """
        Dismisses the cookie message popup
        """
        self._handle_logger("Attempting to dismiss cookie message.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_cookie_popup_dismiss_xpath))).click()
        self._handle_logger("cookie message dismissed.")


    def click_account_button(self):
        """
        Clicks on the account button on the Navbar
        """
        self._handle_logger("Attempting to click account button.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_account_id))).click()
        self._handle_logger("Account button clicked.")

    def click_login_button(self):
        """
        Clicks on the login button on the Navbar -> Account -> Login
        """
        self._handle_logger("Attempting to click login button.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.home_login_button_id))).click()
        self._handle_logger("Login button clicked.")

    def navigate_to_login_page(self):
        """
        Navigate to Login page
        """
        self.dismiss_welcome_message()
        self.dismiss_cookie_message()
        self.click_account_button()
        self.click_login_button()
        self._handle_logger("Navigated to login page.")

    def click_orders_and_payment_button(self):
        """
        Clicks on the order and payment button on the Navbar -> Account -> order and payment
        """
        self._handle_logger("Attempting to click orders and payment button.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_orders_payment_xpath))).click()
        self._handle_logger("Orders and payment button clicked.")

    def click_my_payment_option_button(self):
        """
        Clicks on the payment option button on the Navbar -> Account -> order and payment -> my payment option
        """
        self._handle_logger("Attempting to click my payment option button.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btn_my_payment_option_xpath))).click()
        self._handle_logger("My payment option button clicked.")

    def verify_user_reached_saved_payment_method_page(self, exp_url, expected_text):
        """
        Verify if the user reached the saved payment method page
        """
        self._handle_logger("Verifying user has reached saved payment method page.")
        self.wait.until(EC.url_to_be(exp_url))
        self.wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, 'h1'), expected_text))
        self._handle_logger("User has reached saved payment method page.")

    def navigate_to_saved_payment_method_page(self):
        """
        Navigate to saved payment method page
        """
        self.click_account_button()
        self.click_orders_and_payment_button()
        self.click_my_payment_option_button()
        self._handle_logger("Navigated to saved payment method page.")
