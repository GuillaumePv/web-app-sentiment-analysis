import config
import alpaca_trade_api as tradeapi
import json

api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)

assets = api.list_assets()

data = {}

for asset in assets:
    if asset.status == 'active':
        data[asset.symbol] = {
            'name': asset.name,
            'exchange':asset.exchange,
            'shortable': asset.shortable,
        }
        print(f'stocks registred : {asset.name} / {asset.symbol}')

print(len(data))

with open('db/stocks.json', 'w') as outfile:
    json.dump(data, outfile,indent=4)

