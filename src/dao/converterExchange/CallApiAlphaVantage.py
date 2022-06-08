from projects.cryptoTracking.src.dao.db.ExchangeRateDAO import ExchangeRateDAO
from projects.cryptoTracking.src.model.Crypto import Crypto
from projects.cryptoTracking.src.constants.Constants import Constants as constants

import requests
import configparser
import re
import datetime
import requests
import logging

# https://rapidapi.com/alphavantage/api/alpha-vantage/
# 500 for day
class CallApiAlphaVantage:

    logger = logging.getLogger("logger")
    
    config = configparser.ConfigParser()
    config.read(constants.API_PROPERTIES_FILE_PATH)
    headers = {
	    "X-RapidAPI-Host": config['APIAlphaVantageSection']['X-RapidAPI-Host'],
	    "X-RapidAPI-Key": config['APIAlphaVantageSection']['X-RapidAPI-Key']
    }
    

    hourUpdateExchangeRate = datetime.datetime.now().hour

    def __init__(self):
        pass

    # Return 'tasso di cambio'
    def retrieveExchangeRateFromApi(self, currencySource:str, currencyDest:str):
        endpoint = "https://alpha-vantage.p.rapidapi.com/query"
        querystring = {"function":"CURRENCY_EXCHANGE_RATE", "from_currency":str(currencySource),"to_currency":str(currencyDest)}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)
        exchangeRate=0
        try:
            data = response.json()
            realTimeExchangeRate = data['Realtime Currency Exchange Rate']
            exchangeRate = realTimeExchangeRate['5. Exchange Rate']
        except Exception as e:
            print(constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(e)))
            self.logger.error(constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(e)))
        self.logger.info(constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(exchangeRate)))
        return exchangeRate

    def retrieveExchangeRateFromDB(self):
        exchangeRateDAO = ExchangeRateDAO()
        exchangeRate = exchangeRateDAO.retrieveExchangeRateValue()
        self.logger.info(constants.MSG_CALL_DB %("retrieveExchangeRateFromDB", str(exchangeRate)))
        return exchangeRate



'''
# Test:
callApiAlphaVantage = CallApiAlphaVantage()
print(callApiAlphaVantage.retrieveExchangeRateFromApi("USD", "EUR"))
'''


