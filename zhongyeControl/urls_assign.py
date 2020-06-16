from django.conf.urls import url
from .view import assign

urlpatterns = [
    url(r'assign_index/$', assign.assign_index, name="assign_index"),
    # url(r'assign_index1/$', assign.assign_index1, name="assign_index1"),
    url(r'assignment_index/$', assign.assignment_index, name="assignment_index"),
    # url(r'assignment_index1/$', assign.assignment_index1, name="assignment_index1"),
    url(r'experiment/$', assign.experiment, name="experiment"),
    # url(r'experiment1/$', assign.experiment1, name="experiment1"),
    url(r'test_index/$', assign.test_index, name="test_index"),
    # url(r'test_index1/$', assign.test_index1, name="test_index1"),
    url(r'^LoadExpData/$', assign.LoadExpData, name='LoadData'),
    url(r'^LoadAssignData/$', assign.LoadAssignData, name='LoadData'),
    url(r'^getPeopleNames/$', assign.getPeopleNames, name='LoadData'),
    url(r'^updateGetPeople/$', assign.updateGetPeople, name='LoadData'),
    url(r'^saveExpData/$', assign.saveExpData, name='LoadData'),
    url(r'^selectExpData/$', assign.selectExpData, name='LoadData'),
    url(r'^assignWrong/$', assign.assignWrong, name='LoadData'),
    url(r'^getMachine/$', assign.getMachine, name='LoadData'),
    url(r'^selectSample/$', assign.selectSample, name='LoadData'),
    url(r'^PrintExpData/$', assign.PrintExpData, name='LoadData'),
    url(r'^LoadExpInformation/$', assign.LoadExpInformation, name='LoadData'),
    url(r'^experiment_print/$', assign.experiment_print, name='experiment_print'),
]
