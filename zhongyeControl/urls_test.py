# -*- coding: utf-8 -*-
# project:zhongye
# author: Administrator
# contact: 1506032039@qq.com
# software: PyCharm
# file: urls.py
# time: 2019/5/2 14:38

from django.conf.urls import url
from .view import test

urlpatterns = [

    url(r'experiment/$', test.experiment, name="experiment"),
    url(r'test_index/$', test.test_index, name="test_index"),
    url(r'^experiment_print/$', test.experiment_print, name='experiment_print'),
    url(r'^LoadExpData/$', test.LoadExpData, name='LoadData'),
    url(r'^saveExpData/$', test.saveExpData, name='LoadData'),
    url(r'^selectExpData/$', test.selectExpData, name='LoadData'),
    url(r'^assignWrong/$', test.assignWrong, name='LoadData'),
    url(r'^getMachine/$', test.getMachine, name='LoadData'),
    url(r'^selectSample/$', test.selectSample, name='LoadData'),
    url(r'^PrintExpData/$', test.PrintExpData, name='LoadData'),
    url(r'^LoadExpInformation/$', test.LoadExpInformation, name='LoadData'),
]
