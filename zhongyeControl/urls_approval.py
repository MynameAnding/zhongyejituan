# -*- coding: utf-8 -*-
# project:zhongye
# author: Administrator
# contact: 1506032039@qq.com
# software: PyCharm
# file: urls.py
# time: 2019/5/2 14:38

from django.conf.urls import url
from . import views
from .view import approval

urlpatterns = [
    # url(r'zhongye/$', views.first, name='first'),
    url(r'approval_index/$', approval.approval_index, name="approval_index"),
    url(r'approval_report/$', approval.approval_report, name="approval_report"),
    url(r'search/$', approval.search, name='search'),
    url(r'search_index/$', approval.search_index, name="search_index"),
    url(r'detailReport/$', approval.detailReport, name='detailReport'),
    url(r'detailReportData/$', approval.detailReportData, name='detailReportData'),
    url(r'report_head/$', approval.report_head, name='report_head'),
    url(r'report_tension/$', approval.report_tension, name='report_tension'),
    url(r'updateReportHead/$', approval.updateReportHead, name='updateReportHead')

]
