from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import HttpResponseRedirect
from .decoBean import CheckSession
from django.core import serializers
from .models import Allusers,Professors
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from datetime import datetime
import time
import os
import re

# Create your views here.

def index(request):
    return render(request, 'professor/Login.html')


# @csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
# def unCheckedProf(request):
#     if request.is_ajax():
#         AllProf = Professors.objects.filter(ischeck=0).all()
#     else:
#         AllProf = Professors.objects.filter(ischeck=0).all()
#     data = json.loads(serializers.serialize('json', AllProf))
#     result = []
#     for item in data:
#         prof = item['fields']
#         #print(type(prof['labels']))
#         if not prof['labels'] == None:
#             pattern = "[\u4e00-\u9fa5]+"
#             regex = re.compile(pattern)
#             labelsList = regex.findall(prof['labels'])
#             prof['labels'] = labelsList
#         prof['ID'] = item['pk']
#         profImgs = list(Photos.objects.filter(professorid=prof['ID']).values('photourl'))
#         ProImagesUrl = []
#         for index in range(0,min(len(profImgs),5)):
#             ImageUrl = profImgs[index]['photourl']
#             ProImagesUrl.append(ImageUrl)
#         prof['photos'] = ProImagesUrl
#         result.append(prof)
#     return HttpResponse(json.dumps(result))

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def checkProfYes(request):
    if request.is_ajax():
        profId = request.POST['profId']
        Professors.objects.filter(id= profId).update(**{"ischeck":1})
        return render(request, 'professor/checkProf.html', {"profId":profId})
    else:
        return HttpResponse('<script>alert("审核出现错误！");location.href="/";</script>')

def userAdmin(request):
    return render(request, 'professor/userAdmin.html')

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

def checkProf(request):
    return render(request, 'professor/checkProf.html')

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
                # return render(request, 'professor/professorTable.html')
                return HttpResponseRedirect('/professors/')
            else:
                return HttpResponse('<script>alert("登录信息(密码)填写有误，请重新填写！");location.href="/";</script>')
        return HttpResponse('<script>alert("登录信息(用户名)填写有误，请重新填写！");location.href="/";</script>')
    elif request.method == 'GET':
        return render(request, 'professor/login.html')

@CheckSession
def professors(request):
    if  request.session.get('LoginSession')['LoginCx'] == 1:
        return render(request, 'professor/professorTable.html')
    else:
        return render(request, 'professor/professorTableUser.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def LoadData(request):

    AllProf = Professors.objects.all()
    data = json.loads(serializers.serialize('json', AllProf))
    result = []
    for item in data:
        prof = item['fields']
        #print(type(prof['labels']))
        # if not prof['labels'] == None:
        #     pattern = "[\u4e00-\u9fa5]+"
        #     regex = re.compile(pattern)
        #     labelsList = regex.findall(prof['labels'])
        #     prof['labels'] = labelsList
        prof['id'] = item['pk']
        result.append(prof)
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def createProf(request):
    data = {}
    data['name'] = request.POST['name']
    data['danwei'] = request.POST['danwei']
    data['zhengzhimianmao'] = request.POST['zhengzhimianmao']
    data['zhiwu'] = request.POST['zhiwu']
    data['zhicheng'] = request.POST['zhicheng']
    data['shenfenzhenghao'] = request.POST['shenfenzhenghao']
    data['lianxidianhua'] = request.POST['lianxidianhua']
    data['kechengmingcheng'] = request.POST['kechengmingcheng']
    data['kaihuhang'] = request.POST['kaihuhang']
    data['kahao'] = request.POST['kahao']
    data['shehuijianzhi'] = request.POST['shehuijianzhi']
    data['jianjie'] = request.POST['jianjie']
    data['hezuoqingkuang'] = request.POST['hezuoqingkuang']
    data['zhengzhibiaoxian'] = request.POST['zhengzhibiaoxian']
    data['shoukejilu'] = request.POST['shoukejilu']
    data['ischeck'] = 0
    if request.session.get('LoginSession') is None:
        return HttpResponse('<script>alert("登录信息过期，请重新登录！");location.href="/";</script>')
    data['adduserid'] = request.session.get('LoginSession')['LoginId']
    labels = request.POST['labels']
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    results = regex.findall(labels)
    #print(results)
    labelsStr = ''
    for label in results:
        labelsStr = label+','
    data['labels'] = labelsStr
    Professors.objects.create(**data)
    return HttpResponseRedirect('/professors/')


def upImages(request,paraID):
    if request.method == "GET":
        # proName = request.GET['name']
        proId = paraID
        #print(proId)
        return render(request, 'professor/upImages.html', {'proId':proId})
    else:
        return HttpResponse(request, "<script>alert('图片上传出现问题！')</script>")


# @csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
# def profImages(request,paraId):
#     imgData = {}
#     imgFiles = request.FILES.get("profPhoto")
#    # print(imgFiles)
#     profid = paraId
#     #print(profid)
#     imgData['professorid'] = profid
#     photoForm = imgFiles.name.split('.')[1]
#     # print(photoForm)
#     cur_dir = 'static\\media'
#     curForderName = os.path.join(cur_dir, profid)
#     if not os.path.exists(curForderName):
#         os.makedirs(curForderName)
#     path = os.path.join(curForderName, datetime.now().strftime('%Y%m%d%H%M%S%f') + '.' + photoForm)
#     # print(path)
#     f = open(path, 'wb')
#     for chunk in imgFiles.chunks(chunk_size=1024):
#         f.write(chunk)
#     f.close()
#     imgData['photourl'] = path
#     imgData['addtime'] = datetime.now()
#     Photos.objects.create(**imgData)
#
#     return HttpResponse(json.dumps({'status': True}))
    #
    #     return HttpResponse(json.dumps({'status': True}))
    # else:
    #     return HttpResponse(json.dumps({'status': False}))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def updateProf(request):
    data = {}
    id = request.POST['id']
    data['name'] = request.POST['name']
    data['danwei'] = request.POST['danwei']
    data['zhengzhimianmao'] = request.POST['zhengzhimianmao']
    data['zhiwu'] = request.POST['zhiwu']
    data['zhicheng'] = request.POST['zhicheng']
    data['shenfenzhenghao'] = request.POST['shenfenzhenghao']
    data['lianxidianhua'] = request.POST['lianxidianhua']
    data['kechengmingcheng'] = request.POST['kechengmingcheng']
    data['kaihuhang'] = request.POST['kaihuhang']
    data['kahao'] = request.POST['kahao']
    data['shehuijianzhi'] = request.POST['shehuijianzhi']
    data['jianjie'] = request.POST['jianjie']
    data['hezuoqingkuang'] = request.POST['hezuoqingkuang']
    data['zhengzhibiaoxian'] = request.POST['zhengzhibiaoxian']
    data['shoukejilu'] = request.POST['shoukejilu']
    labels = request.POST['labels']
    pattern = "[\u4e00-\u9fa5]+"
    regex = re.compile(pattern)
    results = regex.findall(labels)
    #print(results)
    labelsStr = ''
    for label in results:
        labelsStr += label+','
   # print(results,labelsStr)
    data['labels'] = labelsStr
    Professors.objects.filter(field_id=id).update(**data)
    return HttpResponseRedirect('/professors')


# @CheckSession
# def del_prof(request):
#     if request.method == 'GET':
#         id = request.GET['id']
#         Professors.objects.filter(field_id= id).delete()
#     return HttpResponseRedirect('/professors')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def getOneProf(request):
    if request.method == 'POST':
        Id = request.POST['id']
        professor = Professors.objects.filter(field_id=Id).values()
        professor = professor.first()
        return HttpResponse(json.dumps(professor))
    else:
        return HttpResponse('<script>alert("访问出错，请重新登录！");location.href="/";</script>')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def getPhotos(request):
    return HttpResponseRedirect('/professors')
