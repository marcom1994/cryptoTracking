import logging
import os
import psycopg2
import configparser
from src.constants.Constants import Constants
from src.constants.QueryConstants import QueryConstants
from src.model.CryptoLimit import CryptoLimit


class CryptoTrackDAO:

    logger = logging.getLogger("logger")
    config = configparser.ConfigParser()
    config.read(Constants.DB_PROPERTIES_FILE_PATH)
    # dbProperties = config['DBSection']
    DATABASE_URL = os.environ['DATABASE_URL']

    def __init__(self):
        pass

    def retrieveCryptoToTrack(self):
        cryptoLimitList = []
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.RETRIEVE_CRYPTO_TO_TRACK)
            data = cursor.fetchall()
            #Convert:
            for crypto in data:
                cryptoLimit = CryptoLimit(crypto[0],crypto[1], crypto[2], crypto[3])
                cryptoLimitList.append(cryptoLimit)
            connection.commit()
            cursor.close()
        return cryptoLimitList

    def updateCryptoLimitPriceBuyToTrack(self, id, price):
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.UPDATE_CRYPTO_PRICE_BUY_TO_TRACK %(price, id))
            connection.commit()
            cursor.close()
    
    def updateCryptoLimitPriceSellToTrack(self, id, price):
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.UPDATE_CRYPTO_PRICE_SELL_TO_TRACK %(price, id))
            connection.commit()
            cursor.close()

    

    def retrieveAllCryptoId(self):
        coinLoreNameToIdDict = {}
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.RETRIEVE_ALL_CRYPTO_ID)
            listNameId = cursor.fetchall()
            for nameId in listNameId:
                coinLoreNameToIdDict[nameId[1]] = nameId[0]
            connection.commit()
            cursor.close()
        return coinLoreNameToIdDict

    def retrieveCryptoIdByName(self, name):
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.RETRIEVE_CRYPTO_ID_BY_NAME %(name))
            id = cursor.fetchone()
            if(id):
                id = id[0]
            connection.commit()
            cursor.close()
        return id

'''
# Test retrieveExchangeRateValue
cryptoTRackDAO = CryptoTrackDAO()
list = cryptoTRackDAO.retrieveExchangeRateValue()
for cryptoLimit in list:
    print(cryptoLimit)
'''

'''
# Test updateCryptoPriceToTrack
cryptoTRackDAO = CryptoTrackDAO()
cryptoTRackDAO.updateCryptoLimitPriceBuyToTrack(90,24000)
'''

'''
# Test updateCryptoPriceToTrack
cryptoTRackDAO = CryptoTrackDAO()
print(cryptoTRackDAO.retrieveCryptoIdByName('Bitcoin'))
'''


'''
# Test updateCryptoPriceToTrack
cryptoTRackDAO = CryptoTrackDAO()
print(cryptoTRackDAO.retrieveAllCryptoId())
'''



