# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)

    train_user_file  = filenamelist[0:50]
    test_user_file = filenamelist[50:100]


    train = []

    for filename in train_user_file:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()
        pinyin_name = filename.split('.')[1]
        hanyu_name = dataset[0][:-1].split('\t')[1]
        train.append([pinyin_name,hanyu_name])


    test = []
    for filename in test_user_file:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()
        pinyin_name = filename.split('.')[1]
        hanyu_name = dataset[0][:-1].split('\t')[1]
        test.append([pinyin_name,hanyu_name])


    train_path = os.path.join(basepath,'data/train/train_user.txt')
    with open(train_path,'w') as f:
        for pair in train:
            line = pair[0]+'\t' + pair[1] + '\n'
            f.write(line)

    test_path = os.path.join(basepath,'data/train/test_user.txt')
    with open(test_path,'w') as f:
        for pair in test:
            line = pair[0]+'\t' + pair[1] + '\n'
            f.write(line)






    print 'finished ...'
    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__=='__main__':
    main()