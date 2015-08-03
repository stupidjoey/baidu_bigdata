# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
import pickle

''' get all kinds of relations from the tupu data  '''
def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])


    #  get the original relation count
    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)

    orig_relation_dict = dict()

    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            orig_relation_dict.setdefault(rel,set())
            if (entity1,entity2) not in orig_relation_dict[rel] and (entity2,entity1) not in orig_relation_dict[rel]:
                pair = (entity1,entity2)
                orig_relation_dict[rel].add(pair)
         
    for rel in orig_relation_dict.keys():
        pairset = orig_relation_dict[rel]
        orig_relation_dict[rel] = len(pairset)


    # get the predicted relation count  
    par_datapath = os.path.join(basepath,'data/output/predict/')
    filenamelist = os.listdir(par_datapath)

    hit_dict_file = open(os.path.join(basepath,'data/info/relation_hit_dict.pkl'))
    relation_hit_dict = pickle.load(hit_dict_file)
    hit_dict_file.close()

    match_dict_file = open(os.path.join(basepath,'data/info/relation_match_dict.pkl'))
    relation_match_dict = pickle.load(match_dict_file)
    match_dict_file.close()


    relation_dict = dict()

    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/output/predict/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            relation_dict.setdefault(rel,set())
            if (entity1,entity2) not in relation_dict[rel] and (entity2,entity1) not in relation_dict[rel]:
                pair = (entity1,entity2)
                relation_dict[rel].add(pair)
         

    for rel in relation_dict.keys():
        pairset = relation_dict[rel]
        relation_dict[rel] = len(pairset)

    relation_dict = sorted(relation_dict.iteritems(), key = lambda x:x[1], reverse = True)

    count =0 
    for pair in relation_dict:
        print pair[0],pair[1]
        count += int(pair[1])
    print count


    rel_path  =  os.path.join(basepath,'data/info/all_predict_relation2.txt')
    with open(rel_path,'w') as f:
        writestr = 'rel\t\tpred/orig\t\thit\t\tmatch\n'
        f.write(writestr)
        for pair in relation_dict:
            hit_count = 0
            match_count = 0
            orig_count = 0
            if pair[0] in relation_hit_dict:
                hit_count = relation_hit_dict[pair[0]]
            if pair[0] in relation_match_dict:
                match_count = relation_match_dict[pair[0]]
            if pair[0] in orig_relation_dict:
                orig_count = orig_relation_dict[pair[0]]
            writestr = '%s\t\t%d/%d\t\t%d\t\t%d\n' % (pair[0].encode('utf-8'),pair[1],orig_count,hit_count,match_count)
            f.write(writestr)








    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
