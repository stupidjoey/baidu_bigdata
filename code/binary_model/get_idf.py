# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import pickle
import math
import feature_tool as ft

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

    data_count = len(dataset)
    idf_dict = {}
    for line in dataset:
        temp_data = []
        data = line[:-1].split('\t')
        entity1 = data[1].decode('utf-8')
        entity2 = data[2].decode('utf-8')
        sentence = data[3].decode('utf-8')
        x = ft.get_word_feature(entity1,entity2,sentence)
        if x == None:
            continue
        x = x[0:8]  # get rid of non-word feature
        wordset = set([ w for w in x if w != 0])
        for w in wordset:
            idf_dict[w] = idf_dict.get(w, 0.0) + 1.0

    for w in idf_dict.keys():
        idf_dict[w] = math.log( data_count / idf_dict[w] )

    idf_dictname = 'data/idf_dict.pkl'
    idf_dictfile = open(os.path.join(basepath,idf_dictname),'w')
    pickle.dump(idf_dict,idf_dictfile)
    idf_dictfile.close()



    # idf_dictname = 'data/idf_dict.pkl'
    # idf_dictfile = open(os.path.join(basepath,idf_dictname))
    # idf_dict = pickle.load(idf_dictfile)
    # idf_dictfile.close()

    # idf_dict = sorted(idf_dict.iteritems(), key = lambda x:x[1], reverse = True)
    # print len(idf_dict)



    # for pair in idf_dict[0:100]:
    #     print pair[0],pair[1]




    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds





if __name__=='__main__':
    main()