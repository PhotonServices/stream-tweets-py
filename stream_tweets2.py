from TwitterAPI import TwitterAPI


TRACK_TERM = '#EverySimpsonsEver'


CONSUMER_KEY = '9pBBabr7MpVbpOk7YPOx3RjYy'
CONSUMER_SECRET = 'LH7A7jMjQqYXNK07WOIKqZv9tEBrovDmWv40Sg2Md61EjwPdEj'
ACCESS_TOKEN_KEY = '19495636-lcYOEgKPfOp4xky5CTGQwzf5VdZuIcVV1ifGOi3ss'
ACCESS_TOKEN_SECRET = 'I4O0FciZA8HxqGgC6jEz6oS21kHWObPChLpI9Syd299Jf'


api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track': TRACK_TERM})

for item in r:
    print(item['text'] if 'text' in item else item)
