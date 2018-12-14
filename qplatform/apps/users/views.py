# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .models import UserProfile, EmailVerifyCode
from .forms import LoginForm, RegisterForm, ForgetPwdForm, ModifyPwdForm
from qplatform.apps.utils.email_send import send_email_to_user


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username) | Q(mobile=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_random_str_code = EmailVerifyCode.objects.filter(code=active_code)
        if all_random_str_code:
            for random_code in all_random_str_code:
                email = random_code.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ResetPwdView(View):
    def get(self, request, reset_code):
        all_random_str_code = EmailVerifyCode.objects.filter(code=reset_code)
        if all_random_str_code:
            for random_code in all_random_str_code:
                email = random_code.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')


class ModifyPwdView(View):
    def post(self, request):
        modify_pwd_form = ModifyPwdForm(request.POST)
        if modify_pwd_form.is_valid():
            pwd = request.POST.get('password', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd != pwd2:
                return render(request, 'password_reset.html', {'msg': '密码不一致!', 'email': email})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'modify_pwd_form': modify_pwd_form, 'email': email})


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            email = request.POST.get('email', '')
            # 必须要判断一下email地址是否已经注册过了
            if UserProfile.objects.filter(email=email):
                return render(request, 'register.html', {'msg': '这个邮箱地址已经注册啦，请更换！', 'register_form': register_form})
            password = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = email
            user_profile.email = email
            user_profile.password = make_password(password)
            # 必须将用户的激活状态改为未激活
            user_profile.is_active = False
            user_profile.save()
            # 开始发送验证邮件
            send_email_to_user(email, 'register')
            return render(request, 'login.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html', {'msg': '用户邮箱还未激活呢！'})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username', '')
        pass_word = request.POST.get('password', '')
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'msg': '用户名或密码错误！'})
    elif request.method == 'GET':
        return render(request, 'login.html', {})


class ForgetPwdView(View):
    def get(self, request):
        forget_pwd_form = ForgetPwdForm()
        return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form})

    def post(self, request):
        forget_pwd_form = ForgetPwdForm(request.POST)
        if forget_pwd_form.is_valid():
            email = request.POST.get('email', '')
            # 必须判断一下邮箱地址是否在用户数据表里存在
            if UserProfile.objects.filter(email=email):
                send_email_to_user(email, 'forget')
                return render(request, 'send_success.html')
            else:
                return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form, 'msg': '邮箱地址没有注册过！'})
        else:
            return render(request, 'forgetpwd.html', {'forget_pwd_form': forget_pwd_form})
