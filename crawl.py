#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import tweepy
import codecs


# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# このプログラムの使い方
# python twitter_crawl_sample.py takapon_jp 300 takapon_jp.txt
# python crawl.py  300 list_tweet.txt
max_count = int(sys.argv[1])
outfile = sys.argv[2]

count = 200
tweets = []
oldest = None

while len(tweets) < max_count:
    tmp = api.list_timeline("yocto_0821", "keio-univ-sfc-161", count=count, max_id=oldest)

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

