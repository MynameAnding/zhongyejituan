# -*- coding: utf-8 -*-
# project:zhongye
# author: Administrator
# contact: 1506032039@qq.com
# software: PyCharm
# file: urls.py
# time: 2019/5/2 14:38

from django.conf.urls import url
from .view import assign

urlpatterns = [

    url(r'assign_index/$', assign.assign_index, name="assign_index"),
    url(r'assignment_index/$', assign.assignment_index, name="assignment_index"),
    url(r'^LoadAssignData/$', assign.LoadAssignData, name='LoadData'),
    url(r'^getPeopleNames/$', assign.getPeopleNames, name='LoadData'),
    url(r'^updateGetPeople/$', assign.updateGetPeople, name='LoadData'),
]
