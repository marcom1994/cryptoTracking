import multiprocessing
from projects.cryptoTracking.src.constants.Constants import Constants as constants
from projects.cryptoTracking.src.core.CryptoTrackingCore import CryptoTrackingCore
from logging.handlers import RotatingFileHandler
import logging
import configparser
from telegram.ext import Updater, CommandHandler
from projects.cryptoTracking.src.model.Crypto import Crypto
from projects.cryptoTracking.src.telegram.HandlerTelegram import HandlerTelegram
from projects.cryptoTracking.src.dao.converterExchange.CallApiAlphaVantage import CallApiAlphaVantage

import time
import schedule


'''
class CryptoTrackingMain:
    logger = logging.getLogger("logger")
    callApiAlphaVantage = CallApiAlphaVantage()

    config = configparser.ConfigParser()
    config.read(constants.TELEGRAM_PROPERTIES_FILE_PATH)
    bot_token = config['TelegramBot']['token']
    bot_chatID = config['TelegramBot']['chat-id']

    def __init__(self):
        self


    # Configuration logging (DEBUG,INFO,WARNING,ERROR) (From the lowest level of detail to the highest level of detail)
    # When the logs have reached the 'MAX_SIZE_LOG' create a new file (PATH_LOG) and rename all others files. 
    # It does this until MAX_FILES_LOG, then delete the oldest and continue.
    def defineLogging(self):
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        logger.propagate=False  # Non propaga i log anche in console
        file_handler = RotatingFileHandler(constants.PATH_LOG, maxBytes=constants.MAX_SIZE_LOG, backupCount=constants.MAX_FILES_LOG, encoding=constants.ENCODE)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    def main(self):        
        self.logger.info("++++++++++ Start CryptoTracking ++++++++++")
        self.defineLogging()
        core = CryptoTrackingCore()
        #core.handlerCrypto()       # If you need to start it only once
        self.jobScheduleOnMultipleCalls()  # If you need to start it 'n' Se serve avviarlo 'n' times
    
    def jobScheduleOnMultipleCalls(self):
        # Call httpMultipleCalls each 'x' seconds (calculated by the end of the previous call)
        core = CryptoTrackingCore()
        core.handlerCrypto() # I make the first call immediately
        schedule.every(10).seconds.do(core.handlerCrypto)
        while True:
            schedule.run_pending()
            #time.sleep(1)





    
    def startListenerTelegramCommand(self):
        updater = Updater(self.bot_token)
        updater.dispatcher.add_handler(CommandHandler("start", self.start))
        updater.start_polling()
        updater.idle()

    def start(self, update, context):
        chat_id = update.effective_chat.id
        update.message.reply_text("start executed")
        print("start called from chat with id = {}".format(chat_id))
        self.cryptoTrackingLauncher.main()

    def stop(self, update, context):
        chat_id = update.effective_chat.id
        update.message.reply_text("stop executed")
        print("stop called from chat with id = {}".format(chat_id))
        self.cryptoTrackingLauncher.main()
'''

























class CryptoTrackingMain:
    logger = logging.getLogger("logger")
    callApiAlphaVantage = CallApiAlphaVantage()

    config = configparser.ConfigParser()
    config.read(constants.TELEGRAM_PROPERTIES_FILE_PATH)
    bot_token = config['TelegramBot']['token']
    bot_chatID = config['TelegramBot']['chat-id']

    core = CryptoTrackingCore()

    def __init__(self):
        self


    # Configuration logging (DEBUG,INFO,WARNING,ERROR) (From the lowest level of detail to the highest level of detail)
    # When the logs have reached the 'MAX_SIZE_LOG' create a new file (PATH_LOG) and rename all others files. 
    # It does this until MAX_FILES_LOG, then delete the oldest and continue.
    def defineLogging(self):
        logger = logging.getLogger("logger")
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        logger.propagate=False  # Non propaga i log anche in console
        file_handler = RotatingFileHandler(constants.PATH_LOG, maxBytes=constants.MAX_SIZE_LOG, backupCount=constants.MAX_FILES_LOG, encoding=constants.ENCODE)
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    def main(self):        
        self.defineLogging()
        self.startListenerTelegramCommand()
        
    
    
    def jobScheduleOnMultipleCalls(self):
        # Call httpMultipleCalls each 'x' seconds (calculated by the end of the previous call)
        self.core.handlerCrypto(True) # I make the first call immediately
        schedule.every(10).seconds.do(self.core.handlerCrypto,False)
        
        
        while True:
            schedule.run_pending()
            #time.sleep(1)



    #t = Thread(target=self.jobScheduleOnMultipleCalls)  
    proc = None
    
    def startListenerTelegramCommand(self):
        updater = Updater(self.bot_token)
        updater.dispatcher.add_handler(CommandHandler("start", self.start))
        updater.dispatcher.add_handler(CommandHandler("stop", self.stop))
        updater.dispatcher.add_handler(CommandHandler("info", self.info))
        updater.start_polling()
        updater.idle()

    def start(self, update, context):
        chat_id = update.effective_chat.id
        if(not self.proc or not self.proc.is_alive()):
            update.message.reply_text("start executed")
            self.logger.info("++++++++++ Start CryptoTracking called from chat with id = {} ++++++++++".format(chat_id))
            print("start called from chat with id = {}".format(chat_id))
            # If you need to start it 'n' Se serve avviarlo 'n' times
            self.proc = multiprocessing.Process(target=self.jobScheduleOnMultipleCalls)     
            # If you need to start it only once
            #core = CryptoTrackingCore()
            #self.proc = multiprocessing.Process(target=core.handlerCrypto())    
            self.proc.start()
        else:
            update.message.reply_text("Process already started")
            self.logger.info("++++++++++ Process already started - start called from chat with id = {} ++++++++++".format(chat_id))
            print("++++++++++ Process already started - start called from chat with id = {} ++++++++++".format(chat_id))
        

    def stop(self, update, context):
        chat_id = update.effective_chat.id
        
        if(self.proc and self.proc.is_alive()):
            update.message.reply_text("stop executed")
            self.logger.info("---------- Stop CryptoTracking called from chat with id = {} ----------".format(chat_id))
            print("---------- stop called from chat with id = {} ----------".format(chat_id))
            self.proc.terminate()
        else:
            update.message.reply_text("No processes started")
            self.logger.info("---------- No processes started - stop called from chat with id = {} ----------".format(chat_id))
            print("---------- No processes started - stop called from chat with id = {} ----------".format(chat_id))
        
    def info(self, update, context):
        chat_id = update.effective_chat.id

        if(self.proc and self.proc.is_alive()):
            #TODO: retrieve info from last call to crypto api
            update.message.reply_text("info executed")
            #update.message.reply_text(self.core.cryptoDictTracking['Bitcoin'])
            self.logger.info("---------- Info CryptoTracking called from chat with id = {} ----------".format(chat_id))
            print("---------- info called from chat with id = {} ----------".format(chat_id))
        else:
            update.message.reply_text("No processes started")
            self.logger.info("---------- No processes started - info called from chat with id = {} ----------".format(chat_id))
            print("---------- No processes started - info called from chat with id = {} ----------".format(chat_id))
