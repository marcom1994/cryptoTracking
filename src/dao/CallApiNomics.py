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
# ATTENTION: After each call to an api he sleeps for 1 second in accord to limit of Nomics Api 
# ATTENTION: This API has 2 hours of delay!!!
# https://nomics.com/docs/#section/Authentication
class CallApiNomics:

    logger = logging.getLogger("logger")
    
    config = configparser.ConfigParser()
    config.read(constants.API_PROPERTIES_FILE_PATH)
    apiKey = config['APINomicsSection']['X-CoinRanking-Key']

    def __init__(self):
        pass
    
    
    # I call api from page 23 to 18. Return if find crypto Gods
    def retrieveGodsUnchainedInfo(self):
        crypto=None
        x=23
        while(not crypto or x<18):
            try:
                endpoint = "https://api.nomics.com/v1/currencies/ticker?key=%s&interval=1d,30d&convert=EUR&per-page=100&page=%s" %(self.apiKey,x)
                response = requests.get(endpoint)
                if(response.status_code==200):
                    json = response.json()
                    for coin in json:
                        if re.search('GODS',coin['id'], re.IGNORECASE):
                            crypto = Crypto(coin['id'], coin['name'], coin['price'])
                if(not crypto):
                    x-=1
                time.sleep(1)
            except Exception as e:
                self.logger.error(constants.MSG_CALL_API %("retrieveGodsUnchainedInfo", str(response.status_code), str(e)))
                raise Exception("Exception: " + str(e))
        self.logger.info(constants.MSG_CALL_API %("retrieveGodsUnchainedInfo", str(response.status_code), str(crypto)))
        return crypto

    def retrieveFirstOneHundredCrypto(self):
        endpoint = "https://api.nomics.com/v1/currencies/ticker?key=%s&interval=1d,30d&convert=EUR&per-page=100&page=1" %(self.apiKey)
        response = requests.get(endpoint)
        cryptoDict = {}
        if(response.status_code==200):
            json = response.json()
            for coin in json:
                crypto = Crypto(coin['id'], coin['name'], coin['price'])
                cryptoDict[crypto.name] = crypto
        time.sleep(1)
        self.logger.info(constants.MSG_CALL_API %("retrieveFirstOneHundredCrypto", str(response.status_code), str(crypto)))
        return cryptoDict

    def retrieveCryptoById(self, ids: str):
        ids=ids.upper()
        endpoint = "https://api.nomics.com/v1/currencies/ticker?key=%s&ids=%s&convert=EUR&per-page=100&page=1" %(self.apiKey, ids)
        crypto = None
        response = requests.get(endpoint)
        cryptoDict = {}
        if(response.status_code==200):
            json = response.json()
            for coin in json:
                crypto = Crypto(coin['id'], coin['name'], coin['price'])
                cryptoDict[crypto.name] = crypto
        time.sleep(1)
        self.logger.info(constants.MSG_CALL_API %("retrieveCryptoById", str(response.status_code), str(cryptoDict.keys())))
        return cryptoDict

    def retrieveCryptoAllInformationById(self, ids: str):
        ids=ids.upper()
        endpoint = "https://api.nomics.com/v1/currencies/ticker?key=%s&ids=%s&interval=1d,30d&convert=EUR&per-page=100&page=1" %(self.apiKey, ids)
        crypto = None
        response = requests.get(endpoint)
        cryptoDict = {}
        if(response.status_code==200):
            json = response.json()
            for coin in json:
                cryptoDict[coin['name']] = coin
        time.sleep(1)
        self.logger.info(constants.MSG_CALL_API %("retrieveCryptoById", str(response.status_code), str(cryptoDict.keys())))
        return cryptoDict


'''
# Test retrieveGodsUnchainedInfo():
callApiNomics = CallApiNomics()
print(callApiNomics.retrieveGodsUnchainedInfo())
'''


'''
# Test retrieveCryptoById():
callApiNomics = CallApiNomics()
#print(callApiNomics.retrieveCryptoById("BTC"))
cryptoDict = callApiNomics.retrieveCryptoById("BTC,ETH")
for crypto in cryptoDict.keys():
    print(cryptoDict[crypto])
'''

'''
# Test retrieveCryptoAllInformationById():
callApiNomics = CallApiNomics()
#print(callApiNomics.retrieveCryptoAllInformationById("BTC"))
cryptoDict = callApiNomics.retrieveCryptoAllInformationById("BTC,ETH,ALGO,GODS")
for crypto in cryptoDict.keys():
    print(cryptoDict[crypto])
'''



