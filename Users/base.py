from myblogdjango.base import DataSqlHandler
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import Users
from rest_framework_jwt.settings import api_settings
#serializer = Serializer(settings.SECRET_KEY, 300)

class UserSqlHandler(DataSqlHandler):
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
			jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
			jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
			jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
			if type(response).__name__ != 'dict':
				return response
			checkData = ModelClass.objects.filter(**response)
			if checkData:
				payload = jwt_payload_handler(checkData[0])
				token = jwt_encode_handler(payload)
				print(token)
				result = jwt_decode_handler(token)
				print(result)
			extra['extraFields'] = {
				'Token': token
			}
			return self.mapDatabase(self, ModelClass,response, extra)
		except Exception as e:
			print(e)
			return self.ResponseHandler(self, False)
 