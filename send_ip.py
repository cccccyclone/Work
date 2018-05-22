#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import socket
from email.mime.text import MIMEText
from email.header import Header

def sendIP(server,user,pwd,receiver,ip):
    # 第三方 SMTP 服务
    mail_host = server  # 设置服务器
    mail_user = user  # 用户名
    mail_pass = pwd  # 口令

    sender = user
    receivers = [receiver]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(ip, 'plain', 'utf-8')
    message['From'] = Header("树莓派ip地址", 'utf-8')
    message['To'] = Header("测试", 'utf-8')

    subject = 'Python SMTP 邮件测试'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

#获取本级制定接口的ip地址
def get_ip_address():
        s =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(("1.1.1.1",80))
        ipaddr=s.getsockname()[0]
        s.close()
        return ipaddr

if  __name__ == '__main__' :
        ipaddr= get_ip_address()
        sendIP("smtp.163.com", "xxxx@163.com" , "xxxx", 'xxxx', ipaddr)
