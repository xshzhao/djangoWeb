#!/usr/bin/env python
# -*- coding=utf-8 -*-

"""
    
    @version: 1.0
    @author: xingshen.zhao
    @contact: zxswork@aliyun.com
    @time: 16/5/12 下午4:43
"""
from django.conf.urls import *
from blog.views import archive

urlpatterns = [
    url(r'^$', archive),
]
