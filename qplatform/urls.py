# -*- coding: utf-8 -*-
"""izengzhi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.views.static import serve
import xadmin

# from izengzhi.apps.users.views import user_login
from qplatform.apps.users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetPwdView, ModifyPwdView
from qplatform.apps.organization.views import OrgListView
from qplatform.settings import MEDIA_ROOT

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^login/$', TemplateView.as_view(template_name='login.html'), name='login'),
    # url(r'^login/$', user_login, name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>[A-Za-z0-9]+)$', ActiveUserView.as_view(), name='active_user'),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<reset_code>[A-Za-z0-9]+)$', ResetPwdView.as_view(), name='reset_pwd'),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),


    # 配置上传文件的访问处理
    url(r'^upload/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 课程机构urls分发
    url(r'^org/', include('qplatform.apps.organization.urls', namespace='org'))


]
