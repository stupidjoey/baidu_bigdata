# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
import cPickle as pickle
import relation_classifier as rc


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)

    target_ent_pinyin = 'songqian'
    target_ent_hanyu = u'宋茜'
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.%s' % target_ent_pinyin)

    with open(datapath) as f:
        dataset = f.readlines()    

    relation_pair = []
    count = 0
    data_len = len(dataset)
    for line in dataset:
        try:
            count += 1
            if count % ( data_len/5 ) == 0:
                print '20%...'
            data = line[:-1].split('\t')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            sentence = data[0].decode('utf-8')
            sentence_len = len(sentence)
            if sentence_len < 10 or sentence_len > 30:
                continue
            pos1 = sentence.find(entity1)
            pos2 = sentence.find(entity2)

            if pos1 < pos2:
                midstr = sentence[pos1+len(entity1):pos2]
            else:
                midstr = sentence[pos2+len(entity2):pos1]

            if len(midstr) > 5:
                continue

            if u'朋友' in midstr or u'好友' in midstr:
                if u'男' not in midstr and u'女' not in midstr:
                    print  sentence,entity1,entity2
                    relation_pair.append([entity1,entity2])
            
        except Exception, e:
            print e

    print len(relation_pair)

    # relation_map = dict()
    # for pair in relation_pair:
    #     entity1 = pair[0]
    #     entity2 = pair[1]
    #     relation = pair[2]
    #     relation_map.setdefault(entity1,dict())
    #     relation_map[entity1].setdefault(entity2,dict())
    #     relation_map[entity1][entity2][relation] = relation_map[entity1][entity2].get(relation, 0) + 1

    #     relation_map.setdefault(entity2,dict())
    #     relation_map[entity2].setdefault(entity1,dict())
    #     relation_map[entity2][entity1][relation] = relation_map[entity2][entity1].get(relation, 0) + 1

    



    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    







if __name__== '__main__':
    main()


