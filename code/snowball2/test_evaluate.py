# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
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


    relation_map_path = os.path.join(basepath,'data/output/test_relation_map2.pkl')
    relation_map_file = open(relation_map_path)
    relation_map = pickle.load(relation_map_file)
    relation_map_file.close() 

    print len(relation_map.keys())

    # for entity1 in relation_map.keys():
    #     for entity2 in relation_map[entity1].keys():
    #         pair = relation_map[entity1][entity2]
    #         print entity1,entity2,pair[0],pair[1]


    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/all_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])

    user_num = len(all_user_list)


    relation_pair = set()
    for user in all_user_list:
        print 'current user is %s ,%s' % (user[0],user[1])
        target_ent_pinyin = user[0]
        tupupath = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % target_ent_pinyin)
        with open(tupupath) as f:
            tupu_data = f.readlines()
        for line in tupu_data:
            data = line[:-1].split('\t')
            relation = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            pair = (entity1,entity2)
            if relation != u'朋友':
                continue
            if (entity1,entity2) not in relation_pair and (entity2,entity1) not in relation_pair:
                relation_pair.add(pair)


    pair_count = len(relation_pair)
    hit_count = 0.0
    for pair in relation_pair:
        entity1 = pair[0]
        entity2 = pair[1]
        if entity1 in relation_map and entity2 in relation_map[entity1]:
            # print entity1,entity2
            hit_count += 1


    print 'pair_count is %d , hit_count is %d' %(pair_count,hit_count)
    print 'recall  is %f' % (hit_count/pair_count)


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__== '__main__':
    main()


