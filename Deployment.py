import os

class AutoDeploy(object):
	#默认新建的用户名和密码
	DefaultName = 'ljc114'
	DefaultPasswd = 'ljc834775778'

	#连接IP
	IP = '112.74.47.33'

	#服务器初始用户名和密码
	UserName = 'root'
	PassWord = 'Qq123456'

	#默认端口
	Port = 22
	
	#创建角色指令
	createUserOrderList = [
		'useradd -m -s /bin/bash ' + DefaultName + '\r',
		'usermod -a -G sudo ' + DefaultName + '\r',
		'echo "' + DefaultName + '":"' + DefaultPasswd + '" | chpasswd' + '\r',
	]

	#更新环境指令
	updateEnvirOrderList = [
		'sudo apt-get update\r',
		#'sudo pip3 install virtualenv\r',
		#'sudo service nginx start\r',
	]
	#更新环境指令
	upgradeEnvirOrderList = [
		'sudo apt-get upgrade\r',
		'sudo apt-get install nginx\r',
		'sudo apt-get install git python3 python3-pip\r',
	]
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

	#读取回显
	def read_output(self, exp, order, map):
		exp.send(order)
		result = ''
		p = re.compile(r'%s'%map)
		Choice = re.compile(r'continue')
		while True:
			time.sleep(0.5)
			rst = exp.recv(65535)
			rst = rst.decode('utf-8')
			result += rst
			if '[Y/n]' in rst:
				print('map!!!!!!')
			if p.search(rst):
				print(result)
				print(len(rst))
				break
		return True

	#创建角色
	def create_User(self, exp, list, map):
		return self.excute_Order(exp, list)

	#遍历指令并执行
	def excute_Order(self, tran, list, map):
		exp = tran.open_session()
		exp.get_pty()
		exp.invoke_shell()
		for order in list:
			if self.read_output(exp, order, map):
				print('成功')
			else:
				print('失败')
		exp.close()
		return True

	def connect_to_linux(self):


		'''
		ps = 'ljc834775778'
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.IP, self.Port, self.UserName, self.PassWord, timeout=10)
		cmd = 'useradd -m -s /bin/bash ljc7;usermod -a -G sudo ljc7;password ljc7'
		stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
		stdin.write('%s' % ps)
		time.sleep(1)
		#stdin.write('%s\n' % ps)
		#time.sleep(1)
		stdin.flush()
		
		out = stdout.readlines()
		print(out)
		ssh.close()
		#result = stdout.read()
		#print(result.decode('utf-8'))
		#ssh.close()'''
		
		tran = paramiko.Transport((self.IP, 22,))
		tran.start_client()
		tran.auth_password(self.UserName, self.PassWord)
		
		#创建角色并设置密码
		self.excute_Order(tran, self.createUserOrderList, '~#')
		self.excute_Order(tran, self.updateEnvirOrderList, 'Done')
		self.excute_Order(tran, self.upgradeEnvirOrderList, 'upgraded')

		#更新环境
		#self.excute_Order(tran, self.updateEnvirOrderList)
		orderlist = [
			#'sudo apt-get update\r',
			#'sudo apt-get upgrade\r',
			#'sudo apt-get install nginx\r',
			#'sudo apt-get install git python3 python3-pip',
			#'sudo pip3 install virtualenv\r',
			#'sudo service nginx start',
			#'su - ' + name + '\r',
		]
		
		tran.close()
		#return


if __name__ == '__main__':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myblogdjango.settings")
	import django
	django.setup()
	import paramiko
	import socket
	import sys
	import select
	from paramiko.py3compat import u
	import re
	import time
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