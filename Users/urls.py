from django.conf.urls import url
 
from .UsersViews import UserManagementViews
 
urlpatterns = [
	#用户管理api
	url(r'^User/Create/$', UserManagementViews.createUserHandler, name='createUserHandler')
]