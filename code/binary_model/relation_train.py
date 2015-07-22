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
from sklearn import svm


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])
    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)
    datapath = os.path.join(basepath,'data/train/relation_train/task1.trainSentence')


    idf_dictname = 'data/idf_dict.pkl'
    idf_dictfile = open(os.path.join(basepath,idf_dictname))
    idf_dict = pickle.load(idf_dictfile)
    idf_dictfile.close()

    with open(datapath) as f:
        dataset = f.readlines()    


    feature_num = min(3000, len(idf_dict.keys()))
    xmat = []
    ymat = []
    for line in dataset:
        temp_data = []
        data = line[:-1].split('\t')

        entity1 = data[1].decode('utf-8')
        entity2 = data[2].decode('utf-8')
        sentence = data[3].decode('utf-8')
        x = ft.get_word_feature(entity1,entity2,sentence)
        if x == None:
            continue

        x = ft.feature2vec(x, idf_dict, feature_num)
        xmat.append(x)
        ymat.append(int(data[4]))





    print 'start building model...'
    

    # # random forest... 
    # clf = RandomForestClassifier(n_estimators=50)
    # clf = clf.fit(xmat, ymat)


    # print 'store the model...' 
    # modelname = 'data/classifier/binary_relation_rf.pkl' 
    # modelfile  = open(os.path.join(basepath,modelname),'w')
    # pickle.dump(clf,modelfile)
    # modelfile.close()



    clf = svm.SVC(kernel='linear',C = 1.0,cache_size= 1000 )
    clf.fit(xmat, ymat)

    modelname = 'data/classifier/binary_relation_svm.pkl' 
    modelfile  = open(os.path.join(basepath,modelname),'w')
    pickle.dump(clf ,modelfile)
    modelfile.close()




    print 'finished...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds





if __name__== '__main__':
    main()