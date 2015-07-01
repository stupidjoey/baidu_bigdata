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

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)

    target_ent_pinyin = 'angelababy'
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.%s' % target_ent_pinyin)

    with open(datapath) as f:
        dataset = f.readlines()    

    relation_pair = []
    count = 0 
    data_len = len(dataset)
    print data_len
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
            sen_split = cut_sentence(sentence,entity1,entity2)
            if sen_split == None:
                continue
            # relation = rc.classify(sen_split)
            # if relation == None:
            #     continue
            # relation_pair.append([entity1,entity2,relation])
            
        except Exception, e:
            print e


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

    
    # predictpath = os.path.join(basepath,'data/predict.%s' % target_ent_pinyin )
    # with open(predictpath,'w') as f:   
    #     ent_set = set()
    #     layer = 1
    #     layer_max_count = [10,3,2] 
    #     target_ent_list = [u'angelababy']
    #     while layer <= 3 and len(target_ent_list) != 0:
    #         new_target_ent_list = []
    #         for target_ent in target_ent_list:
    #             ent_set.add(target_ent)  
    #             current_layer = sorted(relation_map[target_ent].iteritems(), key = lambda x:len(x[1]), reverse = True)
    #             layercount = min(len(current_layer), layer_max_count[layer-1])
    #             tempcount = 1
    #             for pair in  current_layer:
    #                 another_ent =  pair[0]
    #                 if another_ent in ent_set:
    #                     continue
    #                 relcount = pair[1]
    #                 relcount = sorted(relcount.iteritems(), key = lambda x: x[1], reverse = True)
    #                 relation = relcount[0][0]
    #                 writeline = '%s\t%s\t%s\n' % (relation,target_ent.encode('utf-8'),another_ent.encode('utf-8'))
    #                 f.write(writeline)
    #                 print writeline
    #                 new_target_ent_list.append(another_ent)
    #                 ent_set.add(another_ent)
    #                 tempcount += 1
    #                 if tempcount > layercount:
    #                     break
    #         target_ent_list = new_target_ent_list[:]
    #         layer += 1





    print 'finished ...'


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


