# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import os
import re
import numpy as np
import pickle


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)

    target_rel = u'夫妻'

    train_user_path =  os.path.join(basepath,'data/train_user.txt')
    with open(train_user_path) as f:
        userdata = f.readlines()

    userset = []
    for line in userdata:
        userset.append(line[:-1])

    for user in userset[0:1]:
        tupu_path = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % user)
        with open(tupu_path) as f:
            tupu_data = f.readlines()

        entity_pair = []
        for line in tupu_data:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            if rel == target_rel:
                entity_pair.append([entity1,entity2])


        datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.%s' % user)
        with open(datapath) as f:
            dataset = f.readlines()    

        three_split_set = []
        for line in dataset:
            try:
                data = line[:-1].split('\t')
                entity1 = data[1].decode('utf-8')
                entity2 = data[2].decode('utf-8')
                sentence = data[0].decode('utf-8')
                if [entity1,entity2] in entity_pair or [entity2,entity1] in entity_pair:
                    print sentence,entity1,entity2
                    jieba.add_word(entity1,1000)
                    jieba.add_word(entity2,1000)
                    three_split = cut_sentence(sentence,entity1,entity2)
                    if three_split == None:
                        continue
                    three_split_set.append(three_split)

                    # if rel in sentence:
                        # print sentence
            except Exception, e:
                print e

        # left_dict,mid_dict,right_dict = {},{},{}
        # for three_split in three_split_set:
        #     left_wordset,mid_wordset,right_wordset = three_split[0],three_split[1],three_split[2]
        #     for w in left_wordset:
        #         left_dict[w] = left_dict.get(w, 0) + 1
        #     for w in mid_wordset:
        #         mid_dict[w] = mid_dict.get(w, 0) + 1
        #     for w in right_wordset:
        #         right_dict[w] = right_dict.get(w, 0) + 1

        # left_dict = sorted(left_dict.iteritems(), key = lambda x:x[1], reverse = True)
        # for pair in left_dict[0:100]:
        #     print pair[0],pair[1]

        # mid_dict = sorted(mid_dict.iteritems(), key = lambda x:x[1], reverse = True)
        # for pair in mid_dict[0:100]:
        #     print pair[0],pair[1]

        # right_dict = sorted(right_dict.iteritems(), key = lambda x:x[1], reverse = True)
        # for pair in right_dict[0:100]:
        #     print pair[0],pair[1]

  

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



def cut_sentence(sentence,entity1,entity2):
    seg_list = list( jieba.cut(sentence, cut_all = 'True') )
    entity_idx_set = []
    for w in seg_list:
        if w == entity1 or w == entity2:
            entity_idx_set.append(seg_list.index(w))
    if len(entity_idx_set) != 2:
        return None
    ent_idx1 = entity_idx_set[0]
    ent_idx2 = entity_idx_set[1]

    return [seg_list[0:ent_idx1],seg_list[ent_idx1+1:ent_idx2],seg_list[ent_idx2+1:]]







if __name__== '__main__':
    main()
