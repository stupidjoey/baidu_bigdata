# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import feature_tool as ft
import pickle


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.poyoutian')



    idf_dictname = 'data/idf_dict.pkl'
    idf_dictfile = open(os.path.join(basepath,idf_dictname))
    idf_dict = pickle.load(idf_dictfile)
    idf_dictfile.close()

    modelname = 'data/classifier/binary_relation_rf.pkl' 
    modelfile  = open(os.path.join(basepath,modelname))
    clf = pickle.load(modelfile)
    modelfile.close()


    rel_datapath = os.path.join(basepath,'data/relation_pair.txt')
    with open(rel_datapath) as f:
        rel_dataset = f.readlines()  

    rel_dict = dict()
    for line in rel_dataset:
        data = line[:-1].split('\t')
        key = data[0].decode('utf-8')
        rel_dict[key] = []
        for d in data:
            rel_dict[key].append(d.decode('utf-8'))

    with open(datapath) as f:
        dataset = f.readlines()    


    for line in dataset[:]:
        data = line[:-1].split('\t')
        entity1 = data[1].decode('utf-8')
        entity2 = data[2].decode('utf-8')
        sentence = data[0].decode('utf-8')

        x = ft.get_word_feature(entity1,entity2,sentence, rel_dict )
        if x == None:
            continue
        x = ft.feature2vec(x, idf_dict, 3000)

        if clf.predict(x) == 1:
            print sentence + '\t' + entity1 + '\t' + entity2


    # ************************************************************************
    # ************************************************************************


  


    # final_rel_dict = dict()

    # for rel_idx,rel_pinyin in enumerate(relation_pinyin):
    #     rel = relation[rel_idx]
    #     print rel
    #     print rel_pinyin

    #     testname = 'data/%s/%s_test.pkl' % (name_pinyin,rel_pinyin)
    #     testfile = open(os.path.join(basepath,testname))
    #     xtest = pickle.load(testfile)
    #     testfile.close()

    #     transname = 'data/%s/%s_trans_test.pkl' % (name_pinyin,rel_pinyin)
    #     trans_datafile = open(os.path.join(basepath,transname))
    #     trans_data = pickle.load(trans_datafile)
    #     trans_datafile.close()


    #     modelname = 'data/classifier/%s_rf.pkl' % rel_pinyin
    #     modelfile  = open(os.path.join(basepath, modelname))
    #     clf = pickle.load(modelfile)
    #     modelfile.close()

    #     predY = []
    #     count = 0
    #     idxList = []
    #     for x in xtest:
    #         predY.append(clf.predict(x))
    #         if clf.predict(x) == 1:
    #             idxList.append(count)
    #         count += 1
    #     predY = np.array(predY)

    #     idx = predY == 1
        

    #     final_rel_dict[rel] = set()
    #     for i in idxList:
    #         ent1 = trans_data[i][0]
    #         ent2 = trans_data[i][1]
    #         # print trans_data[i][0],trans_data[i][1],trans_data[i][2]
    #         if ent1.decode('utf-8') != name:
    #             final_rel_dict[rel].add(ent1)
    #         if ent2.decode('utf-8') != name:
    #             final_rel_dict[rel].add(ent2)

    # for rel in final_rel_dict.keys():
    #     print '*********************************'
    #     print '%s:' % rel 
    #     for n in  final_rel_dict[rel]:
    #         print n
        


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
