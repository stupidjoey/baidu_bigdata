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

    relation_dict = dict()

    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')
            relation_dict.setdefault(rel,set())
            if (entity1,entity2) not in relation_dict[rel] and (entity2,entity1) not in relation_dict[rel]:
                pair = (entity1,entity2)
                relation_dict[rel].add(pair)
         
    for rel in relation_dict.keys():
        pairset = relation_dict[rel]
        relation_dict[rel] = len(pairset)

    relation_dict = sorted(relation_dict.iteritems(), key = lambda x:x[1], reverse = True)



    count =0 
    for pair in relation_dict:
        print pair[0],pair[1]
        count += int(pair[1])
    print count


    rel_path  =  os.path.join(basepath,'data/info/all_relation.txt')
    with open(rel_path,'w') as f:
        for pair in relation_dict:
            writestr = '%s\t%s\n' % (pair[0].encode('utf-8'),pair[1])
            f.write(writestr)








    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
