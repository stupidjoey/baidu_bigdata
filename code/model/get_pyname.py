# !/usr/bin/env python
# -*- coding: utf-8 -*-


import os



''' visit the tupu fold and get all user's pinyin name '''
'''  store the name '''


path = os.path.abspath('.')
path = path.split('/')
basepath = "/".join(path[:-2])
datapath = os.path.join(basepath,'data/train/entity_tupu/')
l = os.listdir(datapath)
print l