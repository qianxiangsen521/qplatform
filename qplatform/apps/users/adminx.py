# -*- coding: utf-8 -*-
import xadmin
from xadmin import views

from .models import UserProfile, EmailVerifyCode, Banner
__author__ = 'dongfangyao'
__date__ = '2017/9/22 下午5:23'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'


class EmailVerifyCodeAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time')
    list_filter = ('code', 'email', 'send_type', 'send_time')
    search_fields = ('code', 'email')


class BannerAdmin(object):
    list_display = ('title', 'image', 'url', 'add_time', 'index')
    list_filter = ('title', 'image', 'url', 'add_time', 'index')
    search_fields = ('title', 'image', 'url', 'index')


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u'qxs后台管理系统'
    site_footer = u'qxs公司'
    menu_style = 'accordion'

# xadmin.site.register(UserProfile)
xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
