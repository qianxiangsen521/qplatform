# -*- coding: utf-8 -*-
from django import forms

from captcha.fields import CaptchaField
__author__ = 'dongfangyao'
__date__ = '2017/9/29 上午10:07'
__product__ = 'PyCharm'
__filename__ = 'forms.py'


class LoginForm(forms.Form):
    username = forms.CharField(required=True, max_length=20)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6, max_length=20)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ForgetPwdForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': u'验证码错误'})


class ModifyPwdForm(forms.Form):
    password = forms.CharField(required=True, min_length=6, max_length=20)
    password2 = forms.CharField(required=True, min_length=6, max_length=20)
