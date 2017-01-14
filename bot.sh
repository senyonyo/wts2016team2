#!/bin/sh
WD=/home/t16298sk/wts3
python ${WD}/crawl.py 300 ${WD}/tweet_sfc.txt
chasen < ${WD}/tweet_sfc.txt > ${WD}/tweet_sfc.txt.chasen
python ${WD}/bot_sfc.py