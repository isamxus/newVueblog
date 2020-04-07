from django.views.decorators.csrf import csrf_exempt
from ..models import IndexTab, IndexImage, IndexImageManagement
from myblogdjango.base import DataSqlHandler
from myblogdjango.filesHandle import FilesHandler
from django.http import JsonResponse
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


#首页轮播图上传
@csrf_exempt
def Index_ImageUpload_Handler(request):
	return FilesHandler.Upload_Files_Handler(FilesHandler, IndexImage, request)

#创建首页轮播图
@csrf_exempt
def createImageHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexImageManagement, request, 'add')

#更新首页轮播图
@csrf_exempt
def updateImageHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexImageManagement, request, 'update')

#获取一个首页轮播图
@csrf_exempt
def getSingleImageHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexImageManagement, request, 'getsingle')

#删除一个首页轮播图
@csrf_exempt
def deleteImageHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexImageManagement, request, 'delete')

#获取首页轮播图集合(不分页)
@csrf_exempt
def getImageListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,IndexImageManagement, request, 'getlist')