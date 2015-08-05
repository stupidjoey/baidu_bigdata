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

    all_user_list = []
    all_user_path =  os.path.join(basepath,'data/info/all_user.txt')
    with open(all_user_path) as f:
        for line in f:
            data = line[:-1].split('\t')
            pinyin = data[0]
            hanyu = data[1].decode('utf-8')
            all_user_list.append([pinyin,hanyu])


    for idx,user in enumerate(all_user_list[0:100]):

        relation_pair = []
        print 'current idx is %d, user is %s' % (idx,user[0])
        tbasepath = '/media/stupidjoey/Elements/baidu_bigdata/train/'
        datapath = os.path.join(tbasepath,'data/train/entity_sentence/entity_sentence.%s' % user[0])

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
                entity1 = data[1]
                entity2 = data[2]
                
                sentence = data[0]
                sentence_len = len(sentence)
                if sentence_len < 30 or sentence_len > 90:
                    continue
                pos1 = sentence.find(entity1)
                pos2 = sentence.find(entity2)
                
                r_len = len(data)
                uid1 = data[r_len/2+1]
                uid2 = data[r_len/2+2]

                if pos1 < pos2:
                    mid = sentence[pos1+len(entity1):pos2]
                    left = sentence[:pos1]
                    right = sentence[pos2+len(entity2):]
                    real_entity1 = entity1
                    real_entity2 = entity2
                    real_uid1 = uid1
                    real_uid2 = uid2
                else:
                    mid = sentence[pos2+len(entity2):pos1]
                    left = sentence[:pos2]
                    right = sentence[pos1+len(entity1):]
                    real_entity1 = entity2
                    real_entity2 = entity1
                    real_uid1 = uid2
                    real_uid2 = uid1

                if len(mid) > 30:
                    continue
                    
                sen_split = [left,mid,right,sentence]
                relationlist = rc.classify(sen_split)
                
                if len(relationlist) == 0:
                    continue

                for relation in relationlist:
                    relation_pair.append([real_entity1,real_entity2,real_uid1,real_uid2,relation])
                
            except Exception, e:
                print e

        f.close()

        save_relation_pair_path = os.path.join(basepath,'data/output/single_relation_pair/relation_pair_%s.pkl' % user[0])
        save_relation_pair_file = open(save_relation_pair_path ,'w')
        pickle.dump(relation_pair,save_relation_pair_file)
        save_relation_pair_file.close()




    print 'finished ...'


    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds    







if __name__== '__main__':
    main()


