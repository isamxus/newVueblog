from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import ParamsSettings,ParamsContent
import json
import simplejson
from django.core import serializers

#请求成功返回
SuccessMsg = {
	'status':True,
	'Msg': '成功！！！'
}


#请求失败返回
FailedMsg = {
	'status':False, 
	'PostContent':'failed', 
	'Msg': '服务器发生错误，请联系管理员！！！'
}

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
		return JsonResponse(dict({'PostContent':'success'}, **SuccessMsg))
	except:
		return JsonResponse(FailedMsg)

#更新参数
@csrf_exempt
def updateParamsHandler(request):
	try:
		requestData = json.loads(RequestHandler(request)['PostContent'])
		updateParam = get_object_or_404(ParamsSettings, pk=requestData['id'])
		updateParam.paramsName = requestData['paramsName']
		updateParam.paramsCode = requestData['paramsCode']
		updateParam.save()
		return JsonResponse(dict({'PostContent':'success'}, **SuccessMsg))
	except:
		return JsonResponse(FailedMsg)

#删除参数
@csrf_exempt
def deleteParamsHandler(request):
	try:
		requestData = json.loads(RequestHandler(request)['PostContent'])
		updateParam = get_object_or_404(ParamsSettings, pk=requestData['id'])
		updateParam.delete()
		return JsonResponse(dict({'PostContent':'success'}, **SuccessMsg))
	except:
		return JsonResponse(FailedMsg)

#获取参数列表
@csrf_exempt
def getParamsListHandler(request):
	try:
		PostContent = ParamsSettings.objects.all().order_by('paramsCreateTime')
		
		def fn(obj):
			dict = {}
			dict['paramsName'] = obj['fields']['paramsName']
			dict['paramsCode'] = obj['fields']['paramsCode']
			dict['id'] = obj['pk']
			return dict
		PostContent = list(map(fn, json.loads(serializers.serialize('json',PostContent))))
		return JsonResponse(dict({'PostContent':PostContent}, **SuccessMsg))
	except:
		return JsonResponse(FailedMsg)