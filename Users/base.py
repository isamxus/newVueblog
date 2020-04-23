from myblogdjango.base import DataSqlHandler
from myblogdjango.authCheck import AuthTokenHandler
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.conf import settings
from .models import Users

class UserSqlHandler(AuthTokenHandler, DataSqlHandler):
	#添加数据
	def Create_User_Handler(self, ModelClass, request, action):
		try:
			requestData = self.RequestHandler(self, request)
			if ModelClass.objects.filter(UserName=requestData['UserName']).count() > 0:
				return self.ResponseHandler(self, False, err={'err':'用户名已经存在！！！'})
			return self.Data_Handler(self, ModelClass, request, action)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False, e)

	#用户登录
	def User_Login_Handler(self, ModelClass, request, extra={}):
		try:
			requestData = self.RequestHandler(self, request)
			response = self.mustFieldsCheck(self, ModelClass, requestData, extra)
			if type(response).__name__ != 'dict':
				return response
			checkData = ModelClass.objects.filter(**response)
			if checkData:
				extra['extraFields'] = {
					'IsLogin': True,
					'Token': self.sign_Token_Handler(self, checkData.values()[0])
				}
			return self.mapDatabase(self, ModelClass,response, extra)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False)

	#获取用户登录状态
	def User_CheckStatus_Handler(self, ModelClass, request, extra={}):
		try:
			requestData = self.RequestHandler(self, request, True)
			result = self.check_login_status(self, requestData)
			return self.ResponseHandler(self, True,
				extra={
					'extraFields': {
						'IsLogin': result
					}
				})
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False)

	#修改用户密码
	def Change_PassWord_Handler(self, ModelClass, request, extra={}):
		try:
			requestData = self.RequestHandler(self, request)
			extra = self.loginStatus(self, request, extra)
			response = self.mustFieldsCheck(self, ModelClass, requestData, extra)
			if type(response).__name__ != 'dict':
				return response
			checkData = ModelClass.objects.filter(**response)
			if not checkData:
				return self.ResponseHandler(self, False, err={'err': '原密码不正确'}, extra=extra)
			requestData['PassWord'] = requestData['NewPassWord']
			return self.Updata_Data_Handler(self, ModelClass, requestData, extra)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False)