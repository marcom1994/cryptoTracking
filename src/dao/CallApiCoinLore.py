from src.model.Crypto import Crypto
from src.constants.Constants import Constants

import requests
import configparser
import re
import time
import requests
import logging

'''
    * Name *            * ID *
    Bitcoin:            90
    Ethereum:           80
    Cardano:            257
    Algorand:           34406
    Aave:               46018
    Shiba Inu:          45088   
    Gods Unchained:     56829
'''

# https://rapidapi.com/coinlore/api/coinlore-cryptocurrency/
# Limit 1 per second
# ATTENTION: price are generated by average of different exchange (paragraph 'Real-time asset valuation' of https://blog.cryptostars.is/coinlore-review-an-all-in-one-asset-tracking-platform-1858a213b66)
class CallApiCoinLore:
    logger = logging.getLogger("logger")
    
    config = configparser.ConfigParser()
    config.read(Constants.API_PROPERTIES_FILE_PATH)
    headers = {
	    "X-RapidAPI-Host": config['APICoinLoreSection']['X-RapidAPI-Host'],
	    "X-RapidAPI-Key": config['APICoinLoreSection']['X-RapidAPI-Key']
    }

    def __init__(self):
        pass
    
    
    def retrieveFirstNCrypto(self, numberCrypto):
        endpoint = "https://coinlore-cryptocurrency.p.rapidapi.com/api/tickers/"
 
        limitApiForPage = 100
        arr = self.__getArrayQueryStringLimit__(limitApiForPage,numberCrypto)
        x=0
        cryptoDict = {}
        while(x<len(arr)):
            querystring = {"start":x*100,"limit":arr[x]}
            x+=1
            response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

            try:
                json = response.json()
                data = json['data']
                for coin in data:
                    crypto = Crypto(coin['id'], coin['name'], coin['price_usd'], coin['rank'])
                    cryptoDict[crypto.name] = crypto
                    #print(crypto)
            except Exception as e:
                print(Constants.MSG_CALL_API %("retrieveFirstNCrypto", str(response.status_code), str(e)))
                self.logger.error(Constants.MSG_CALL_API %("retrieveFirstNCrypto", str(response.status_code), str(e)))
            time.sleep(1)
            self.logger.info(Constants.MSG_CALL_API_ONLY_STATUS_CODE %("retrieveFirstNCrypto", str(response.status_code)))
        return cryptoDict

    def __getArrayQueryStringLimit__(self, limitApiForPage, numberCrypto):
        arr=[]
        while(limitApiForPage<numberCrypto):
            arr.append(limitApiForPage)
            limitApiForPage+=100
        arr.append(numberCrypto)
        return arr

    
    def retrieveCryptoById(self, id):
        endpoint = "https://coinlore-cryptocurrency.p.rapidapi.com/api/ticker/"
        querystring = {"id":str(id)}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

        crypto = None
        try:
            json = response.json()
            for coin in json:
                crypto = Crypto(coin['id'], coin['name'], coin['price_usd'], coin['rank'])
                #print(crypto)
        except Exception as e:
            print(Constants.MSG_CALL_API %("retrieveCryptoById", str(response.status_code), str(e)))
            self.logger.error(Constants.MSG_CALL_API %("retrieveCryptoById", str(response.status_code), str(e)))
        time.sleep(1)
        self.logger.info(Constants.MSG_CALL_API_ONLY_STATUS_CODE %("retrieveCryptoById", str(response.status_code)))
        return crypto

'''
# For test:   
#callApiCoinLore = CallApiCoinLore()
#callApiCoinLore.retrieveFirstNCrypto(1000)
callApiCoinLore.retrieveCryptoById("90")
'''

