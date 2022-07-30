from src.dao.db.ExchangeRateDAO import ExchangeRateDAO
from src.constants.Constants import Constants

import os
import requests
import configparser
import datetime
import requests
import logging

# https://rapidapi.com/alphavantage/api/alpha-vantage/
# 500 for day
class CallApiAlphaVantage:

    logger = logging.getLogger("logger")
    
    '''
    # With locale properties:
    config = configparser.ConfigParser()
    config.read(Constants.API_PROPERTIES_FILE_PATH)
    headers = {
	    "X-RapidAPI-Host": config['APIAlphaVantageSection']['X-RapidAPI-Host'],
	    "X-RapidAPI-Key": config['APIAlphaVantageSection']['X-RapidAPI-Key']
    }
    '''
    headers = {
	    "X-RapidAPI-Host": os.getenv('ALPHAVANTAGE_HOST'),
	    "X-RapidAPI-Key": os.getenv('RAPIAPI_PASS')
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
            print(Constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(e)))
            self.logger.error(Constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(e)))
        self.logger.info(Constants.MSG_CALL_API %("retrieveExchangeRateFromApi", str(response.status_code), str(exchangeRate)))
        return exchangeRate

    def retrieveExchangeRateFromDB(self):
        exchangeRateDAO = ExchangeRateDAO()
        exchangeRate = exchangeRateDAO.retrieveExchangeRateValue()
        self.logger.info(Constants.MSG_CALL_DB %("retrieveExchangeRateFromDB", str(exchangeRate)))
        return exchangeRate



'''
# Test:
callApiAlphaVantage = CallApiAlphaVantage()
print(callApiAlphaVantage.retrieveExchangeRateFromApi("USD", "EUR"))
'''


