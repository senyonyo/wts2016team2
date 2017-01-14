import sys
import tweepy
import codecs

consumer_key        = 'l7BzIvdktZtWVZSvOKTQfOcFc'
consumer_secret     = 'p2yBRcFvWzSOkzeEsOQB5SFSnom18Aqz8IT0AipjbP6fZHtGSD'
access_token        = '800555565160153088-ZRbyUXU6BztrMkepbNesEMIqeKYQFxw'
access_token_secret = 'Drc4sOJySWbLwCBzXzdKAcxpeeKlY3oHjjaSLQMvzqvIt'

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# python crawl.py  300 list_tweet.txt
max_count = int(sys.argv[1])
outfile = sys.argv[2]

count = 200
tweets = []
oldest = None

while len(tweets) < max_count:
    tmp = api.list_timeline("tmi_intro", "keio", count=count, max_id=oldest)

    if len(tmp) == 0:
        break

    oldest = tmp[-1].id
    tweets += tmp

with codecs.open(outfile,"w","euc-jp") as fp:
    for i, tweet in enumerate(tweets[:max_count]):
        try:
            fp.write("%d\t%s\n" % (i, tweet.text))
        except:
            pass

fp.close()

