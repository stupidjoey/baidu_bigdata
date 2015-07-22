# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
import pickle



def main():
    starttime = datetime.datetime.now()
    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    target_ent_pinyin = 'linzhengying'
    
    tupupath = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % target_ent_pinyin)
    with open(tupupath) as f:
        tupu_data = f.readlines()


    real_relation = []
    for line in tupu_data:
        data = line[:-1].split('\t')
        relation = data[0].decode('utf-8')
        entity1 = data[1].decode('utf-8')
        entity2 = data[2].decode('utf-8')
        real_relation.append([entity1,entity2])


    predictpath = os.path.join(basepath,'data/predict.%s' % target_ent_pinyin )
    with open(predictpath) as f:  
        predict_tupu_data = f.readlines()

    predict_relation = []
    hit_count = 0 
    for line in predict_tupu_data:
        data = line[:-1].split('\t')
        relation = data[0].decode('utf-8')
        entity1 = data[1].decode('utf-8')
        entity2 = data[2].decode('utf-8')
        predict = [entity1,entity2]
        if predict in real_relation:
            print predict[0],predict[1]
            hit_count += 1

    total_count = len(real_relation)

    hit_rate = hit_count * 1.0 /total_count
    print 'hitcount is %d, hit rate is %f ' % ( hit_count,hit_rate)





    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__== '__main__':
    main()


