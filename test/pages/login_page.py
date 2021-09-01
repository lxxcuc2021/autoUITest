#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from selenium import webdriver
from selenium.webdriver.common.by import By

from test.common.basepage import BasePage
from utils.log import Logger
from config import globalconfig
import os
from utils.read_excel import ReadExcel

# 定义TestData类，处理excel数据，得到测试所需数据
class TestData(object):
    def get_data(self):
        # 获取excel文件数据
        excel = ReadExcel(sheet_name='Login')
        file_data = excel.excel_reader()
        # 得到所需数据的索引，根据索引获取相应顺序的数据
        user_index = file_data[0].index('用户名')
        pwd_index = file_data[0].index('密码')
        type_index = file_data[0].index('类型')
        assert_index = file_data[0].index('预期结果')

        row_num = len(file_data)
        print(row_num)
        all_data = []
        for i in range(1, row_num):
            row_data = []
            row_data.append(file_data[i][user_index])
            row_data.append(file_data[i][pwd_index])
            row_data.append(file_data[i][type_index])
            row_data.append(file_data[i][assert_index])
            all_data.append(row_data)
        return all_data

class LoginPage(BasePage):
    def user_element(self):
        return self.locate(By.XPATH, "//input[@class='email']")
    def pwd_element(self):
        return self.locate(By.XPATH, "//input[@class='password']")
    def button_element(self):
        return self.locate(By.XPATH, '//input[@type="button"]')
    # username = ('By.XPATH', "//input[@class='email']")
    # password = ('By.XPATH', "//input[@class='password']")
    # login_button = ('By.XPATH', '//input[@type="button"]')

    def login(self, name, pwd):

        # self.name = name
        # self.pwd = pwd
        if name is not None:
            self.set_value(self.user_element(), name)
        if pwd is not None:
            # element = self.locate(* self.password)
            self.set_value(self.pwd_element(), pwd)
        self.button_element().click()

    def get_assert_msg(self, result_type):
        if result_type == 'login success':
            assert_msg = self.driver.find_element(By.XPATH, "//h1[text()='TYNAM后台管理系统']").text
        elif result_type == 'email error':
            assert_msg = self.driver.find_elements(By.XPATH, '//div[@class="msg"]')[0].text
        elif result_type == 'password error':
            assert_msg = self.driver.find_elements(By.XPATH, '//div[@class="msg"]')[1].text
        elif result_type == 'alert error':
            assert_msg = self.driver.switch_to.alert.text
            self.driver.switch_to.alert.accept()
        return assert_msg

# if __name__ == '__main__':
#     data1 = TestData().get_data()
#     print(data1)

