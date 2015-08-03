# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import re
import pickle

''' get all kinds of relations from the tupu data  '''
def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)

    relation_count_dict = dict()

    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            layer = data[5]
            if layer == 'layer3':
                relation_count_dict[rel] = relation_count_dict.get(rel,0) + 1


    relation_count_dict = sorted(relation_count_dict.iteritems(), key = lambda x:x[1], reverse = True)



    count =0 
    for pair in relation_count_dict:
        print pair[0],pair[1]
        count += pair[1]
    print count


    rel_path  =  os.path.join(basepath,'data/info/layer3_hot_relation.txt')
    with open(rel_path,'w') as f:
        for pair in relation_count_dict:
            writestr = '%s\t%s\n' % (pair[0].encode('utf-8'),pair[1])
            f.write(writestr)








    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
