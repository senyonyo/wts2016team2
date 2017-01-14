#!/usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import re
import math

sfc_dict={}
non_dict={}
ful_dict={}
i = 0


for line in codecs.open("dict_non_sfc.txt","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    non_dict[lis[0]]=float(lis[5])


for line in codecs.open("dict_sfc.txt","r","euc-jp"):
    line = line.rstrip()
    lis = line.split("\t")
    sfc_dict[lis[0]]=float(lis[5])
    #0=wrd,1=part,2=tweets,3=users,4=sum,5=Ratio_tweets,6=Ratio_users


for k in sorted(sfc_dict.values()):
    print (k, sfc_dict[k])

t = sorted(sfc_dict.iteritems(), key=lambda x:x[1])[:5]

for x in t:
    print "{0}: {1}".format(*x)
    if sfc_dict[0] in non_dict:
        if sfc_dict[5] > non_dict[5]:
            print sfc_dict[5]
        else:
            pass

    else:
        pass
    


    


    
