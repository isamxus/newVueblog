from django.db import models

# Create your models here.
# 首页轮播图
class HomePageCarouselImage(models.Model):
	pass


class ArticleDetail(models.Model):
	articleTitle = models.CharField(max_length=100)
	articleAuthor = models.CharField(max_length=50)
	articleAbstract = models.CharField(max_length=200,blank=True)
	articleTagsName = models.CharField(max_length=200,blank=True)
	articleTagsID = models.CharField(max_length=400,blank=True)
	articleContent = models.TextField()
	articleCagetoryID = models.CharField(max_length=50)
	articleCagetoryName = models.CharField(max_length=50)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)
