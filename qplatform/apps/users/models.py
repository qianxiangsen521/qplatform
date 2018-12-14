# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, default=u'', verbose_name=u'昵称')
    birth = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=(('male', u'男'), ('female', u'女')), default='female',
                              verbose_name=u'性别')
    address = models.CharField(max_length=100, verbose_name=u'地址', default=u'')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name=u'手机号码')
    avatar = models.ImageField(max_length=100, upload_to=u'avatar/%Y/%m', default=u'avatar/default.png',
                               verbose_name=u'用户头像')

    class Meta:
        verbose_name = u'用户信息表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyCode(models.Model):
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮件地址')
    send_type = models.CharField(max_length=10, choices=(('register', u'注册'), ('forget', u'忘记密码')),
                                 verbose_name=u'发送类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = u'邮箱验证码'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}---({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'标题')
    image = models.ImageField(max_length=100, verbose_name=u'轮播图片地址', upload_to='banner/%Y/%m')
    url = models.CharField(max_length=200, verbose_name=u'跳转地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    index = models.IntegerField(default=100, verbose_name=u'排列顺序')

    class Meta:
        verbose_name = u'轮播图'
        verbose_name_plural = verbose_name
