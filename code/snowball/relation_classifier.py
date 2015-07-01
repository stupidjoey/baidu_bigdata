# !/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import jieba
import jieba.posseg as pseg
import os
import re
import numpy as np
import pickle



def classify(sen_split):
    relation = pengyou_rule(sen_split)
    if  relation != None:
        return relation
    relation = guimi_rule(sen_split)
    if  relation != None:
        return relation
    relation = qiannvyou_rule(sen_split)   
    if  relation != None:
        return relation
    relation = aimei_rule(sen_split)
    if  relation != None:
        return relation
    relation = zhuanglian_rule(sen_split)
    if  relation != None:
        return relation
    relation = zhuangshan_rule(sen_split)
    if  relation != None:
        return relation
    relation = fufu_rule(sen_split)
    if  relation != None:
        return relation
    relation = fuzi_rule(sen_split)
    if  relation != None:
        return relation
    relation = tongxue_rule(sen_split)
    if  relation != None:
        return relation
    relation = ouxiang_rule(sen_split)
    if  relation != None:
        return relation
    relation = qianqi_rule(sen_split)
    if  relation != None:
        return relation
    relation = feiwen_rule(sen_split)
    if  relation != None:
        return relation
    relation = qingdi_rule(sen_split)
    if  relation != None:
        return relation
    relation = nvyou_rule(sen_split)
    if  relation != None:
        return relation
    relation = buhe_rule(sen_split)
    if  relation != None:
        return relation
    relation = xiaohua_rule(sen_split)
    if  relation != None:
        return relation
    relation = jiuai_rule(sen_split)
    if  relation != None:
        return relation
    relation = laoxiang_rule(sen_split)
    if  relation != None:
        return relation
    relation = jingjiren_rule(sen_split)
    if  relation != None:
        return relation
    relation = laoshi_rule(sen_split)
    if  relation != None:
        return relation
    relation = didi_rule(sen_split)
    if  relation != None:
        return relation
    relation = tongmen_rule(sen_split)
    if  relation != None:
        return relation
    relation = hezuo_rule(sen_split)
    if  relation != None:
        return relation
    relation = fuhe_rule(sen_split)
    if  relation != None:
        return relation
    relation = duiyou_rule(sen_split)
    if  relation != None:
        return relation
    relation = tishen_rule(sen_split)
    if  relation != None:
        return relation
    relation = jiedilian_rule(sen_split)
    if  relation != None:
        return relation
    relation = qixiayiren_rule(sen_split)
    if  relation != None:
        return relation
    relation = tongju_rule(sen_split)
    if  relation != None:
        return relation
    relation = gonggong_rule(sen_split)
    if  relation != None:
        return relation
    relation = jiejie_rule(sen_split)
    if  relation != None:
        return relation

    return None


def pengyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'私底下'
    keyword2 = u'私下'
    keyword3 = u'朋友'
    keyword4 = u'好友'
    keyword5 = u'搭档'
    keyword6 = u'密友'
    keyword7 = u'基友'
    keyword8 = u'拍档'

    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total or \
    keyword7 in total or \
    keyword8 in total:
        return 'pengyou'
    else:
        return None


def guimi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'闺蜜'
    if keyword1 in total:
        return 'guimi'
    else:
        return None


def qiannvyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'前女友'
    keyword2 = u'前女朋友'
    keyword3 = u'前男友'
    keyword4 = u'前男朋友'

    if keyword1 in mid or \
    keyword2 in mid :
        return 'qiannvyou'
    elif keyword3 in mid or \
    keyword4 in mid:
        return 'qiannanyou'
    else:
        return None

def aimei_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'暧昧'
    keyword2 = u'亲密'
    keyword3 = u'亲昵'
    keyword4 = u'甜蜜'

    if keyword1 in right or \
    keyword2 in right or \
    keyword3 in right or \
    keyword4 in right:
        return 'aimei'
    else:
        return None

def zhuanglian_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'撞脸'
    if keyword1 in total:
        return 'zhuanglian'
    else:
        return None


def zhuangshan_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'撞衫'
    if keyword1 in total:
        return 'zhuangshan'
    else:
        return None


def fufu_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'夫妇'
    keyword2 = u'配偶'
    keyword3 = u'夫妻'
    keyword4 = u'结婚'
    keyword5 = u'丈夫'
    keyword6 = u'爱妻'
    keyword7 = u'妻子'
    keyword8 = u'老婆'
    keyword9 = u'爱人'


    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total or \
    keyword7 in total or \
    keyword8 in total or \
    keyword9 in total:
        return 'fufu'
    else:
        return None

def fuzi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'子女'
    keyword2 = u'儿子'
    keyword3 = u'女儿'
    keyword4 = u'父亲'
    keyword5 = u'爸爸'
    keyword6 = u'母亲'
    keyword7 = u'妈妈'

    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total or \
    keyword7 in total:
        return 'fuzi'
    else:
        return None

def tongxue_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'同学'   
    keyword2 = u'同班'   
    keyword3 = u'同窗'   
    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total:
        return 'tongxue'
    else:
        return None

def ouxiang_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'偶像' 
    keyword2 = u'崇拜' 

    if keyword1 in mid or \
    keyword2 in mid :
        return 'ouxiang'
    else:
        return None

def qianqi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'前妻' 
    keyword2 = u'前夫'    

    if keyword1 in mid:
        return 'qianqi'
    elif keyword2 in mid:
        return 'qianfu'
    else:
        return None

def feiwen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'绯闻' 
    if keyword1 in total:
        return 'feiwen'
    else:
        return None


def qingdi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'情敌' 

    if keyword1 in total:
        return 'qingdi'
    else:
        return None

def nvyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'女友' 
    keyword2 = u'男友' 
    keyword3 = u'情侣' 
    keyword4 = u'恋爱' 
    keyword5 = u'恋情' 

    if keyword1 in mid:
        return 'nvyou'
    elif keyword2 in mid:
        return 'nanyou'
    elif keyword3 in total or keyword4 in total or keyword5 in total:
        return 'qinglv'
    else:
        return None

def buhe_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'不和'    
    keyword2 = u'撕破脸'    
    keyword3 = u'翻脸'    
    keyword4 = u'结怨'    
    keyword5 = u'反目'    
    keyword6 = u'决裂'    
    keyword7 = u'骂战'    
    keyword8 = u'交恶'    


    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total or \
    keyword7 in total or \
    keyword8 in total:
        return 'buhe'
    else:
        return None


def xiaohua_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'校花'

    if keyword1 in total:
        return 'xiaohua'
    else:
        return None



def jiuai_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'旧爱'
    keyword2 = u'分手'
    keyword3 = u'前任'

    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total:
        return 'jiuai'
    else:
        return None

def laoxiang_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'老乡'
    if keyword1 in total:
        return 'laoxiang'
    else:
        return None

def jingjiren_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'经纪人'
    if keyword1 in mid:
        return 'jingjiren'
    else:
        return None

def laoshi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'恩师'
    keyword2 = u'老师'
    keyword3 = u'师傅'
    keyword4 = u'师父'
    keyword5 = u'师徒'
    keyword6 = u'恩师'
    keyword7 = u'教练'
    keyword8 = u'教练'
    keyword9 = u'徒弟'
    keyword10 = u'学生'
    keyword11 = u'捧起'
    keyword12 = u'捧红'


    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total or \
    keyword7 in total or \
    keyword8 in total or \
    keyword9 in total or \
    keyword10 in total or \
    keyword11 in total or \
    keyword12 in total:
        return 'laoshi'
    else:
        return None



def didi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'弟弟'
    keyword2 = u'哥哥'
    keyword3 = u'兄弟'
    keyword4 = u'手足'
    keyword5 = u'表哥'
    keyword6 = u'表弟'

    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total or \
    keyword4 in total or \
    keyword5 in total or \
    keyword6 in total:
        return 'didi'
    else:
        return None

def tongmen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'同门'   
    keyword2 = u'师弟'   
    keyword3 = u'师兄'   

    if keyword1 in total or \
    keyword2 in total or \
    keyword3 in total:
        return 'tongmen'
    else:
        return None


def hezuo_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'合作' 

    if keyword1 in total:
        return 'hezuo'
    else:
        return None

def fuhe_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'复合' 

    if keyword1 in total:
        return 'fuhe'
    else:
        return None


def duiyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'队友' 
    keyword2 = u'成员' 

    if keyword1 in total or \
    keyword2 in total:
        return 'duiyou'
    else:
        return None

def tishen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'替身' 

    if keyword1 in total:
        return 'tishen'
    else:
        return None


def jiedilian_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'姐弟恋' 

    if keyword1 in total:
        return 'jiedilian'
    else:
        return None   

def qixiayiren_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'旗下艺人' 

    if keyword1 in total:
        return 'qixiayiren'
    else:
        return None   

def tongju_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'同居' 

    if keyword1 in total:
        return 'tongju'
    else:
        return None   

def gonggong_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'公公' 

    if keyword1 in total:
        return 'gonggong'
    else:
        return None   


def jiejie_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'姐姐' 
    keyword2 = u'妹妹' 

    if keyword1 in total or \
    keyword2 in total:
        return 'jiejie'
    else:
        return None 
