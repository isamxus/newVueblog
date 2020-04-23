from .base import DataSqlHandler
from .settings import BASE_DIR
from django.http import JsonResponse
class FilesHandler(DataSqlHandler):
	
	#添加文件
	def Upload_Files_Handler(self, ModelClass, requestData, extra={}):
		batchList = []
		fileField = ModelClass().get_file_field()
		filePath = ModelClass().get_file_path()
		file = requestData.FILES.getlist('file')
		for item in file:
			exp = {}
			exp['FileName'] = item.name
			exp[fileField] = item
			batchList.append(exp)
		extra['Data'] = batchList
		extra['extraFields'] = {
			'State': 1
		}
		self.Batch_Insert_Data(self, ModelClass, requestData, extra)
		return self.ResponseHandler(self, True, {
				'name': file[0].name,
				'Address': filePath + file[0].name
			},extra=extra)