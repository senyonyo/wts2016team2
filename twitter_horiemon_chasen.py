#!/usr/bin/python                                                              
# -*- coding: utf-8 -*-

import re
import codecs

dict_horie = {}

for line in codecs.open('horie3_3.txt.chasen','r','euc-jp'):
    line = line.rstrip('\r\n')
    if line == "EOS":
        pass
    else:
        lis = line.split("\t")
        if re.search(ur'名詞',lis[3]):
            if lis[0] in dict_horie:
                dict_horie[lis[0]] += 1
            else:
                dict_horie[lis[0]] = 1

fp = codecs.open('dict_horie.txt', 'w', 'euc-jp')

for x in sorted(dict_horie.items(), key=lambda x:x[1],reverse=True):
    print x[0], x[1]
