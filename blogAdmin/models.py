from django.db import models
import uuid
# Create your models here.
#参数设置表
class ParamsSettings(models.Model):
	params_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	paramsName = models.CharField(max_length=100)
	paramsCode = models.CharField(max_length=50)
	IsDeleted = models.BooleanField(default=False)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)


#参数内容详情表
class ParamsContent(models.Model):
	detail_params_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	detailName = models.CharField(max_length=100)
	detailCode = models.CharField(max_length=50, blank=True)
	detailParentParamCode = models.CharField(max_length=50)
	detailParentParamID = models.CharField(max_length=100)
	detailParentParam = models.CharField(max_length=100)
	IsDeleted = models.BooleanField(default=False)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)

