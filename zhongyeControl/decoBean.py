# -*- coding: utf-8 -*-
#project:zhongye
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: decoBean.py

from django.http import HttpResponse



#装饰器文件
def CheckSession(func):#验证登录的session信息
    def _CheckSession(request):
        if  request.session.get('LoginSession'):
            return func(request)
        else:
            return HttpResponse('<script>alert("登录信息过期，请再次登录！");location.href="/";</script>')
    return _CheckSession


def CheckAuthShouyang(func):#验证登录的session信息
    def _CheckAuthShouyang(request):
        if  request.session.get('LoginSession')["LoginCx"] == 0 or request.session.get('LoginSession')["LoginCx"] == -1:
            return func(request)
        else:
            return HttpResponse('<script>alert("对不起，你没有权限！");</script>')
    return _CheckAuthShouyang


def CheckAuthFenpei(func):#验证登录的session信息
    def _CheckAuthFenpei(request):
        if  request.session.get('LoginSession')["LoginCx"] == 1 or request.session.get('LoginSession')["LoginCx"] == -1:
            return func(request)
        else:
            return HttpResponse('<script>alert("对不起，你没有权限！");</script>')
    return _CheckAuthFenpei

def CheckAuthShiyan(func):#验证登录的session信息
    def _CheckAuthShiyan(request):
        if  request.session.get('LoginSession')["LoginCx"] == 2 or request.session.get('LoginSession')["LoginCx"] == -1:
            return func(request)
        else:
            return HttpResponse('<script>alert("对不起，你没有权限！");</script>')
    return _CheckAuthShiyan

def CheckAuthShenpi(func):
    def _CheckAuthShouyang(request):
        if  request.session.get('LoginSession')["LoginCx"] == 3 or request.session.get('LoginSession')["LoginCx"] == -1:
            return func(request)
        else:
            return HttpResponse('<script>alert("对不起，你没有权限！");</script>')
    return _CheckAuthShouyang

def CheckAuthAdmin(func):
    def _CheckAuthAdmin(request):
        if request.session.get('LoginSession')["LoginCx"] == -1:
            return func(request)
        else:
            return HttpResponse('<script>alert("对不起，你没有权限！");</script>')
    return _CheckAuthAdmin
