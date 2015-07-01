# !/usr/bin/env python
# -*- coding: utf-8 -*-

import string
import re
import math
b = string.punctuation
print string.punctuation

b = list(b)
b = [x.decode('utf-8') for x in b]
print b
s = '：'.decode('utf-8')
print s
if s in b:
    print 'ha'

temp = "想做/ 兼_职/学生_/ 的 、加,我Q：  1 5.  8 0. ！！？？  8 6 。0.  2。 3     有,惊,喜,哦"
temp = temp.decode("utf8")
string = re.sub("[\d\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：《》]+".decode("utf8"), "".decode("utf8"),temp)
print string


a = dict()
a[1] = [1,'a','cc']
a[2] = ['gag',[5,6],'d']
print a.values()