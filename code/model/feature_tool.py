# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
from sklearn.ensemble import RandomForestClassifier


def get_feature(dataset,posdict):

    xmat = []
    ymat = []

    for data in dataset:

        entity1,entity2 = data[0].decode('utf-8'),data[1].decode('utf-8')
        sentence = data[2].decode('utf-8')
        # print entity1,entity2,sentence
        ent1_pos = sentence.find(entity1)
        ent2_pos = sentence.find(entity2)

        x = [0,0,0,0,0,0,0,0,0,0]   # wa-2 wa-1 wa1 wa 2  wb-2 wb-1 wb1 wb2  (a<b or a >b)  (a...b)

        words = pseg.cut(sentence)
        posList = []
        ent_pos_idx = []
        for w in words:
            # print "%s %s %s "  % (w.word, w.flag,posdict[w.flag])
            if w.flag not in posdict.keys():
                continue
            posList.append(w.flag)

            if w.word == entity1 or w.word ==entity2:
                ent_pos_idx.append(len(posList) - 1)
        # print sentence
        # print ent_pos_idx

        ent1_pos_idx = ent_pos_idx[0]
        ent2_pos_idx = ent_pos_idx[1]
        x[9] = ent2_pos_idx - ent1_pos_idx -1
        if ent1_pos < ent2_pos:
            x[8] = 1
        else:
            x[8] = 0

        if ent1_pos_idx - 2 >= 0 :
            pos = posList[ent1_pos_idx-2]
            x[0] = posdict[pos]

        if ent1_pos_idx - 1 >= 0 :
            pos = posList[ent1_pos_idx-1]
            x[1] = posdict[pos]

        if ent1_pos_idx + 1 < ent2_pos_idx:
            pos = posList[ent1_pos_idx + 1]
            x[2] = posdict[pos]

        if ent1_pos_idx + 2 < ent2_pos_idx:
            pos = posList[ent1_pos_idx + 2]
            x[3] = posdict[pos]

        if ent2_pos_idx - 2 > ent1_pos_idx :
            pos = posList[ent2_pos_idx-2]
            x[4] = posdict[pos]

        if ent2_pos_idx - 1 > ent1_pos_idx :
            pos = posList[ent2_pos_idx-1]
            x[5] = posdict[pos]    

        if ent2_pos_idx + 1 < len(posList) :
            pos = posList[ent2_pos_idx + 1]
            x[6] = posdict[pos]    

        if ent2_pos_idx + 2 < len(posList) :
            pos = posList[ent2_pos_idx + 2]
            x[7] = posdict[pos]  


        xmat.append(x)




    xmat = np.array(xmat)

    return xmat


