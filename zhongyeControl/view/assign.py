from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from ..decoBean import CheckSession
from django.core import serializers
from ..models import *
from ..dateTime import ComplexEncoder
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from datetime import datetime
import time
import os
import re
from django.utils.http import urlquote

# Create your views here.
@CheckSession
def assignment_index(request):
    return render(request, 'zhongye/assignment_index.html')

@CheckSession
def assign_index(request):
    return render(request, 'zhongye/assign_index.html')


# @csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
# def login(request):  # 验证登录信息
#     if request.method == 'POST':
#         username = request.POST['username']
#         userpwd = request.POST['userpwd']
#         user = Allusers.objects.filter(username=username).all()
#         if user.count() > 0:
#             user = user.first()
#             if user.pwd == userpwd:
#                 LoginSession = {'LoginName': username, 'LoginId': user.id, 'LoginCx': user.cx}
#                 request.session['LoginSession'] = LoginSession
#                 request.session.set_expiry(0)
#                 # return render(request, 'zhongye/professorTable.html')
#                 if user.cx == 0:
#                     return HttpResponseRedirect("/sample_index/")
#                     # return render(request, 'zhongye/sample_index.html')
#                 elif user.cx == 1:
#                     return HttpResponseRedirect("/assign_index/")
#                 elif user.cx == 2:
#                     return HttpResponseRedirect("/test_index/?userID=" + str(user.id))
#                 else:
#                     return HttpResponseRedirect("/approval_index/")
#             else:
#                 return HttpResponse('<script>alert("登录信息(密码)填写有误，请重新填写！");location.href="/";</script>')
#         return HttpResponse('<script>alert("登录信息(用户名)填写有误，请重新填写！");location.href="/";</script>')
#     elif request.method == 'GET':
#         return render(request, 'zhongye/login1.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def LoadAssignData(request):
    re = []
    datas = Tension.objects.values("sample_id").filter(status=0).all()

    for data in datas:
        sam_datas = Sample.objects.values("sample_actual_id", "brand_grade", "d", "sheet_id").filter(sample_id=data['sample_id']).all()
        conData = CommissionSheet.objects.values("sample_name", "test_basis", "period").filter(id=sam_datas[0]['sheet_id']).all()
        temp = conData[0]
        temp['sample_actual_id'] = sam_datas[0]['sample_actual_id']
        temp['sample_id'] = data['sample_id']
        temp['d'] = sam_datas[0]['d']
        temp['brand_grade'] = sam_datas[0]['brand_grade']
        re.append(temp)
    result = {"rows": re, "total": len(re)}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def getPeopleNames(request):
    data = []
    datas = Allusers.objects.values("username", "id").filter(cx=2).all()

    for temp in datas:
        data.append(temp)
    #result = {"rows": re, "total": len(re)}
    return HttpResponse(json.dumps(data))


@csrf_exempt
def updateGetPeople(request):
    if request.method == "POST":
        sample_id = request.POST.get('sample_id')
        get_people = request.POST.get('get_people')
        Tension.objects.filter(sample_id=sample_id).update(get_people=get_people, status=1)

    return HttpResponseRedirect("/assignment_index/")
