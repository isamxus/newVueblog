from django.db import models

# Create your models here.
# 首页轮播图
class HomePageCarouselImage(models.Model):
	pass

#文章详情表
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

#评论详情表
class CommentDetail(models.Model):
	commentAuthor = models.CharField(max_length=50)
	commentHeadImg = models.CharField(max_length=200,blank=True)
	commentContent = models.CharField(max_length=400,blank=True)
	parentArticleID = models.CharField(max_length=200)
	parentArticleTitle = models.CharField(max_length=200)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)


