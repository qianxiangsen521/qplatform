# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from qplatform.apps.organization.models import CourseOrg


class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name=u'所属的课程机构')
    name = models.CharField(max_length=50, verbose_name=u'课程名字')
    desc = models.CharField(max_length=300, verbose_name=u'课程描述')
    detail = models.TextField(verbose_name=u'课程详情')
    degree = models.CharField(max_length=2, verbose_name=u'课程难度',
                              choices=(('cj', u'初级'), ('zj', u'中级'), ('gj', u'高级')), default='cj')
    learn_duration = models.IntegerField(default=0, verbose_name=u'学习时长(分钟数)')
    student_num = models.IntegerField(default=0, verbose_name=u'学生人数')
    favorites_num = models.IntegerField(default=0, verbose_name=u'收藏人数')
    image = models.ImageField(max_length=200, upload_to='courses/%Y/%m', verbose_name=u'封面图')
    click_num = models.IntegerField(default=0, verbose_name=u'点击数')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'课程信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所属课程')
    name = models.CharField(max_length=100, verbose_name=u'章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'章节信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'所属章节')
    name = models.CharField(max_length=100, verbose_name=u'视频名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')

    class Meta:
        verbose_name = u'视频信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u'所属课程')
    name = models.CharField(max_length=100, verbose_name=u'课程资源名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'添加时间')
    download = models.FileField(max_length=100, upload_to='course/resource/%Y/%m', verbose_name=u'课程资源文件')

    class Meta:
        verbose_name = u'课程资源'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
