import os



class InitBlog(object):
	#参数列表
	paramsList = [
		{'paramsName': '文章分类', 'paramsCode': '0001'},
		{'paramsName': '博客文章', 'paramsCode': '0002'},
		{'paramsName': '文章标签', 'paramsCode': '0003'},
		{'paramsName': '文章评论', 'paramsCode': '0004'},
		{'paramsName': '用户管理', 'paramsCode': '0005'},
		{'paramsName': '首页Tab页', 'paramsCode': '0006'},
	]
	#权限
	AuthList = '00,01,0001,0002,0003,0004,0005,0006'
	#首页Tab页
	TabList = [
		{'IndexTabName': '最新文章', 'IndexTabContent': '', 'IndexTabCode': '000601'}
	]
	def Create_SuperUser_Handler(self):
		Pass = False
		UserName = None
		PassWord = None
		while not Pass:
			if not UserName:
				UserName = input('please enter your UserName: ')
				continue
			if not PassWord:
				PassWord = input('please enter your PassWord: ')
				continue
			ConfirmPassWord = input('please enter your PassWord again: ')
			if ConfirmPassWord != PassWord:
				print('The two passwords are inconsistent')
				UserName = None
				PassWord = None
				continue
			if Users.objects.filter(UserName=UserName).count() > 0:
				print('UserName already exists')
				UserName = None
				PassWord = None
				continue
			print('SuperUser created successfully')
			Pass = True
		try:
			user = Users()
			user.UserName = UserName
			user.PassWord = PassWord
			user.Jurisdiction = self.AuthList
			user.IsSuperUser = True
			user.save()
		except Exception as e:
			print(e)
			return
	#批量初始化数据
	def Init_Data(self, source, ModelClass, MsgStart, MsgEnd):
		List_To_Insert = []
		try:
			print(MsgStart)
			for item in source:
				exp = ModelClass()
				for field in item.keys():
					setattr(exp, field, item[field])
				List_To_Insert.append(exp)
			ModelClass.objects.bulk_create(List_To_Insert)
			print(MsgEnd)
		except Exception as e:
			print(e)
			print('初始化数据失败')

	#初始化博客功能
	def Init_Blog_Function(self):
		confirm = False
		confirmInit = None
		while not confirm:
			if not confirmInit:
				confirmInit = input('是否初始化博客数据(原有博客数据将丢失)(yes/no): ')
				continue
			if confirmInit == 'no':
				confirmInit = None
				print('中止初始化博客数据')
				return
			if confirmInit == 'yes':
				confirm = True
			if confirmInit != 'yes' or confirmInit != 'no':
				confirmInit = None
				continue
		Params_List_To_Insert = []
		Tab_List_To_Insert = []
		Status = os.system(r"python manage.py flush")
		self.Init_Data(self.paramsList, ParamsSettings, '正在初始化博客参数', '博客参数初始化成功')
		self.Init_Data(self.TabList, IndexTab, '正在初始化Tab页', '初始化Tab页成功')

if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblogdjango.settings")
	import django
	django.setup()
	from Users.models import Users
	from blogAdmin.models import ParamsSettings
	from blogIndex.models import IndexTab
	exp = InitBlog()
	exp.Init_Blog_Function()
	exp.Create_SuperUser_Handler()