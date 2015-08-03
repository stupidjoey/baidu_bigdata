# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import relation_classifier as rc
import pickle
import cProfile

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])
    target_relation = '旧爱'
    relation_rule_func = rc.jiuai_rule
    relation_sentence_path = os.path.join(basepath,'data/relation_sentence/%s.txt' % target_relation)

    relation_pair = set()
    with open(relation_sentence_path) as f:
        for line in f:
            data = line[:-1].split('\t')      
            entity1 = data[1]  
            entity2 = data[2] 
            sentence = data[0]
            pos1 = sentence.find(entity1)
            pos2 = sentence.find(entity2)
            if (entity1,entity2) in relation_pair or (entity2,entity1) in relation_pair:
                continue

            if pos1 < pos2:
                mid = sentence[pos1+len(entity1):pos2]
                left = sentence[:pos1]
                right = sentence[pos2+len(entity2):]
                real_entity1 = entity1
                real_entity2 = entity2
            else:
                mid = sentence[pos2+len(entity2):pos1]
                left = sentence[:pos2]
                right = sentence[pos1+len(entity1):]
                real_entity1 = entity2
                real_entity2 = entity1



            sen_split = [left,mid,right,sentence]
            relation = relation_rule_func(sen_split)
            if relation == None:
                continue

            relation_pair.add((entity1,entity2))


    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/all_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])

    user_num = len(all_user_list)

    real_relation_pair = set()
    for user in all_user_list:
        target_ent_pinyin = user[0]
        tupupath = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % target_ent_pinyin)
        with open(tupupath) as f:
            tupu_data = f.readlines()
        for line in tupu_data:
            data = line[:-1].split('\t')
            relation = data[0]
            if relation != target_relation:
                continue
            entity1 = data[1]
            entity2 = data[2]
            pair = (entity1,entity2)
            if (entity1,entity2) not in real_relation_pair and (entity2,entity1) not in real_relation_pair:
                real_relation_pair.add(pair)

    real_count = len(real_relation_pair)
    my_count = len(relation_pair)
    hit_count = 0.0
    for pair in relation_pair:
        entity1,entity2 = pair[0],pair[1]
        if (entity1,entity2)  in real_relation_pair or (entity2,entity1)  in real_relation_pair:
            hit_count += 1

    print 'hit_count is %d, real_count is %d, my count is %d ' %(hit_count,real_count,my_count)
    print 'hit rate is %f' % (hit_count/real_count)


    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    







if __name__== '__main__':
    # cProfile.run("main()")
    main()
    


