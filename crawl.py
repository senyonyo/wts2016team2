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
total = 0
oldest = -1

fp = codecs.open(outfile,"w","utf-8")

mentions =  api.list_timeline("yocto_0821","keio-univ-sfc-161",count=200)
if len(mentions) == 0:
    fp.close()
    sys.exit()

for tweet in mentions:
    fp.write("%d\t%s\n" % (total, tweet.text))
    total += 1
    oldest = tweet.id
    if total >= max_count:
        fp.close()
        sys.exit()

if oldest != -1:
    while True:
        #mentions = api.list_timeline(count=count, screen_name=user, max_id=oldest-1)
        mentions =  api.list_timeline("yocto_0821","keio-univ-sfc-161",count=200,max_id=oldest-1)
        if len(mentions) == 0:
            break
        for tweet in mentions:
            fp.write("%d\t%s\n" % (total, tweet.text))
            total += 1
            oldest = tweet.id
            if total >= max_count:
                fp.close()
                sys.exit()
fp.close()
