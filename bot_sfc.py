#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import codecs

dict_sfc = {}
dict_non = {}

#sfcの頻度計算
for line in codecs.open('/home/t16298sk/wts3/tweet_sfc.txt.chasen','r','euc-jp'):
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
fp = codecs.open('/home/t16298sk/wts3/dict_sfc.txt', 'w', 'euc-jp')

for x in sorted(dict_sfc.items(), key=lambda x:x[1],reverse=True):
    print x[0], x[1]
