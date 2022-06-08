from projects.cryptoTracking.src.model.Crypto import Crypto
from projects.cryptoTracking.src.constants.Constants import Constants as constants

import requests
import configparser

'''
Not used
'''
# https://docs.coinapi.io/?python#get-all-current-rates-get
# Limit: 100 for day
class CallApiCoinApi:

    config = configparser.ConfigParser()
    config.read(constants.API_PROPERTIES_FILE_PATH)
    headers = {'X-CoinAPI-Key' : config['APICoinSection']['X-CoinAPI-Key']}


    def __init__(self):
        pass


    
    '''
    Only crypto:
        Bitcoin
        NIS
        Litecoin
        VeChain
        Ripple
        Namecoin
        Tether
    '''
    def retrieveAllCryptoInfo(self):
        cryptoDict = {}
        endpoint = "https://rest.coinapi.io/v1/assets"

        response = requests.get(endpoint, headers=self.headers)

        json = response.json()
        
        try:
            for coin in json:
                if(coin['type_is_crypto']==1):
                    crypto = Crypto(coin['asset_id'], coin['name'], coin['price_usd'])
                    cryptoDict[crypto.name] = crypto
                    print(crypto)
        except Exception as e:
            print("[retrieveAllCryptoInfo]: ", str(e))

        return cryptoDict

'''
# For test:
callApiCoinApi = CallApiCoinApi()
callApiCoinApi.retrieveAllCryptoInfo()
'''








