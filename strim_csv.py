# encoding: utf-8

"""
__title__ = 'strim_csv'
__author__ = 'Jeffmxh'
"""

import argparse
import codecs
import numpy as np

def strim_csv(filename, output='output.txt', sep='\t'):
    '''处理一些非对齐的csv

    用于处理一些本应该是每一行项目数相同却
    有各种bug的csv文件，该函数会逐行读取文本
    并保留行长度为众数的生成一个新的文本文件

    Arguments:
        filename: path to the input file
        output: filename of the output file, 'output.txt' by default
        sep: Specify the sep between items
    Usage:
        strim_csv(filename='input.txt', output='output.txt', sep='\t')
    '''
    content_raw = []
    with codecs.open(filename , 'r', encoding='utf-8') as f:
        for line in f.readlines():
            content_raw.append(line)

    content_len = np.array([len(x.split(sep)) for x in content_raw])
    most_common = np.argmax(np.bincount(content_len))
    content = []
    for i,x in enumerate(content_raw):
        if content_len[i] == most_common:
            content.append(x)
    with codecs.open(output, 'w', encoding='utf-8') as f:
        f.writelines(''.join(content))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='处理讨厌的csv文件脚本说明')
    parser.add_argument('-i', '--inpath', dest='input_path', nargs='?', default='',
                        help='Path to the txt file to deal with.')
    parser.add_argument('-o', '--outpath', dest='output_path', nargs='?', default='output.txt',
                        help='Path to the txt file to deal with.')
    parser.add_argument('-s', '--sep', dest='sep_mark', nargs='?', default='\t',
                        help='Specify the symbol used as sep.')

    args = parser.parse_args()
    strim_csv(filename = args.input_path,
              output = args.output_path,
              sep = args.sep_mark)