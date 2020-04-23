import hashlib
from django.core import signing
import time
from datetime import datetime
from Users.models import Users 
#验证状态类
class AuthTokenHandler(object):
	HEADER = {'typ': 'JWP', 'alg': 'default'}
	KEY = 'Amxue_Li'
	SALT = 'www.amxus.info'
	TIME_OUT = 20 * 60
	#加密
	def encrypt(self, obj):
		value = signing.dumps(obj, key=self.KEY, salt=self.SALT)
		value = signing.b64_encode(value.encode()).decode()
		return value
	
	#解密
	def decrypt(self, src):
		src = signing.b64_decode(src.encode()).decode()
		raw = signing.loads(src, key=self.KEY, salt=self.SALT)
		return raw


	#生成Token
	def sign_Token_Handler(self, Data):
		header = self.encrypt(self, self.HEADER)
		payload = {
			'user_id': Data['user_id'].__str__(),
			'UserName': Data['UserName'],
			'iat': time.time()
		}
		payload = self.encrypt(self, payload)
		md5 = hashlib.md5()
		md5.update(("%s.%s" % (header, payload)).encode())
		signature = md5.hexdigest()
		token = "%s.%s.%s" % (header, payload, signature)
		return token

	#获取payload
	def get_payload(self, Token):
		payload = str(Token).split('.')[1]
		payload = self.decrypt(self, payload)
		return payload


	#重新签发Token
	def resign_Token(self, Token):
		payload = self.get_payload(self, Token)
		UserInfo = Users.objects.filter(user_id=payload['user_id']).values()[0]
		return self.sign_Token_Handler(self, UserInfo)
		
	#验证登陆状态
	def check_login_status(self, Data, NeedsUserInfo=False):
		check_result = {
			'IsLogin': False,
			'UserInfo': None
		}
		if 'Token' not in Data.keys() or not Data['Token']:
			return check_result['IsLogin']
		Token = Data['Token']
		payload = self.get_payload(self, Token)
		ot = datetime.utcfromtimestamp(payload['iat'])
		nt = datetime.utcfromtimestamp(time.time())
		if ((nt - ot).seconds) > self.TIME_OUT:
			return check_result['IsLogin']
		user_id = payload['user_id']
		result = Users.objects.filter(user_id=user_id).values()[0]
		if not result:
			return check_result['IsLogin']
		del result['PassWord']
		check_result['IsLogin'] = True
		check_result['UserInfo'] = result
		return check_result if(NeedsUserInfo) else check_result['IsLogin']
		