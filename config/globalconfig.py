#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import os
from utils.read_config import ReadConfig

# 获取config.ini的路径
file_path = os.path.abspath(os.path.dirname(__file__))
# 获取配置文件
file_name = os.path.join(file_path, 'config.ini')

# 获取config.ini中参数值
project_path = ReadConfig(file_name).get_value('project', 'project_path')
browser_name = ReadConfig(file_name).get_value('browserType', 'browserName')
base_url = ReadConfig(file_name).get_value('env', 'base_url')
user = ReadConfig(file_name).get_value('env', 'user')
pwd = ReadConfig(file_name).get_value('env', 'pwd')
# 日志路径
log_path = os.path.join(project_path, 'log')
# 测试用例路径
testcase_path = os.path.join(project_path, 'test', 'case')
# 测试报告路径
report_path = os.path.join(project_path, 'report')
# 测试数据路径
data_path = os.path.join(project_path, 'data')
# 浏览器驱动路径
driver_path = os.path.join(project_path, 'drivers')
