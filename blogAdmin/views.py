from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ParamsSettings,ParamsContent
import json
import simplejson
from django.core import serializers
# Create your views here.
def RequestHandler(request):
	return json.loads(json.dumps(request.POST))

#添加参数
@csrf_exempt
def createParamsHandler(request):
	try:
		requestData = json.loads(RequestHandler(request)['PostContent'])
		newParam = ParamsSettings(
			paramsName=requestData['paramsName'],
			paramsCode=requestData['paramsCode']
		)
		newParam.save()
		return JsonResponse({'status':True, 'PostContent':'success'})
	except:
		print
		return JsonResponse({'status':False, 'PostContent':'failed'})

#获取参数列表
@csrf_exempt
def getParamsListHandler(request):
	try:
		PostContent = ParamsSettings.objects.all().order_by('paramsCreateTime')
		
		def fn(obj):
			dict = {}
			dict['paramsName'] = obj['fields']['paramsName']
			dict['id'] = obj['pk']
			return dict
		PostContent = list(map(fn, json.loads(serializers.serialize('json',PostContent))))
		return JsonResponse({'status':True, 'PostContent':PostContent})
	except:
		return JsonResponse({'status':False, 'PostContent':'failed'})