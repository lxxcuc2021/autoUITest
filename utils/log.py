#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
import os
import time
from config import globalconfig
# 日志文件路径
log_path = globalconfig.log_path

# 定义日志类
class Logger(object):
    # 初始化Logger类
    def __init__(self, logger, cmdLevel='DEBUG', fileLevel='DEBUG'):
        """
        :param logger: logger name
        :param cmdLevel: 控制台日志级别
        :param fileLevel: 文件日志级别
        """

        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        fmt = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设定日志文件名称
        self.LogFileName = os.path.join(log_path, '{0}.log'.format(time.strftime('%Y-%m-%d')))
        # 设置文件日志
        fh = logging.FileHandler(self.LogFileName)
        fh.setFormatter(fmt)
        fh.setLevel(fileLevel)
        # 设置控制台日志
        ch = logging.StreamHandler()
        ch.setFormatter(fmt)
        ch.setLevel(cmdLevel)
        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

# if __name__ == '__main__':
#     logger = Logger(logger='lixx', CmdLevel='DEBUG', FileLevel='DEBUG')
#     logger.debug('this is a dug message')
#     logger.info('this is a info message')

