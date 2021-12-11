import logging
import requests

logger = logging.getLogger()

def get_contracts():

    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    contracts = []


    for contract in response_object.json()['symbols']
        contracts.append(contract['pair'])

    return contracts

print(get_contracts())

class BinanceFutureClient:
    def __init__(self, testnet):
        if testnet:
            self.base_url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
        else:
            self.base_url = "https://fapi.binanc.com"

        logger.info("Binance Future client Succesfully initialized")

    def make_request(self, method, endpoint, date):
        if method == "GET":
           response =  request.get(self.base_url + endpoint, params=data)
        else:
            raise ValueError()

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("error while making %s request to %s: %s (error code %s) method, endpoint, response.json(), response.status_code")
            return None


    def get_contacts(self):
        exchange_info = self.make_request("GET","/fapi/v1/exchangeInfo", None)
        return

        if exchange_info is not None:
            for contract in exchange_info['symbols']:
                contracts[s['pair']] = contract_data
        return contracts

    def get_historical_candles(self):
        request.get()
        return

    def get_bid_ask(self):
        request.get()
        return






