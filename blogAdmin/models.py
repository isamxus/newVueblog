from django.db import models

# Create your models here.
#参数设置表
class ParamsSettings(models.Model):
	paramsName = models.CharField(max_length=100)
	paramsCode = models.CharField(max_length=50)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)

	def mustNeedFields(self):
		return ['paramsName', 'paramsCode']
	def mustReturnFields(self):
		return ['paramsName', 'paramsCode', 'id']

#参数内容详情表
class ParamsContent(models.Model):
	detailName = models.CharField(max_length=100)
	detailCode = models.CharField(max_length=50, blank=True)
	detailParentParamCode = models.CharField(max_length=50)
	detailParentParamID = models.CharField(max_length=100)
	detailParentParam = models.CharField(max_length=100)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)

	def mustNeedFields(self):
		return ['detailName', 'detailCode', 'detailParentParamID', 'detailParentParam', 'detailParentParamCode']
	def mustReturnFields(self):
		return ['detailName', 'detailCode', 'detailParentParamID', 'detailParentParamCode', 'detailParentParam', 'id']