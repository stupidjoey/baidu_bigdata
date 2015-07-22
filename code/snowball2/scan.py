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
import relation_classifier as rc

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)

    target_ent_pinyin = 'songzhixiao'
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.songzhixiao')
    
    with open(datapath) as f:
        dataset = f.readlines()    

    target_ent_list = [u'宋智孝']

    layer = 1
    layercount = [10,3,2]
    while layer <= 3:
        new_target_ent_list = []
        for target_ent in target_ent_list:
            relation_dict = dict()
            for line in dataset:
                try:
                    data = line[:-1].split('\t')
                    entity1 = data[1].decode('utf-8')
                    entity2 = data[2].decode('utf-8')
                    if entity1 != target_ent and entity2 != target_ent:
                        continue

                    sentence = data[0].decode('utf-8')
                    sen_split = cut_sentence(sentence,entity1,entity2)
                    if sen_split == None:
                        continue
                    relation = rc.classify(sen_split)
                    if relation == None:
                        continue

                    another_ent = ''
                    if entity1 == target_ent:
                        another_ent = entity2
                    else:
                        another_ent = entity1
                    relation_dict.setdefault(another_ent,dict())
                    relation_dict[another_ent][relation] = relation_dict[another_ent].get(relation, 0) + 1

                except Exception, e:
                    print e

            relation_dict = sorted(relation_dict.iteritems(), key = lambda x:len(x[1]), reverse = True)

            predictpath = os.path.join(basepath,'data/predict.%s' % target_ent_pinyin )

            with open(predictpath,'a') as f:   
                for pair in  relation_dict[0:layercount[layer-1]]:
                    another_ent =  pair[0]
                    relcount = pair[1]
                    relcount = sorted(relcount.iteritems(), key = lambda x: x[1], reverse = True)
                    relation = relcount[0][0]
                    writeline = '%s\t%s\t%s\n' % (relation,target_ent.encode('utf-8'),another_ent.encode('utf-8'))
                    f.write(writeline)
                    new_target_ent_list.append(another_ent)

        target_ent_list = new_target_ent_list[:]    
        print 'current layer is %d'  % layer
        layer += 1


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    




def cut_sentence(sentence,entity1,entity2):
    seg_list = list( jieba.cut(sentence, cut_all = 'True') )
    
    entity_idx_set = []
    for idx,w in enumerate(seg_list):
        if w == entity1 or w == entity2:
            entity_idx_set.append(idx)
    if len(entity_idx_set) != 2:
        return None
    ent_idx1 = entity_idx_set[0]
    ent_idx2 = entity_idx_set[1]

    return [seg_list[0:ent_idx1],seg_list[ent_idx1+1:ent_idx2],seg_list[ent_idx2+1:],seg_list]




if __name__== '__main__':
    main()
