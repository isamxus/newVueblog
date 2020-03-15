from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ..models import ParamsSettings,ParamsContent
import json
import simplejson
from django.core import serializers
from ..base import DataSqlHandler


#添加参数
@csrf_exempt
def createParamsHandler(request):
	return DataSqlHandler.Create_Data_Handler(DataSqlHandler,ParamsSettings, request)

#更新参数
@csrf_exempt
def updateParamsHandler(request):
	return DataSqlHandler.Updata_Data_Handler(DataSqlHandler,ParamsSettings, request)

#删除参数
@csrf_exempt
def deleteParamsHandler(request):
	return DataSqlHandler.Delete_Data_Handler(DataSqlHandler, ParamsSettings, request)

#获取参数列表
@csrf_exempt
def getParamsListHandler(request):
	return DataSqlHandler.GetList_Data_Handler(DataSqlHandler, ParamsSettings, request,'paramsCreateTime')

		