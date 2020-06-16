from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .decoBean import CheckSession
from django.core import serializers
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

def index(request):
    return render(request, 'zhongye/Login.html')





@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def assignment(request):
    return render(request, 'zhongye/assignment.html')


@CheckSession
def assignment_index(request):
    return render(request, 'zhongye/assignment_index.html')

@CheckSession
def test_index(request):
    return render(request, 'zhongye/test_index.html')

@CheckSession
def test(request):
    return render(request, 'zhongye/test.html')


@CheckSession
def admin(request):
    return render(request, 'zhongye/index.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def login(request):  # 验证登录信息
    if request.method == 'POST':
        username = request.POST['username']
        userpwd = request.POST['userpwd']
        user = Allusers.objects.filter(username=username).all()
        if user.count() > 0:
            user = user.first()
            if user.pwd == userpwd:
                LoginSession = {'LoginName': username, 'LoginId': user.id, 'LoginCx': user.cx}
                request.session['LoginSession'] = LoginSession
                request.session.set_expiry(0)
                return HttpResponseRedirect("/admin/")

            else:
                return HttpResponse('<script>alert("登录信息(密码)填写有误，请重新填写！");location.href="/";</script>')
        return HttpResponse('<script>alert("登录信息(用户名)填写有误，请重新填写！");location.href="/";</script>')
    elif request.method == 'GET':
        return render(request, 'zhongye/login1.html')


@CheckSession
def first(request):
    if request.session.get('LoginSession')['LoginCx'] == 1:
        return render(request, 'zhongye/approval_index.html')
    else:
        return render(request, 'zhongye/login.html')



