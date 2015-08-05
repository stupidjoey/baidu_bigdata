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

    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/all_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])

    for idx,user in enumerate(all_user_list[0:100]):
        print 'current idx is%d, user is %s' % (idx,user[0])

        relation_store_path = os.path.join(basepath,'data/output/single_relation_store/relation_store_%s.pkl' % user[0])
        relation_store_file = open(relation_store_path)
        relation_map = pickle.load(relation_store_file)
        relation_store_file.close() 


        with open(os.path.join(basepath,'data/output/single_relation_store_output/%s.txt' % user[0]),'w') as wf:
            entity1 = user[1]
            for entity2 in relation_map[entity1].keys():
                for relation in relation_map[entity1][entity2].keys():
                    rel_count = relation_map[entity1][entity2][relation]
                    writeline = '%s\t%d\t%s\t%s\n' %(relation.encode('utf-8'),rel_count,entity1.encode('utf-8'),entity2.encode('utf-8'))
                    wf.write(writeline)

    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    











if __name__== '__main__':
    main()
    # cProfile.run("main()")


