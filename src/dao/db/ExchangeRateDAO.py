import logging
import os
import psycopg2
import configparser
from datetime import datetime
from src.constants.Constants import Constants
from src.constants.QueryConstants import QueryConstants

class ExchangeRateDAO:

    logger = logging.getLogger("logger")
    config = configparser.ConfigParser()
    config.read(Constants.DB_PROPERTIES_FILE_PATH)
    # dbProperties = config['DBSection']
    DATABASE_URL = os.environ['DATABASE_URL']


    def __init__(self):
        pass

    def retrieveExchangeRateLastCall(self):
        ret=0
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.RETRIEVE_EXCHANGE_RATE_LAST_CALL)
            for dateTime, in cursor:
                ret = dateTime
            connection.commit()
            cursor.close()
        return ret

    def retrieveExchangeRateValue(self):
        ret=0
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            cursor.execute(QueryConstants.RETRIEVE_EXCHANGE_RATE_VALUE)
            for exchangeRateValue, in cursor:
                ret = exchangeRateValue
            connection.commit()
            cursor.close()
        return ret

    def updateTimestampExchangeRate(self, exchangeRate):
        with(psycopg2.connect(self.DATABASE_URL, sslmode='require') as connection):
            cursor = connection.cursor()
            now = datetime.now()
            cursor.execute(QueryConstants.UPDATE_OR_INSERT_EXCHANGE_RATE %(now,exchangeRate,now,exchangeRate))
            connection.commit()
            cursor.close()

'''
# Test:
exchangeRateDAO = ExchangeRateDAO()
exchangeRateDAO.updateTimestampExchangeRate(34)
print(exchangeRateDAO.retrieveExchangeRateLastCall())
print(exchangeRateDAO.retrieveExchangeRateValue())
'''


 