# -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.contrib import admin
# from .models import Comment
# from typeIdea import custom_site
#
# # Register your models here.
#
#
# @admin.register(Comment, site=custom_site)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['post', 'nickname', 'content', 'website', 'created_time']

from __future__ import unicode_literals

from django.contrib import admin

from .models import Comment
from typeIdea.custom_site import custom_site


@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'nickname', 'content', 'website', 'created_time')
