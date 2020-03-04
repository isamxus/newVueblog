from django.db import models

# Create your models here.
#用户信息表
class Users:
	UserHeadImg = models.ImageField(upload_to='UserHeadImg',blank=True)
	UserName = models.CharField(max_length=50)
	PassWord = models.CharField(max_length=50)