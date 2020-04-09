import os

class AutoDeploy(object):
	#设置IP账号密码并返回
	IP = None
	UserName = None
	PassWord = None
	Port = 22
	def set_user_password(self):
		confirm = False
		while not confirm:
			if not self.IP:
				self.IP = input('请输入IP地址: ')
				continue
			if not re.match(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',self.IP):
				print('ip地址格式不正确')
				self.IP = None
				continue
			if not self.UserName:
				self.UserName = input('请输入服务器用户名: ')
				continue
			if not self.PassWord:
				self.PassWord = input('请输入服务器密码: ')
				continue
			confirm = True
		return

	def connect_to_linux(self):
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.IP, self.Port, self.UserName, self.PassWord, timeout=10)
		chan = ssh.invoke_shell()
		chan.send('cd blogManagement'+'\n')
		resp=chan.recv(65535)
		print(resp)
		#stdin, stdout, stderr = ssh.exec_command(a, get_pty=True)
		#result = stdout.read()
		#print(result.decode('utf-8'))
		#ssh.close()
		return


if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblogdjango.settings")
	import django
	django.setup()
	import paramiko
	import re
	exp = AutoDeploy()
	exp.set_user_password()
	exp.connect_to_linux()
	'''
	ip = "112.74.47.33"
	port = 22
	user = "ljc"
	password = "ljc834775778"
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(ip, port, user, password, timeout=10)
	a = "source env/bin/activate;ls;cd blogManagement;pip install -i https://pypi.tuna.tsinghua.edu.cn/simple numpy"
	stdin, stdout, stderr = ssh.exec_command(a, get_pty=True)
	result = stdout.read()
	print(result.decode('utf-8'))
	ssh.close()'''