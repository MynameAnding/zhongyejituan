from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
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

def approval_index(request):
    return render(request, 'zhongye/approval_index.html')

def approval_report(request):
    return render(request, 'zhongye/approval_report.html')

def assignment(request):
    return render(request, 'zhongye/assignment.html')

def assignment_index(request):
    return render(request, 'zhongye/assignment_index.html')

def consignment(request):
    return render(request, 'zhongye/consignment.html')

def experiment(request):
    return render(request, 'zhongye/experiment.html')

def sample_index(request):
    return render(request, 'zhongye/sample_index.html')

def test_index(request):
    return render(request, 'zhongye/test_index.html')

def test(request):
    return render(request, 'zhongye/test.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def userEdit(request):
    if request.is_ajax():
        userId = request.POST['id']
        field = request.POST['field']
        value = request.POST['value']
        data = {field:value}
        Allusers.objects.filter(id=userId).update(**data)
        return  JsonResponse({'status':"success"})
    else:
        return HttpResponse({"status":"error"})

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def userData(request):
    allUsers = Allusers.objects.filter().all()
    print(allUsers)
    data = json.loads(serializers.serialize('json', allUsers))
    #print(data)
    result = []
    for item in data:
        prof = item['fields']
        prof['ID'] = item['pk']
        prof['addtime'] = prof['addtime'].replace("T",' ')
        prof['addtime'] = prof['addtime'].replace("Z", ' ')
        result.append(prof)
   # print(result)
    return HttpResponse(json.dumps(result))

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def userCreate(request):
    if request.is_ajax():
        data={}
        data['adduserid'] = request.session.get('LoginSession')['LoginId']
        data['addusername'] = request.session.get('LoginSession')['LoginName']
        Allusers.objects.create(**data)
        return JsonResponse({'status':'success'})
    else:
        return HttpResponse("<script>alert('非法操作！');location.href='/';</script>")

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def userDelete(request):
    if request.is_ajax():
        id = request.POST.get('delProfId')
        #print(id)
        Allusers.objects.filter(id=id).delete()
        return JsonResponse({'status':'success'})
    else:
        return HttpResponse("<script>alert('非法操作！');location.href='/';</script>")



@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def login(request):  # 验证登录信息
    if request.method == 'POST':
        username = request.POST['username']
        userpwd = request.POST['userpwd']
        user = Allusers.objects.filter(username=username).all()
        if user.count() >0:
            user = user.first()
            if user.pwd == userpwd:
                LoginSession = {'LoginName': username, 'LoginId': user.id,'LoginCx':user.cx }
                request.session['LoginSession'] = LoginSession
                request.session.set_expiry(0)
                # return render(request, 'zhongye/professorTable.html')
                return HttpResponseRedirect('/zhongye/')
            else:
                return HttpResponse('<script>alert("登录信息(密码)填写有误，请重新填写！");location.href="/";</script>')
        return HttpResponse('<script>alert("登录信息(用户名)填写有误，请重新填写！");location.href="/";</script>')
    elif request.method == 'GET':
        return render(request, 'zhongye/login1.html')

@CheckSession
def first(request):
    if  request.session.get('LoginSession')['LoginCx'] == 1:
        return render(request, 'zhongye/approval_index.html')
    else:
        return render(request, 'zhongye/login.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def LoadData(request):

    AllProf = Professors.objects.all()
    data = json.loads(serializers.serialize('json', AllProf))
    result = []
    for item in data:
        prof = item['fields']
        prof['id'] = item['pk']
        result.append(prof)
    re = {"data":result,"biaotou":len(result)}
    return HttpResponse(json.dumps(re))


@csrf_exempt#加载钢材拉力试验原始记录数据
def loadOriginalRecord(request):
    data = {}
    data["weituodanbianhao"]="00000"
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





def upImages(request,paraID):
    if request.method == "GET":
        # proName = request.GET['name']
        proId = paraID
        #print(proId)
        return render(request, 'zhongye/upImages.html', {'proId':proId})
    else:
        return HttpResponse(request, "<script>alert('图片上传出现问题！')</script>")



