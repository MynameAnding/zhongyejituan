# -*- coding: utf-8 -*-
#project:zhongye
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: urls.py
#time: 2019/5/2 14:38

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^login/$', views.login, name = 'login'),
    url(r'zhongye/$', views.first, name = 'first'),
    url(r'approval_index/$',views.approval_index,name="approval_index"),
    url(r'zhongye/approval_report/$',views.approval_report,name="approval_report"),
    url(r'zhongye/assignment/$',views.assignment,name="assignment"),
    url(r'assignment_index/$',views.assignment_index,name="assignment_index"),
    url(r'consignment/$',views.consignment,name="consignment"),
    url(r'zhongye/experiment/$',views.experiment,name="experiment"),
    url(r'sample_index/$',views.sample_index,name="sample_index"),
    url(r'test_index/$',views.test_index,name="test_index"),
    url(r'zhongye/test/$',views.test,name="test"),
    url(r'^LoadData/$', views.LoadData, name = 'LoadData'),

    url(r'^loadOriginalRecord/$', views.loadOriginalRecord, name='loadOriginalRecord'),
]
