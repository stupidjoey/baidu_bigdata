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

    relation_store = dict()
    for num in range(20):
        print 'current num is %d' % num
        relation_pair_path = os.path.join(basepath,'data/output/relation_pair/relation_pair%d.pkl' % num)
        relation_pair_file = open(relation_pair_path)
        relation_pair = pickle.load(relation_pair_file)
        relation_pair_file.close()    

        for pair in relation_pair:
            entity1 = pair[0].decode('utf-8')
            entity2 = pair[1].decode('utf-8')
            relation = pair[5]

            rev_relation = rc.not_relation(relation)
            
            relation_store.setdefault(entity1,dict())
            relation_store[entity1].setdefault(entity2,dict())
            relation_store[entity1][entity2][relation] = relation_store[entity1][entity2].get(relation, 0.0) + 1

            relation_store.setdefault(entity2,dict())
            relation_store[entity2].setdefault(entity1,dict())
            relation_store[entity2][entity1][rev_relation] = relation_store[entity2][entity1].get(rev_relation, 0.0) + 1


    relation_store_path = os.path.join(basepath,'data/output/relation_store.pkl')
    relation_store_file = open(relation_store_path,'w')
    pickle.dump(relation_store, relation_store_file)
    relation_store_file.close() 



    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    











if __name__== '__main__':
    main()
    # cProfile.run("main()")


