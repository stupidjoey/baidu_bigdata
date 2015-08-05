# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
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

    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/train_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])

    user_num = len(all_user_list)
    total_final_eva = 0.0

    relation_hit_dict = dict()
    relation_match_dict = dict()
    
    for user in all_user_list:
        print 'current user is %s ,%s' % (user[0],user[1])

        target_ent_pinyin = user[0]

        tupupath = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % target_ent_pinyin)
        
        with open(tupupath) as f:
            tupu_data = f.readlines()


        real_relation_map = dict()

        layer1_list = []
        layer2_list = []
        layer3_list = []

        for line in tupu_data:
            data = line[:-1].split('\t')
            relation = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            layer = data[5]
            pair = (entity1,entity2)
            if layer == 'layer1':
                layer1_list.append(pair)
            elif layer == 'layer2':
                layer2_list.append(pair)
            elif layer == 'layer3':
                layer3_list.append(pair)

            real_relation_map[pair] = relation


        predictpath = os.path.join(basepath,'data/output/single_predict/predict.%s' % target_ent_pinyin )
        with open(predictpath) as f:  
            predict_tupu_data = f.readlines()

        eva_part1 = 0.0  # relattion match rate
        eva_part2 = 0.0  # f value


        hit_count = 0.0
        relation_match_count = 0.0

        layer1_hit_count = 0.0
        layer2_hit_count = 0.0
        layer3_hit_count = 0.0

        layer1_pred_count = 0.0
        layer2_pred_count = 0.0
        layer3_pred_count = 0.0

        for line in predict_tupu_data:
            data = line[:-1].split('\t')
            pred_relation = data[0].decode('utf-8')
            pred_entity1 = data[1].decode('utf-8')
            pred_entity2 = data[2].decode('utf-8')
            pred_layer = data[3]

            predict_pair = (pred_entity1,pred_entity2)
            rev_predict_pair = (pred_entity2,pred_entity1)

            if predict_pair in real_relation_map:
                hit_count += 1

                relation_hit_dict.setdefault(pred_relation,set())
                if predict_pair not in relation_hit_dict[pred_relation] and rev_predict_pair not in relation_hit_dict[pred_relation]:
                    relation_hit_dict[pred_relation].add(predict_pair)


                if pred_relation == real_relation_map[predict_pair]:
                    relation_match_count += 1
                    
                    relation_match_dict.setdefault(pred_relation,set())
                    if predict_pair not in relation_match_dict[pred_relation] and rev_predict_pair not in relation_match_dict[pred_relation]:
                        relation_match_dict[pred_relation].add(predict_pair)


            if  pred_layer == 'layer1':
                layer1_pred_count += 1
                if predict_pair in layer1_list:
                    layer1_hit_count += 1
            elif pred_layer == 'layer2':
                layer2_pred_count += 1
                if predict_pair in layer2_list:
                    layer2_hit_count += 1
            elif pred_layer == 'layer3':
                layer3_pred_count += 1
                if predict_pair in layer3_list:
                    layer3_hit_count += 1


        total_count = len(real_relation_map.keys())
        if hit_count == 0:
            eva_part1 = 0.0
        else:
            eva_part1 = (hit_count * 1.0 / total_count) * (relation_match_count / hit_count)

        if layer1_pred_count == 0:
            p1 = 0.0
        else:
            p1 = layer1_hit_count/layer1_pred_count
        r1 = layer1_hit_count/len(layer1_list)
        if p1 == 0.0 and r1 == 0.0:
            f1 = 0.0
        else:
            f1 = 2*p1*r1/(p1+r1)

        if layer2_pred_count == 0:
            p2 = 0.0
        else:
            p2 = layer2_hit_count/layer2_pred_count
        r2 = layer2_hit_count/len(layer2_list)
        if p2 == 0.0 and r2 == 0.0:
            f2 = 0.0
        else:
            f2 = 2*p2*r2/(p2+r2)

        if layer3_pred_count == 0:
            p3 = 0.0
        else:
            p3 = layer3_hit_count/layer3_pred_count
        r3 = layer3_hit_count/len(layer3_list)
        if p3 == 0.0 and r3 == 0.0:
            f3 = 0.0
        else:
            f3 = 2*p3*r3/(p3+r3)

        eva_part2 = (f1 + f2 + f3)/3

        final_eva = (eva_part1 + eva_part2) / 2

        total_final_eva += final_eva
        print 'hit count is %d' %hit_count
        print 'relation_match_count is %d' % relation_match_count
        print 'first round hit is %d ' % layer1_hit_count
    # print 'final evaluation is %f' % final_eva


    avg_final_eva = total_final_eva/user_num

    print 'avg_final_eva is %f' % avg_final_eva


    # for rel in relation_hit_dict.keys():
    #     pairset = relation_hit_dict[rel]
    #     relation_hit_dict[rel] = len(pairset)


    # for rel in relation_match_dict.keys():
    #     pairset = relation_match_dict[rel]
    #     relation_match_dict[rel] = len(pairset)


    # hit_dict_file = open(os.path.join(basepath,'data/info/relation_hit_dict.pkl') ,'w')
    # pickle.dump(relation_hit_dict,hit_dict_file)
    # hit_dict_file.close()

    # match_dict_file = open(os.path.join(basepath,'data/info/relation_match_dict.pkl') ,'w')
    # pickle.dump(relation_match_dict,match_dict_file)
    # match_dict_file.close()



    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__== '__main__':
    main()


