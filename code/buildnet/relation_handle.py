# !/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import os
import re
import pickle




def relation_reverse(rel):
    rev_rel = ''
    
    if rel == u'前女友':
        rev_rel = u'前男友'

    if rel == u'前男友':
        rev_rel =  u'前女友'

    if rel == u'绯闻女友':
        rev_rel = u'绯闻男友'

    if rel == u'绯闻男友':
        rev_rel = u'绯闻女友'

    if rel == u'前绯闻女友':
        rev_rel = u'前绯闻男友'

    if rel == u'前绯闻男友':
        rev_rel = u'前绯闻女友'