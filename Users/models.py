from django.db import models
import uuid
# Create your models here.
#用户信息表
class Users(models.Model):
	user_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	UserHeadImg = models.ImageField(upload_to='ImageCollect/UserHeadImg',blank=True)
	UserName = models.CharField(max_length=50)
	PassWord = models.CharField(max_length=50)
	Jurisdiction = models.CharField(max_length=400,blank=True)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)

