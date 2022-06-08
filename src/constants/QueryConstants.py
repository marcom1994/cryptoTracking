class QueryConstants:

    RETRIEVE_EXCHANGE_RATE_LAST_CALL = "SELECT timestamp_last_call FROM exchange_rate;"
    RETRIEVE_EXCHANGE_RATE_VALUE = "SELECT exchange_rate_value FROM exchange_rate;"

    UPDATE_OR_INSERT_EXCHANGE_RATE = """
    UPDATE public.exchange_rate SET timestamp_last_call = '%s', exchange_rate_value = '%f';
    INSERT INTO public.exchange_rate (timestamp_last_call, exchange_rate_value) 
        SELECT '%s', '%f'
        WHERE NOT EXISTS (SELECT * FROM public.exchange_rate);
    """

    RETRIEVE_CRYPTO_TO_TRACK = "SELECT id,name,limit_value_buy,limit_value_sell FROM public.crypto_track;"
    UPDATE_CRYPTO_PRICE_BUY_TO_TRACK = "UPDATE public.crypto_track SET limit_value_buy = %s where id=%s;"
    UPDATE_CRYPTO_PRICE_SELL_TO_TRACK = "UPDATE public.crypto_track SET limit_value_sell = %s where id=%s;"
    RETRIEVE_ALL_CRYPTO_ID = "SELECT id, name FROM public.coinlore_api_info;"
    RETRIEVE_CRYPTO_ID_BY_NAME = "SELECT id FROM public.coinlore_api_info WHERE name='%s';"
    