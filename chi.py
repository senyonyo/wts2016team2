#!/usr/bin/python                                                  
# -*- coding: utf-8 -*-                                            
import tweepy
import codecs
import re

sfc_list = []
non_list = []

all_list = []

sfc_dic = {}
non_dic = {}

sfc_chi_dic = {}
non_chi_dic = {}


for line in codecs.open("/home/yawata/wts/final/dict_non.txt","r","euc-jp"):
    line = line.rstrip()
    lis = line.split(" ")
    non_dic[lis[0]] = int(lis[1])
    if lis[0] not in all_list:
        if re.search(ur'ちんぽ', lis[0]):
            pass
        else:
            all_list.append(lis[0])

for line in codecs.open("/home/yawata/wts/final/dict_sfc.txt","r","euc-jp"):
    line = line.rstrip()
    lis = line.split(" ")
    sfc_dic[lis[0]] = int(lis[1])
    if lis[0] not in all_list:
        if re.search(ur'ちんぽ', lis[0]):
            pass
        else:
            all_list.append(lis[0])

for w in all_list:

    x = 0
    y = 0

    if w in non_dic and w in sfc_dic:
        x = sfc_dic[w]
        y = non_dic[w]
    elif w in non_dic and w not in sfc_dic:
        y = non_dic[w]
    elif w not in non_dic and w in sfc_dic:
        x = sfc_dic[w]

    z = x + y
    a = float(z/2.0)
    b = float(z/2.0)

    chi_sv_sfc = float((x - a) **2 /a )
    chi_sv_non = float((y - b) **2 /b )
    chi_square_value = float(chi_sv_sfc + chi_sv_non)
    if chi_square_value > 3 and z > 4:
        if re.search(ur"^[ぁ-んァ-ン]$",w):
            pass
        else:
#            print ("%d %d %f %f %f %s" % (x, y, chi_sv_sfc, chi_sv_non, chi_square_value, w))
            if x > y:
                sfc_chi_dic[w] = chi_square_value
            elif x < y:
                non_chi_dic[w] = chi_square_value
            else:
                pass

fp = codecs.open('/home/yawata/wts/final/sfc_rank.txt','w', 'euc-jp')
sfc_rank = []
non_rank = []
#print "sfc"
for key in sorted(sfc_chi_dic.items(),key=lambda x:x[1],reverse=True):
    sfc_rank.append(key[0])

#    print key[0],key[1]
for i in sfc_rank[0:3]:
    fp.write("sfc: %s\n" % (i))

#print "non"
for key in sorted(non_chi_dic.items(),key=lambda x:x[1],reverse=True):
    non_rank.append(key[0])
#    print key[0],key[1]
for i in non_rank[0:3]:
    fp.write("non: %s\n" % (i))






#for sfc in sfc_list:
    #print "{0}: {1}".format(sfc[0].encode('utf-8'), sfc[1])
#    sfc_word = sfc[0]
#    sfc_count = int(sfc[1])
#    for non in non_list:
#        non_word = non[0]
#        non_count = int(non[1])

#        if sfc_word == non_word:
#            if sfc_count > non_count:
#                fp.write("sfc: %s\n" % (sfc_word))
#            else:
#                fp.write("non: %s\n" % (non_word))



