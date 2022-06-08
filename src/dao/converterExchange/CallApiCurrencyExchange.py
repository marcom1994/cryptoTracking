from projects.cryptoTracking.src.model.Crypto import Crypto
from projects.cryptoTracking.src.constants.Constants import Constants as constants

import requests
import configparser
import re
import time
import requests
import logging

'''
Not used
'''
# https://rapidapi.com/fyhao/api/currency-exchange/
# No limit
class CallApiCurrencyExchange:

    logger = logging.getLogger("logger")
    
    config = configparser.ConfigParser()
    config.read(constants.API_PROPERTIES_FILE_PATH)
    headers = {
	    "X-RapidAPI-Host": config['APICurrencyExchangeSection']['X-RapidAPI-Host'],
	    "X-RapidAPI-Key": config['APICurrencyExchangeSection']['X-RapidAPI-Key']
    }
    
    def __init__(self):
        pass

    # Retrun 'tasso di cambio'
    def retrieveExchangeRate(self, currencySource:str, currencyDest:str):
        endpoint = "https://currency-exchange.p.rapidapi.com/exchange"
        querystring = {"from":str(currencySource),"to":str(currencyDest)}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

        exchangeRate = response.json()
        return exchangeRate

    def convertCurrencyValue(self, currencySource:str, currencyDest:str, currencyValue:float=1):
        endpoint = "https://currency-exchange.p.rapidapi.com/exchange"
        querystring = {"from":str(currencySource),"to":str(currencyDest)}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

        exchangeRate = response.json()
        currencyConverted = float(exchangeRate) * float(currencyValue)
        return currencyConverted



# For test
callApiCurrencyExchange = CallApiCurrencyExchange()
#print(callApiCurrencyExchange.retrieveExchangeRate("USD","EUR"))
#print(callApiCurrencyExchange.convertCurrencyValue("USD","EUR",300))