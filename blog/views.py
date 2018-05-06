# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Post, Tag, Category
from config.models import SlideBar
from comment.models import Comment


# Create your views here.


class CommonMixin(object):
    def get_context_data(self, **kwargs):

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

        extra_context = {
            'nav_cates': nav_cates,
            'cates': cates,
            'slidebars': slidebars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,

        }

        return super(CommonMixin, self).get_context_data(**extra_context)


class BasePostView(CommonMixin, ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3


class IndexView(BasePostView):
    pass


class CategoryView(BasePostView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        # 从URL中获取category_id值
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts


class PostView(CommonMixin, DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'


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
