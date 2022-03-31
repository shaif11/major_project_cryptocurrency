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





#new update from shaif


