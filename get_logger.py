# -*- coding: utf-8 -*-

import logging
import os

def singleton(cls):
    instances = {}
    def _singleton(*args, **kargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kargs)
        return instances[cls]
    return _singleton

'''
设定日志文件格式
'''
@singleton
class SingleLogger:
    def __init__(self, logger_name='default_logger'):
        if not os.path.isdir('log'):
            os.makedirs('log')
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        # 建立一个filehandler来把日志记录在文件里，级别为debug以上
        fh = logging.FileHandler('log/' + logger_name + ".log")
        fh.setLevel(logging.DEBUG)
        # 建立一个streamhandler来把日志打在CMD窗口上，级别为info以上
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        # 设置日志格式
        formatter = logging.Formatter('[%(levelname)-3s]%(asctime)s %(filename)s[line:%(lineno)d]:%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        #将相应的handler添加在logger对象中
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

def get_logger(logger_name='default_logger'):
    return SingleLogger(logger_name).logger

@singleton
class SingleStreamLogger:
    def __init__(self, logger_name='default_logger'):
        if not os.path.isdir('log'):
            os.makedirs('log')
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('[%(levelname)-3s]%(asctime)s %(filename)s[line:%(lineno)d]:%(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

def get_stream_logger(logger_name='default_logger'):
    return SingleStreamLogger(logger_name).logger

if __name__ == '__main__':
    logger = get_stream_logger('test')
    logger = get_stream_logger('test')
    logger.info('Everything is all right.')
    logger.debug('Print some debug message.')
    logger.error('Send out when encountered with bugs.')
