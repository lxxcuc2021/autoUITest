#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import smtplib   # 连接邮箱
from email import encoders
from email.mime.text import MIMEText   # 处理邮件文本信息
from email.mime.multipart import MIMEMultipart  # 处理邮件附件信息
from email.header import Header  # 处理邮件标题
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from utils.log import Logger

logger = Logger(logger='sendEmail').getlog()

def sendmail(filename):
    # 第三方SMTP服务
    mail_server = 'smtp.qq.com'
    mail_user = '123@qq.com'
    mail_pwd = '456'

    from_address = '123@qq.com'
    to_address = ['lixinxin0806@163.com']

    # 创建一个带附件的实例
    email = MIMEMultipart()
    email['Subject'] = Header('自动化测试报告', 'utf-8')
    email['From'] = Header('vanilla', 'utf-8')
    email['To'] = Header('全体人员', 'utf-8')

    # 邮件正文内容
    content = MIMEText('请大家查收自动化测试报告', 'plain', 'utf-8')
    email.attach(content)

    # 添加非图片附件
    att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
    att1['Content-Type'] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="test.txt"'
    email.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL(mail_server, port=465)
        smtp.login(mail_user, mail_pwd)
        smtp.sendmail(from_address, to_address, email.as_string())
        logger.info('邮件发送成功')
        smtp.quit()
    except smtplib.SMTPException:
        logger.error('error；无法发送邮件')