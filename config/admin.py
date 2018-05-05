# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
from typeIdea.custom_site import custom_site
from typeIdea.custom_admin import BaseOwnerAdmin

# Register your models here.


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = ('title', 'href', 'status', 'weight', 'created_time')


@admin.register(SlideBar, site=custom_site)
class SlideBar(BaseOwnerAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
