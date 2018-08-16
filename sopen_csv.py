# encoding: utf-8

"""
__title__ = 'sopen_csv'
__author__ = 'Jeffmxh'
"""

import codecs
import numpy as np
import pandas as pd

def sopen_csv(filename, sep='\t', header=True):
    '''
    超绝csv读取函数
    '''
    content_raw = []
    with codecs.open(filename , 'r', encoding='utf-8') as f:
        for line in f.readlines():
            content_raw.append(line.strip())

    content_raw = [x.split(sep) for x in content_raw]
    content_len = np.array([len(x) for x in content_raw])
    most_common = np.argmax(np.bincount(content_len))
    content = []
    for i,x in enumerate(content_raw):
        if content_len[i] == most_common:
            content.append(x)
    temp_dict = {}
    if header:
        for i,key in enumerate(content[0]):
            temp_dict[key] = [x[i] for x in content][1:]
        df = pd.DataFrame(temp_dict, columns=content[0])
    else:
        for i,key in enumerate(content[0]):
            temp_dict[i] = [x[i] for x in content][0:]
        df = pd.DataFrame(temp_dict)
    for column in df.columns:
        try:
            df[[column]] = df[[column]].astype(int)
        except:
            pass
    return df