from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseRedirect
from ..decoBean import *
from django.core import serializers
from ..models import *
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt  # 增加装饰器，作用是跳过 csrf 中间件的保护
@CheckSession
def sample(request):
        return render(request, 'zhongye/sample.html')

