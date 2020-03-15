from django.db import models

# Create your models here.
#参数设置表
class ParamsSettings(models.Model):
	paramsName = models.CharField(max_length=100)
	paramsCode = models.CharField(max_length=50)
	paramsCreateTime = models.DateTimeField(auto_now_add=True)
	paramsUpdateTime = models.DateTimeField(auto_now=True)

	def mustNeedFields(self):
		return ['paramsName', 'paramsCode']
	def mustReturnFields(self):
		return ['paramsName', 'paramsCode', 'id']

#参数内容详情表
class ParamsContent(models.Model):
	detailName = models.CharField(max_length=100)
	detailCode = models.CharField(max_length=50, blank=True)
	detailParentParamID = models.CharField(max_length=100)
	detailParentParam = models.ForeignKey(ParamsSettings, on_delete=models.CASCADE)
	paramsCreateTime = models.DateTimeField(auto_now_add=True)
	paramsUpdateTime = models.DateTimeField(auto_now=True)