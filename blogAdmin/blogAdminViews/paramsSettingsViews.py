from django.views.decorators.csrf import csrf_exempt
from ..models import ParamsSettings,ParamsContent
from myblogdjango.base import DataSqlHandler

#DataSqlHandler类封装了对请求的处理和响应的返回逻辑
#类方法Data_Handler对数据进行处理, 该方法可接收五个参数
#Data_Handler(DataSqlHandler, ModelClass, request, type, extra)
#DataSqlHandler 固定参数,不可更改，必传
#ModelClass 需要操作的Model类，必传
#request 固定参数，包含request请求数据，必传
#type 操作类型，有以下几种类型, 必传:
	#add 添加数据
	#update 更新数据
	#getsingle 获取单个数据
	#delete 删除数据
	#getlist 获取列表
#extra 额外操作集合，可选传

#添加参数
@csrf_exempt
def createParamsHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsSettings, request, 'add')

#更新参数
@csrf_exempt
def updateParamsHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsSettings, request, 'update')

#更新参数
@csrf_exempt
def getSingleParamsHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,ParamsSettings, request, 'getsingle')

#删除参数
@csrf_exempt
def deleteParamsHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ParamsSettings, request, 'delete')

#获取参数列表
@csrf_exempt
def getParamsListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, ParamsSettings, request, 'getlist')

		