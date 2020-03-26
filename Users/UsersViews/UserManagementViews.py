from django.views.decorators.csrf import csrf_exempt
from ..models import Users
from ..base import UserSqlHandler

#添加参数
@csrf_exempt
def createUserHandler(request):
	return UserSqlHandler.Data_Handler(UserSqlHandler, Users, request, 'add')





