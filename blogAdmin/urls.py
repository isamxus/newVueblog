from django.conf.urls import url
 
from . import views
 
urlpatterns = [
	url(r'^ParamsSettings/Create/$', views.createParamsHandler, name='createParamsHandler'),
	url(r'^ParamsSettings/Update/$', views.updateParamsHandler, name='updateParamsHandler'),
	url(r'^ParamsSettings/Delete/$', views.deleteParamsHandler, name='deleteParamsHandler'),
	url(r'^ParamsSettings/GetList/$', views.getParamsListHandler, name='getParamsListHandler'),
]