#!/usr/bin/env python
# -*- coding:utf-8 -*-

import codecs
import re

dict_sfc = {}

for line in codecs.open('/home/yawata/wts/final/tweet_sfc.txt.chasen','r','euc-jp'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur'^(名詞-一般|名詞-サ変接続)',lis[3]):
            if lis[0] in dict_sfc:
                dict_sfc[lis[0]] += 1
            else:
                dict_sfc[lis[0]] = 1

fp = codecs.open('/home/yawata/wts/final/dict_sfc.txt', 'w', 'euc-jp')
for x in sorted(dict_sfc.items(), key=lambda x:x[1],reverse=True):
#print x[0], x[1]
    fp.write("%s %s\n" % (x[0],x[1]))
