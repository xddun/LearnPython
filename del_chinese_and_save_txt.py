# -!- coding=utf-8 -!-
import re
import sys

f = open('q.txt', 'r', encoding='UTF-8')

txts = ''
txts = f.read()

m = re.findall(r'[^\u4e00-\u9fa5]', txts)

strresult = ''
fq = open('result.txt', 'w', encoding='UTF-8')
strresult = strresult.join(m)

fq.write(strresult)
 
# English book
