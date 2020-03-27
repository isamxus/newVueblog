import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.core import serializers
from django.forms import model_to_dict
from django.db.models import Q
from django.db.models import F





#基础类
class DataSqlHandler(object):
	#处理后的PostContent
	PostContent = None
	#请求成功返回
	def SuccessMsg(self, success={}):
		return dict({
			'status':True,
			'Msg': '成功！！！'
		}, **(success if (success) else {'success': '请求成功！！！'}))

	#请求失败返回
	def FailedMsg(self, err={}):
		return dict({
			'status':False,
			'Msg': '失败！！！'
		}, **(err if(err) else {'err': '服务器发生错误，请联系管理员！！！'}))

	#判断key是否存在于dict中并返回value
	def Is_In_Dict(self, key, dict, type={}):
		return dict[key] if (dict and key in dict.keys()) else type

	#对请求数据进行处理
	def RequestHandler(self, request):
		requestData = json.loads(json.dumps(request.POST))
		return json.loads(requestData['PostContent']) if('PostContent' in requestData.keys()) else {}

	#对请求进行响应
	def ResponseHandler(self, status, obj={}, success={}, err={}):
		return JsonResponse(dict({'PostContent':obj if(obj) else []}, **(self.SuccessMsg(self, success) if(status) else self.FailedMsg(self, err))))


	#取得Model类中所有字段并生成列表
	def Put_Fields_to_List(self, ModelClass, extra):
		att_list = []
		ignoreList = self.Is_In_Dict(self, 'ignoreFields', extra, [])
		for field in ModelClass._meta.fields:
			if field.attname in ignoreList:
				continue
			att_list.append(field.attname)
		return att_list

	#序列化数据库查询数据
	def SerializeData(self, Data, ModelClass, extra):
		Data = json.loads(serializers.serialize('json',Data))
		ret_list = []
		ret_Fields = ModelClass()
		for batch in Data:
			obj = {}
			for key in self.Put_Fields_to_List(self, ModelClass, extra):
				obj[key] = batch['pk'] if(key=='id') else batch['fields'][key]
			ret_list.append(obj)
		return ret_list

	#验证必传字段并根据筛选条件与数据库匹配
	def mustFieldsCheck(self, ModelClass, Data, extra):
		_filter = {}
		for field in self.Is_In_Dict(self, 'mustFields', extra, []):
			if field not in Data.keys() or not Data[field]:
				return self.ResponseHandler(self, False, err={'err':("缺少%s参数！！！")%field})
			if Data[field]:
				_filter[field] = Data[field]

		checkData = ModelClass.objects.filter(**_filter)																				
		if checkData:
			return self.ResponseHandler(self, True, self.SerializeData(self, checkData, ModelClass, extra), success={'IsOK': self.Is_In_Dict(self, 'success', extra, False)})
		return self.ResponseHandler(self, False, err={
				'err': self.Is_In_Dict(self, 'err', extra, '接口extra传参错误！！！')
			})

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
			return self.ResponseHandler(self, False)

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
			return self.ResponseHandler(self, False)

	#获取单个数据
	def Getsingle_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			SingleData = ModelClass.objects.filter(id=requestData['id']).values()[0]
			return self.ResponseHandler(self, True, SingleData)
		except Exception as e:
			return self.ResponseHandler(self, False)

	#删除数据
	def Delete_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			get_object_or_404(ModelClass, pk=requestData['id']).delete()
			return self.ResponseHandler(self, True)
		except Exception as e:
			return self.ResponseHandler(self, False)

	#获取列表数据（不分页）
	def GetList_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			_filter = self.Is_In_Dict(self, 'filter', requestData)
			_OrderBy = self.Is_In_Dict(self, '_OrderBy', requestData, 'CreateTime')
			PostContent = ModelClass.objects.filter(**_filter).order_by(_OrderBy)
			PostContent = self.SerializeData(self, PostContent, ModelClass, extra)
			return self.ResponseHandler(self, True, PostContent)
		except Exception as e:
			return self.ResponseHandler(self, False)
	#获取列表数据（分页）
	def GetPageList_Data_Handler(self, ModelClass, extra):
		try:
			requestData = self.PostContent
			_filter = self.Is_In_Dict(self, 'filter', requestData, {})
			_OrderBy = self.Is_In_Dict(self, '_OrderBy', requestData, 'CreateTime')
			_PageSize = self.Is_In_Dict(self, 'PageSize', requestData, False)
			_PageNumber = self.Is_In_Dict(self, 'PageNumber', requestData, False)
			if _PageSize and _PageNumber:
				PostContent = ModelClass.objects.filter(**_filter).order_by(_OrderBy)
				count = PostContent.count()
				PostContent = PostContent[((_PageNumber-1) * _PageSize):((_PageNumber) * _PageSize)]	
				PostContent = self.SerializeData(self, PostContent, ModelClass, extra)
				return self.ResponseHandler(self, True, {
						'Items': PostContent,
						'PageSize': _PageSize,
						'PageNumber': _PageNumber,
						'TotalItems': count
					})
			else:
				return self.ResponseHandler(self, False, err={'err':'缺少PageSize或PageNumber参数！！！'})

		except Exception as e:
			return self.ResponseHandler(self, False, e)
	def Data_Handler(self, ModelClass, requestData, type, extra={}):
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




