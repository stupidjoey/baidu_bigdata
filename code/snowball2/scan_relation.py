# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import numpy as np
import pickle
import relation_classifier as rc

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    target_relation = u'好友'
    target_relation_pinyin = 'haoyou'

    relation_sentence_path = os.path.join(basepath,'data/relation_sentence/%s.txt' % target_relation_pinyin)
    with open(relation_sentence_path) as f:
        for line in f:
            try:
                data = line[:-1].split('\t')
                entity1 = data[1].decode('utf-8')
                entity2 = data[2].decode('utf-8')
                sentence = data[0].decode('utf-8')
                if u'好友' not in sentence:
                    continue
                print line
            except Exception, e:
                print e

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__== '__main__':
    main()
