#!/usr/bin/env python
# -*- coding=utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


# Create your models here.
# 增加模块
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


admin.site.register(BlogPost, BlogPostAdmin)
