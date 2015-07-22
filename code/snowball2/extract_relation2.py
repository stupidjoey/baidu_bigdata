# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import relation_classifier as rc
import pickle

def main():
    starttime = datetime.datetime.now()

    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])

    # ******************** #
    basepath = '/media/stupidjoey/Elements/baidu_bigdata/train/'
    # ******************** #

    par_datapath = os.path.join(basepath,'data/train/entity_sentence/')
    filenamelist = os.listdir(par_datapath)


    relation_pair = []
    for filename in filenamelist[0:5]:
        print filename
        datapath = os.path.join(basepath,'data/train/entity_sentence/%s' % filename)

        # with open(datapath) as f:
            # dataset = f.readlines()    
        count = 0
        # data_len = len(dataset)
        data_len = 11000000
        f = open(datapath)
        for line in f:
            try:
                count += 1
                if count % ( data_len/5 ) == 0:
                    print '20%...'
                data = line[:-1].split('\t')
                entity1 = data[1].decode('utf-8')
                entity2 = data[2].decode('utf-8')
                sentence = data[0].decode('utf-8')
                sentence_len = len(sentence)
                if sentence_len < 10 or sentence_len > 30:
                    continue
                pos1 = sentence.find(entity1)
                pos2 = sentence.find(entity2)

                if pos1 < pos2:
                    mid = sentence[pos1+len(entity1):pos2]
                    left = sentence[:pos1]
                    right = sentence[pos2+len(entity2):]
                    real_entity1 = entity1
                    real_entity2 = entity2
                else:
                    mid = sentence[pos2+len(entity2):pos1]
                    left = sentence[:pos2]
                    right = sentence[pos1+len(entity1):]
                    real_entity1 = entity2
                    real_entity2 = entity1

                if len(mid) > 5:
                    continue

                sen_split = [left,mid,right,sentence]
                relationlist = rc.classify(sen_split)
                
                if len(relationlist) == 0:
                    continue
                for relation in relationlist:
                    if relation != None:
                        relation_pair.append([real_entity1,real_entity2,relation])
                
            except Exception, e:
                print e

        f.close()

    basepath = "/".join(path[:-2])
    save_relation_pair_path = os.path.join(basepath,'data/train/relation_pair5.pkl')
    save_relation_pair_file = open(save_relation_pair_path ,'w')
    pickle.dump(relation_pair,save_relation_pair_file)
    save_relation_pair_file.close()




    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    







if __name__== '__main__':
    main()


