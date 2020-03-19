from django.conf.urls import url
 
from .blogIndexViews import blogArticleViews
 
urlpatterns = [
	#博客文章
	url(r'^Article/Create/$', blogArticleViews.createArticleHandler, name='createArticleHandler'),
	url(r'^Article/Update/$', blogArticleViews.updateArticleHandler, name='updateArticleHandler'),
	url(r'^Article/Delete/$', blogArticleViews.deleteArticleHandler, name='deleteArticleHandler'),
	url(r'^Article/GetSingle/$', blogArticleViews.getSingleArticleHandler, name='getSingleArticleHandler'),
	url(r'^Article/GetList/$', blogArticleViews.getArticleListHandler, name='getArticleListHandler'),
	url(r'^Article/GetPageList/$', blogArticleViews.getArticlePageListHandler, name='getArticlePageListHandler'),
]