# encoding: utf-8

"""
__title__ = 'json_format' 
__author__ = 'Jeffmxh' 
# code is far away from bugs with the god animal protecting 
    I love animals. They taste delicious. 
              ┏┓      ┏┓ 
            ┏┛┻━━━┛┻┓ 
            ┃      ☃       ┃ 
            ┃  ┳┛  ┗┳  ┃ 
            ┃      ┻      ┃ 
            ┗━┓      ┏━┛ 
                ┃      ┗━━━┓ 
                ┃  神兽保佑    ┣┓ 
                ┃　永无BUG！   ┏┛ 
                ┗┓┓┏━┳┓┏┛ 
                  ┃┫┫  ┃┫┫ 
                  ┗┻┛  ┗┻┛ 
"""

import argparse
import json

def json_format(infile):
    assert isinstance(infile, str)
    assert infile.endswith('.json')
    with open(infile, 'r') as f:
        message = json.load(f)

    with open(infile, 'w') as f:
        json.dump(message, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='格式化json文件脚本说明')
    parser.add_argument('-i', '--inpath', dest='input_path', nargs='?', default='',
                        help='Path to the json file to deal with.')
    args = parser.parse_args()
    json_format(args.input_path)
