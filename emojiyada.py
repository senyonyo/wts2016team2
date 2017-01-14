#!/usr/bin/python
# -*- coding:utf-8 -*-

import codecs

for line in codecs.open("horie3_2.txt.chasen","r","euc-jp"):
    line = line.rstrip('\r\n')
    print line
