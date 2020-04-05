from django.views.decorators.csrf import csrf_exempt
from ..models import IndexTab
from myblogdjango.base import DataSqlHandler

#添加Tab
@csrf_exempt
def createTabHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexTab, request, 'add')

#更新Tab
@csrf_exempt
def updateTabHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexTab, request, 'update')

#获取一个Tab
@csrf_exempt
def getSingleTabHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexTab, request, 'getsingle')

#删除Tab
@csrf_exempt
def deleteTabHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, IndexTab, request, 'delete')


#获取Tab列表 (不分页)
@csrf_exempt
def getTabListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, IndexTab, request, 'getlist')
