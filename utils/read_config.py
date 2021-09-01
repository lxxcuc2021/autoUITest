#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import os

class ReadConfig(object):
	"""
	读取配置文件
	"""
	def __init__(self, filename):
		self.cf = configparser.ConfigParser()
		self.cf.read(filename)

	# 读取配置文件的值
	def get_value(self, section, option):
		value = self.cf.get(section, option)
		return value
# 测试代码
# if __name__ == '__main__':
# 	filepath = os.path.dirname(__file__)
# 	file = os.path.join(filepath, 'testconfig.ini')
# 	cf = ReadConfig(file)
# 	BaiDuUrl = cf.getConfigValue('url', 'BaiduUrl')
# 	print(BaiDuUrl)


