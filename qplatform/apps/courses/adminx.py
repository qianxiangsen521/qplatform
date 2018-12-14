# -*- coding: utf-8 -*-
import xadmin

from .models import Course, Lesson, Video, CourseResource
__author__ = 'dongfangyao'
__date__ = '2017/9/22 下午5:39'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'


class CourseAdmin(object):
    list_display = ('name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image',
                    'click_num', 'add_time')
    list_filter = ('name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image',
                   'click_num', 'add_time')
    search_fields = ('name', 'desc', 'detail', 'degree', 'learn_duration', 'student_num', 'favorites_num', 'image',
                     'click_num')


class LessonAdmin(object):
    list_display = ('course', 'name', 'add_time')
    list_filter = ('course__name', 'name', 'add_time')
    search_fields = ('course__name', 'name')


class VideoAdmin(object):
    list_display = ('lesson', 'name', 'add_time')
    list_filter = ('lesson__name', 'name', 'add_time')
    search_fields = ('lesson__name', 'name')


class CourseResourceAdmin(object):
    list_display = ('course', 'name', 'add_time', 'download')
    list_filter = ('course__name', 'name', 'add_time', 'download')
    search_fields = ('course__name', 'name', 'download')

xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

