import pytest
from api_objects.post_payment_card import PaymentCardApi
from utilities.utilities import generate_credit_card_details, loggen

# @pytest.mark.skip(reason="Test class is not implemented yet")
@pytest.mark.run(order=2)
class TestPaymentCardAPI:
    logger = loggen()

    @pytest.fixture(scope='module')
    def api_setup(self):
        self.logger.info("Setting up API for testing.")
        pca = PaymentCardApi()
        name, card_number, card_exp_month, card_exp_year = generate_credit_card_details()
        card_data = {
            "fullName": name,
            "cardNum": card_number,
            "expMonth": card_exp_month,
            "expYear": card_exp_year
        }
        res = pca.post_card(card_data)

        self.logger.info(f"API setup complete. Response: {res.json()}")

        return card_data, res

    def test_validate_the_create_card_post_response_code(self, api_setup):
        self.logger.info("Running test: test_validate_the_create_card_post_response_code")
        card_data, res = api_setup
        assert res.status_code == 201, f"Expected status code 201, but got {res.status_code}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_the_create_card_post_response_code')
    def test_validate_response_status(self, api_setup):
        self.logger.info("Running test: test_validate_response_status")
        card_data, res = api_setup
        resbody = res.json()
        assert resbody['status'] == 'success', f"Expected status 'success', but got {resbody['status']}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_response_status')
    def test_validate_response_body_fields(self, api_setup):
        self.logger.info("Running test: test_validate_response_body_fields")
        card_data, res = api_setup
        resbody = res.json()
        expected_fields = {'id', 'UserId', 'updatedAt', 'createdAt', 'fullName', 'cardNum', 'expMonth', 'expYear'}
        resbody_fields = set(resbody['data'].keys())
        assert expected_fields == resbody_fields, f"Expected fields {expected_fields}, but got {resbody_fields}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_response_body_fields')
    def test_validate_response_fullName(self, api_setup):
        self.logger.info("Running test: test_validate_response_fullName")
        card_data, res = api_setup
        resbody = res.json()
        assert resbody['data']['fullName'] == card_data['fullName'], f"Expected full name {card_data['fullName']}, but got {resbody['data']['fullName']}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_response_body_fields')
    def test_validate_response_expMonth(self, api_setup):
        self.logger.info("Running test: test_validate_response_expMonth")
        card_data, res = api_setup
        resbody = res.json()
        assert resbody['data']['expMonth'] == int(card_data['expMonth']), f"Expected expiration month {card_data['expMonth']}, but got {resbody['data']['expMonth']}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_response_body_fields')
    def test_validate_response_expYear(self, api_setup):
        self.logger.info("Running test: test_validate_response_expYear")
        card_data, res = api_setup
        resbody = res.json()
        assert resbody['data']['expYear'] == int(card_data['expYear']), f"Expected expiration year {card_data['expYear']}, but got {resbody['data']['expYear']}"

    @pytest.mark.run(after='TestPaymentCardAPI::test_validate_response_body_fields')
    def test_validate_response_cardNum(self, api_setup):
        self.logger.info("Running test: test_validate_response_cardNum")
        card_data, res = api_setup
        resbody = res.json()
        assert resbody['data']['cardNum'] == card_data['cardNum'], f"Expected card number {card_data['cardNum']}, but got {resbody['data']['cardNum']}"
