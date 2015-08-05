# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re
import pickle

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.').split('/')
    basepath = "/".join(path[:-2])

    all_user_list = []
    with open( os.path.join(basepath,'data/info/train_user.txt')) as f:
        for line in f:
            data = line[:-1].split('\t')
            all_user_list.append([data[0],data[1].decode('utf-8')])

    with open(os.path.join(basepath,'data/info/layer1_hot_relation.txt')) as f:
        hot_relation_data = f.readlines()

    hot_relation = []
    for line in hot_relation_data[0:10]:
        data = line[:-1].split('\t')
        relation = data[0].decode('utf-8')
        hot_relation.append(relation)

    for user in all_user_list:
        print 'current user is %s ,%s' %(user[0],user[1])
        target_ent_pinyin = user[0]
        target_ent_hanyu = user[1]

        with open(os.path.join(basepath,'data/output/single_relation_map_repair/relation_map_%s.pkl' % user[0])) as ff:
            relation_map = pickle.load(ff)

        predictpath = os.path.join(basepath,'data/output/single_predict/predict.%s' % target_ent_pinyin )
        with open(predictpath,'w') as f:   
            ent_set = set()
            layer = 1
            layer_max_count = [10,3,2] 
            # layer_max_count = [15,5,3] 
            target_ent_list = [target_ent_hanyu]
            while layer <= 3 and len(target_ent_list) != 0:
                new_target_ent_list = []
                for target_ent in target_ent_list:
                    ent_set.add(target_ent)
                    current_layer = sorted(relation_map[target_ent].iteritems(), key = lambda x:x[1][1], reverse = True)
                    layercount = min(len(current_layer), layer_max_count[layer-1])
                    tempcount = 1
                    
                    # if layer == 1:
                    #     for data in current_layer[:]:
                    #         if tempcount > layercount:
                    #             break 
                    #         another_ent = data[0]
                    #         if another_ent in ent_set:
                    #             continue
                    #         rel_pair = data[1]
                    #         relation = rel_pair[0]
                    #         if relation in hot_relation:
                    #             writeline = '%s\t%s\t%s\tlayer%d\n' % (relation.encode('utf-8'),target_ent.encode('utf-8'),another_ent.encode('utf-8'),layer)
                    #             f.write(writeline)
                    #             new_target_ent_list.append(another_ent)
                    #             ent_set.add(another_ent)
                    #             tempcount += 1
                    #             current_layer.remove(data)
                  

                    for data in current_layer:
                        if tempcount > layercount:
                            break
                        another_ent = data[0]
                        if another_ent in ent_set:
                            continue
                        rel_pair = data[1]
                        relation = rel_pair[0]
                        writeline = '%s\t%s\t%s\tlayer%d\n' % (relation.encode('utf-8'),target_ent.encode('utf-8'),another_ent.encode('utf-8'),layer)
                        f.write(writeline)
                        new_target_ent_list.append(another_ent)
                        ent_set.add(another_ent)
                        tempcount += 1
                target_ent_list = new_target_ent_list[:]
                layer += 1





    print 'finished ...'

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__=='__main__':
    main()