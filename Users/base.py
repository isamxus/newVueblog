from myblogdjango.base import DataSqlHandler, AuthTokenHandler
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import Users
from rest_framework_jwt.settings import api_settings
#serializer = Serializer(settings.SECRET_KEY, 300)

class UserSqlHandler(DataSqlHandler, AuthTokenHandler):
	#添加数据
	def Create_User_Handler(self, ModelClass, request, action):
		try:
			requestData = self.RequestHandler(self, request)
			if ModelClass.objects.filter(UserName=requestData['UserName']).count() > 0:
				return self.ResponseHandler(self, False, err={'err':'用户名已经存在！！！'})
			return self.Data_Handler(self, ModelClass, request, action)
		except Exception as e:
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
			self.check_Token_Handler(self, requestData)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False)