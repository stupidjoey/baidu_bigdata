# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import relation_classifier as rc
import pickle
import json

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.').split('/')
    basepath = "/".join(path[:-2])

    keys = set()
    with open(os.path.join(basepath,'data/train/entity_attribute/train_attribute')) as f:
        for line in f:
            d = json.loads(line[:-1])
            for key in d.keys():
                keys.add(key)

    with open(os.path.join(basepath,'data/info/attribute_key_copy.txt'),'w') as wf:
        for key in keys:
            wf.write(key.encode('utf-8')+'\n')

    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    







if __name__== '__main__':
    main()


