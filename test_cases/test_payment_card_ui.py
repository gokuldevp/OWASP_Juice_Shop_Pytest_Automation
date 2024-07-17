import pytest
from time import sleep
from utilities.utilities import generate_credit_card_details
from page_objects.home_page import HomePage
from page_objects.login_page import LoginPage
from page_objects.my_payment_page import MyPaymentPage

@pytest.mark.run(order=1)
class TestPaymentCardUI:

    @pytest.fixture()
    def setup(self,setup):
        driver, logger = setup
        driver.get("http://localhost:3000/")
        hp = HomePage(driver,logger)
        lp = LoginPage(driver,logger)
        hp.navigate_to_login_page()
        lp.user_login_with_saved_credentials()
        yield driver, logger

    def test_user_navigate_to_payment_page_and_submitting_card_details(self, setup):
        """
        Test to navigate to the payment page and submit card details.
        - Navigates to the saved payment method page.
        - Verifies that the user has reached the payment method page.
        - Enters and submits credit card details.
        - Validates that the submitted details are added as a line item.
        """
        driver, logger =  setup
        hp = HomePage(driver,logger)
        hp.navigate_to_saved_payment_method_page()
        hp.verify_user_reached_saved_payment_method_page(hp.payment_page_url,"My Payment Options")
        mpp = MyPaymentPage(driver,logger)
        name, card_number, exp_month, exp_year = generate_credit_card_details()
        mpp.enter_credit_card_details_and_submit(name, card_number, exp_month, exp_year)
        mpp.validate_if_submited_details_added_as_line_item(name, card_number, exp_month, exp_year)
