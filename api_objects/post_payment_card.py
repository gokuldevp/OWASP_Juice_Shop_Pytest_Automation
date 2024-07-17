import requests

from utilities.utilities import loggen

class PaymentCardApi:
    logger = loggen()
    def __init__(self):
        self.base_url = 'http://localhost:3000/'
        self.CARD = 'api/Cards/'
        self.token = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0dHB2dF9nZGp1aWNlc2hvcDAxQHlvcG1haWwuY29tIiwicGFzc3dvcmQiOiJmOTI1OTE2ZTI3NTRlNWUwM2Y3NWRkNThhNTczMzI1MSIsInJvbGUiOiJjdXN0b21lciIsImRlbHV4ZVRva2VuIjoiIiwibGFzdExvZ2luSXAiOiIwLjAuMC4wIiwicHJvZmlsZUltYWdlIjoiL2Fzc2V0cy9wdWJsaWMvaW1hZ2VzL3VwbG9hZHMvZGVmYXVsdC5zdmciLCJ0b3RwU2VjcmV0IjoiIiwiaXNBY3RpdmUiOnRydWUsImNyZWF0ZWRBdCI6IjIwMjQtMDctMTcgMTY6MTY6MDAuMTU3ICswMDowMCIsInVwZGF0ZWRBdCI6IjIwMjQtMDctMTcgMTY6MTY6MDAuMTU3ICswMDowMCIsImRlbGV0ZWRBdCI6bnVsbH0sImlhdCI6MTcyMTIzMzQ4MH0.yPF1XDzII1N5GwBc5rr-x12gvf-LpsFYOX2gb8u-8CxzINgzdWFyY1m4qyWet2ny85f9HrHa91T_vVawWjzmdRwW5a9zxOdEonyqKWieYv-8PnIOtqggZ7bbTO-wAoL70lnC7Oqj1kqydioCtsLAeCDkpfz4_2rjdnqc2LFDrEo'
        self.content_type = 'application/json'
        self.headers = {
            'Authorization': self.token,
            'Content-Type': self.content_type
        }

    def handle_logger(self, info):
        self.logger.info(f"API :: {info}")

    def post_card(self, card_data):
        url = self.base_url + self.CARD
        try:
            self.handle_logger("Posting card data to the API.")
            response = requests.post(url, headers=self.headers, json=card_data)
            response.raise_for_status()
            self.handle_logger(f"Card data posted successfully: {response.status_code}")
            return response
        except requests.exceptions.HTTPError as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            self.logger.error(f"An error occurred: {err}")
            raise

