
from django.conf.urls import url
from . import views
from .view import sample

urlpatterns = [
    # url(r'toConsignment/$',views.toConsignment,name='toConsignment'),
    url(r'sample_index/consignment/$', sample.consignment, name="consignment"),
    url(r'sample_index/report/$', sample.report, name="report"),
    url(r'sample_index/sample/$', sample.sample, name="sample"),
    url(r'sample_index/updateSample/$', sample.updateSample, name="updateSample"),
    url(r'sample_index/createSample/$', sample.createSample, name="createSample"),
    url(r'sample_index/loadSampleData/$', sample.loadSampleData, name="loadExperimentData"),
    url(r'sample_index/sample_experiment/$', sample.sample_experiment, name="sample_experiment"),
    url(r'sample_index/updateSample/$', sample.updateSample, name="updateSample"),
    url(r'sample_index/loadSampleData/$', sample.loadSampleData, name="loadSampleData"),
    url(r'sample_index/updateCommissionSheet/$', sample.updateCommissionSheet, name="updateConsignment"),
    url(r'sample_index/loadCommissionSheet/$', sample.loadCommissionSheet, name="loadCommissionSheet"),
    url(r'sample_index/updateCommissionSheetReport/$', sample.updateCommissionSheetReport, name="updateCommissionSheetReport"),
    url(r'consignmentData/$', sample.consignmentData, name="consignmentData"),
    url(r'zhongye/experiment/$', sample.experiment, name="experiment"),
    url(r'sample_index/$', sample.sample_index, name="sample_index"),
    url(r'sample_index/companyAdmin/$', sample.companyAdmin, name="companyAdmin"),
    url(r'sample_index/updateCompany/$', sample.updateCompany, name="updateCompany"),
    url(r'sample_index/loadCompany/$', sample.loadCompany, name="loadCompany"),
    url(r'samIndexData/$', sample.samIndexData, name='LoadData'),
    url(r'test_index/$', views.test_index, name="test_index"),

]
