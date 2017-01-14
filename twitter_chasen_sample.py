#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import codecs
import re
import tweepy

consumer_key        = ''
consumer_secret     = ''
access_token        = ''
access_token_secret = ''

# Twitter OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.secure = True
auth.set_access_token(access_token, access_token_secret)

# Twitter API
api = tweepy.API(auth)

# 自分のタイムラインを取得
timeline = api.home_timeline(count=10)

# タイムラインのテキストをoutput.txtに書き出し
fp = codecs.open('output.txt', 'w', 'euc-jp')
for tweet in timeline:
    fp.write(tweet.text + "\n")
fp.close()

# 外部コマンドの実行には `os.system()` を使う
# ここでは `from os import system` を宣言済み
system('chasen < output.txt > output.txt.chasen')

dict = {}

for line in codecs.open('output.txt.chasen','r','euc-jp'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur'名詞',lis[3]):
            if lis[0] in dict:
                dict[lis[0]] += 1
            else:
                dict[lis[0]] = 1

for x in sorted(dict.items(), key=lambda x:x[1], reverse=True):
    print x[0], x[1]
