import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms import model_to_dict
from django.db.models import Q
from django.db.models import F
class DataSqlHandler(object):
	#请求成功返回
	def SuccessMsg(self):
		return {
			'status':True,
			'Msg': '成功！！！'
		}

	#请求失败返回
	def FailedMsg(self):
		return {
			'status':False,
			'Msg': '服务器发生错误，请联系管理员！！！'
		}
	#处理后的PostContent
	PostContent = None
	#对请求数据进行处理
	def RequestHandler(self, request):
		requestData = json.loads(json.dumps(request.POST))
		if 'PostContent' not in requestData.keys():
			return {}
		return json.loads(requestData['PostContent'])

	#对请求进行响应
	def ResponseHandler(self, status, obj={}):
		obj = obj if(obj) else []
		return JsonResponse(dict({'PostContent':obj}, **(self.SuccessMsg(self) if(status) else self.FailedMsg(self))))


	#取得Model类中所有字段并生成列表
	def Put_Fields_to_List(self, ModelClass):
		att_list = []
		for field in ModelClass._meta.fields:
			att_list.append(field.attname)
		return att_list

	#序列化数据库查询数据
	def SerializeData(self, Data, ModelClass):
		Data = json.loads(serializers.serialize('json',Data))
		ret_list = []
		ret_Fields = ModelClass()
		for batch in Data:
			obj = {}
			for key in self.Put_Fields_to_List(self, ModelClass):
				if key=='id':
					obj[key] = batch['pk']
				else:
					obj[key] = batch['fields'][key]
			ret_list.append(obj)
		return ret_list

	#添加数据
	def Create_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			Create_Data = ModelClass()
			for field in requestData:
				setattr(Create_Data, field, requestData[field])
			Create_Data.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#更新数据
	def Updata_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			UpdataData = get_object_or_404(ModelClass, pk=requestData['id'])
			Updata_Data = ModelClass()
			for field in requestData:
				setattr(UpdataData, field, requestData[field])
			UpdataData.save()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#获取单个数据
	def Getsingle_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			SingleData = ModelClass.objects.filter(id=requestData['id']).values()[0]
			return self.ResponseHandler(self, True, SingleData)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#删除数据
	def Delete_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			get_object_or_404(ModelClass, pk=requestData['id']).delete()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False, e)

	#获取列表数据（不分页）
	def GetList_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			_filter = requestData['filter'] if('filter' in requestData.keys()) else {}
			_OrderBy = requestData['Order_By'] if('Order_By' in requestData.keys()) else {}
			PostContent = ModelClass.objects.filter(**_filter).order_by(**_OrderBy)
			PostContent = self.SerializeData(self, PostContent, ModelClass)
			return self.ResponseHandler(self, True, PostContent)
		except Exception as e:
			return self.ResponseHandler(self, False, e)
	#获取列表数据（分页）
	def GetPageList_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			_filter = requestData['filter'] if('filter' in requestData.keys()) else {}
			_OrderBy = requestData['_OrderBy'] if('_OrderBy' in requestData.keys()) else {}
			_PageSize = requestData['PageSize'] if('PageSize' in requestData.keys()) else False
			_PageNumber = requestData['PageNumber'] if('PageNumber' in requestData.keys()) else False
			if _PageSize and _PageNumber:
				PostContent = ModelClass.objects.filter(**_filter).order_by(_OrderBy)
				count = PostContent.count()
				PostContent = PostContent[((_PageNumber-1) * _PageSize):((_PageNumber) * _PageSize)]	
				PostContent = self.SerializeData(self, PostContent, ModelClass)
				return self.ResponseHandler(self, True, {
						'Items': PostContent,
						'PageSize': _PageSize,
						'PageNumber': _PageNumber,
						'TotalItems': count
					})
			else:
				return self.ResponseHandler(self, False, '传参错误！！！')

		except Exception as e:
			return self.ResponseHandler(self, False, e)
	def Data_Handler(self, ModelClass, requestData, type, extra=None):
		self.PostContent = self.RequestHandler(self, requestData)
		if type=='add':
			return self.Create_Data_Handler(self, ModelClass, extra)
		if type=='update':
			return self.Updata_Data_Handler(self, ModelClass, extra)
		if type=='getsingle':
			return self.Getsingle_Data_Handler(self, ModelClass, extra)
		if type=='delete':
			return self.Delete_Data_Handler(self, ModelClass, extra)
		if type=='getlist':
			return self.GetList_Data_Handler(self, ModelClass, extra)
		if type=='getpagelist':
			return self.GetPageList_Data_Handler(self, ModelClass, extra)
