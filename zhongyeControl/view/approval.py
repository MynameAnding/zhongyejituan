from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from ..decoBean import *
from django.core import serializers
from ..models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.forms.models import model_to_dict
from datetime import datetime
import time
import os
import re



@CheckSession
@CheckAuthShenpi
def approval_index(request):
    return render(request, 'zhongye/approval_index.html')

@CheckSession
@CheckAuthShenpi
def approval_report(request):
    return render(request, 'zhongye/approval_report.html')
# Create your views here.
global global_report_id

@CheckSession
@CheckAuthShenpi
def search_index(request):
    return render(request, 'zhongye/approval_search.html')


@CheckSession
@CheckAuthShenpi
def search(request):

    search_report = request.GET.get("search", default="")
    # print("search_report:", search_report)
    # companies = CommissionCompany.objects.values("company_name", "id")[0]
    # print(companies)
    datas = Sample.objects.values("sheet_id", "product_number", "laiyang_id").distinct()
    rows = []
    for data1 in datas:
        temp1data = CommissionSheet.objects.values("report_id", "project_name", "company_id", "id").filter(
            Q(report_id__contains=search_report), id=data1['sheet_id']
        )
        for data2 in temp1data:
            conData = CommissionCompany.objects.values("company_name").filter(company_id=data2['company_id']).all()
            temp = conData[0]
            temp['report_id'] = data2['report_id']
            temp['project_name'] = data2['project_name']
            temp['id'] = data2['id']
            temp['product_number'] = data1['product_number']
            temp['laiyang_id'] = data1['laiyang_id']
            rows.append(temp)
    total = CommissionSheet.objects.count()
    # datas = json.loads(serializers.serialize("json", datas))

    result = {"total": total, "rows": rows}
    # print(result)
    return HttpResponse(json.dumps(result))
@CheckAuthShenpi
@CheckSession
def detailReportData(request):
    # 加载数据
    id = request.GET.get('report_id')
    product_number = request.GET.get('product_number')
    targetSamples = Sample.objects.values(
        "sample_actual_id", "lashen", "wanqu", "fanwan", "huaxue", "jinxiang", "biaomianbiaozhi", "biaomianzhiliang",
        "ceq"
    ).filter(sheet_id=id, product_number=product_number).all()
    # print(targetSamples)
    rows = []
    total = Sample.objects.count()
    for data in targetSamples:
        rows.append(data)
    result = {"total": total, "rows": rows}
    return HttpResponse(json.dumps(result))
@CheckAuthShenpi
@csrf_exempt
@CheckSession
def detailReport(request):

    return render(request, 'zhongye/detailReport.html')

@CheckAuthShenpi
@csrf_exempt
@CheckSession
def report_head(request):
    result = {}
    id = request.GET.get("report_id")
    # print(id)
    product_number = request.GET.get("product_number")
    datas = Sample.objects.values("brand_grade", "d", "sample_number").filter(
            sheet_id=id, product_number=product_number).first()
    result["product_number"] = product_number
    result["brand_grade"] = datas["brand_grade"]
    result["d"] = datas["d"]
    result["sample_number"] = datas["sample_number"]

    datas_sheet = CommissionSheet.objects.values("report_id", "company_id", "date", "project_name", "sample_name",
                                                 "test_basis", "number", "jiaohuo", "sample_state", "conclusion").filter(id=id).first()
    result["report_id"] = datas_sheet["report_id"]
    result["date"] = datas_sheet["date"]
    result["project_name"] = datas_sheet["project_name"]
    result["sample_name"] = datas_sheet["sample_name"]
    result["test_basis"] = datas_sheet["test_basis"]
    result["number"] = datas_sheet["number"]
    result["jiaohuo"] = datas_sheet["jiaohuo"]
    result["sample_state"] = datas_sheet["sample_state"]
    result["conclusion"] = datas_sheet["conclusion"]

    compamy_id = CommissionSheet.objects.values("company_id").filter(id=id).first()["company_id"]
    datas_company = CommissionCompany.objects.values("company_name", "contactor").filter(company_id=compamy_id).first()
    result["company_name"] = datas_company["company_name"]
    result["contactor"] = datas_company["contactor"]

    datas_sample_first = Sample.objects.values("sample_actual_id").filter(sheet_id=id, product_number=product_number).first()
    datas_sample_last = Sample.objects.values("sample_actual_id").filter(sheet_id=id, product_number=product_number).last()
    # datas_sample_number = Sample.objects.values("sample_actual_id").filter(sheet_id=id, product_number=product_number).count()
    # print(datas_sample_number)
    result["sample_id_first"] = datas_sample_first["sample_actual_id"]
    result["sample_id_last"] = datas_sample_last["sample_actual_id"]

    lashen = 0
    wanqu = 0
    fanwan = 0
    jinxiang = 0
    huaxue = 0
    biaomianzhiliang = 0
    biaomianbiaozhi = 0
    chicun = 0
    zhongliangpiancha = 0
    ceq =0
    samples = Sample.objects.values("sample_id").filter(sheet_id=id, product_number=product_number).all()
    # print(samples)
    for i in samples:
        temp = Sample.objects.values("lashen", "wanqu", "fanwan", "jinxiang", "huaxue", "biaomianzhiliang", "biaomianbiaozhi", "chicun", "zhonglaingpiancha", "ceq").filter(sample_id=i["sample_id"]).first()
        if lashen == 0:
            if temp["lashen"] == 1:
                lashen = 1
        if wanqu == 0:
            if temp["wanqu"] == 1:
                wanqu = 1
        if fanwan == 0:
            if temp["fanwan"] == 1:
                fanwan = 1
        if jinxiang == 0:
            if temp["jinxiang"] == 1:
                jinxiang = 1
        if huaxue == 0:
            if temp["huaxue"] == 1:
                huaxue = 1
        if biaomianzhiliang == 0:
            if temp["biaomianzhiliang"] == 1:
                biaomianzhiliang = 1
        if biaomianbiaozhi == 0:
            if temp["biaomianbiaozhi"] == 1:
                biaomianbiaozhi = 1
        if chicun == 0:
            if temp["chicun"] == 1:
                chicun = 1
        if ceq == 0:
            if temp["ceq"] == 1:
                ceq = 1
        if zhongliangpiancha == 0:
            if temp["zhonglaingpiancha"] == 1:
                zhongliangpiancha = 1
    if lashen == 1:
        result["lashen"] = "√"
    else:
        result["lashen"] = "/"

    if wanqu == 1:
        result["wanqu"] = "√"
    else:
        result["wanqu"] = "/"
    if fanwan == 1:
        result["fanwan"] = "√"
    else:
        result["fanwan"] = "/"
    if huaxue == 1:
        result["huaxue"] = "√️"
    else:
        result["huaxue"] = "/"
    if biaomianbiaozhi == 1:
        result["biaomianbiaozhi"] = "√️"
    else:
        result["biaomianbiaozhi"] = "/"
    if biaomianzhiliang == 1:
        result["biaomianzhiliang"] = "√️"
    else:
        result["biaomianzhiliang"] = "/"
    if zhongliangpiancha == 1:
        result["zhongliangpiancha"] = "√️"
    else:
        result["zhongliangpiancha"] = "/"
    if chicun == 1:
        result["chicun"] = "√️"
    else:
        result["chicun"] = "/"
    if ceq == 1:
        result["ceq"] = "√️"
    else:
        result["ceq"] = "/"
    if jinxiang == 1:
        result["jinxiang"] = "√️"
    else:
        result["jinxiang"] = "/"

    return render(request, 'zhongye/report_head.html', {"data": result})

@CheckAuthShenpi
@CheckSession
def report_tension(request):
    result = {}
    id = request.GET.get('report_id')
    product_number = request.GET.get('product_number')
    brand_grade = Sample.objects.values("brand_grade").filter(sheet_id=id, product_number=product_number).first()["brand_grade"]
    d = Sample.objects.values("d").filter(sheet_id=id, product_number=product_number).first()["d"]
    report_id = CommissionSheet.objects.values("report_id").filter(id=id).first()["report_id"]

    datas_stardard = Standard.objects.values("rel", "rm", "agt", "rm0_rel0", "rel0_rel", "a", "waquyatou", "fanxiangwanqu").filter(
        brand_grade=brand_grade, d=d).first()

    result["report_id"] = report_id
    result["product_number"] = product_number
    result["brand_grade"] = brand_grade
    result["d"] = d
    result["rel"] = datas_stardard["rel"]
    result["rm"] = datas_stardard["rm"]
    result["a"] = datas_stardard["a"]
    result["rm0rel0"] = datas_stardard["rm0_rel0"]
    result["rel0rel"] = datas_stardard["rel0_rel"]
    result["agt"] = datas_stardard["agt"]
    result["wanquyatou"] = datas_stardard["waquyatou"]
    result["fanxiangwanqu"] = datas_stardard["fanxiangwanqu"]

    datas_sample = Sample.objects.values("sample_actual_id", "sample_id").filter(sheet_id=id, product_number=product_number, lashen=1).all()
    sample_actual_id_1 = datas_sample[0]["sample_actual_id"]
    sample_actual_id_2 = datas_sample[1]["sample_actual_id"]
    result["sample_actual_id_1"] = sample_actual_id_1
    result["sample_actual_id_2"] = sample_actual_id_2

    datas_sampe_wanqu = Sample.objects.values("sample_actual_id").filter(sheet_id=id, product_number=product_number, fanwan=1).all()
    result["sample_actual_id_3"] = datas_sampe_wanqu[0]["sample_actual_id"]

    sample_id_1 = datas_sample[0]["sample_id"]
    sample_id_2 = datas_sample[1]["sample_id"]
    datas_tension1 = Tension.objects.values("rel", "rm", "agt", "rm0_rel0", "rel0_rel", "a").filter(
        sample_id=sample_id_1).first()

    datas_tension2 = Tension.objects.values("rel", "rm", "agt", "rm0_rel0", "rel0_rel", "a").filter(
        sample_id=sample_id_2).first()

    result["rel_1"] = datas_tension1["rel"]
    result["rm_1"] = datas_tension1["rm"]
    result["a_1"] = datas_tension1["a"]
    result["rm0rel0_1"] = datas_tension1["rm0_rel0"]
    result["rel0rel_1"] = datas_tension1["rel0_rel"]
    result["agt_1"] = datas_tension1["agt"]

    result["rel_2"] = datas_tension2["rel"]
    result["rm_2"] = datas_tension2["rm"]
    result["a_2"] = datas_tension2["a"]
    result["rm0rel0_2"] = datas_tension2["rm0_rel0"]
    result["rel0rel_2"] = datas_tension2["rel0_rel"]
    result["agt_2"] = datas_tension2["agt"]

    return render(request, "zhongye/report_tension.html", {"data": result})


@csrf_exempt
@CheckSession
@CheckAuthShenpi
def updateReportHead(request):  # 修改report的内容
    if request.method == "POST":
        data = request.POST.copy().dict()
        updateData = {}
        report_id = data["pk"]
        print(report_id)
        id = CommissionSheet.objects.values("id").filter(report_id=report_id).first()
        updateData[data["name"]] = data["value"]
        CommissionSheet.objects.filter(id=id["id"]).update(**updateData)
        commission = CommissionSheet.objects.filter(id=id["id"]).first()
        return render(request, 'zhongye/report_head.html', {"data": commission})
    else:
        return render(request, 'zhongye/report_head.html')

