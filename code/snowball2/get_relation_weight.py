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

    relation_path = os.path.join(basepath,'data/info/all_relation.txt')
    with open(relation_path) as f:
        relation_data = f.readlines()

    weight_dict = dict()

    for line  in relation_data:
        data = line[:-1].split('\t')
        relation = data[0].decode('utf-8')
        count = int(data[1])
        weight_dict[relation] = count

    base_count = weight_dict[u'朋友']
    for key in weight_dict:
        if weight_dict[key] >= 10:
            weight_dict[key] = weight_dict[key]*1.0/base_count
        else:
            weight_dict[key] = 1.0
        print key,weight_dict[key]

    weight_path = os.path.join(basepath,'data/info/weight_dict.pkl')
    weight_file = open(weight_path,'w')
    pickle.dump(weight_dict,weight_file)
    weight_file.close()


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
