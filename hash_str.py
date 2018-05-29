# encoding: utf-8

"""
__title__ = 'hash_str'
__author__ = 'Jeffmxh'
"""

import hashlib
import argparse

def hash_md5(string):
    md5 = hashlib.md5()
    md5.update(bytes(string, encoding='utf-8'))
    return md5.hexdigest()

def hash_sha1(string):
    sha1 = hashlib.sha1()
    sha1.update(bytes(string, encoding='utf-8'))
    return sha1.hexdigest()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='md5/sha1加密脚本说明')
    parser.add_argument('-i', '--input', dest='input_str', nargs='?', default='',
                        help='String to hash.')
    args = parser.parse_args()
    print('Hash with md5: ', hash_md5(args.input_str))
    print('Hash with sha1: ', hash_sha1(args.input_str))