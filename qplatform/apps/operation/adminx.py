# -*- coding: utf-8 -*-
import xadmin

from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse
__author__ = 'dongfangyao'
__date__ = '2017/9/22 下午8:29'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'


class UserAskAdmin(object):
    list_display = ('name', 'mobile', 'course_name', 'add_time')
    list_filter = ('name', 'mobile', 'course_name', 'add_time')
    search_fields = ('name', 'mobile', 'course_name')


class CourseCommentAdmin(object):
    list_display = ('user', 'course', 'comments', 'add_time')
    list_filter = ('user__username', 'course__name', 'comments', 'add_time')
    search_fields = ('user__username', 'course__name', 'comments')


class UserFavoriteAdmin(object):
    list_display = ('user', 'fav_type', 'fav_id', 'add_time')
    list_filter = ('user__username', 'fav_type', 'fav_id', 'add_time')
    search_fields = ('user__username', 'fav_type', 'fav_id')


class UserMessageAdmin(object):
    list_display = ('user', 'message', 'has_read', 'add_time')
    list_filter = ('user', 'message', 'has_read', 'add_time')
    search_fields = ('user', 'message', 'has_read')


class UserCourseAdmin(object):
    list_display = ('user', 'course', 'add_time')
    list_filter = ('user__username', 'course__name', 'add_time')
    search_fields = ('user__username', 'course__name')


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
