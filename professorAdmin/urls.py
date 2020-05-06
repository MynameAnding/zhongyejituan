# -*- coding: utf-8 -*-
#project:professor
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
    url(r'^professors/$', views.professors, name = 'professors'),
    url(r'^LoadData/$', views.LoadData, name = 'LoadData'),
    url(r'^professors/updateProf/$', views.updateProf, name = 'updateProf'),
    #url(r'^update_prof/$', views.update_prof),
    #url(r'^professors/del_prof/$', views.del_prof, name = 'update_prof'),
    url(r'^professors/getPhotos/$', views.getPhotos, name = 'getPhotos'),
    url(r'^professors/getOneProf/$', views.getOneProf, name = 'getOneProf'),
    url(r'^professors/createProf/$', views.createProf, name = 'createProf'),
    url(r'^upImages/(.+)/$', views.upImages, name = 'upImages'),
    # url(r'^profImages/(.+)/$', views.profImages, name = 'profImages'),
    url(r'^checkProf/$', views.checkProf, name = 'profImages'),
    url(r'^checkProf/checkProfYes/$', views.checkProfYes, name = 'profImages'),
    # url(r'^unCheckProf/$', views.unCheckedProf, name = 'profImages'),
    url(r'^userAdmin/$', views.userAdmin, name = 'profImages'),
    url(r'^userAdmin/userData/$', views.userData, name = 'profImages'),
    url(r'^userAdmin/userEdit/$', views.userEdit, name='profImages'),
    url(r'^userAdmin/userCreate/$', views.userCreate, name='profImages'),
    url(r'^userAdmin/userDelete/$', views.userDelete, name='profImages'),
]
