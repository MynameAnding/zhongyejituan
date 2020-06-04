# -*- coding: utf-8 -*-
# project:zhongye
# author: Administrator
# contact: 1506032039@qq.com
# software: PyCharm
# file: urls.py
# time: 2019/5/2 14:38

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/$', views.login, name='login'),
    url(r'zhongye/$', views.first, name='first'),
    url(r'approval_index/$', views.approval_index, name="approval_index"),
    url(r'approval_report/$', views.approval_report, name="approval_report"),
    url(r'zhongye/assignment/$', views.assignment, name="assignment"),
    url(r'assignment_index/$', views.assignment_index, name="assignment_index"),
    url(r'assignment/$', views.assignment, name="assignment"),
    # url(r'toConsignment/$',views.toConsignment,name='toConsignment'),
    url(r'sample_index/consignment/$', views.consignment, name="consignment"),
    url(r'sample_index/report/$', views.report, name="report"),
    url(r'sample_index/sample/$', views.sample, name="sample"),
    url(r'sample_index/updateExperiment/$', views.updateExperiment, name="updateExperiment"),
    url(r'sample_index/loadExperimentData/$', views.loadExperimentData, name="loadExperimentData"),
    url(r'sample_index/sample_experiment/$', views.sample_experiment, name="sample_experiment"),
    url(r'sample_index/updateSample/$', views.updateSample, name="updateSample"),
    url(r'sample_index/loadSampleData/$', views.loadSampleData, name="loadSampleData"),
    url(r'sample_index/updateCommissionSheet/$', views.updateCommissionSheet, name="updateConsignment"),
    url(r'sample_index/updateCommissionSheetReport/$', views.updateCommissionSheetReport, name="updateCommissionSheetReport"),
    url(r'consignmentData/$', views.consignmentData, name="consignmentData"),
    url(r'zhongye/experiment/$', views.experiment, name="experiment"),
    url(r'sample_index/$', views.sample_index, name="sample_index"),
    url(r'sample_index/companyAdmin/$', views.companyAdmin, name="companyAdmin"),
    url(r'sample_index/updateCompany/$', views.updateCompany, name="updateCompany"),
    url(r'sample_index/loadCompany/$', views.loadCompany, name="loadCompany"),
    url(r'samIndexData/$', views.samIndexData, name='LoadData'),
    url(r'test_index/$', views.test_index, name="test_index"),
    url(r'zhongye/test/$', views.test, name="test"),
    url(r'^LoadData/$', views.LoadData, name='LoadData'),
    url(r'^loadOriginalRecord/$', views.loadOriginalRecord, name='loadOriginalRecord'),
]
