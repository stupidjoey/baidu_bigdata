# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import numpy as np
import pickle
import relation_classifier as rc

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])


    relation_set = ['夫妻','配偶','儿子','同为校花','前妻','合作','同居','兄弟','复合','姐弟恋','队友','旧爱']
    relation_set_sent = ['夫妻','配偶','儿子','校花','前妻','合作','同居','兄弟','复合','姐弟恋','队友','旧爱']


    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/all_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])

    wf_list = []
    for rel in relation_set:
        save_sentence_path = os.path.join(basepath,'data/relation_sentence/%s.txt' % rel)
        wf = open(save_sentence_path,'a')
        wf_list.append(wf)

    
    for idx,user in enumerate(all_user_list[0:100]):
        print 'current idx is %d, user is %s' % (idx,user[0])
        target_ent_pinyin = user[0]
        tupu_path =  os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % target_ent_pinyin)
        
        entity_pair_dict = dict()
        rel_hit_count = 0
        with open(tupu_path) as f:
            for line in f:
                data = line[:-1].split('\t')
                relation = data[0]
                if relation not in relation_set:
                    continue
                entity1 = data[1]
                entity2 = data[2]
                entity_pair_dict.setdefault(relation,[])
                entity_pair_dict[relation].append([entity1,entity2])
                rel_hit_count += 1

        if rel_hit_count == 0:
            continue

        tbasepath = '/media/stupidjoey/Elements/baidu_bigdata/train/'
        sentence_path = os.path.join(tbasepath,'data/train/entity_sentence/entity_sentence.%s' % target_ent_pinyin)
        f = open(sentence_path) 
        count = 0
        data_len = 11000000

        for line in f:
            try:
                count += 1
                if count % ( data_len/5 ) == 0:
                    print '20%...'
                data = line[:-1].split('\t')
                entity1 = data[1]
                entity2 = data[2]
                sentence = data[0]
                sentence_len = len(sentence)
                if sentence_len < 30 or sentence_len > 90:
                    continue
                target_relation = None
                for rel in entity_pair_dict.keys():
                    entity_pair = entity_pair_dict[rel]
                    if [entity1,entity2]  in entity_pair or [entity2,entity1]  in entity_pair:
                        target_relation = rel
                        break
                if target_relation == None:
                    continue
                rel_idx = relation_set.index(target_relation)
                wf = wf_list[rel_idx]
                if relation_set_sent[rel_idx] not in sentence:
                    continue
                wf.write(line)
                # print line
            except Exception, e:
                print e

    for wf in wf_list:
        wf.close()


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    




if __name__== '__main__':
    main()
