import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms import model_to_dict
from django.db.models import Q
from django.db.models import F
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
		requestData = json.loads(json.dumps(request.POST))
		if 'PostContent' not in requestData.keys():
			return {}
		return json.loads(requestData['PostContent'])

	#对请求进行响应
	def ResponseHandler(self, status, obj={}):
		obj = obj if(obj) else []
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
		Data = json.loads(serializers.serialize('json',Data))
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
	def Create_Data_Handler(self, ModelClass, requestData, extra):
		try:
			requestData = self.RequestHandler(self, requestData)
			Create_Data = ModelClass()
			for field in requestData:
				setattr(Create_Data, field, requestData[field])
			Create_Data.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#更新数据
	def Updata_Data_Handler(self, ModelClass, requestData, extra):
		try:
			requestData = self.RequestHandler(self, requestData)
			UpdataData = get_object_or_404(ModelClass, pk=requestData['id'])
			Updata_Data = ModelClass()
			for field in requestData:
				setattr(Updata_Data, field, requestData[field])
			UpdataData.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#获取单个数据
	def Getsingle_Data_Handler(self, ModelClass, requestData, extra):
		try:
			requestData = self.RequestHandler(self, requestData)
			SingleData = model_to_dict(ModelClass.objects.get(pk=requestData['id']))
			return self.ResponseHandler(self, True, SingleData)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#删除数据
	def Delete_Data_Handler(self, ModelClass, requestData, extra):
		try:
			requestData = self.RequestHandler(self, requestData)
			get_object_or_404(ModelClass, pk=requestData['id']).delete()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#获取数据
	def GetList_Data_Handler(self, ModelClass, requestData, extra):
		try:
			requestData = self.RequestHandler(self, requestData)
			_filter = {}
			_OrderBy = {}
			if 'filter' in requestData.keys():
				_filter = requestData['filter']
			if 'Order_By' in requestData.keys():
				_OrderBy = requestData['Order_By']

			PostContent = ModelClass.objects.filter(**_filter).order_by(**_OrderBy)
			PostContent = self.SerializeData(self, PostContent, ModelClass)
			return self.ResponseHandler(self, True, PostContent)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	def Data_Handler(self, ModelClass, requestData, type, extra=None):
		if type=='add':
			return self.Create_Data_Handler(self, ModelClass, requestData, extra)
		elif type=='update':
			return self.Updata_Data_Handler(self, ModelClass, requestData, extra)
		elif type=='getsingle':
			return self.Getsingle_Data_Handler(self, ModelClass, requestData, extra)
		elif type=='delete':
			return self.Delete_Data_Handler(self, ModelClass, requestData, extra)
		else:
			return self.GetList_Data_Handler(self, ModelClass, requestData, extra)
