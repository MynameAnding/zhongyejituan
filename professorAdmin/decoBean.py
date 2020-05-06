# -*- coding: utf-8 -*-
#project:professor
#author: Administrator
#contact: 1506032039@qq.com
#software: PyCharm
#file: decoBean.py
#time: 2019/5/2 22:28
from django.http import HttpResponse



#装饰器文件
def CheckSession(func):#验证登录的session信息
    def _CheckSession(request):
        if  request.session.get('LoginSession'):
            return func(request)
        else:
            return HttpResponse('<script>alert("登录信息过期，请再次登录！");location.href="/";</script>')
    return _CheckSession