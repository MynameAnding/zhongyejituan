from django.db.models import Q, Min
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from ..decoBean import CheckSession, CheckAuthShouyang
from django.core import serializers
from ..models import *
from django.views.decorators.csrf import csrf_exempt
import json
from ..aggregate import *
from copy import deepcopy
import time


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
@CheckAuthShouyang
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
@CheckAuthShouyang
def report(request):
    # return render(request, 'zhongye/consignment.html')
    # if request.method == "AJAX":
    if request.GET.get("id") != None:
        id = request.GET.get("id")
        commissionSheet = CommissionSheet.objects.get(id=id)

        return render(request, 'zhongye/report.html', {"data": commissionSheet})
    else:
        return render(request, 'zhongye/report.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
@CheckAuthShouyang
def sample(request):
    return render(request, 'zhongye/sampleNew.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
@CheckAuthShouyang
def loadSampleData(request):
    para = request.GET.copy().dict()
    sheet_id = para["sheet_id"]
    if 'laiyang_id' in para.keys():
        laiyang_id = para["laiyang_id"]
        sql = "select sample_id,sample_actual_id,sheet_id,sample_number,d,brand_grade,product_number from sample where sheet_id ="+sheet_id+" and  laiyang_id = "+laiyang_id+" order by sample_id"
    else:
        sql = "select sample_id,sample_actual_id,sheet_id,sample_number,d,brand_grade,product_number from sample where sheet_id ="+sheet_id+" group by laiyang_id order by sample_id"
    datas = Sample.objects.raw(sql)
    datas = json.loads(serializers.serialize("json", datas))

    rows = []
    for data in datas:
        result = {}
        # print(data)
        result["sample_id"] = data["pk"]
        result.update(data["fields"])
        rows.append(result)
    return HttpResponse(json.dumps(rows))



@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
@CheckAuthShouyang
def consignmentData(request):
    # return render(request, 'zhongye/consignment.html')
    # if request.method == "AJAX":

    if request.GET.get("id") != None:
        id = request.GET.get("id")
        datas = CommissionSheet.objects.filter(id=id).values("laiyang_id", "id", "number", "test_basis")[0:1]
        rows = []
        for data in datas:
            rows.append(data)
        return HttpResponse(json.dumps({"total": 1, "rows": rows}))


@CheckSession
@CheckAuthShouyang
def experiment(request):
    return render(request, 'zhongye/experiment.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def sample_index(request):
    return render(request, 'zhongye/sample_index.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def sample_experiment(request):
    return render(request, 'zhongye/sample_experiment.html')


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def updateSample(request):
    data = request.POST.copy().dict()
    data.pop('csrfmiddlewaretoken') if "csrfmiddlewaretoken" in data.keys() else data
    Sample.objects.update_or_create(sample_id=request.POST.get("sample_id"), defaults=data)
    result = {"statue": 200}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def createSample(request):
    # if request.method == "POST":
    data = request.POST.copy().dict()
    # report_id = data.pop("report_id")
    data.pop('csrfmiddlewaretoken') if "csrfmiddlewaretoken" in data.keys() else data
    if "sample_id" in data.keys():
        sample = Sample.objects.get(sample_id = data['sample_id'])
        if sample.sample_actual_id == None:
            sample.sample_actual_id = sample.laiyang_id + '-1'
            sample.save()
            for index in range(1,sample.sample_number):
                data = deepcopy(sample)
                data.sample_id = None
                data.sample_actual_id = data.laiyang_id + '-' + str(index+1)
                data.save()
    else:
        Sample(sheet_id=data['sheet_id']).save()
    result = {"statue": 200}
    return HttpResponse(json.dumps(result))


# @CheckSession
# def loadSampleData(request):
#     order = request.GET.get("order", default="asc")
#     search = request.GET.get("search", default="")
#     sheet_id = request.GET.get("sheet_id")
#     print(sheet_id)
#     offset = int(request.GET.get("offset", default=0))
#     limit = int(request.GET.get("limit", default=2000))
#     datas = Sample.objects.filter(sheet_id=sheet_id).order_by("sample_id").all()[offset:offset + limit]
#     total = Sample.objects.filter(sheet_id=sheet_id).count()
#     datas = json.loads(serializers.serialize("json", datas))
#     rows = []
#     for data in datas:
#         result = {}
#         result["id"] = data["pk"]
#         result.update(data["fields"])
#         rows.append(result)
#     result = {"total": total, "rows": rows}
#     return HttpResponse(json.dumps(result))


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def companyAdmin(request):
    # company_name = request.GET.get("company_name")
    return render(request, 'zhongye/companyAdmin.html')


@CheckSession
@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def loadCompany(request):
    datas = []
    if request.method == "GET":
        order = request.GET.get("order", default="asc")
        search = request.GET.get("search", default="")
        # id = "id" if order == "asc" else "-id"
        offset = int(request.GET.get("offset", default=0))
        limit = int(request.GET.get("limit", default=2000))
        datas = CommissionCompany.objects.filter(
            Q(company_name__contains=search) | Q(contactor__contains=search)).order_by("-company_id").all()[
                offset:offset + limit]
    total = CommissionCompany.objects.count()
    datas = json.loads(serializers.serialize("json", datas))
    # print(datas)
    rows = []
    for data in datas:
        result = {}
        result["company_id"] = data["pk"]
        result.update(data["fields"])
        rows.append(result)
    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckAuthShouyang
def updateCompany(request):
    if request.method == "POST":
        data = request.POST.copy().dict()
        # report_id = data.pop("report_id")
        data.pop('csrfmiddlewaretoken') if "csrfmiddlewaretoken" in data.keys() else data
        CommissionCompany.objects.update_or_create(id=request.POST.get("id"), defaults=data)
        # return render(request, 'zhongye/companyAdmin.html',{"reoprt_id":report_id})
        result = {"statue": 200}
        return HttpResponse(json.dumps(result))


@csrf_exempt
@CheckAuthShouyang
def samIndexData(request):
    if request.method == "GET":
        order = request.GET.get("order", default="asc")
        offset = int(request.GET.get("offset", default=0))
        limit = int(request.GET.get("limit", default=2000))
        search = request.GET.get("search", default="")
        if search == "":
            datas = CommissionSheet.objects.order_by("id").values("id", "report_id", "company_id", "date",
                                                                  "project_name")[offset:offset + limit]
        else:
            datasCompanyIds = CommissionCompany.objects.filter(Q(company_name__contains=search)).values("id")
            datas = CommissionSheet.objects.filter(
                Q(report_id__contains=search) | Q(project_name__contains=search) | Q(
                    company_id__in=datasCompanyIds)).order_by("-id").values("id", "report_id", "date", "company_id",
                                                                            "project_name")[
                    offset:offset + limit]
    rows = []
    for data in datas:
        if data["company_id"] != None:
            company = CommissionCompany.objects.get(company_id=data["company_id"])
            data["company_name"] = company.company_name
        else:
            data["company_name"] = "请点击选择公司名称"
        # data["date"] = data["date"].strftime("%Y-%m-%d %H:%M:%S")
        # if data["date"] != None:
        #     data["date"] = data["date"].strftime("%Y-%m-%d %H:%M:%S")
        # print(data)
        rows.append(data)
    total = CommissionSheet.objects.count()
    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))


@csrf_exempt
@CheckAuthShouyang
def updateCommissionSheet(request):
    if request.method == "POST":
        if request.POST.get('id') == None:
            data = request.POST.copy().dict()
            # data['report_id'] = "建钢检字2020RX第027号"
            # data["project_name"] = ""
            com = CommissionSheet()
            # CommissionSheet.objects.create(**{})
            com.save()
            com.report_id = "建钢检字"+time.strftime("%Y", time.localtime())+"RX第0"+str(com.id)+'号'
            com.save()
            HttpResponse(request, "<script>alert('添加成功！')</script>")
        else:
            data = request.POST.copy().dict()
            id = data.pop('id')
            CommissionSheet.objects.filter(id=id).update(**data)
    return HttpResponseRedirect("/sample_index/")


@csrf_exempt
@CheckAuthShouyang
def updateCommissionSheetReport(request):  # 修改report的内容
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
