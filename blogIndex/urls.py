from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from .blogIndexViews import blogArticleViews, articleCommentViews, blogIndexViews
 
urlpatterns = [
	#博客文章
	url(r'^Article/Create/$', blogArticleViews.createArticleHandler, name='createArticleHandler'),
	url(r'^Article/Update/$', blogArticleViews.updateArticleHandler, name='updateArticleHandler'),
	url(r'^Article/Delete/$', blogArticleViews.deleteArticleHandler, name='deleteArticleHandler'),
	url(r'^Article/GetSingle/$', blogArticleViews.getSingleArticleHandler, name='getSingleArticleHandler'),
	url(r'^Article/GetList/$', blogArticleViews.getArticleListHandler, name='getArticleListHandler'),
	url(r'^Article/GetPageList/$', blogArticleViews.getArticlePageListHandler, name='getArticlePageListHandler'),

	#文章评论
	url(r'^Comment/Create/$', articleCommentViews.createCommentHandler, name='createCommentHandler'),
	url(r'^Comment/Update/$', articleCommentViews.updateCommentHandler, name='updateCommentHandler'),
	url(r'^Comment/Delete/$', articleCommentViews.deleteCommentHandler, name='deleteCommentHandler'),
	url(r'^Comment/GetSingle/$', articleCommentViews.getSingleCommentHandler, name='getSingleCommentHandler'),
	url(r'^Comment/GetList/$', articleCommentViews.getCommentListHandler, name='getCommentListHandler'),
	url(r'^Comment/GetPageList/$', articleCommentViews.getCommentPageListHandler, name='getCommentPageListHandler'),

	#Tab
	url(r'^Tab/Create/$', blogIndexViews.createTabHandler, name='createTabHandler'),
	url(r'^Tab/Update/$', blogIndexViews.updateTabHandler, name='updateTabHandler'),
	url(r'^Tab/Delete/$', blogIndexViews.deleteTabHandler, name='deleteTabHandler'),
	url(r'^Tab/GetSingle/$', blogIndexViews.getSingleTabHandler, name='getSingleTabHandler'),
	url(r'^Tab/GetList/$', blogIndexViews.getTabListHandler, name='getTabListHandler'),

	#首页轮播图
	url(r'^IndexImage/Upload/$', blogIndexViews.Index_ImageUpload_Handler, name='Index_ImageUpload_Handler'),
	url(r'^IndexImage/Create/$', blogIndexViews.createImageHandler, name='createImageHandler'),
	url(r'^IndexImage/Update/$', blogIndexViews.updateImageHandler, name='updateImageHandler'),
	url(r'^IndexImage/Delete/$', blogIndexViews.deleteImageHandler, name='deleteImageHandler'),
	url(r'^IndexImage/GetSingle/$', blogIndexViews.getSingleImageHandler, name='getSingleImageHandler'),
	url(r'^IndexImage/GetList/$', blogIndexViews.getImageListHandler, name='getImageListHandler'),
]