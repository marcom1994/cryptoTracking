import os
import logging
import requests
import configparser
import logging
from src.constants.Constants import Constants as constants

class HandlerTelegram:

    logger = logging.getLogger("logger")
    
    '''
    # With locale properties:
    config = configparser.ConfigParser()
    config.read(constants.TELEGRAM_PROPERTIES_FILE_PATH)
    bot_token = config['TelegramBot']['token']
    bot_chatID = config['TelegramBot']['chat-id']
    '''
    bot_token = os.environ['TELEGRAM_HOST']
    bot_chatID = os.environ['TELEGRAM_CHATID']

    def __init__(self):
        pass


    def telegram_bot_sendtext(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_chatID + '&parse_mode=html&text=' + bot_message
        print("Telegram_msg:" + str(send_text))
        self.logger.info("Telegram_msg:" + str(send_text))
        response = requests.get(send_text)
        json = response.json()
        self.logger.info(json)
        return json


    



'''
# For test
handlerTelegram = HandlerTelegram()
handlerTelegram.telegram_bot_sendtext("Testing Telegram bot")
'''







