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


    # dictpath = os.path.join(basepath,'data/myDict.txt')
    # jieba.load_userdict(dictpath)
    # datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.poyoutian')
    # with open(datapath) as f:
    #     dataset = f.readlines()    

    # trans_dataset = []
    # newtrans_dataset = []
    # relationset = set()
    # rel = u'女友'
    # name = [u'朴有天',u'朴嘉熙']
    # for line in dataset[:]:
    #     data = line[:-1].split('\t')
    #     entity1 = data[1]
    #     entity2 = data[2]
    #     sentence = data[0]
    #     sentence_dec = sentence.decode('utf-8')
    #     if sentence_dec.find(rel) == -1:
    #         continue
    #     if entity1.decode('utf-8') not in name:
    #         continue
    #     if entity2.decode('utf-8') not in name:
    #         continue

    #     words = pseg.cut(sentence)
    #     posList = []
    #     ent_pos_idx = []    

    #     for w in words:
    #         # print "%s %s %s "  % (w.word, w.flag,posdict[w.flag])
    #         posList.append(w.flag)
    #         if w.word == entity1.decode('utf-8') or w.word ==entity2.decode('utf-8'):
    #             ent_pos_idx.append(len(posList) - 1)
    #     if len(ent_pos_idx) != 2 :
    #         continue

    #     trans_dataset.append([entity1,entity2,sentence])
    #     newtrans_dataset.append([entity1.decode('utf-8'),entity2.decode('utf-8'),sentence.decode('utf-8')])

    # posdictpath = os.path.join(basepath,'data/posdict.txt')
    # with open(posdictpath) as f:
    #     posdata = f.readlines()    
    
    # posdict = dict()
    # for line in posdata:
    #     data = line[:-1].split('\t')
    #     pos  = data[0]
    #     num = data[1]
    #     posdict[pos] = num

    # xtest = ft.get_feature(trans_dataset,posdict)

    # xtest = np.array(xtest)

    # testfile = open(os.path.join(basepath,'data/test.pkl'),'w')
    # pickle.dump(xtest,testfile)
    # testfile.close()

    # trans_datafile = open(os.path.join(basepath,'data/trans_test.pkl'),'w')
    # pickle.dump(newtrans_dataset,trans_datafile)
    # trans_datafile.close()





    testfile = open(os.path.join(basepath,'data/test.pkl'))
    xtest = pickle.load(testfile)
    testfile.close()


    trans_datafile = open(os.path.join(basepath,'data/trans_test.pkl'))
    trans_data = pickle.load(trans_datafile)
    trans_datafile.close()


    modelfile  = open(os.path.join(basepath,'data/classifier/qiannvyou_rf.pkl'))
    clf = pickle.load(modelfile)
    modelfile.close()
    predY = []
    count = 0
    idxList = []
    for x in xtest:
        predY.append(clf.predict(x))
        if clf.predict(x) == 1:
            idxList.append(count)
        count += 1
    predY = np.array(predY)




    idx = predY == 1
    

    for i in idxList:
        print trans_data[i][0].encode('utf-8'),trans_data[i][1].encode('utf-8'),trans_data[i][2].encode('utf-8')

    print sum(idx),len(idxList)

    for data in trans_data:
        print data[0].encode('utf-8'),data[1].encode('utf-8'),data[2].encode('utf-8')


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    






if __name__== '__main__':
    main()
