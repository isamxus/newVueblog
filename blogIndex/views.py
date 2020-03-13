from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.
@csrf_exempt
def index(request):
	print(request.POST.get('info'))
	return HttpResponse("欢迎访问我的博客首页！")
