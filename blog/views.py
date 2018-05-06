# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render
from blog.models import Post, Tag

# Create your views here.


def post_list(request, tag_id=None, category_id=None):
    queryset = Post.objects.all()

    # 分页
    page_size = 3
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        # 分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        # 标签页面
        try:
            tag = Tag.objects.all()
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = queryset.filter(tag_id=tag_id)

    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('post does not exist')
    context = {
        'post': 'post'
    }
    return render(request, 'blog/detail.html', context=context)