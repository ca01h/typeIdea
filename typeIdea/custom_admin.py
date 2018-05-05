# -*- coding:utf-8 -*-
from __future__ import unicode_literals
__author__ = 'cao.yh'
__date__ = '2018/4/5 下午12:02'


from django.contrib import admin


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    针对有Owner属性的数据(文章、分类、标签、侧边栏、友链)，重写
    1. save_model - 保证每一条数据都属于当前用户
    2. get_queryset - 保证每个用户只能看到自己的文章
    """
    # 此方法为admin界面显示所有可编辑的Model实例
    def get_queryset(self, request):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user)

    # 此方法为admin界面用户保存Model实例时的行为：request为HttpRequest实例，obj为model实例，form为ModelForm实例，change为bool值，取决于model实例是新增的还是修改的。
    def save_model(self, request, obj, form, change):
        obj.owner = request.user  # 把request.user保存为model实例的属性
        return super(BaseOwnerAdmin, self).save_model(request, obj, form, change)