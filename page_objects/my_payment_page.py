from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from utilities.utilities import ScreeShots
from time import sleep

class MyPaymentPage:
    # locators
    mat_expansion_panel_header_tag = "mat-expansion-panel-header"
    input_name_xpath = "//mat-label[text()='Name']/ancestor::span/preceding-sibling::input[contains(@id,'mat-input')]"
    input_card_number_xpath = "//mat-label[text()='Card Number']/ancestor::span/preceding-sibling::input[contains(@id,'mat-input')]"
    dropdown_expiry_month_xpath = "//mat-label[text()='Expiry Month']/ancestor::span/preceding-sibling::select[contains(@id,'mat-input')]"
    dropdown_expiry_year_xpath = "//mat-label[text()='Expiry Year']/ancestor::span/preceding-sibling::select[contains(@id,'mat-input')]"
    btn_submit_id = "submitButton"

    txt_name_xpath = "//mat-row/mat-cell[2]"
    txt_card_number_xpath = "//mat-row/mat-cell[1]"
    txt_expiry_xpath = "//mat-row/mat-cell[3]"

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
    def click_mat_expansion_panel_header_tag(self):
        """
        Clicks the expansion panel header
        """
        self._handle_logger("Clicking the expansion panel header.")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, self.mat_expansion_panel_header_tag))).click()
        self._handle_logger("Expansion panel header clicked.")

    def enter_name(self, name):
        """
        Enters the provided name into the name input field
        """
        self._handle_logger("Entering name.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.input_name_xpath))).send_keys(name)
        self._handle_logger("Name entered.")

    def enter_card_number(self, card_number):
        """
        Enters the provided card number into the card number input field
        """
        self._handle_logger("Entering card number.")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.input_card_number_xpath))).send_keys(card_number)
        self._handle_logger("Card number entered.")

    def select_expiry_month(self, expiry_month):
        """
        Selects the provided expiry month from the dropdown
        """
        self._handle_logger("Selecting expiry month.")
        expiry_month_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_expiry_month_xpath)))
        expiry_month_select = Select(expiry_month_dropdown)
        expiry_month_select.select_by_value(expiry_month)
        self._handle_logger("Expiry month selected.")

    def select_expiry_year(self, expiry_year):
        """
        Selects the provided expiry year from the dropdown
        """
        self._handle_logger("Selecting expiry year.")
        expiry_year_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.dropdown_expiry_year_xpath)))
        expiry_year_select = Select(expiry_year_dropdown)
        expiry_year_select.select_by_value(expiry_year)
        self._handle_logger("Expiry year selected.")

    def submit_credit_card(self):
        """
        Submits the credit card details
        """
        self._handle_logger("Submitting credit card details.")
        self.wait.until(EC.element_to_be_clickable((By.ID, self.btn_submit_id))).click()
        self._handle_logger("Credit card details submitted.")

    def enter_credit_card_details_and_submit(self, name, card_number, exp_month, exp_year):
        """
        Enters and submits the provided credit card details
        """
        self._handle_logger("Entering and submitting credit card details.")
        self.click_mat_expansion_panel_header_tag()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.enter_name(name)
        self.enter_card_number(card_number)
        self.select_expiry_month(exp_month)
        self.select_expiry_year(exp_year)
        self.submit_credit_card()
        self._handle_logger("Credit card details entered and submitted.")

    def validate_latest_credit_card_name(self, name):
        """
        Validates that the latest credit card name matches the provided name
        """
        self._handle_logger("Validating the latest credit card name.")
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.txt_name_xpath)))
        if elements:
            latest_element = elements[-1]
            assert latest_element.text == name, f"Expected {name} but returned {latest_element.text}"
        self._handle_logger("Credit card name validated.")

    def validate_latest_credit_card_number(self, card_number):
        """
        Validates that the latest credit card number matches the provided number
        """
        self._handle_logger("Validating the latest credit card number.")
        card_number = str(card_number)[12:16]
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.txt_card_number_xpath)))
        if elements:
            latest_element = elements[-1]
            assert latest_element.text[12:16] == card_number, f"Expected {card_number} but returned {latest_element.text[12:16]}"
        self._handle_logger("Credit card number validated.")

    def validate_expiry_date_and_month(self, exp_month, exp_year):
        """
        Validates that the latest expiry date matches the provided month and year
        """
        self._handle_logger("Validating the expiry date and month.")
        expiry = f"{exp_month}/{exp_year}"
        elements = self.wait.until(EC.visibility_of_all_elements_located((By.XPATH, self.txt_expiry_xpath)))
        if elements:
            latest_element = elements[-1]
            assert latest_element.text == expiry, f"Expected {expiry} but returned {latest_element.text}"
        self._handle_logger("Expiry date and month validated.")

    def validate_if_submited_details_added_as_line_item(self, name, card_number, exp_month, exp_year):
        """
        Validates that the submitted credit card details are added as a line item
        """
        self._handle_logger("Validating if submitted details are added as a line item.")
        sleep(2)
        self.validate_latest_credit_card_name(name)
        self.validate_latest_credit_card_number(card_number)
        self.validate_expiry_date_and_month(exp_month, exp_year)
        self._handle_logger("Submitted details validated as line item.")
