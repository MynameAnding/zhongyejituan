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
    url(r'^$', views.index),
    url(r'^admin/$', views.admin),
    url(r'^login/$', views.login, name='login'),
    url(r'zhongye/$', views.first, name='first'),

    url(r'test_index/$', views.test_index, name="test_index"),
    url(r'zhongye/test/$', views.test, name="test"),
    # url(r'^LoadData/$', views.LoadData, name='LoadData'),
    # url(r'^loadOriginalRecord/$', views.loadOriginalRecord, name='loadOriginalRecord'),
]
