# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re
import pickle

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    relation_map_path = os.path.join(basepath,'data/train/relation_map.pkl')
    relation_map_file = open(relation_map_path)
    relation_map = pickle.load(relation_map_file)
    relation_map_file.close() 

    with open(os.path.join(basepath,'data/r.txt'), 'w') as f:
        for entity1 in relation_map.keys():
            for entity2 in relation_map[entity1].keys():
                pair = relation_map[entity1][entity2]
                writeline = '%s\t%s\t%s\t%s\t\n' %(entity1.encode('utf-8'),entity2.encode('utf-8'),pair[0].encode('utf-8'),pair[1])
                f.write(writeline)



    # target_ent_hanyu = u'蔡健雅'
    # target_ent_pinyin = 'caijianya'

    # predictpath = os.path.join(basepath,'data/predict.%s' % target_ent_pinyin )
    # with open(predictpath,'w') as f:   
    #     ent_set = set()
    #     layer = 1
    #     layer_max_count = [10,3,2] 
    #     # layer_max_count = [15,5,3] 
    #     target_ent_list = [target_ent_hanyu]
    #     while layer <= 3 and len(target_ent_list) != 0:
    #         new_target_ent_list = []
    #         for target_ent in target_ent_list:
    #             ent_set.add(target_ent)  
    #             current_layer = sorted(relation_map[target_ent].iteritems(), key = lambda x:x[1][1], reverse = True)
    #             layercount = min(len(current_layer), layer_max_count[layer-1])
    #             tempcount = 1
    #             for data in  current_layer:
    #                 another_ent =  data[0]
    #                 if another_ent in ent_set:
    #                     continue
    #                 rel_pair = data[1]
    #                 relation = rel_pair[0]
    #                 if relation == None:
    #                     continue
    #                 writeline = '%s\t%s\t%s\tlayer%d\n' % (relation.encode('utf-8'),target_ent.encode('utf-8'),another_ent.encode('utf-8'),layer)
    #                 f.write(writeline)
    #                 print writeline

    #                 new_target_ent_list.append(another_ent)
    #                 ent_set.add(another_ent)
    #                 tempcount += 1
    #                 if tempcount > layercount:
    #                     break
    #         target_ent_list = new_target_ent_list[:]
    #         layer += 1





    print 'finished ...'

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__=='__main__':
    main()