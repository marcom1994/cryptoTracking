import logging
import psycopg2
import configparser
from datetime import datetime
from projects.cryptoTracking.src.constants.Constants import Constants as constants
from projects.cryptoTracking.src.constants.QueryConstants import QueryConstants as query

class ExchangeRateDAO:

    logger = logging.getLogger("logger")
    config = configparser.ConfigParser()
    config.read(constants.DB_PROPERTIES_FILE_PATH)
    dbProperties = config['DBSection']

    def __init__(self):
        pass

    def retrieveExchangeRateLastCall(self):
        ret=0
        with(psycopg2.connect(dbname=self.dbProperties['dbname'], user=self.dbProperties['user'], password=self.dbProperties['password'], host=self.dbProperties['host']) as connection):
            cursor = connection.cursor()
            cursor.execute(query.RETRIEVE_EXCHANGE_RATE_LAST_CALL)
            for dateTime, in cursor:
                ret = dateTime
            connection.commit()
            cursor.close()
        return ret

    def retrieveExchangeRateValue(self):
        ret=0
        with(psycopg2.connect(dbname=self.dbProperties['dbname'], user=self.dbProperties['user'], password=self.dbProperties['password'], host=self.dbProperties['host']) as connection):
            cursor = connection.cursor()
            cursor.execute(query.RETRIEVE_EXCHANGE_RATE_VALUE)
            for exchangeRateValue, in cursor:
                ret = exchangeRateValue
            connection.commit()
            cursor.close()
        return ret

    def updateTimestampExchangeRate(self, exchangeRate):
        with(psycopg2.connect(dbname=self.dbProperties['dbname'], user=self.dbProperties['user'], password=self.dbProperties['password'], host=self.dbProperties['host']) as connection):
            cursor = connection.cursor()
            now = datetime.now()
            cursor.execute(query.UPDATE_OR_INSERT_EXCHANGE_RATE %(now,exchangeRate,now,exchangeRate))
            connection.commit()
            cursor.close()

'''
# Test:
exchangeRateDAO = ExchangeRateDAO()
exchangeRateDAO.updateTimestampExchangeRate(34)
print(exchangeRateDAO.retrieveExchangeRateLastCall())
print(exchangeRateDAO.retrieveExchangeRateValue())
'''


 