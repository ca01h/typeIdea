# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render
from blog.models import Post, Tag, Category
from config.models import SlideBar
from comment.models import Comment

# Create your views here.

def get_common_context():
    categories = Category.objects.filter(status=1)  # TODO: fix magic number
    """
    1.Hit the DB
    nav_cates = categories.filter(is_nav=True)
    cates = categories.filter(is_nav=False)

    2.
    nav_cates = [cate for cate in categories if cate.is_nav]
    cates = [cate for cate in categories if not cate.is_nav]
    """

    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    slidebars = SlideBar.objects.filter(status=1)

    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]

    context = {
        'nav_cates': nav_cates,
        'cates': cates,
        'slidebars': slidebars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,

    }
    return context



def post_list(request, tag_id=None, category_id=None):

    # 分页
    page_size = 3
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except TypeError:
        page = 1

    queryset = Post.objects.all()
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
        'posts': posts,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404('post does not exist')
    context = {
        'post': post,
    }
    common_context = get_common_context()
    context.update(common_context)
    return render(request, 'blog/detail.html', context=context)