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

    par_datapath = os.path.join(basepath,'data/train/entity_tupu/')
    filenamelist = os.listdir(par_datapath)

    deletefile = 'entity_tupu.linzhengying'
    filenamelist.remove(deletefile)

    relation_net = dict()
    for filename in filenamelist:
        datapath = os.path.join(basepath,'data/train/entity_tupu/%s' % filename)
        with open(datapath) as f:
            dataset = f.readlines()

        for line in dataset:
            data = line[:-1].split('\t')
            rel = data[0].decode('utf-8')
            entity1 = data[1].decode('utf-8')
            entity2 = data[2].decode('utf-8')

            relation_net.setdefault(entity1,dict())
            relation_net[entity1].setdefault(entity2,None)
            relation_net[entity1][entity2] = rel

            rev_rel = relation_reverse(rel)

            if rev_rel == u'not':
                rev_rel = rel

            relation_net.setdefault(entity2,dict())
            relation_net[entity2].setdefault(entity1,None)
            relation_net[entity2][entity1] = rev_rel


    # for key1 in  relation_net.keys():
    #     for key2 in relation_net[key1].keys():
    #         print key1,key2,relation_net[key1][key2]

    netfile = open( os.path.join(basepath,'data/relation_net.pkl'),'w') 
    pickle.dump(relation_net,netfile)
    netfile.close()





    print 'finished ...'

    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    



def relation_reverse(rel):
    rev_rel = u'not'
    
    if rel == u'女友':
        rev_rel = u'男友'
        return rev_rel

    if rel == u'男友':
        rev_rel =  u'女友'
        return rev_rel        

    if rel == u'前女友':
        rev_rel = u'前男友'
        return rev_rel

    if rel == u'前男友':
        rev_rel =  u'前女友'
        return rev_rel


    if rel == u'绯闻女友':
        rev_rel = u'绯闻男友'
        return rev_rel

    if rel == u'绯闻男友':
        rev_rel = u'绯闻女友'
        return rev_rel

    if rel == u'前绯闻女友':
        rev_rel = u'前绯闻男友'
        return rev_rel

    if rel == u'前绯闻男友':
        rev_rel = u'前绯闻女友'
        return rev_rel

    if rel == u'子女':
        rev_rel = u'父母'
        return rev_rel

    if rel == u'儿子':
        rev_rel = u'父母'
        return rev_rel

    if rel == u'女儿':
        rev_rel = u'父母'
        return rev_rel

    if rel == u'母亲':
        rev_rel = u'子女'   
        return rev_rel

    if rel == u'妻子':
        rev_rel = u'丈夫'
        return rev_rel

    if rel == u'前妻':
        rev_rel = u'前夫'
        return rev_rel

    if rel == u'前夫':
        rev_rel = u'前妻'   
        return rev_rel

    if rel == u'老婆':
        rev_rel = u'丈夫'   
        return rev_rel

    if rel == u'弟弟':
        rev_rel = u'哥哥' 
        return rev_rel

    if rel == u'哥哥':
        rev_rel = u'弟弟' 
        return rev_rel

    if rel == u'姐姐':
        rev_rel = u'妹妹' 
        return rev_rel

    if rel == u'妹妹':
        rev_rel = u'姐姐' 
        return rev_rel

    if rel == u'恩师':
        rev_rel = u'学生'   
        return rev_rel

    if rel == u'老师':
        rev_rel = u'学生'   
        return rev_rel

    if rel == u'学生':
        rev_rel = u'老师'   
        return rev_rel

    return rev_rel





if __name__=='__main__':
    main()