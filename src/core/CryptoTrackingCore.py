from projects.cryptoTracking.src.core.HandlerAPI import HandlerAPI

import logging
from projects.cryptoTracking.src.dao.db.CryptoTrackDAO import CryptoTrackDAO

from projects.cryptoTracking.src.constants.Constants import Constants as constants
from projects.cryptoTracking.src.telegram.HandlerTelegram import HandlerTelegram

from logging.handlers import RotatingFileHandler

class CryptoTrackingCore:

    logger = logging.getLogger("logger")

    def handlerCrypto(self, firstCall):
        self.logger.info("********** START: Call to retrieve Crypto pricing **********")
        return self.callForRetriveCryptoPrice(firstCall)
        

    def callForRetriveCryptoPrice(self, firstCall):
        if(firstCall):
            self.defineInternalLogging()
        handlerApi = HandlerAPI()
        handlerTelegram = HandlerTelegram()

        cryptoTrackDAO = CryptoTrackDAO()
        listCryptoLimit = cryptoTrackDAO.retrieveCryptoToTrack()
        cryptoDictToTrackPriceLimitBuy = self.__buildDictCryptoLimitBuy__(listCryptoLimit)
        cryptoDictToTrackPriceLimitSell = self.__buildDictCryptoLimitSell__(listCryptoLimit)
        coinLoreNameToIdDict = cryptoTrackDAO.retrieveAllCryptoId()

        cryptoDictFirstN = handlerApi.retrieveFirstNCrypto(100, constants.DEFAULT_CURRENCY)
        cryptoDictTracking = {}
        
        for cryptoName in cryptoDictToTrackPriceLimitBuy.keys():
            if(cryptoName in cryptoDictFirstN.keys()):
                cryptoDictTracking[cryptoName] = cryptoDictFirstN[cryptoName]


        for cryptoName in cryptoDictToTrackPriceLimitBuy.keys():
            if(cryptoName in coinLoreNameToIdDict.keys() and 
               cryptoName not in cryptoDictTracking.keys()):
                    cryptoDictTracking[cryptoName] = handlerApi.retrieveCryptoById(coinLoreNameToIdDict[cryptoName], constants.DEFAULT_CURRENCY)


        for cryptoName in cryptoDictTracking.keys():
            crypto = cryptoDictTracking[cryptoName]
            self.logger.info(constants.MSG_CRYPTO %("callForRetriveCryptoPrice", str(crypto)))
            if(cryptoName in cryptoDictToTrackPriceLimitBuy.keys()):
                if(self.isPriceForBuy(cryptoDictToTrackPriceLimitBuy, crypto)):
                    priceToBuy = cryptoDictToTrackPriceLimitBuy[crypto.name]
                    newPriceToBuy = priceToBuy - ((priceToBuy * 5) / 100)
                    cryptoTrackDAO.updateCryptoLimitPriceBuyToTrack(crypto.uuid, newPriceToBuy)
                    handlerTelegram.telegram_bot_sendtext("Best moment to buy this crypto: " + str(crypto))
            if(cryptoName in cryptoDictToTrackPriceLimitSell.keys()):
                if(self.isPriceForSell(cryptoDictToTrackPriceLimitSell, crypto)):
                    priceToSell = cryptoDictToTrackPriceLimitSell[crypto.name]
                    newPriceToSell = priceToSell + ((priceToSell * 5) / 100)
                    cryptoTrackDAO.updateCryptoLimitPriceSellToTrack(crypto.uuid, newPriceToSell)
                    handlerTelegram.telegram_bot_sendtext("Best moment to sell this crypto: " + str(crypto))
        self.logger.info("********** END: Call to retrieve Crypto pricing **********")
        return cryptoDictTracking
        





    def isPriceForBuy(self, cryptoDictLimitBuy, crypto):
        return crypto.price <= cryptoDictLimitBuy[crypto.name]

    def isPriceForSell(self, cryptoDictLimitSell, crypto):
        return crypto.price >= cryptoDictLimitSell[crypto.name]

    

    def __buildDictCryptoLimitBuy__(self, listCryptoToBuy):
        dictCryptoToBuy = {}
        
        for crypto in listCryptoToBuy:
            dictCryptoToBuy[crypto.name] = crypto.limitBuy
        return dictCryptoToBuy

    def __buildDictCryptoLimitSell__(self, listCryptoToSell):
        dictCryptoToSell = {}
        for crypto in listCryptoToSell:
            dictCryptoToSell[crypto.name] = crypto.limitSell
        return dictCryptoToSell







    # defineInternalLogging is necessary because I have created a new process.
    def defineInternalLogging(self):
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        logger.propagate=False  # Non propaga i log anche in console
        file_handler = RotatingFileHandler(constants.PATH_LOG, maxBytes=constants.MAX_SIZE_LOG, backupCount=constants.MAX_FILES_LOG, encoding=constants.ENCODE)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


        





#handlerApi.retrieveUidCyptoByName("Bitcoin")
#handlerApi.retrievePriceCrypto()

'''
cryptoDict = handlerApi.retrieveCryptoById("BTC,ETH")
for cryptoName in cryptoDict.keys():
    print(cryptoDict[cryptoName])
cryptoGods = handlerApi.retrieveGodsUnchainedCrypto()
'''