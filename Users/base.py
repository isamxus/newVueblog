from myblogdjango.base import DataSqlHandler
from rest_framework.authtoken.models import Token

class UserSqlHandler(DataSqlHandler):
	#添加数据
	def Create_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			Create_Data = ModelClass()
			if ModelClass.objects.filter(UserName=requestData['UserName']).count() > 0:
				return self.ResponseHandler(self, False, err={'err':'用户名已经存在！！！'})
			for field in requestData:
				setattr(Create_Data, field, requestData[field])
			Create_Data.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#用户登录
	def User_Login_Handler(self, ModelClass, request, extra={}):
		try:
			requestData = self.RequestHandler(self, request)
			return self.mustFieldsCheck(self, ModelClass, requestData, extra)
		except Exception as e:
			return self.ResponseHandler(self, False)