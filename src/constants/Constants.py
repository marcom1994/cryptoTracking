class Constants:
    #Project
    PROJECT_PATH = "D:\\1.Progetti\\MyProjects\\workspace_python\\projects\\cryptoTracking\\"
    
    API_PROPERTIES_FILE_PATH = PROJECT_PATH + "\\files\\properties\\configAPI.properties"
    TELEGRAM_PROPERTIES_FILE_PATH = PROJECT_PATH + "\\files\\properties\\configTelegram.properties"
    DB_PROPERTIES_FILE_PATH = PROJECT_PATH + "\\files\\properties\\configDB.properties"
    
    
    #Log
    PATH_LOG = PROJECT_PATH + "logs\\log.txt"
    MAX_SIZE_LOG = 4194304000 #500 Megabyte
    MAX_FILES_LOG = 10 # Max files number for logs
    ENCODE = "utf-8"


    # Msg to log
    MSG_CALL_API = "[%s] - StatusCode:%s - %s"
    MSG_CALL_API_ONLY_STATUS_CODE = "[%s] - StatusCode:%s"
    MSG_CALL_DB = "[%s] - %s"
    MSG_CRYPTO = "[%s] - %s"


    # Currency
    DEFAULT_CURRENCY = "EUR"