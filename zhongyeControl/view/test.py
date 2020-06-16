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

@CheckSession
def experiment(request):
    return render(request, 'zhongye/experiment.html', {"userID": request.GET.get('userID')})

@CheckSession
def experiment_print(request):
    return render(request, 'zhongye/experiment_print.html', {"userID": request.GET.get('userID')})

@CheckSession
def test_index(request):
    return render(request, 'zhongye/test_index.html', {"userID": request.GET.get('userID')})

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
def LoadExpData(request):
    re = []
    if request.method == "GET":
        userID = request.GET.get('userID')
        user = Allusers.objects.values("username").filter(id=userID).all()
        sam_ids = Tension.objects.values("sample_id").filter(get_people=userID, status=1).all()


        with open('D:/Download/Firefox/zhongzhijituan-master_testAndAssign/zhongzhijituan-master/username.txt', "r+") as f:
            f.seek(0)
            f.truncate()  # 清空文件
            f.write(user[0]['username'])

        for sam_id in sam_ids:
            datas = Sample.objects.values("sample_id", "sample_actual_id", "brand_grade", "d").filter(sample_id=sam_id['sample_id']).all()
            temp = datas[0]
            temp['username'] = user[0]['username']
            try:
                Share.objects.create(sample_actual_id=temp['sample_actual_id'], brand_grade=temp['brand_grade'], d=temp['d'], username=temp['username'], state=0)
            except:
                pass
            re.append(temp)


    result = {"rows": re, "total": len(re)}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def getMachine(request):
    data = []

    temp = {"machine_id": 1, "machine_name": "一号机", "ip": '111.14.12.101'}
    data.append(temp)
    #result = {"rows": re, "total": len(re)}
    return HttpResponse(json.dumps(data))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def selectSample(request):
    if request.method == "POST":
        sample_id = request.POST.get('sample_id')
        Tension.objects.filter(sample_id=sample_id).update(status=2)

    return HttpResponse()



@csrf_exempt
def selectExpData(request):
    rows = []
    if request.method == "GET":
        userID = request.GET.get('userID')
        sam_ids = Tension.objects.values("sample_id").filter(get_people=userID, status=2).all()
        for sam_id in sam_ids:
            sample = Sample.objects.values("sample_actual_id", "brand_grade", "d").filter(sample_id=sam_id['sample_id']).all()

            share_datas = Share.objects.values("rm0_rel0", "rel0_rel", "agt", "rel", "rm", "yeild_load", "peak_load",
                                               "origin_gauge", "post_break_gauge", "max_n_origin",
                                               "max_n_after_bre").filter(
                sample_actual_id=sample[0]['sample_actual_id']).all()
            temp = share_datas[0]
            temp['sample_actual_id'] = sample[0]['sample_actual_id']
            temp['brand_grade'] = sample[0]['brand_grade']
            temp['d'] = sample[0]['d']
            temp['sample_id'] = sam_id['sample_id']
            rows.append(temp)


    result = {"rows": rows, "total": len(rows)}
    return HttpResponse(json.dumps(result))


@csrf_exempt
def PrintExpData(request):
    rows = []
    if request.method == "GET":
        userID = request.GET.get('userID')
        datas = Tension.objects.values("sample_id", "rm0_rel0", "rel0_rel", "agt", "rel", "rm", "yeild_load",
                                         "peak_load", "origin_gauge", "post_break_gauge", "max_n_origin", "a",
                                         "max_n_after_bre").filter(get_people=userID, status=3).all()
        for data in datas:
            sample = Sample.objects.values("sample_actual_id", "brand_grade", "d").filter(sample_id=data['sample_id']).all()

            temp = data
            temp['sample_actual_id'] = sample[0]['sample_actual_id']
            temp['brand_grade'] = sample[0]['brand_grade']
            temp['d'] = sample[0]['d']
            rows.append(temp)
            Tension.objects.filter(sample_id=data['sample_id']).update(status=4)

    result = {"rows": rows, "total": len(rows)}
    return HttpResponse(json.dumps(result))


def LoadExpInformation(request):
    rows = []
    if request.method == "GET":
        userID = request.GET.get('userID')
        information = Tension.objects.values("temperature", "date", "start", "end", "machine_name", "machine_id").filter(get_people=userID, status=3).all()
        rows.append(information[0])
    result = {"data": rows, "total": len(rows)}
    return HttpResponse(json.dumps(result, cls=ComplexEncoder))


@csrf_exempt
def saveExpData(request):
    if request.method == "GET":
        userID = request.GET.get('userID')
        start = request.GET.get('start')
        end = request.GET.get('end')
        date = request.GET.get('date')
        temperature = request.GET.get('temperature')
        machine_id = request.GET.get('machine_id')
        machine_name = request.GET.get('machine_name')

        sam_ids = Tension.objects.values("sample_id").filter(get_people=userID, status=2).all()
        for sam_id in sam_ids:
            sample = Sample.objects.values("sample_actual_id").filter(sample_id=sam_id['sample_id']).all()
            share_datas = Share.objects.values("rm0_rel0", "rel0_rel", "agt", "rel", "rm", "yeild_load", "peak_load",
                                               "origin_gauge", "post_break_gauge", "max_n_origin",
                                               "max_n_after_bre").filter(
                sample_actual_id=sample[0]['sample_actual_id']).all()

            temp = share_datas[0]
            Tension.objects.filter(sample_id=sam_id['sample_id']).update(temperature=temperature, date=date, start=start,
                                                                         end=end, machine_id=machine_id, machine_name=machine_name,
                                                                         rm0_rel0=temp['rm0_rel0'], rel0_rel=temp['rel0_rel'],
                                                                         agt=temp['agt'], rel=temp['rel'], rm=temp['rm'],
                                                                         yeild_load=temp['yeild_load'],
                                                                         peak_load=temp['peak_load'],
                                                                         origin_gauge=temp['origin_gauge'],
                                                                         post_break_gauge=temp['post_break_gauge'],
                                                                         max_n_origin=temp['max_n_origin'],
                                                                         max_n_after_bre=temp['max_n_after_bre'],
                                                                         status=3)
            Share.objects.filter(sample_actual_id=sample[0]['sample_actual_id']).delete()

    return render(request, 'zhongye/experiment.html', {"userID": request.GET.get('userID')})


@csrf_exempt
def assignWrong(request):
    if request.method == "POST":
        sample_id = request.POST.get('sample_id')
        userID = request.POST.get('userID')
        Tension.objects.filter(sample_id=sample_id).update(status=0)

    return render(request, 'zhongye/experiment.html', {"userID": request.POST.get('userID')})
