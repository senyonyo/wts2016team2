#!/usr/bin/python                                                  
# -*- coding: utf-8 -*-                                            

import tweepy
import re
import codecs


consumer_key    = 'l7BzIvdktZtWVZSvOKTQfOcFc'
consumer_secret = 'p2yBRcFvWzSOkzeEsOQB5SFSnom18Aqz8IT0AipjbP6fZHtGSD'
access_token    = '800555565160153088-ZRbyUXU6BztrMkepbNesEMIqeKYQFxw'
access_token_secret = 'Drc4sOJySWbLwCBzXzdKAcxpeeKlY3oHjjaSLQMvzqvIt'

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
#       eval('sfc_ranking0' + str(i)) == lis[1]
#       i += 1
        rank_sfc.append(lis[1])
    elif re.search('non:',lis[0]):
#       eval('hiyoshi_ranking0' + str(j)) == lis[1]
#       j += 1
        rank_non.append(lis[1])
    else:
        pass
for i in rank_sfc:
    print i
for i in rank_non:
    print i

# Mentionの取得                                                    
# 自分宛のツイートを取得して表示                                   
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.text, tweet.user.screen_name


#sfc_ranking02 = "fuga"
#sfc_ranking03 = "hoehoe"

#hiyoshi_ranking01 = "haw"
#hiyoshi_ranking02 = "yea"
#hiyoshi_ranking03 = "aaaaa"

#ツイートを送信                                                    
try:
    api.update_status(status=u'いまSFC生の多くは、' + u' [ ' + rank_sfc[0] + u',' + rank_sfc[1] + u',' + rank_sfc[2] + u' ] ' + u'って呟いているよ')
except tweepy.TweepError as e:
    print e


try:
    api.update_status(status=u'いま日吉生の多くは、' + u' [ ' + rank_non[0] + u','+ rank_non[1]+ u',' + rank_non[2] + u' ] ' + u'って呟いているよ')
except tweepy.TweepError as e:
    print e
