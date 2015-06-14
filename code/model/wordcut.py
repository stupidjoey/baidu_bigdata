# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re


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

    rel = u'校花'
    xmat = []
    ymat = []
    for line in dataset[0:1470]:
        data = line[:-1].split('\t')
        sentence = data[3].decode('utf-8')
        rel_pos = sentence.find(rel)
        if rel_pos == -1:
            continue
        relation = data[0]
        entity1,entity2 = data[1].decode('utf-8'),data[2].decode('utf-8')
        ent1_pos = sentence.find(entity1)
        ent2_pos = sentence.find(entity2)
        x = [0,0]
        if ent1_pos < ent2_pos:
            x[0] = 1
            if rel_pos < ent1_pos:
                x[1] = 1
            elif rel_pos > ent1_pos and rel_pos < ent2_pos:
                x[1] = 2
            else:
                x[1] = 3
        else:
            x[0] = 0
            if rel_pos < ent2_pos:
                x[1] = 4
            elif rel_pos > ent2_pos and rel_pos < ent1_pos:
                x[1] = 5
            else:
                x[1] = 6

        y = int(data[4])
        xmat.append(x)
        ymat.append(y)
    print xmat






    # seg_list = jieba.cut(u"北影学霸校花李依伊完胜杨幂刘诗诗", cut_all = False, HMM = True)

    # words = pseg.cut(u"北影学霸校花李依伊完胜杨幂刘诗诗")
    # for w in words:
    #     print "%s %s "  % (w.word, w.flag)

    # result = jieba.tokenize(u'北影学霸校花李依伊完胜杨幂刘诗诗')
    # for tk in result:
    #     print "word:%s stat:%d \t end:%d \n" %(tk[0],tk[1],tk[2])



    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds





if __name__=='__main__':
    main()