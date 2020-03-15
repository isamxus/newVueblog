import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
class DataSqlHandler(object):
	#请求成功返回
	SuccessMsg = {
		'status':True,
		'Msg': '成功！！！'
	}

	#请求失败返回
	FailedMsg = {
		'status':False, 
		'Msg': '服务器发生错误，请联系管理员！！！'
	}

	#对请求数据进行处理
	def RequestHandler(self, request):
		return json.loads(json.loads(json.dumps(request.POST))['PostContent'])

	#对请求进行响应
	def ResponseHandler(self, status, obj={}):
		obj = obj if(obj) else 'success'
		return JsonResponse(dict({'PostContent':obj}, **(DataSqlHandler.SuccessMsg if(status) else DataSqlHandler.FailedMsg)))

	#取得Model类中所有字段并生成字典
	def Put_Fields_to_Dict(self, ModelClass):
		att_dict = {}
		for field in ModelClass._meta.fields:
			name = field.attname
			att_dict[name] = ''
		return att_dict
	#序列化数据库查询数据
	def SerializeData(self, Data, ModelClass):
		ret_list = []
		ret_Fields = ModelClass()
		for batch in Data:
			obj = {}
			for key in ret_Fields.mustReturnFields():
				if key=='id':
					obj[key] = batch['pk']
				else:
					obj[key] = batch['fields'][key]
			ret_list.append(obj)
		return ret_list

	#添加数据
	def Create_Data_Handler(self, ModelClass, requestData, judgeMent=None):
		try:
			requestData = self.RequestHandler(self, requestData)
			Create_Data = ModelClass()
			need_Fields = Create_Data.mustNeedFields()
			for field in need_Fields:
				if not requestData[field]:
					return self.ResponseHandler(self, False, '缺少%d字段'%field)
				else:
					setattr(Create_Data, field, requestData[field])
			Create_Data.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#更新数据
	def Updata_Data_Handler(self, ModelClass, requestData, judgeMent=None):
		try:
			requestData = self.RequestHandler(self, requestData)
			UpdataData = get_object_or_404(ModelClass, pk=requestData['id'])
			Updata_Data = ModelClass()
			need_Fields = Updata_Data.mustNeedFields()
			for field in need_Fields:
				if not requestData[field]:
					return self.ResponseHandler(self, False, '缺少%d字段'%field)
				else:
					setattr(UpdataData, field, requestData[field])
			UpdataData.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#删除数据
	def Delete_Data_Handler(self, ModelClass, requestData, judgeMent=None):
		try:
			requestData = self.RequestHandler(self, requestData)
			DeleteData = get_object_or_404(ModelClass, pk=requestData['id'])
			DeleteData.delete()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#获取数据
	def GetList_Data_Handler(self, ModelClass, requestData, judgeMent=None):
		try:
			PostContent = ModelClass.objects.all().order_by(judgeMent)
			PostContent = json.loads(serializers.serialize('json',PostContent))
			PostContent = self.SerializeData(self, PostContent, ModelClass)
			return self.ResponseHandler(self, True, PostContent)
		except Exception as e:
			return self.ResponseHandler(self, False, e)