#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

filebasepath = 'I:\\baidu_bigdata\\train\\relation-competition\\train'

def main():
    starttime = datetime.datetime.now()


    tupu_filepath = filebasepath + '\\entity_tupu\\entity_tupu.songqian'

    uids = set()
    f = open(tupu_filepath)
    for line in f:
        data = line[:-1].split('\t')
        uid1,uid2 = data[3],data[4]
        uids.add(uid1)
        uids.add(uid2)
    f.close()
    print len(uids)

    user_relation = dict()
    keyuid = '2355394'
    sentence_filepath = filebasepath + '\\entity_sentence\\entity_sentence.songqian'
    f = open(sentence_filepath)
    for line in f:
        data = line[:-1].split('\t')
        datalen = len(data)
        datalen = datalen - 1
        uidlist = data[(datalen/2)+1:]

        # temp = 0
        for idx,uid in enumerate(uidlist):
            if uid == keyuid:
                uidlist.pop(idx)
                break
        for uid in uidlist:
            user_relation.setdefault(uid,0)
            user_relation[uid] += 1
        # if temp == datalen/2:
        #     count += 1
    f.close()

    
    sorted_user_relation = sorted(user_relation.iteritems(), key = lambda x:x[1], reverse = True)
    for relation in sorted_user_relation[0:20]:
        print relation
    print len(user_relation)





    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds











if __name__=='__main__':
    main()
