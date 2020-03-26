from django.views.decorators.csrf import csrf_exempt
from ..models import Users
from ..base import UserSqlHandler

#添加用户
@csrf_exempt
def createUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'add')

#用户更新
@csrf_exempt
def updateUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'update')

#获取一个用户信息
'''@csrf_exempt
def getSingleUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'getsingle')'''

#删除用户
@csrf_exempt
def deleteUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'delete')

#获取用户列表（分页）
@csrf_exempt
def getUsersPageListHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'getpagelist', extra={
			'ignoreFields': ['PassWord']
		})

#用户登录
@csrf_exempt
def userLoginHandler(request):
	return UserSqlHandler.User_Login_Handler(UserSqlHandler, Users, request, extra = {
				'ignoreFields': ['PassWord'],
				'mustFields': ['UserName', 'PassWord'],
				'err': '用户未注册！！！'
			})

