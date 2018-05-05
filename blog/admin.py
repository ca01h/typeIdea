# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Tag, Category
from typeIdea.custom_site import custom_site
from blog.adminforms import PostAdminForm
from typeIdea.custom_admin import BaseOwnerAdmin

# Register your models here.


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    # form = PostAdminForm
    # # 显示页面
    # list_display = ['title', 'category', 'status', 'owner', 'created_time', 'operator']
    # list_display_links = ['title']
    #
    # list_filter = ['category', 'owner']
    # search_fields = ['title', 'category__name']
    # # show_full_result_count = True
    #
    # actions_on_top = True
    # actions_on_bottom = True
    # date_hierarchy = 'created_time'
    # list_editable = ['status']
    #
    # # 编辑页面
    # fieldsets = (
    #     ('基础配置', {
    #         'fields': (('category', 'title'), 'content')
    #     }),
    #     ('高级配置', {
    #         'classes': ('collapse', 'addon'),
    #         'fields': ('tags',)
    #     })
    # )

    list_display = [
        'title', 'category', 'status', 'owner',
        'created_time', 'operator'
    ]
    list_filter = ['category']
    search_fields = ['title', 'category__name', 'owner__username']

    # 编辑页面
    save_on_top = True

    fields = (
        ('category', 'title'),
        ('desc', 'status'),
        'content', 'tags',
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            # '/cus_admin/blog/post/%s/' % obj.id
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    # operator.allow_tags = True
    operator.short_description = '操作'


# class PostInlineAdmin(admin.TabularInline):
#     fields = ('title', 'status')
#     extra = 1  # 控制额外多几个
#     min_num = 1
#     model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    # inlines = [
    #     PostInlineAdmin,
    # ]
    # list_display = ('name', 'status', 'is_nav', 'created_time')
    # fields = (
    #     'name', 'status',
    #     'is_nav',
    # )

    list_display = ('name', 'status', 'is_nav', 'created_name')
    fields = (
        'name', 'status',
        'is_nav',
    )


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    # list_display = ('name', 'status', 'created_time')
    # fields = (
    #     'name', 'status',
    # )

    list_display = ('name', 'status', 'created_name')
    fields = (
        'name', 'status'
    )
