from django.conf.urls import url
from . import views
from .view import admin

urlpatterns = [
    url(r'admin/sample/$', admin.sample, name="sample"),
]
