from projects.cryptoTracking.src.model.Crypto import Crypto
from projects.cryptoTracking.src.constants.Constants import Constants as constants

import requests
import configparser


'''
Not used
'''
# https://rapidapi.com/Coinranking/api/coinranking1/
# Limit: 10.000 for month
class CallAPICoinRanking:
    config = configparser.ConfigParser()
    config.read(constants.API_PROPERTIES_FILE_PATH)
    headers = {
	    "X-RapidAPI-Host": config['APICoinRankingSection']['X-RapidAPI-Host'],
	    "X-RapidAPI-Key": config['APICoinRankingSection']['X-RapidAPI-Key']
    }

    def __init__(self):
        pass


    
    # Euro: 5k-_VTxqtCEI
    def retrieveFirstNCrypto(self, numberCrypto):
        cryptoDict = {}
        endpoint = "https://coinranking1.p.rapidapi.com/coins"
        querystring = {"referenceCurrencyUuid":"5k-_VTxqtCEI","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc",
                       "limit":numberCrypto,"offset":"0"}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

        json = response.json()
        try:
            data = json['data']
            coinsArr = data['coins']
            for coin in coinsArr:
                crypto = Crypto(coin['uuid'], coin['name'], coin['price'], coin['rank'])
                cryptoDict[crypto.name] = crypto
                #print(crypto)
        except Exception as e:
            print("[retrieveAllCryptoInfo]: ", e)
        return cryptoDict


    def retrieveFirstNCryptoAllInfo(self, numberCrypto):
        cryptoDict = {}
        endpoint = "https://coinranking1.p.rapidapi.com/coins"
        querystring = {"referenceCurrencyUuid":"5k-_VTxqtCEI","timePeriod":"24h","tiers[0]":"1","orderBy":"marketCap","orderDirection":"desc",
                       "limit":numberCrypto,"offset":"0"}
        response = requests.request("GET", endpoint, headers=self.headers, params=querystring)

        json = response.json()
        try:
            data = json['data']
            coinsArr = data['coins']
            for coin in coinsArr:
                cryptoDict[coin['name']] = coin
                #print(crypto)
        except Exception as e:
            print("[retrieveAllCryptoInfo]: ", e)
        return cryptoDict




'''
# For test:
callAPICoinRanking = CallAPICoinRanking()
print(callAPICoinRanking.retrieveFirstNCrypto(50)['Bitcoin'])
#for crypto in callAPICoinRanking.retrieveFirstNCrypto(100).values():
#    print(crypto, "\n")
'''


'''
# For test:
callAPICoinRanking = CallAPICoinRanking()
#print(callAPICoinRanking.retrieveFirstNCryptoAllInfo(50)['Bitcoin'])
for crypto in callAPICoinRanking.retrieveFirstNCryptoAllInfo(100).values():
    print(crypto, "\n")
'''
