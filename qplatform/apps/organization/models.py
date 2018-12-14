# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'城市名字')
    desc = models.CharField(max_length=200, verbose_name=u'城市描述')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'城市信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'机构名字')
    desc = models.TextField(verbose_name=u'机构描述')
    category = models.CharField(max_length=10, verbose_name=u'机构类别',
                                choices=(('pxjg', u'培训机构'), ('gx', u'高校'), ('gr', u'个人')), default='pxjg')
    favorites_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    image = models.ImageField(max_length=200, upload_to='org/%Y/%m', verbose_name=u'封面图')
    address = models.CharField(max_length=150, verbose_name=u'机构地址')
    city = models.ForeignKey(CityDict, verbose_name=u'所属城市')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    student_nums = models.IntegerField(default=0, verbose_name=u'学习人数')
    course_nums = models.IntegerField(default=0, verbose_name=u'课程数')

    class Meta:
        verbose_name = u'课程机构'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg, verbose_name=u'所属机构')
    name = models.CharField(max_length=50, verbose_name=u'教师名')
    image = models.ImageField(max_length=200, upload_to='teachers/%Y/%m', verbose_name=u'头像', default='')
    work_years = models.IntegerField(default=0, verbose_name=u'工作年限')
    work_company = models.CharField(max_length=50, verbose_name=u'就职公司')
    work_position = models.CharField(max_length=50, verbose_name=u'工作职位')
    work_point = models.CharField(max_length=100, verbose_name=u'教学特点')
    favorites_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'教师信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


