# -*- coding: utf-8 -*-
from django.core.mail import send_mail

from random import Random
from qplatform.apps.users.models import EmailVerifyCode
from qplatform.settings import EMAIL_FROM
__author__ = 'dongfangyao'
__date__ = '2017/9/30 上午10:11'
__product__ = 'PyCharm'
__filename__ = 'email_send.py'


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_email_to_user(user_email, send_type='register'):
    email_verify_code = EmailVerifyCode()
    email_verify_code.email = user_email
    email_verify_code.send_type = send_type
    random_str = generate_random_str(18)
    email_verify_code.code = random_str
    email_verify_code.save()
    # 下面就是开始向用户发送邮件 title content 发件人 收件人
    if send_type == 'register':
        email_title = '爱增值网络注册激活邮件'
        email_content = '只差一步啦，请点击这个链接激活您的邮箱地址，链接地址：http://127.0.0.1:8000/active/{0}'.format(random_str)
        # 开始使用django内部的邮件发送方法
        # send_mail()
        # 发件人邮箱地址  www.izengzhi.com   admin@izengzhi.com  info@izengzhi.com
        # kefu@izengzhi.com     邮件服务器   pop3收  smtp发  smtp服务器  smtp.163.com
        # smtp.163.com   smtp.izengzhi.com  17365777638@163.com  dongfangyao
        # 注册的时候   我自己qq309623978@qq.com
        send_status = send_mail(email_title, email_content, EMAIL_FROM, [user_email])
        if send_status:
            pass
    elif send_type == 'forget':
        email_title = '爱增值网络重置密码邮件'
        email_content = '请点击链接重置密码：http://127.0.0.1:8000/reset/{0}'.format(random_str)
        send_status = send_mail(email_title, email_content, EMAIL_FROM, [user_email])
        if send_status:
            pass

