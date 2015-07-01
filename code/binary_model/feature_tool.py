# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
import string



def feature2vec(x, idf_dict, feature_num):
    sorted_idf_dict = sorted(idf_dict.iteritems(), key = lambda x:x[1], reverse = True)
    sorted_idf_dict = sorted_idf_dict[0:feature_num]
    
    
    idf_dict = {}
    word_idx_map = dict()
    idx = 0
    for pair in sorted_idf_dict:
        idf_dict[pair[0]] = pair[1]
        word_idx_map[pair[0]] = idx
        idx += 1


    word_dict = dict()
    for w in x[0:7]:
        if w != 0:
            if w in idf_dict.keys():
                word_dict[w] = word_dict.get(w, 0.0) + 1.0

        
    total_freq = sum(word_dict.values())
    for w in word_dict.keys():
        word_dict[w] *= idf_dict[w] / total_freq
    vec_x = [0] * (feature_num + 2)
    vec_x[-2] = x[-2]
    vec_x[-1] = x[-1]
    for w in word_dict.keys():
        idx = word_idx_map[w]
        weight = word_dict[w]
        vec_x[idx] = weight

    return vec_x



def get_word_feature(entity1,entity2,sentence, rel_dict = None):

    x = [0,0,0,0,0,0,0,0,0,0]   # wa-2 wa-1 wa1 wa 2  wb-2 wb-1 wb1 wb2  (a<b or a >b)  (a...b)

    relset = set()
    if rel_dict != None:
        for key in rel_dict:
            for r in rel_dict[key]:
                relset.add(r)

    sentence = re.sub("[\d\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）：《》“”()""?]+".decode("utf8"), "".decode("utf8"),sentence)
    ent1_pos = sentence.find(entity1)
    ent2_pos = sentence.find(entity2)


    words = pseg.cut(sentence)
    wordList = []
    ent_pos_idx = []

    count = 0
    for w in words:
        # print "%s %s %s "  % (w.word, w.flag,posdict[w.flag])
        if w.word in relset:
            count += 1
        wordList.append(w.word)
        if w.word == entity1 or w.word ==entity2:
            ent_pos_idx.append(len(wordList) - 1)
    
    if rel_dict != None:
        if count == 0:
            return None

    if len(ent_pos_idx) != 2:    ##  分词存在问题，导致命名实体没有被分出来
        return None

    ent1_pos_idx = ent_pos_idx[0]
    ent2_pos_idx = ent_pos_idx[1]
    x[9] = ent2_pos_idx - ent1_pos_idx -1
    if ent1_pos < ent2_pos:
        x[8] = 1
    else:
        x[8] = 0

    if ent1_pos_idx - 2 >= 0 :
        x[0] = wordList[ent1_pos_idx-2]

    if ent1_pos_idx - 1 >= 0 :
        x[1] = wordList[ent1_pos_idx-1]

    if ent1_pos_idx + 1 < ent2_pos_idx:
        x[2] = wordList[ent1_pos_idx + 1]

    if ent1_pos_idx + 2 < ent2_pos_idx:
        x[3] = wordList[ent1_pos_idx + 2]

    if ent2_pos_idx - 2 > ent1_pos_idx :
        x[4] = wordList[ent2_pos_idx-2]

    if ent2_pos_idx - 1 > ent1_pos_idx :
        x[5] = wordList[ent2_pos_idx-1]

    if ent2_pos_idx + 1 < len(wordList) :
        x[6] = wordList[ent2_pos_idx + 1] 

    if ent2_pos_idx + 2 < len(wordList) :
        x[7] = wordList[ent2_pos_idx + 2]


    return x


