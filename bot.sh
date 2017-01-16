#!/bin/sh
#WD=/home/t16298sk/wts3
WD=/home/yawata/wts/final
python ${WD}/crawl_sfc.py 300 ${WD}/tweet_sfc.txt
chasen < ${WD}/tweet_sfc.txt > ${WD}/tweet_sfc.txt.chasen
python ${WD}/crawl_hiyoshi.py 300 ${WD}/tweet_non.txt
chasen < ${WD}/tweet_non.txt > ${WD}/tweet_non.txt.chasen
python ${WD}/hindo_sfc.py
python ${WD}/hindo_non.py
python ${WD}/chi.py
python ${WD}/send.py%
