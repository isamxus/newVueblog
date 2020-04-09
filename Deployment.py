import os

class AutoDeploy(object):
	#设置IP账号密码并返回
	DeFaultIP = '112.74.47.33'
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
		chan = tran.open_session()
		chan.get_pty()
		chan.invoke_shell()
		
		while True:
			readable, writeable, error = select.select([chan, sys.stdin, ],[],[])
			'''
			if chan in readable:
				try:
					x = u(chan.recv(1024))
					if len(x) == 0:
						print('\r\n*** EOF\r\n')
						break
					sys.stdout.write(x)
					sys.stdout.flush()
				except socket.timeout:
					pass
			if sys.stdin in readable:
				inp = sys.stdin.readline()
				chan.sendall(inp)'''
		chan.close()
		#tran.close()
		return


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