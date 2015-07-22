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

    netfile = open( os.path.join(basepath,'data/relation_net.pkl')) 
    relation_net = pickle.load(netfile)
    netfile.close()

    target_ent_hanyu = u'林正英'
    target_ent_pinyin = 'linzhengying'

    predictpath = os.path.join(basepath,'data/predict.%s' % target_ent_pinyin )
    with open(predictpath,'w') as f:   
        ent_set = set()
        layer = 1
        layer_max_count = [10,3,2] 
        # layer_max_count = [15,6,4] 
        target_ent_list = [target_ent_hanyu]
        while layer <= 3 and len(target_ent_list) != 0:
            new_target_ent_list = []
            for target_ent in target_ent_list:
                ent_set.add(target_ent)  
                entity2_set = relation_net[target_ent].keys()
                layercount = min(len(entity2_set), layer_max_count[layer-1])
                tempcount = 1
                for entity2 in  entity2_set:
                    if entity2 in ent_set:
                        continue
                    relation = relation_net[target_ent][entity2]
                    writeline = '%s\t%s\t%s\n' % (relation.encode('utf-8'),target_ent.encode('utf-8'),entity2.encode('utf-8'))
                    f.write(writeline)
                    print writeline
                    new_target_ent_list.append(entity2)
                    ent_set.add(entity2)
                    tempcount += 1
                    if tempcount > layercount:
                        break
            target_ent_list = new_target_ent_list[:]
            layer += 1    





    print 'finished ...'

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



if __name__=='__main__':
    main()