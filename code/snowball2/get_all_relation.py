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

''' get all kinds of relations from the tupu data  '''
def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)


    relation_dict = dict()

    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            relation_dict.setdefault(rel,0)
            relation_dict[rel] += 1
         

    relation_dict = sorted(relation_dict.iteritems(), key = lambda x:x[1], reverse = True)
    # for rel in relation_dict.keys():
        # print rel,relation_dict[rel]
    count =0 
    for pair in relation_dict:
        print pair[0],pair[1]
        count += int(pair[1])
    print count


    rel_path  =  os.path.join(basepath,'data/all_relation.txt')
    with open(rel_path,'w') as f:
        for pair in relation_dict:
            writestr = '%s\t%s\n' % (pair[0].encode('utf-8'),pair[1])
            f.write(writestr)








    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
