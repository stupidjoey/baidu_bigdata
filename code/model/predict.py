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

    relation = [u'老师', u'妻子', u'同学', u'撞衫', u'前妻', u'前女友', u'老乡', u'传闻不和', u'经纪人', u'绯闻女友', u'闺蜜', u'偶像']
    relation_pinyin = ['laoshi','qizi','tongxue','zhuangshan','qianqi','qiannvyou','laoxiang','chuanwenbuhe','jingjiren','feiwennvyou','guimi','ouxiang']
    
    # name = u'朴有天'
    # name_pinyin = 'poyoutian'

    # name = u'邱胜翊'
    # name_pinyin = 'qiushengyi'

    name = u'宋茜'
    name_pinyin = 'songqian'
    
    # name = u'宋智孝'
    # name_pinyin = 'songzhixiao'
  

    # rel_datapath = os.path.join(basepath,'data/relation_pair.txt')
    # with open(rel_datapath) as f:
    #     rel_dataset = f.readlines()  

    # reldict = dict()
    # for line in rel_dataset:
    #     data = line[:-1].split('\t')
    #     reldict[data[0].decode('utf-8')] = []
    #     for d in data:
    #         d = d.decode('utf-8')
    #         reldict[data[0].decode('utf-8')].append(d)

    # with open(datapath) as f:
    #     dataset = f.readlines()    


    # for rel in reldict.keys():
    #     trans_dataset = []
    #     print rel
    #     relset = reldict[rel]
    #     for r in relset:
    #         print r
    #     rel_idx = relation.index(rel)
    #     rel_pinyin = relation_pinyin[rel_idx]
    #     for line in dataset[:]:
    #         data = line[:-1].split('\t')
    #         entity1 = data[1]
    #         entity2 = data[2] 
    #         sentence = data[0]
    #         sentence_dec = sentence.decode('utf-8')
    #         if entity1.decode('utf-8') != name and entity2.decode('utf-8') != name:
    #             continue
    #         hasrel = False
    #         for r in relset:
    #             if r in sentence_dec:
    #                 hasrel = True
    #         if hasrel == False:
    #             continue

    #         # print sentence

    #         words = pseg.cut(sentence)
    #         posList = []
    #         ent_pos_idx = []    

    #         for w in words:
    #             # print "%s %s %s "  % (w.word, w.flag,posdict[w.flag])
    #             posList.append(w.flag)
    #             if w.word == entity1.decode('utf-8') or w.word ==entity2.decode('utf-8'):
    #                 ent_pos_idx.append(len(posList) - 1)
    #         if len(ent_pos_idx) != 2:
    #             continue


    #         trans_dataset.append([entity1,entity2,sentence])
           
    #     posdictpath = os.path.join(basepath,'data/posdict.txt')
    #     with open(posdictpath) as f:
    #         posdata = f.readlines()    
        
    #     posdict = dict()
    #     for line in posdata:
    #         data = line[:-1].split('\t')
    #         pos  = data[0]
    #         num = data[1]
    #         posdict[pos] = num

    #     xtest = ft.get_feature(trans_dataset,posdict)
    #     xtest = np.array(xtest)

    #     testname = 'data/%s/%s_test.pkl' % (name_pinyin,rel_pinyin)
    #     testfile = open(os.path.join(basepath,testname),'w')
    #     pickle.dump(xtest,testfile)
    #     testfile.close()


    #     transname = 'data/%s/%s_trans_test.pkl' % (name_pinyin,rel_pinyin)
    #     trans_datafile = open(os.path.join(basepath,transname),'w')
    #     pickle.dump(trans_dataset,trans_datafile)
    #     trans_datafile.close()


    # ************************************************************************
    # ************************************************************************


  


    final_rel_dict = dict()

    for rel_idx,rel_pinyin in enumerate(relation_pinyin):
        rel = relation[rel_idx]
        print rel
        print rel_pinyin

        testname = 'data/%s/%s_test.pkl' % (name_pinyin,rel_pinyin)
        testfile = open(os.path.join(basepath,testname))
        xtest = pickle.load(testfile)
        testfile.close()

        transname = 'data/%s/%s_trans_test.pkl' % (name_pinyin,rel_pinyin)
        trans_datafile = open(os.path.join(basepath,transname))
        trans_data = pickle.load(trans_datafile)
        trans_datafile.close()


        modelname = 'data/classifier/%s_rf.pkl' % rel_pinyin
        modelfile  = open(os.path.join(basepath, modelname))
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
        

        final_rel_dict[rel] = set()
        for i in idxList:
            ent1 = trans_data[i][0]
            ent2 = trans_data[i][1]
            # print trans_data[i][0],trans_data[i][1],trans_data[i][2]
            if ent1.decode('utf-8') != name:
                final_rel_dict[rel].add(ent1)
            if ent2.decode('utf-8') != name:
                final_rel_dict[rel].add(ent2)

    for rel in final_rel_dict.keys():
        print '*********************************'
        print '%s:' % rel 
        for n in  final_rel_dict[rel]:
            print n
        


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
