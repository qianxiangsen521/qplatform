# -*- coding: utf-8 -*-
import xadmin

from .models import CourseOrg, CityDict, Teacher
__author__ = 'dongfangyao'
__date__ = '2017/9/22 下午8:16'
__product__ = 'PyCharm'
__filename__ = 'adminx.py'


class CityDictAdmin(object):
    list_display = ('name', 'desc', 'add_time')
    list_filter = ('name', 'desc', 'add_time')
    search_fields = ('name', 'desc')


class CourseOrgAdmin(object):
    list_display = ('name', 'desc', 'favorites_num', 'click_num', 'image', 'address', 'city', 'add_time')
    list_filter = ('name', 'desc', 'favorites_num', 'click_num', 'image', 'address', 'city__name', 'add_time')
    search_fields = ('name', 'desc', 'favorites_num', 'click_num', 'image', 'address', 'city__name')


class TeacherAdmin(object):
    list_display = ('org', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num',
                    'click_num', 'add_time')
    list_filter = ('org__name', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num',
                   'click_num', 'add_time')
    search_fields = ('org__name', 'name', 'work_years', 'work_company', 'work_position', 'work_point', 'favorites_num',
                     'click_num')

xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
