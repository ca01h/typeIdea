# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blog.models import Post

# Create your views here.


def post_list(request, tag_id=None, category_id=None):
    queryset = Post.objects.all()
    if category_id:
        # 分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        # 标签页面
        queryset = queryset.filter(tag_id=tag_id)
    context = {
        'posts': queryset
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    context = {
        'name': 'post_detail'
    }
    return render(request, 'blog/detail.html', context=context)