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
    datapath = os.path.join(basepath,'data/train/relation_train/task1.trainSentence')
    with open(datapath) as f:
        dataset = f.readlines()    

    relation = [u'老师', u'妻子', u'同学', u'撞衫', u'前妻', u'前女友', u'老乡', u'传闻不和', u'经纪人', u'绯闻女友', u'闺蜜', u'偶像']
    relation_pinyin = ['laoshi','qizi','tongxue','zhuangshan','qianqi','qiannvyou','laoxiang','chuanwenbuhe','jingjiren','feiwennvyou','guimi','ouxiang']

    for idx,rel in enumerate(relation):
        trans_dataset = []
        ytrain = []
        relationset = set()
        for line in dataset[:]:
            temp_data = []
            data = line[:-1].split('\t')

            entity1 = data[1]
            entity2 = data[2]
            sentence = data[3]
            relation = data[0].decode('utf-8')

            if relation != rel:
                continue
            

            words = pseg.cut(sentence)
            posList = []
            ent_pos_idx = []    

            for w in words:
                # print "%s %s %s "  % (w.word, w.flag,posdict[w.flag])
                posList.append(w.flag)
                if w.word == entity1.decode('utf-8') or w.word ==entity2.decode('utf-8'):
                    ent_pos_idx.append(len(posList) - 1)
            if len(ent_pos_idx) != 2 :
                continue

            trans_dataset.append([entity1,entity2,sentence])
            ytrain.append(int(data[4]))

        posdictpath = os.path.join(basepath,'data/posdict.txt')
        with open(posdictpath) as f:
            posdata = f.readlines()    
        
        posdict = dict()
        for line in posdata:
            data = line[:-1].split('\t')
            pos  = data[0]
            num = data[1]
            posdict[pos] = num

        xtrain = ft.get_feature(trans_dataset,posdict)

        xtrain = np.array(xtrain)
        ytrain = np.array(ytrain)

        print 'start building model...'

        
        clf = RandomForestClassifier(n_estimators=50)
        clf = clf.fit(xtrain, ytrain)

        print 'store the model...%s' % relation_pinyin[idx]
        modelname = 'data/classifier/%s_rf.pkl' % relation_pinyin[idx]
        modelfile  = open(os.path.join(basepath,modelname),'w')
        pickle.dump(clf,modelfile)
        modelfile.close()

        print 'finished...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds





if __name__== '__main__':
    main()