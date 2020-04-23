from django.conf.urls import url
 
from .blogAdminViews import paramsSettingsViews, paramsDetailViews
 
urlpatterns = [
	#参数设置
	url(r'^ParamsSettings/Create/$', paramsSettingsViews.createParamsHandler, name='createParamsHandler'),
	url(r'^ParamsSettings/Update/$', paramsSettingsViews.updateParamsHandler, name='updateParamsHandler'),
	url(r'^ParamsSettings/Delete/$', paramsSettingsViews.deleteParamsHandler, name='deleteParamsHandler'),
	url(r'^ParamsSettings/GetSingle/$', paramsSettingsViews.getSingleParamsHandler, name='getSingleParamsHandler'),
	url(r'^ParamsSettings/GetList/$', paramsSettingsViews.getParamsListHandler, name='getParamsListHandler'),

	#参数设置详情
	url(r'^ParamsDetailSettings/Create/$', paramsDetailViews.createDetailHandler, name='createDetailHandler'),
	url(r'^ParamsDetailSettings/Update/$', paramsDetailViews.updateDetailHandler, name='updateDetailHandler'),
	url(r'^ParamsDetailSettings/Delete/$', paramsDetailViews.deleteDetailHandler, name='deleteDetailHandler'),
	url(r'^ParamsDetailSettings/GetSingle/$', paramsDetailViews.getSingleDetailHandler, name='getSingleDetailHandler'),
	url(r'^ParamsDetailSettings/GetList/$', paramsDetailViews.getDetailListHandler, name='getDetailListHandler'),
]