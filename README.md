# cryptoTracking

## Installing
### Create /files/properties/configAPI.properties and insert into this:
[APICoinLoreSection]
X-RapidAPI-Host=coinlore-cryptocurrency.p.rapidapi.com
X-RapidAPI-Key=<your-key>

[APIAlphaVantageSection]
X-RapidAPI-Host=alpha-vantage.p.rapidapi.com
X-RapidAPI-Key=<your-key>

### Create /files/properties/configTelegram.properties and insert into this:
[TelegramBot]
token=<yuor-token>
chat-id=<your-chat-id>

### Create DB cryptoTracking and execute /files/db/DDL.sql e /files/db/DML.sql

### Install library in /files/lib/requirements.txt

