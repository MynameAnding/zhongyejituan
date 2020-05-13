from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from .decoBean import CheckSession
from django.core import serializers
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from datetime import datetime
import time
import os
import re


# Create your views here.

def index(request):
    return render(request, 'zhongye/Login.html')


@CheckSession
def approval_index(request):
    return render(request, 'zhongye/approval_index.html')


@CheckSession
def approval_report(request):
    return render(request, 'zhongye/approval_report.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def assignment(request):
    return render(request, 'zhongye/assignment.html')


@CheckSession
def assignment_index(request):
    return render(request, 'zhongye/assignment_index.html')





@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def consignment(request):
    # return render(request, 'zhongye/consignment.html')
    # if request.method == "AJAX":
    sample_id = request.POST.get("sample_id")
    return render(request, 'zhongye/consignment.html',{"sample_id":sample_id})


@CheckSession
def experiment(request):
    return render(request, 'zhongye/experiment.html')


@CheckSession
def sample_index(request):
    return render(request, 'zhongye/sample_index.html')


@CheckSession
def test_index(request):
    return render(request, 'zhongye/test_index.html')


@CheckSession
def test(request):
    return render(request, 'zhongye/test.html')


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
                # return render(request, 'zhongye/professorTable.html')
                if user.cx == 0:
                    return HttpResponseRedirect("/sample_index/")
                    # return render(request, 'zhongye/sample_index.html')
                elif user.cx == 1:
                    return HttpResponseRedirect("/assignment_index/")
                elif user.cx == 2:
                    return HttpResponseRedirect("/test_index/")
                else:
                    return HttpResponseRedirect("/approval_index/")
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


@csrf_exempt
def samIndexData(request):
    datas = []
    if request.method == "GET":
        order = request.GET.get("order")
        if not order == 'asc':
            sample_id = '-sample_id'
        else:
            sample_id = "sample_id"
        offset = int(request.GET.get("offset"))
        limit = int(request.GET.get("limit"))
        datas = CommissionSheet.objects.order_by(sample_id).values("sample_id", "company_name", "project_name")[
                offset:offset + limit]
    total = CommissionSheet.objects.count()
    rows = []
    for data in datas:
        rows.append(data)

    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def LoadData(request):
    AllProf = Professors.objects.all()
    data = json.loads(serializers.serialize('json', AllProf))
    result = []
    for item in data:
        prof = item['fields']
        prof['id'] = item['pk']
        result.append(prof)
    re = {"data": result, "biaotou": len(result)}
    return HttpResponse(json.dumps(re))


@csrf_exempt  # 加载钢材拉力试验原始记录数据
def loadOriginalRecord(request):
    data = {}
    data["weituodanbianhao"] = "00000"
    data["shiyanrenyuan"] = "00000"
    data["shiyankaishi"] = "00000"
    data["shiyanjieshu"] = "00000"
    data["shiyangkaishi"] = "00000"
    data["shebeimingcheng"] = "00000"
    data["liangjumingcheng"] = "00000"
    data["jianyanyiju"] = "00000"
    data["shebeibianhao"] = "00000"
    data["liangjubianhao"] = "00000"
    result = {}
    result["statues"] = 0
    result["data"] = data
    return HttpResponse(json.dumps(result))


def upImages(request, paraID):
    if request.method == "GET":
        # proName = request.GET['name']
        proId = paraID
        # print(proId)
        return render(request, 'zhongye/upImages.html', {'proId': proId})
    else:
        return HttpResponse(request, "<script>alert('图片上传出现问题！')</script>")
