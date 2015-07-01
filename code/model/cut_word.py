# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import pickle


def main():
    starttime = datetime.datetime.now()
    
    path = os.path.abspath('.')
    path = path.split('/')
    basepath = "/".join(path[:-2])
    dictpath = os.path.join(basepath,'data/myDict.txt')
    jieba.load_userdict(dictpath)
    datapath = os.path.join(basepath,'data/train/entity_sentence/entity_sentence.poyoutian')


    # with open(datapath) as f:
    #     dataset = f.readlines()

    # total_len = len(dataset)
    # count = 0
    # word_dict = {}
    # for line in dataset:
    #     data = line[:-1].split('\t')
    #     sentence = data[0].decode('utf-8')
    #     words = list(jieba.cut(sentence, cut_all = True, HMM = True ))  # 全模式   
    #     words = set(words)
    #     for w in words:
    #         word_dict[w] = word_dict.get(w,0.0) + 1.0

    #     count += 1
    #     if count % (total_len/10) == 0:
    #         print '10%...'
    # # print word_dict


    # word_dictname = 'data/word_dict.pkl'
    # dictfile = open(os.path.join(basepath,word_dictname),'w')
    # pickle.dump(word_dict,dictfile)
    # dictfile.close()



    word_dictname = 'data/word_dict.pkl'
    dictfile = open(os.path.join(basepath,word_dictname))
    word_dict = pickle.load(dictfile)
    dictfile.close()

    word_dict = sorted(word_dict.iteritems(), key = lambda x:x[1], reverse = True)
    print len(word_dict)

    # for pair in word_dict:
    #     print pair[0],pair[1]


    # seg_list = jieba.cut(u"北影学霸校花李依伊完胜杨幂刘诗诗", cut_all = False, HMM = True)

    # words = pseg.cut(u"北影学霸校花李依伊完胜杨幂刘诗诗")
    # for w in words:
    #     print "%s %s "  % (w.word, w.flag)

    # result = jieba.tokenize(u'北影学霸校花李依伊完胜杨幂刘诗诗')
    # for tk in result:
    #     print "word:%s stat:%d \t end:%d \n" %(tk[0],tk[1],tk[2])



    endtime = datetime.datetime.now()
    print 'elapsed time is %f'  %(endtime - starttime).seconds





if __name__=='__main__':
    main()