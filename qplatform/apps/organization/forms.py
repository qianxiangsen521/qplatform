# -*- coding: utf-8 -*-
from django import forms

import re

from qplatform.apps.operation.models import UserAsk
__author__ = 'dongfangyao'
__date__ = '2017/11/6 下午4:37'
__product__ = 'PyCharm'
__filename__ = 'forms'


class UserAskForm(forms.ModelForm):
    # email = forms.CharField(required=True)
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u'手机号码非法', code='mobile_invalid')
