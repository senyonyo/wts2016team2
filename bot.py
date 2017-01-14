#!/usr/bin/python
# -*- coding: utf-8 -*-

consumer_key    = 'l7BzIvdktZtWVZSvOKTQfOcFc'
consumer_secret = 'p2yBRcFvWzSOkzeEsOQB5SFSnom18Aqz8IT0AipjbP6fZHtGSD'
access_token    = '800555565160153088-ZRbyUXU6BztrMkepbNesEMIqeKYQFxw'
access_token_secret = 'Drc4sOJySWbLwCBzXzdKAcxpeeKlY3oHjjaSLQMvzqvIt'

import re
import codecs

dict_sfc = {}
dict_non = {}

#sfcの頻度計算
for line in codecs.open('sfc.txt.chasen','r','euc-jp'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur'名詞',lis[3]):
            if lis[0] in dict_sfc:
                dict_sfc[lis[0]] += 1
            else:
                dict_sfc[lis[0]] = 1

#dict_sfc.txtに書き込む
fp = codecs.open('dict_sfc.txt', 'w', 'euc-jp')

for x in sorted(dict_sfc.items(), key=lambda x:x[1],reverse=True):
    print x[0], x[1]

#nonの頻度計算
for line in codecs.open('non.txt.chasen','r','euc-jp'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur'名詞',lis[3]):
            if lis[0] in dict_sfc:
                dict_non[lis[0]] += 1
            else:
                dict_non[lis[0]] = 1

#dict_non.txtに書き込む
fp = codecs.open('dict_non.txt', 'w', 'euc-jp')

for x in sorted(dict_non.items(), key=lambda x:x[1],reverse=True):
    print x[0], x[1]

#sfc_dict={}
#non_dict={}
#ful_dict={}
#i = 0


#for line in codecs.open("dict_non_sfc.txt","r","euc-jp"):
#line = line.rstrip()
#lis = line.split("\t")
#non_dict[lis[0]]=float(lis[5])


#for line in codecs.open("dict_sfc.txt","r","euc-jp"):
#line = line.rstrip()
#lis = line.split("\t")
#sfc_dict[lis[0]]=float(lis[5])
                #0=wrd,1=part,2=tweets,3=users,4=sum,5=Ratio_tweets,6=Ratio_users


#for k in sorted(sfc_dict.values()):
#print (k, sfc_dict[k])

t = sorted(dict_sfc.iteritems(), key=lambda x:x[1])[:5]
i=1
for x in t:
    print "{0}: {1}".format(*x)
    if dict_sfc[0] in dict_non:
        if dict_sfc[1] > dict_non[1]:
            print dict_sfc[1]
            #ranking01,ranking02,ranking03という変数に代入
            eval('ranking0' + str(i)) == dict_sfc[0]

        else:
            pass

        else:
            pass



# Mentionの取得
# 自分宛のツイートを取得して表示
mentions = api.mentions_timeline(count=10)
for tweet in mentions:
    print tweet.text, tweet.user.screen_name

#ranking01 ='バス'
#ranking02 = '雨'
#ranking03 = '寒い'

#ツイートを送信
try:
    api.update_status(status='今SFC生の多くは、' + ' [ ' + ranking01 + ','+ ranking02 + ','+ ranking03 + ' ] ' +'って呟いているよ')
except tweepy.TweepError as e:
    print e


