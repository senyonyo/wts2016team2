#!/usr/bin/python                                                  
# -*- coding: utf-8 -*-                                            

import tweepy
import re
import codecs


consumer_key    = ''
consumer_secret = ''
access_token    = ''
access_token_secret = ''

# Twitter OAuth                                                    
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token,access_token_secret)

# Twitter API                                                      
api = tweepy.API(auth)

rank_sfc = []
rank_non = []
#i = 1
#j = 1
for line in codecs.open('/home/yawata/wts/final/sfc_rank.txt','r','euc-jp'):
    line = line.rstrip('\r\n')
    lis = line.split(" ")
    if re.search('sfc:',lis[0]):
        rank_sfc.append(lis[1])
    elif re.search('non:',lis[0]):
        rank_non.append(lis[1])
    else:
        pass
# Mentionの取得                                                    
# 自分宛のツイートを取得して表示                                   
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.text, tweet.user.screen_name

#ツイートを送信                                                    
try:
    api.update_status(status=u'いまSFC生の多くは、' + u' [ 1位: ' + rank_sfc[0] + u', 2位: ' + rank_sfc[1] + u', 3位: ' + rank_sfc[2] + u' ] ' + u'って呟いているよ #sfc_rank_tweet')
except tweepy.TweepError as e:
    print e


try:
    api.update_status(status=u'いま日吉生の多くは、' + u' [ 1位: ' + rank_non[0] + u', 2位: '+ rank_non[1]+ u' ,3位: ' + rank_non[2] + u' ] ' + u'って呟いているよ #hiyoshi_rank_tweet')
except tweepy.TweepError as e:
    print e

