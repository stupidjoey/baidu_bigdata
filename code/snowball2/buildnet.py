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





    relation_map = dict()
    for num in range(20):

        print 'current num is %d' % num
        relation_pair_path = os.path.join(basepath,'data/output/relation_pair/relation_pair%d.pkl' % num)
        relation_pair_file = open(relation_pair_path)
        relation_pair = pickle.load(relation_pair_file)
        relation_pair_file.close()    



        for pair in relation_pair:
            entity1 = pair[0].decode('utf-8')
            entity2 = pair[1].decode('utf-8')
            relation = pair[2]
            rev_relation = rc.not_relation(relation)

            # if relation not in weight_dict or rev_relation not in weight_dict:
            #     weight = 1
            #     rev_weight = 1
            # else:
            #     weight = weight_dict[relation]
            #     rev_weight = weight_dict[rev_relation]
            
            relation_map.setdefault(entity1,dict())
            relation_map[entity1].setdefault(entity2,dict())
            relation_map[entity1][entity2][relation] = relation_map[entity1][entity2].get(relation, 0) + 1 * 1


            relation_map.setdefault(entity2,dict())
            relation_map[entity2].setdefault(entity1,dict())
            relation_map[entity2][entity1][rev_relation] = relation_map[entity2][entity1].get(rev_relation, 0) + 1* 1


    # for key1 in relation_map.keys():
    #     for key2 in relation_map[key1].keys():
    #         for rel in relation_map[key1][key2].keys():
    #             print key1,key2,rel,relation_map[key1][key2][rel]




    # combine the multiple relations
    for entity1 in relation_map.keys():
        for entity2 in relation_map[entity1].keys():
            sort_relation = sorted(relation_map[entity1][entity2].iteritems(), key = lambda x:x[1], reverse = True)
            total_count = 0
            max_count = sort_relation[0][1]
            max_rel = sort_relation[0][0]
            for rel,count in sort_relation:
                if count > max_count:
                    max_rel = rel
                    max_count = count
                total_count += count
            relation_map[entity1][entity2] = [max_rel,max_count]

    # for entity1 in relation_map.keys():
    #     for entity2 in relation_map[entity1].keys():
    #         pair = relation_map[entity1][entity2]
    #         print entity1,entity2,pair[0],pair[1]


    relation_map_path = os.path.join(basepath,'data/output/relation_map_8.3.pkl')
    relation_map_file = open(relation_map_path,'w')
    pickle.dump(relation_map, relation_map_file)
    relation_map_file.close() 



    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    











if __name__== '__main__':
    main()
    # cProfile.run("main()")


