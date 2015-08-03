# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re
import pickle
import relation_classifier as rc


def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    relation_map_path = os.path.join(basepath,'data/output/relation_map_8.3.pkl')
    relation_map_file = open(relation_map_path)
    relation_map = pickle.load(relation_map_file)
    relation_map_file.close() 



    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)

    train_user_list = []
    train_user_path =  os.path.join(basepath,'data/info/train_user.txt')
    with open(train_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            train_user_list.append([pinyin,hanyu])



    for user in train_user_list:
        print 'current user is %s' %user[0]
        datapath = os.path.join(basepath,'data/train/entity_tupu/entity_tupu.%s' % user[0])
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            relation = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')

            if entity1 not in relation_map:
                relation_map[entity1] = dict()
            relation_map[entity1][entity2] = [relation,float('inf')]

            rev_relation = rc.not_relation(relation)

            if entity2 not in relation_map:
                relation_map[entity2] = dict()
            relation_map[entity2][entity1] = [rev_relation,float('inf')]




    relation_map_path = os.path.join(basepath,'data/output/relation_map_8.3_repair.pkl')
    relation_map_file = open(relation_map_path,'w')
    pickle.dump(relation_map, relation_map_file)
    relation_map_file.close() 


    print 'finished ...'

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__=='__main__':
    main()