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
    relationList = []

    relation = pengyou_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = guimi_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = nvyou_rule(sen_split)
    if  relation != None:
        relationList.append(relation)    

    relation = qiannvyou_rule(sen_split)
    if  relation != None:
        relationList.append(relation)    

    relation = aimei_rule(sen_split)
    if  relation != None:
        relationList.append(relation)  

    relation = zhuanglian_rule(sen_split)
    if  relation != None:
        relationList.append(relation)  

    relation = zhuangshan_rule(sen_split)
    if  relation != None:
        relationList.append(relation)  

    relation = qizi_rule(sen_split)
    if  relation != None:
        relationList.append(relation)  

    relation = erzi_rule(sen_split)
    if  relation != None:
        relationList.append(relation) 

    relation = tongxue_rule(sen_split)
    if  relation != None:
        relationList.append(relation) 

    relation = tongmen_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = ouxiang_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = qianqi_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = feiwen_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = qingdi_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = buhe_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = xiaohua_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = jiuai_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = laoxiang_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = jingjiren_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = laoshi_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = gege_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = hezuo_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = fuhe_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = duiyou_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = tishen_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = jiedilian_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = qixiayiren_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = tongju_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = gonggong_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = jiejie_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = zufu_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    relation = nvxu_rule(sen_split)
    if  relation != None:
        relationList.append(relation)

    return relationList


def not_relation(relation):

    not_change_set = [u'朋友',u'闺蜜',u'暧昧',u'撞脸',u'撞衫', \
                    u'夫妻',u'同学',u'同门',u'偶像',u'绯闻', \
                    u'情敌',u'不和',u'校花',u'旧爱',u'老乡',\
                     u'经纪人',u'合作',u'复合',u'队友',u'替身',\
                     u'姐弟恋',u'旗下艺人',u'同居',u'公公',u'女婿']

    if relation in not_change_set:
        return relation 


    if relation == u'女友':
        return u'男友'
    if relation == u'男友':
        return u'女友'

    if relation == u'前女友':
        return u'前男友'
    if relation == u'前男友':
        return u'前女友'   

    if relation == u'妻子':
        return u'丈夫'
    if relation == u'丈夫':
        return u'妻子' 

    if relation == u'儿子':
        return u'父母'
    if relation == u'女儿':
        return u'父母' 
    if relation == u'父亲':
        return u'子女'
    if relation == u'母亲':
        return u'子女' 

    if relation == u'前妻':
        return u'前夫'
    if relation == u'前夫':
        return u'前妻'

    if relation == u'绯闻女友':
        return u'绯闻男友'
    if relation == u'绯闻男友':
        return u'绯闻女友'

    if relation == u'老师':
        return u'学生'
    if relation == u'学生':
        return u'老师'

    if relation == u'哥哥':
        return u'弟弟'
    if relation == u'弟弟':
        return u'哥哥'

    if relation == u'祖父':
        return u'孙子'
    if relation == u'孙子':
        return u'祖父'

    if relation == u'姐姐':
        return u'妹妹'
    if relation == u'妹妹':
        return u'姐姐'





def pengyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'朋友'
    keyword2 = u'好友'
    keyword3 = u'密友'
    keyword4 = u'基友'


    # case 1 : A + keyword + B
    if (keyword1 in mid  and u'男' not in mid and u'女' not in mid)or \
    keyword2 in mid or \
    keyword3 in mid or \
    keyword4 in mid:
        return u'朋友'

    # case2 A  B  是 好朋友
    if len(mid) == 0:
        if u'是' in right and \
        (keyword1 in right or \
        keyword2 in mid or \
        keyword3 in mid or \
        keyword4 in mid):
            return u'朋友'

    return None


def guimi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'闺蜜'

    # case 1  A +闺蜜 + B
    if keyword1 in mid and \
        u'男' not in mid:
        return u'闺蜜'
    
    # case 2  A  B  是 闺蜜
    if len(mid) == 0:
        if u'是' in right and \
        keyword1 in right and \
        u'男' not in right:
            return u'闺蜜'

    return None



def nvyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'女友' 
    keyword2 = u'女朋友'

    # case 1 A 女友 B
    if keyword1 in mid or \
    keyword2 in mid:
        return u'女友' 


    # case 1 A 男友 B
    keyword3 = u'男友' 
    keyword4 = u'男朋友'

    if keyword3 in mid or \
    keyword4 in mid:
        return u'男友' 

    return None




def qiannvyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'前女友' 
    keyword2 = u'前女朋友'

    # case 1 A 前女友 B
    if keyword1 in mid or \
    keyword2 in mid:
        return u'前女友' 


    # case 1 A 前男友 B
    keyword3 = u'前男友' 
    keyword4 = u'前男朋友'

    if keyword3 in mid or \
    keyword4 in mid:
        return u'前男友' 

    return None


def aimei_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'暧昧'
    keyword2 = u'亲密'
    keyword3 = u'亲昵'
    keyword4 = u'甜蜜'

    # case 1 A B 暧昧
    if keyword1 in right or \
    keyword2 in right or \
    keyword3 in right or \
    keyword4 in right:
        return u'暧昧'
    
    return None



def zhuanglian_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'撞脸'

    # case 1 A 撞脸 B
    if keyword1 in mid:
        return u'撞脸'

    # case 2  A 与 B 撞脸
    if u'与' in mid and \
    keyword1 in right:
        return u'撞脸'
    
    return None



def zhuangshan_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'撞衫'

    # case 1 A 撞衫 B
    if keyword1 in mid:
        return u'撞衫'

    return None


def qizi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    #####################################

    keyword1 = u'妻子'
    keyword2 = u'爱妻'
    keyword3 = u'老婆'
    keyword4 = u'爱人'

    # case 1 A + 妻子 +B
    if keyword1 in mid or \
    keyword2 in mid or \
    keyword3 in mid or \
    keyword4 in mid:
        return u'妻子'

    ####################################

    keyword5 = u'丈夫'
    keyword6 = u'老公'

    # case 1 A + 丈夫 +B
    if keyword5 in mid or \
    keyword6 in mid :
        return u'丈夫'


    ####################################

    keyword7 = u'夫妻'
    keyword8 = u'夫妇'
    keyword9 = u'配偶'

    # case 1 AB 夫妻
    if len(mid) == 0:
        if keyword7 in right or \
        keyword8 in right or \
        keyword9 in right:
            return u'夫妻'

    return None

def erzi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'儿子'
    # case 1 A 儿子 B
    if keyword1 in mid:
        return u'儿子'

    keyword2 = u'女儿'
    # case 1 A 女儿 B
    if keyword2 in mid:
        return u'女儿'

    keyword3 = u'父亲'
    keyword4 = u'爸爸'
    # case 1 A 父亲 B
    if keyword3 in mid or \
    keyword4 in mid:
        return u'父亲'

    keyword5 = u'母亲'
    keyword6 = u'妈妈'
    # case 1 A 母亲 B
    if keyword5 in mid or \
    keyword6 in mid:
        return u'母亲'

    return None
    


def tongxue_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'同学'   
    keyword2 = u'同班'   
    keyword3 = u'同窗'   

    # case 1 A 同学 B

    if keyword1 in mid or \
    keyword2 in mid or \
    keyword3 in mid:
        return u'同学'
    
    # case 2 A 与 B 是同学/同窗

    if u'与' in mid and \
    u'是' in right and \
    (keyword1 in right or \
    keyword2 in right or \
    keyword3 in right):
        return u'同学'

    return None


def tongmen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'同门'   
    keyword2 = u'师弟'   
    keyword3 = u'师兄'   
    keyword4 = u'师妹'
    keyword5 = u'师姐'

    # case 1 A  同门/师弟/师妹/师兄/师姐  B
    if keyword1 in mid or \
    keyword2 in mid or \
    keyword3 in mid or \
    keyword4 in mid or \
    keyword5 in mid:
        return u'同门' 


    return None



def ouxiang_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'偶像' 
    keyword2 = u'崇拜' 

    # case 1 A 偶像 B
    if keyword1 in mid or \
    keyword2 in mid :
        return u'偶像' 
    
    return None

def qianqi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'前妻' 
    keyword2 = u'前夫'    

    #case 1  A 前妻 B
    if keyword1 in mid:
        return u'前妻' 

    # case 1 A 前夫 B
    if keyword2 in mid:
        return u'前夫' 

    return None



def feiwen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'绯闻女友' 
    #case 1
    if keyword1 in mid:
        return u'绯闻女友' 

    keyword2 = u'绯闻男友' 
    #case 1 
    if keyword2 in mid:
        return u'绯闻男友' 


    keyword3 = u'绯闻' 
    # case 1 
    if keyword3 in mid:
        return u'绯闻'

    return None


def qingdi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'情敌' 
    # case 1 A 情敌 B
    if keyword1 in mid:
        return u'情敌' 
    
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
        return u'不和' 
  
    return None


def xiaohua_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'校花'

    if keyword1 in total:
        return  u'校花'

    return None



def jiuai_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'旧爱'
    keyword2 = u'前任'

    #case 1 A 旧爱 B
    if keyword1 in mid or \
    keyword2 in mid:
        return u'旧爱'

    return None

def laoxiang_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'老乡'
    if keyword1 in total:
        return u'老乡'
    
    return None

def jingjiren_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'经纪人'
    # case A 经纪人 B
    if keyword1 in mid:
        return u'经纪人'

    return None

def laoshi_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'恩师'
    keyword2 = u'老师'
    keyword3 = u'师傅'
    keyword4 = u'师父'

    # case 1 A 老师 B

    if keyword1 in mid or \
    keyword2 in mid or \
    keyword3 in mid or \
    keyword4 in mid:
        return u'老师' 



    keyword5 = u'徒弟'
    keyword6 = u'学生'
    keyword7 = u'捧起'
    keyword8 = u'捧红'
    # case 1  A 学生 B
    if keyword5 in mid or \
    keyword6 in mid or \
    keyword7 in mid or \
    keyword8 in mid:
        return u'学生'


    keyword9 = u'师徒'
    # AB 师徒
    if len(mid) == 0:
        if keyword9 in right:
            return u'师徒'

    return None



def gege_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]

    keyword1 = u'哥哥'
    keyword2 = u'表哥'
    # case 1 A 哥哥 B
    if keyword1 in mid or \
    keyword2 in mid :
        return u'哥哥'


    keyword3 = u'弟弟'
    keyword4 = u'表弟'
    # case 1 A 弟弟 B
    if keyword3 in mid or \
    keyword4 in mid:
        return u'弟弟'

    keyword5 = u'兄弟'
    keyword6 = u'手足'
    # case 1 A B兄弟
    if keyword5 in right or \
    keyword6 in right:
        return u'兄弟'

    return None



def hezuo_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'合作' 

    if keyword1 in total:
        return u'合作'
    
    return None

def fuhe_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'复合' 
    # case 1 A B 复合
    if keyword1 in right:
        return u'复合' 

    return None


def duiyou_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'队友' 
    keyword2 = u'成员' 

    if keyword1 in total or \
    keyword2 in total:
        return u'队友' 

    return None

def tishen_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'替身' 
    # case 1 A 替身 B
    if keyword1 in mid:
        return u'替身' 

    return None


def jiedilian_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'姐弟恋' 

    if keyword1 in right:
        return u'姐弟恋' 

    return None   

def qixiayiren_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'旗下艺人' 

    if keyword1 in total:
        return u'旗下艺人' 
    return None   

def tongju_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'同居' 

    if keyword1 in right:
        return u'同居' 

    return None   

def gonggong_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'公公' 

    if keyword1 in mid:
        return u'公公' 

    return None   


def jiejie_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'姐姐' 

    # case 1 
    if keyword1 in mid :
        return u'姐姐' 

    keyword2 = u'妹妹' 
    # case 1 
    if keyword2 in mid:
        return u'妹妹' 

    return None 

def zufu_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'祖父' 

    if keyword1 in mid:
        return u'祖父' 

    return None 


def nvxu_rule(sen_split):
    left,mid,right,total = sen_split[0],sen_split[1],sen_split[2],sen_split[3]
    keyword1 = u'女婿' 

    if keyword1 in mid:
        return u'女婿' 

    return None 