#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
import time
from selenium.common.exceptions import NoSuchElementException
from utils.log import Logger
from config import globalconfig
import os

logger = Logger(logger='BasePage').getlog()

class BasePage(object):
	"""
	定义一个基类，封装常用的页面方法
	"""
	def __init__(self, driver=None, base_url=None):
		"""
		:param driver: 浏览器驱动
		:param base_url: 默认打开的url
		"""
		if driver is None:
			driver_path = os.path.join(globalconfig.driver_path, 'chromedriver.exe')
			self.driver = webdriver.Chrome(driver_path)
		else:
			self.driver = driver

		if base_url is None:
			self.base_url = globalconfig.base_url
		else:
			self.base_url = base_url
		# 设置默认打开的页面
		self.open_page()
		logger.info('打开默认页面')

	# 打开页面
	def open_page(self):
		self.driver.maximize_window()
		self.driver.get(self.base_url)
		sleep(1)

	# 定位单个元素
	def locate(self, by, element):
		try:
			element = self.driver.find_element(by, element)
			logger.info('find the element successful')
		except NoSuchElementException as e:
			logger.error('NoSuchElementException:{0}'.format(e))
			self.get_windows_img()
		return element

	# 定位多个元素
	def locates(self,by, element):
		try:
			element = self.driver.find_elements(by, element)
			logger.info('find the elements successful')
		except NoSuchElementException as e:
			logger.error('NoSuchElementException:{0}'.format(e))
			self.get_windows_img()
		return element

	# 文本框输入
	def set_value(self, element, text):
		element.clear()
		try:
			element.send_keys(text)
			logger.info('type {} in inputbox'.format(text))
		except NameError as e:
			logger.error('fail to type in inputbox with {}'.format(e))
			self.get_windows_img()

	# 浏览器最大化
	def max_window(self):
		self.driver.maximize_window()

	# 设置浏览器的大小
	def set_window(self, width, height):
		self.driver.set_window_size(width, height)

	# 退出浏览器
	def quit(self):
		self.driver.quit()

	# 浏览器前进
	def forward(self):
		self.driver.forward()

	# 浏览器后退
	def back(self):
		self.driver.back()

	# 隐式等待
	def wait(self, second):
		self.driver.implicitly_wait(second)

	# 关闭当前窗口
	def close(self):
		try:
			self.driver.close()
		except NameError as e:
			print('Fail to close')

	# 保存图片
	def get_windows_img(self):
		img_path = globalconfig.report_path+'/screenpicture'
		img_name_format = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
		image_name = os.path.join(img_path, '{0}.png'.format(img_name_format))
		try:
			self.driver.get_screenshot_as_file(image_name)
			logger.info('take screenshot and save to folder:/screenshots')
		except NameError as e:
			logger.error('fail to take screenpicture!{0}'.format(e))
			self.get_windows_img()
	# 浏览器刷新
	def refresh(self):
		self.driver.refresh()

	# 返回弹框页面
	def switch_alert(self):
		return self.driver.switch_to.alert

