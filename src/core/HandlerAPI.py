from src.dao.converterExchange.CallApiAlphaVantage import CallApiAlphaVantage
from src.dao.CallApiCoinLore import CallApiCoinLore
from src.constants.Constants import Constants as constants
from src.dao.db.ExchangeRateDAO import ExchangeRateDAO

from datetime import datetime


class HandlerAPI:

    callApiCoinLore = CallApiCoinLore()
    callApiAlphaVantage = CallApiAlphaVantage()
    

    def __init__(self):
        pass


    def retrieveFirstNCrypto(self, number, currency=constants.DEFAULT_CURRENCY):
        cryptoDict = self.callApiCoinLore.retrieveFirstNCrypto(number)
        if("USD"!=currency):
            exchangeRate = self.__updateExchangeRate__(currency)
            for crypto in cryptoDict.keys():
                price = float(cryptoDict[crypto].price) * float(exchangeRate)
                cryptoDict[crypto].price = price
        return cryptoDict

    def retrieveCryptoById(self, id, currency=constants.DEFAULT_CURRENCY):
        crypto = self.callApiCoinLore.retrieveCryptoById(id)
        if("USD"!=currency):
            exchangeRate = self.__updateExchangeRate__(currency)
            crypto.price = float(crypto.price) * float(exchangeRate)
        return crypto
        

    def __updateExchangeRate__(self, currency):
        exchangeRate = None
        exchangeRateDAO = ExchangeRateDAO()
        dateLastCall = exchangeRateDAO.retrieveExchangeRateLastCall()
        dateNow = datetime.now()
        dateDifference = dateNow - dateLastCall
        hoursDifference = dateDifference.total_seconds() / 3600

        # Call api for retrieve echangeRate each hour
        if(hoursDifference > 1):
            exchangeRate = self.callApiAlphaVantage.retrieveExchangeRateFromApi("USD",currency)
            exchangeRateDAO.updateTimestampExchangeRate(float(exchangeRate))
        else:
            exchangeRate = self.callApiAlphaVantage.retrieveExchangeRateFromDB()
        return exchangeRate

'''
handlerAPI = HandlerAPI()
handlerAPI.__updateExchangeRate__("EUR")
'''

