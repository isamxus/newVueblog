from django.db import models

#文章标签
class Tag(models.Model):
	tagName = models.CharField(max_length=100)

	def __str__(self):
		return self.name

# 文章分类
class articleCategory(models.Model):
	name = models.CharField(max_length=100)
	cateString = models.CharField(max_length=100)

#文章详情
class articleDetail(models.Model):
	articleTitle = models.CharField(max_length=100)
	articleAuthor = models.CharField(max_length=100)
	articleAbstract = models.CharField(max_length=200,blank=True)
	articleCreateTime = models.DateTimeField()
	articleUpdateTime = models.DateTimeField()
	articleTags = models.ManyToManyField(Tag,blank=True)