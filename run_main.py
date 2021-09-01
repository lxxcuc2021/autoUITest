#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import os
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
from config import globalconfig
from utils.send_mail import sendmail
from utils.log import Logger


report_name = '测试报告名称'
report_title = '测试报告标题'
report_desc = '测试报告描述'
report_path = os.path.abspath(os.path.dirname(__file__)) + '/report/'
now = time.strftime("%Y%m%d %H%M", time.localtime(time.time()))
report_file = os.path.join(report_path, now + '.html')


def all_case():
	testcase_path = globalconfig.testcase_path
	discover = unittest.defaultTestLoader.discover(start_dir=testcase_path, pattern='test*.py')
	return discover


if __name__ == '__main__':
	with open(report_file, 'wb') as fp:
		runner = HTMLTestRunner(stream=fp, title=report_title, description=report_desc)
		runner.run(all_case())
	sendmail(report_file)

