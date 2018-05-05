# -*- coding:utf-8 -*-
__author__ = 'cao.yh'
__date__ = '2018/4/4 下午4:51'

from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required='False')
