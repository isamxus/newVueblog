from django.db import models
import uuid
# Create your models here.
# 首页轮播图
class HomePageCarouselImage(models.Model):
	pass

#文章详情表
class ArticleDetail(models.Model):
	article_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	articleTitle = models.CharField(max_length=100)
	articleAuthor = models.CharField(max_length=50)
	articleAbstract = models.CharField(max_length=200,blank=True)
	articleTagsName = models.CharField(max_length=200,blank=True)
	articleTagsID = models.CharField(max_length=400,blank=True)
	articleContent = models.TextField()
	articleCagetoryID = models.CharField(max_length=50)
	articleCagetoryName = models.CharField(max_length=50)
	IsDeleted = models.BooleanField(default=False)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)

#评论详情表
class CommentDetail(models.Model):
	comment_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	commentAuthor = models.CharField(max_length=50)
	commentHeadImg = models.CharField(max_length=200,blank=True)
	commentContent = models.CharField(max_length=400,blank=True)
	parentArticleID = models.CharField(max_length=200)
	parentArticleTitle = models.CharField(max_length=200)
	IsDeleted = models.BooleanField(default=False)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)


#首页Tab页表
class IndexTab(models.Model):
	IndexTabID = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	IndexTabName = models.CharField(max_length=20)
	IndexTabContent = models.TextField()
	IndexTabCode = models.CharField(max_length=20)
	IsShowTab = models.BooleanField(default=True, blank=True)
	CreateTime = models.DateTimeField(auto_now_add=True)
	UpdateTime = models.DateTimeField(auto_now=True)
	IsDeleted = models.BooleanField(default=False)