from django.conf.urls import url
 
from .blogAdminViews import paramsSettingsViews
 
urlpatterns = [
	url(r'^ParamsSettings/Create/$', paramsSettingsViews.createParamsHandler, name='createParamsHandler'),
	url(r'^ParamsSettings/Update/$', paramsSettingsViews.updateParamsHandler, name='updateParamsHandler'),
	url(r'^ParamsSettings/Delete/$', paramsSettingsViews.deleteParamsHandler, name='deleteParamsHandler'),
	url(r'^ParamsSettings/GetSingle/$', paramsSettingsViews.getSingleParamsHandler, name='getSingleParamsHandler'),
	url(r'^ParamsSettings/GetList/$', paramsSettingsViews.getParamsListHandler, name='getParamsListHandler'),
]