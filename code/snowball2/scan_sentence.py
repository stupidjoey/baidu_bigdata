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


    target_ent_pinyin = 'songzhixiao'
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.%s' % target_ent_pinyin)
    
    with open(datapath) as f:
        dataset = f.readlines()    

    entity_set = [u'李栋旭',u'李多海']
    rel = u'绯闻'
    for line in dataset:
        try:
            data = line[:-1].split('\t')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            if entity1 not in  entity_set or entity2 not in entity_set:
                continue
            sentence = data[0].decode('utf-8')
            if rel not in sentence:
                continue
            sentence_len = len(sentence)
            if sentence_len < 10 or sentence_len > 30:
                continue
            print sentence

        except Exception, e:
            print e

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    




if __name__== '__main__':
    main()
