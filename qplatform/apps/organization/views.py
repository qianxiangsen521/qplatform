# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import CityDict, CourseOrg
from .forms import UserAskForm
from qplatform.apps.courses.models import Course
from qplatform.apps.operation.models import UserFavorite

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger


class OrgListView(View):
    def get(self, request):
        all_citys = CityDict.objects.all()
        all_orgs = CourseOrg.objects.all()

        # 对热门机构排序的提取
        hot_orgs = all_orgs.order_by('-click_num')[:5]

        # 对城市信息的筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))

        # 对机构类别进行筛选
        org_category = request.GET.get('ct', '')
        if org_category:
            all_orgs = all_orgs.filter(category=org_category)

        # 对学习人数 课程数的排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_orgs = all_orgs.order_by('-student_nums')
            elif sort == 'courses':
                all_orgs = all_orgs.order_by('-course_nums')

        orgs_num = all_orgs.count()

        # 课程列表页面的分页功能
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 2, request=request)

        orgs = p.page(page)

        return render(request, 'org-list.html', {'all_citys': all_citys,
                                                 'orgs': orgs,
                                                 'orgs_num': orgs_num,
                                                 'city_id': city_id,
                                                 'org_category': org_category,
                                                 'hot_orgs': hot_orgs,
                                                 'sort': sort})


class UserAskView(View):
    """
    用户咨询
    """
    def post(self, request):
        user_ask_form = UserAskForm(request.POST)
        if user_ask_form.is_valid():
            # mobile = request.POST.get('mobile', '')

           user_ask = user_ask_form.save(commit=True)
           # user_ask.xxx = request.POST.get('xxx', '')
           # user_ask.save()
           return HttpResponse('{"status":"success"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail", "msg":"咨询失败"}', content_type='application/json')


class OrgDetailHomeView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # all_courses = Course.objects.filter(course_org_id=int(org_id))
        # 反向查询的方法 有外键的地方都可以这样做 django ORM的一种用法
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:1]
        current_page = 'home'
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=3):
                has_fav = True
        return render(request, 'org-detail-homepage.html',
                      {'all_courses': all_courses,
                       'all_teachers': all_teachers,
                       'course_org': course_org,
                       'current_page': current_page,
                       'has_fav': has_fav})


class OrgDetailCourseView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # all_courses = Course.objects.filter(course_org_id=int(org_id))
        # 反向查询的方法 有外键的地方都可以这样做 django ORM的一种用法
        all_courses = course_org.course_set.all()
        current_page = 'course'
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=3):
                has_fav = True
        return render(request, 'org-detail-course.html',
                      {'all_courses': all_courses,
                       'course_org': course_org,
                       'current_page': current_page,
                       'has_fav': has_fav})


class OrgDetailDescView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # all_courses = Course.objects.filter(course_org_id=int(org_id))
        # 反向查询的方法 有外键的地方都可以这样做 django ORM的一种用法
        current_page = 'desc'
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=3):
                has_fav = True
        return render(request, 'org-detail-desc.html',
                      {
                       'course_org': course_org,
                       'current_page': current_page,
                       'has_fav': has_fav})


class OrgDetailTeacherView(View):
    def get(self, request, org_id):
        course_org = CourseOrg.objects.get(id=int(org_id))
        # all_courses = Course.objects.filter(course_org_id=int(org_id))
        # 反向查询的方法 有外键的地方都可以这样做 django ORM的一种用法
        all_teachers = course_org.teacher_set.all()
        current_page = 'teacher'
        has_fav = False
        if request.user.is_authenticated():
            if UserFavorite.objects.filter(user=request.user, fav_id=course_org.id, fav_type=3):
                has_fav = True
        return render(request, 'org-detail-teachers.html',
                      {
                       'all_teachers': all_teachers,
                       'course_org': course_org,
                       'current_page': current_page,
                       'has_fav': has_fav})


class AddUserFavView(View):
    def post(self, request):
        fav_id = request.POST.get('fav_id', '0')
        fav_type = request.POST.get('fav_type', '0')
        # 判断一下用户是否已经登录
        if not request.user.is_authenticated():
            return HttpResponse('{"status":"fail", "msg":"用户未登录"}', content_type='application/json')
        # 查询收藏记录是否存在 如果存在呢就是用户取消收藏 否则呢就是添加收藏
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            exist_records.delete()
            return HttpResponse('{"status":"success", "msg":"收藏"}', content_type='application/json')
        else:
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.user = request.user
                user_fav.fav_type = int(fav_type)
                user_fav.fav_id = int(fav_id)
                user_fav.save()
                return HttpResponse('{"status":"success", "msg":"已收藏"}', content_type='application/json')
            else:
                return HttpResponse('{"status":"fail", "msg":"收藏出错"}', content_type='application/json')
