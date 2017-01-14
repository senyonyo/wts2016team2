#!/usr/bin/python                                                                                   
# -*- coding: utf-8 -*-                                                                             
   
import tweepy

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

# Mentionの取得                                                                                       
# 自分宛のツイートを取得して表示                                                                      
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.text, tweet.user.screen_name

sfc_ranking01 = "hoge"
sfc_ranking02 = "fuga"
sfc_ranking03 = "hoehoe"

hiyoshi_ranking01 = "haw"
hiyoshi_ranking02 = "yea"
hiyoshi_ranking03 = "aaaaa"

#ツイートを送信                                                                                             
try:
    api.update_status(status='いまSFC生の多くは、' + ' [ ' + sfc_ranking01 + ','+ sfc_ranking02 + ','+
sfc_ranking03 + ' ] ' +'って呟いているよ')
    api.update_status(status='いま日吉生の多くは、' + ' [ ' + hiyoshi_ranking01 + ','+ hiyoshi_ranking02 + ','+ hiyoshi_ranking03 + ' ] ' +'って呟いているよ')
except tweepy.TweepError as e:
    print e

