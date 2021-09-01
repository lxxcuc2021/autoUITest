#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
from time import sleep
from ddt import ddt, file_data, unpack, data
from selenium import webdriver
from test.pages.login_page import LoginPage, TestData
from utils.log import Logger

logger = Logger(logger='testcase').getlog()

@ddt
class TestUI(unittest.TestCase):
	@classmethod
	def setUpClass(cls) -> None:
		cls.login = LoginPage()

	@classmethod
	def tearDownClass(cls) -> None:
		cls.login.close()
		logger.info('退出浏览器')

	test_data = TestData().get_data()
	logger.info('获取测试数据')
	print(test_data)

	@data(*test_data)
	@unpack
	def test_login(self, username, pwd, result_type, msg):
		self.login.login(username, pwd)
		assert_msg = self.login.get_assert_msg(result_type)
		assert msg == assert_msg
		sleep(5)
		self.login.refresh()


if __name__ == '__main__':
	unittest.main(verbosity=2)
