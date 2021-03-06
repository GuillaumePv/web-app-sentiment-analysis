from psaw import PushshiftAPI
import datetime as dt
import json

subreddits=[
    'CryptoCurrency',
    'Bitcoin',
    'Crypto_Currency_News',
    'CryptoMarkets'
]
api = PushshiftAPI()

start_epoch=int(dt.datetime(2021, 2, 1).timestamp())

submissions = api.search_submissions(after=start_epoch,
                            subreddit='CryptoCurrency',
                            filter=['url','author', 'title', 'subreddit'],
                            limit=100)

with open('db/stocks.json') as json_file:
    stocks = json.load(json_file)

data = {}
for sub in submissions:

    words = sub.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'),words)))
    print(sub)
    print(cashtags)
#     if len(cashtags) > 0:
#         for cashtag in cashtags:
#             if cashtag.split("$")[1] in stocks.keys():
#                 print(f'found one stock {cashtag.split("$")[1]}')
#                 data[cashtag.split("$")[1]] = {
#                     'title': sub.title,
#                     'author': sub.author,
#                     'date': dt.datetime.utcfromtimestamp(sub.created_utc).strftime('%Y-%m-%d'),
#                     'url': sub.url
#                 }

# with open('db/reddit/wsb/wsb.json', 'w',encoding='utf-8') as outfile:
#     json.dump(data, outfile,indent=4,ensure_ascii=False)

