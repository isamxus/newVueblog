from django.views.decorators.csrf import csrf_exempt
from ..models import CommentDetail
from myblogdjango.base import DataSqlHandler


#添加文章
@csrf_exempt
def createCommentHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,CommentDetail, request, 'add')

#更新文章
@csrf_exempt
def updateCommentHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,CommentDetail, request, 'update')

#获取一篇文章
@csrf_exempt
def getSingleCommentHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler,CommentDetail, request, 'getsingle')

#删除文章
@csrf_exempt
def deleteCommentHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, CommentDetail, request, 'delete')


#获取文章列表 (不分页)
@csrf_exempt
def getCommentListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, CommentDetail, request, 'getlist')

#获取文章列表 （分页）
@csrf_exempt
def getCommentPageListHandler(request):
	return DataSqlHandler.Data_Handler(DataSqlHandler, CommentDetail, request, 'getpagelist')