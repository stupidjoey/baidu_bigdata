# !/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
import os

def main():
    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])
    print basepath
    datapath = os.path.join(basepath,'data/train/relation_train/task1.trainSentence')
    
    with open(datapath) as f:
        dataset = f.readlines()

    entityset = set()
    for line in dataset:
        data = line[:-1].split('\t')
        relation = data[0]
        entity1,entity2 = data[1].decode('utf-8'),data[2].decode('utf-8')
        sentence = data[3]
        y = int(data[4])
        entityset.add(entity1)
        entityset.add(entity2)


    writepath = os.path.join(basepath,'data/myDict.txt')
    with open(writepath,'w') as f:
        for entity in entityset:
            writeline = '%s 1000\n' % entity.encode('utf-8')
            f.write(writeline)
    print 'finished ...'














if __name__ == '__main__':
    main()