# -*- coding: utf-8 -*-
# project:zhongye
# author: Administrator
# contact: 1506032039@qq.com
# software: PyCharm
# file: urls.py
# time: 2019/5/2 14:38

from django.conf.urls import url
from . import views
from .view import sample

urlpatterns = [
    url(r'zhongye/$', views.first, name='first'),
    url(r'approval_index/$', views.approval_index, name="approval_index"),
    url(r'approval_report/$', views.approval_report, name="approval_report"),
]
