CREATE DATABASE cryptoTracking;


CREATE TABLE public.exchange_rate (
	timestamp_last_call timestamp NULL,
	exchange_rate_value float8 NULL
);

CREATE TABLE public.crypto_track (
	id int4 NOT NULL,
	"name" varchar NULL,
	limit_value_buy float8 NULL,
	limit_value_sell float8 NULL,
	CONSTRAINT crypto_track_pk PRIMARY KEY (id)
);


CREATE TABLE public.coinlore_api_info (
	id int4 NOT NULL,
	"name" varchar NOT NULL,
	CONSTRAINT coinlore_api_info_pk PRIMARY KEY (name)
);