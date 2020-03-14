from django.db import models

# Create your models here.
#参数设置表
class ParamsSettings(models.Model):
	paramsName = models.CharField(max_length=100)
	paramsCode = models.CharField(max_length=50)
	paramsCreateTime = models.DateTimeField(auto_now_add=True)
	paramsUpdateTime = models.DateTimeField(auto_now=True)

#参数内容详情表
class ParamsContent(models.Model):
	detailName = models.CharField(max_length=100)
	paramsCreateTime = models.DateTimeField()
	paramsUpdateTime = models.DateTimeField()