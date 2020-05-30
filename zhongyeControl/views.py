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
    if request.POST.get("id") != None:
        id = request.POST.get("id")
        commissionSheet = CommissionSheet.objects.get(id=id)
        commissionSheet.report_idPro = commissionSheet.report_id[:2]
        commissionSheet.report_idFoll = commissionSheet.report_id[2:]
        print(commissionSheet)
        # company = CommissionCompany.objects.filter(id=commissionSheet.company_id).first()
        return render(request, 'zhongye/consignment.html', {"data": commissionSheet})
    else:
        return render(request, 'zhongye/consignment.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def report(request):
    # return render(request, 'zhongye/consignment.html')
    # if request.method == "AJAX":
    if request.GET.get("id") != None:
        id = request.GET.get("id")
        commissionSheet = CommissionSheet.objects.get(id=id)
        # commissionSheet.report_idPro = commissionSheet.report_id[:2]
        # commissionSheet.report_idFoll = commissionSheet.report_id[2:]
        # print(commissionSheet)
        # company = CommissionCompany.objects.filter(id=commissionSheet.company_id).first()
        return render(request, 'zhongye/report.html', {"data": commissionSheet})
    else:
        return render(request, 'zhongye/report.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def sample(request):
    if request.GET.get("id") != None:
        id = request.GET.get("id")
        commissionSheet = CommissionSheet.objects.get(id=id)
        return render(request, 'zhongye/sample.html', {"data": commissionSheet})
    else:
        return render(request, 'zhongye/sample.html')

@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def consignmentData(request):
    # return render(request, 'zhongye/consignment.html')
    # if request.method == "AJAX":

    if request.GET.get("id") != None:
        id = request.GET.get("id")
        datas = CommissionSheet.objects.filter(id=id).values("laiyang_id", "id", "number", "test_basis")[0:1]
        rows = []
        for data in datas:
            rows.append(data)
            print(data)
        return HttpResponse(json.dumps({"total": 1, "rows": rows}))


@CheckSession
def experiment(request):
    return render(request, 'zhongye/experiment.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def sample_index(request):
    return render(request, 'zhongye/sample_index.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def companyAdmin(request):
    # company_name = request.GET.get("company_name")
    return render(request, 'zhongye/companyAdmin.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def loadCompany(request):
    datas = []
    if request.method == "GET":
        order = request.GET.get("order", default="asc")
        search = request.GET.get("search", default="")
        # id = "id" if order == "asc" else "-id"
        offset = int(request.GET.get("offset", default=0))
        limit = int(request.GET.get("limit", default=2000))
        datas = CommissionCompany.objects.filter(
            Q(company_name__contains=search) | Q(contactor__contains=search)).order_by("-id").all()[
                offset:offset + limit]
    total = CommissionCompany.objects.count()
    datas = json.loads(serializers.serialize("json", datas))
    # print(datas)
    rows = []
    for data in datas:
        result = {}
        result["id"] = data["pk"]
        result.update(data["fields"])
        rows.append(result)
    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
def updateCompany(request):
    if request.method == "POST":
        data = request.POST.copy().dict()
        # report_id = data.pop("report_id")
        data.pop('csrfmiddlewaretoken') if "csrfmiddlewaretoken" in data.keys() else data
        CommissionCompany.objects.update_or_create(id=request.POST.get("id"), defaults=data)
        # return render(request, 'zhongye/companyAdmin.html',{"reoprt_id":report_id})
        result = {"statue": 200}
        return HttpResponse(json.dumps(result))


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
    if request.method == "GET":
        # order = request.GET.get("order", default="asc")
        offset = int(request.GET.get("offset", default=0))
        limit = int(request.GET.get("limit", default=2000))
        search = request.GET.get("search", default="")
        if search == "":
            datas = CommissionSheet.objects.order_by("-id").values("id", "report_id", "company_id", "date","project_name")[
                    offset:offset + limit]
        else:
            datasCompanyIds = CommissionCompany.objects.filter(Q(company_name__contains=search)).values("id")
            datas = CommissionSheet.objects.filter(
                Q(report_id__contains=search) | Q(project_name__contains=search) | Q(
                    company_id__in=datasCompanyIds)).order_by("-id").values("id", "report_id", "date","company_id",
                                                                            "project_name")[
                    offset:offset + limit]
    rows = []
    for data in datas:
        if data["company_id"] != None:
            company = CommissionCompany.objects.get(id=data["company_id"])
            data["company_name"] = company.company_name
        else:
            data["company_name"] = "请点击选择公司名称"
        # data["date"] = data["date"].strftime("%Y-%m-%d %H:%M:%S")
        if data["date"] != None:
            data["date"] = data["date"].strftime("%Y-%m-%d %H:%M:%S")
        # print(data)
        rows.append(data)
    total = CommissionSheet.objects.count()
    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))


@csrf_exempt
def updateCommissionSheet(request):
    if request.method == "POST":
        if request.POST.get('id') == None:
            data = request.POST.copy().dict()
            data['report_id'] = "建钢检字2020RX第027号"
            data["project_name"] = ""
            object, created = CommissionSheet.objects.update_or_create(id=request.POST.get('id'), defaults=data)
            if created:
                HttpResponse(request, "<script>alert('添加成功！')</script>")
        else:
            data = request.POST.copy().dict()
            id = data.pop('id')
            CommissionSheet.objects.filter(id=id).update(**data)
    return HttpResponseRedirect("/sample_index/")



@csrf_exempt
def updateCommissionSheetReport(request):#修改report的内容
    if request.method == "POST":
        data = request.POST.copy().dict()
        updateData = {}
        id = data["pk"]
        updateData[data["name"]] = data["value"]
        CommissionSheet.objects.filter(id=id).update(**updateData)
        commission = CommissionSheet.objects.filter(id=id).first()
        return render(request, 'zhongye/report.html', {"data": commission})
    else:
        return render(request, 'zhongye/report.html')


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
