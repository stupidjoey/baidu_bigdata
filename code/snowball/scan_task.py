# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)
    datapath = os.path.join(basepath,'data/train/relation_train/task1.trainSentence')
    with open(datapath) as f:
        dataset = f.readlines()    

    target_rel = u'朋友'
    for line in dataset:
        try:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            sentence = data[3].decode('utf-8')
            mark = int(data[4])
            if rel == target_rel:
                if mark == 1:
                    print sentence,entity1,entity2
        except Exception, e:
            print e

  

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
