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

    weight_path = os.path.join(basepath,'data/info/weight_dict.pkl')
    weight_file = open(weight_path)
    weight_dict = pickle.load(weight_file)
    weight_file.close()


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

        relation_store_path = os.path.join(basepath,'data/output/single_relation_store/relation_store_%s.pkl' %user[0])
        relation_store_file = open(relation_store_path)
        relation_map = pickle.load(relation_store_file)
        relation_store_file.close() 

        # combine the multiple relations
        for entity1 in relation_map.keys():
            for entity2 in relation_map[entity1].keys():
                sort_relation = sorted(relation_map[entity1][entity2].iteritems(), key = lambda x:x[1], reverse = True)
                total_count = 0
                max_rel = sort_relation[0][0]
                max_count = sort_relation[0][1]
                for rel,count in sort_relation:
                    total_count += count
                relation_map[entity1][entity2] = [max_rel,max_count]

        # for entity1 in relation_map.keys():
        #     for entity2 in relation_map[entity1].keys():
        #         pair = relation_map[entity1][entity2]
        #         print entity1,entity2,pair[0],pair[1]


        relation_map_path = os.path.join(basepath,'data/output/single_relation_map/relation_map_%s.pkl' %user[0])
        relation_map_file = open(relation_map_path,'w')
        pickle.dump(relation_map, relation_map_file)
        relation_map_file.close() 

    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    





if __name__== '__main__':
    main()
    # cProfile.run("main()")


