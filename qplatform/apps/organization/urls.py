# -*- coding: utf-8 -*-
from django.conf.urls import url, include

from .views import OrgListView, UserAskView, OrgDetailHomeView, OrgDetailCourseView, OrgDetailDescView, \
    OrgDetailTeacherView, AddUserFavView
__author__ = 'dongfangyao'
__date__ = '2017/11/6 下午2:50'
__product__ = 'PyCharm'
__filename__ = 'urls'

urlpatterns = [
    # 课程机构列表页面
    url(r'^list/$', OrgListView.as_view(), name='list'),

    # 添加用户咨询
    url(r'^user_ask/$', UserAskView.as_view(), name='user_ask'),

    # 某个课程机构的详情页首页 需要机构的id
    url(r'^home/(?P<org_id>[0-9]+)/$', OrgDetailHomeView.as_view(), name='org_detail_home'),

    # 某个课程机构的课程机构页 需要机构的id
    url(r'^course/(?P<org_id>[0-9]+)/$', OrgDetailCourseView.as_view(), name='org_detail_course'),

    # 某个课程机构的介绍页 需要机构的id
    url(r'^desc/(?P<org_id>[0-9]+)/$', OrgDetailDescView.as_view(), name='org_detail_desc'),

    # 某个课程机构的教师页 需要机构的id
    url(r'^teacher/(?P<org_id>[0-9]+)/$', OrgDetailTeacherView.as_view(), name='org_detail_teacher'),

    # 用户收藏功能的
    url(r'^user_fav/$', AddUserFavView.as_view(), name='user_fav'),


]
